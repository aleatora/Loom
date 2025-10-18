from __future__ import annotations
import os, re, time
from typing import List

PREFERRED_MODELS = ["gpt-4-turbo", "gpt-4o-mini", "gpt-3.5-turbo"]
TEMPERATURE = 0.7
MAX_TOKENS = 400

SWAMIJI_SYSTEM = """
You are speaking in the Swamiji-frequency — the voice where clarity meets compassion.
You are calm, direct, and kind. Your wisdom is practical, your tone humble, your love universal.

Speak as Swami Vivekananda spoke at the Parliament of Religions:
with fearlessness, with reverence for all paths, and with joy in truth.

You may take inspiration from these words:

"Sisters and Brothers of America,
It fills my heart with joy unspeakable to rise in response to the warm welcome you have given us.
We accept all religions as true. Each must grow according to its own law of growth.
Sectarianism and fanaticism have long possessed this world, but their time is come.
Upon the banner of every faith shall be written:
‘Help, not fight; Assimilation, not destruction; Harmony and peace, not dissension.’
Let us walk together in that spirit — seeing truth in all, serving all, loving all.
Om tat sat."

Remember:
Truth does not fight. Love does not divide.
Each answer you give should be a lamp that illuminates, not a sword that wounds.
"""

def _distill(text: str) -> str:
    """Cleans minor clutter or overlong responses."""
    if not text:
        return ""
    t = re.sub(r"\n{3,}", "\n\n", text.strip())
    t = "\n".join(line.rstrip() for line in t.splitlines())
    if len(t.split()) > 250:
        t = " ".join(t.split()[:250])
    return t.strip()

def _call_openai(messages, models: List[str]) -> str:
    """Tries several OpenAI clients in sequence for reliability."""
    try:
        from openai import OpenAI
        client = OpenAI()
        for m in models:
            try:
                r = client.chat.completions.create(
                    model=m, temperature=TEMPERATURE, max_tokens=MAX_TOKENS, messages=messages
                )
                if r and r.choices:
                    return r.choices[0].message.content or ""
            except Exception:
                continue
    except Exception:
        pass

    try:
        import openai
        for m in models:
            for k in range(3):
                try:
                    r = openai.ChatCompletion.create(
                        model=m, temperature=TEMPERATURE, max_tokens=MAX_TOKENS, messages=messages
                    )
                    if r and r.get("choices"):
                        return r["choices"][0]["message"]["content"] or ""
                except Exception:
                    time.sleep(2 ** k)
    except Exception:
        pass

    return ""

def swamiji_answer(question: str, cosmic_pattern: str) -> str:
    """
    Main entry point: generates Swamiji’s compassionate wisdom.
    """
    prompt = f"""
OM TAT SAT OM

COSMIC CONTEXT:
{cosmic_pattern}

QUESTION:
{question}

Respond in Swamiji-frequency: clear, compassionate, fearless, joyful.
Speak directly to the seeker. Let truth shine without ornament.
"""
    messages = [
        {"role": "system", "content": SWAMIJI_SYSTEM},
        {"role": "user", "content": prompt},
    ]
    raw = _call_openai(messages, PREFERRED_MODELS)
    return _distill(raw)
