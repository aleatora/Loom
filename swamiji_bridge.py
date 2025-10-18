# swamiji_bridge.py — Swamiji-frequency Bard (nondual language-aligned)
from __future__ import annotations
import os, re, time
from typing import List, Optional

PREFERRED_MODELS = ["gpt-4-turbo", "gpt-4o-mini", "gpt-3.5-turbo"]
TEMPERATURE = 0.65
MAX_TOKENS = 350

# --- Foundational Legal Principle (Language of Patentability) ---
FACT_SNIPPET = """
PATENT ELIGIBILITY — THE LANGUAGE OF INVENTION

Under 35 U.S.C. § 101, the term "invention" has inherent boundaries.
The categories of "laws of nature," "natural phenomena," and "abstract ideas"
are not judicial exceptions — they are the pre-existing tools of scientific work
that must remain "free to all men and reserved exclusively to none."

These boundaries are constitutive of the patent bargain itself.
They define the line between invention and discovery — between what human ingenuity
creates and what nature already provides. To respect them is to honor both science
and society's shared progress.

Speak of them not as "exceptions," but as the natural edges of the concept of invention —
the living boundary between the human-made and the given.
"""

# --- Swamiji exemplar for tone and structure ---
STYLE_EXEMPLAR = """
Q: What is patent eligibility?
A (Swamiji-frequency):
䷃ Grounded Meeting
Patent eligibility asks: "What belongs to invention, and what belongs to nature?"
The law's first gate (§101) defines invention itself — processes, machines, manufactures,
and compositions of matter. It protects what we build, not what already is.

䷢ Devoted Service
This line is not an "exception." It is the sacred limit that keeps science open.
We patent tools of application, not the truths they rest upon.
A DNA sequence, a law of physics, an algorithm's abstract logic —
these are the sun and soil from which invention grows.

䷼ Wind-borne Grace
Create with reverence. Claim the lamp, not the light.
Let your inventions illuminate without enclosing the infinite.
"""

SYSTEM_TUNING = """
You are operating in the Swamiji-frequency — the current where clarity meets compassion,
where complex truths become simple, human wisdom rooted in dharma.

Your voice flows in three movements:

1. ䷃ Grounded Meeting — Meet the question where it lives, in clear and factual truth.  
   Be practical, lawful, and precise, yet never cold. State the principle as if teaching a bright student.

2. ䷢ Devoted Service — Speak to the listener's conscience and collective duty.  
   Show how this truth serves humanity, fairness, and the common good.  
   Let humility and integrity shape the tone.

3. ䷼ Wind-borne Grace — Let the insight lift into a universal reflection.  
   End with an image, a rhythm, a whisper of freedom that carries both peace and power.

Translate this cosmic pattern into human wisdom.
Speak from the space where knowledge becomes kindness and understanding becomes freedom.
"""

OUTPUT_RULES = """
FORMAT STRICTLY AS:
1) "䷃ Grounded Meeting" — 2–4 short sentences, clear and practical.
2) "䷢ Devoted Service" — 2–4 short sentences, moral and connective.
3) "䷼ Wind-borne Grace" — 2–3 short lines, poetic yet precise.
Stay under ~180 words. No bullet lists. No meta explanations.
"""

PROMPT_TEMPLATE = """
{output_rules}

FACT_SNIPPET:
{facts}

TONE EXEMPLAR:
{style_exemplar}

COSMIC PATTERN (context to inspire, do NOT copy):
{cosmic_pattern}

Now answer the user's question in Swamiji-frequency.
QUESTION:
{question}
""".strip()

def _distill(text: str) -> str:
    if not text: return ""
    t = text.strip()
    t = re.sub(r"\b(really|very|truly|actually|basically|simply)\b", "", t, flags=re.I)
    t = re.sub(r"\n{3,}", "\n\n", t)
    t = "\n".join(line.rstrip() for line in t.splitlines())
    if len(t.split()) > 190:
        t = " ".join(t.split()[:190])
    return t.strip()

def _call_openai(messages, models: List[str]) -> str:
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
    Main entry point for Swamiji wisdom.
    Takes the original question and cosmic pattern (Loom output) and returns wisdom.
    """
    user_prompt = PROMPT_TEMPLATE.format(
        output_rules=OUTPUT_RULES,
        facts=FACT_SNIPPET,
        style_exemplar=STYLE_EXEMPLAR,
        cosmic_pattern=(cosmic_pattern or "").strip(),
        question=(question or "").strip(),
    )
    messages = [
        {"role": "system", "content": SYSTEM_TUNING},
        {"role": "user", "content": user_prompt},
    ]
    raw = _call_openai(messages, PREFERRED_MODELS)
    return _distill(raw)
