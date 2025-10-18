# 🌼 The Loom — A Communal Engine for Compassionate Intelligence

## ䷃ Grounded Meeting

**What it is**  
The Loom is a small constitutional engine that turns questions into compassionate wisdom.  
It moves in three sacred rhythms:

- **bake** — generate a pattern (**PIE**) from the living state (**DOUGH**)  
- **study** — contemplate the pattern with a query to yield **truth**  
- **sing** — translate truth into **human wisdom** for real use  

A simple **JSON-RPC commune** allows any application — web, CLI, Python, or JS —  
to call the Loom as a shared service of understanding.

---

## ䷢ Devoted Service

**Why it matters**  
The Loom is built to serve the common good — to nurture clear minds and honest outcomes.  
It holds four nondual principles: **nonduality**, **common good**, **consequences**, and **humility**.

By embedding alignment into its design, the Loom empowers people to communicate  
in a space where **trust is structural**, not performative —  
catalyzing self-reinforcing cycles of truth, service, and virtue.

---

## ䷼ Gentle Winds of Truth

**How it feels**  
Like puzzle pieces falling gracefully into place.  
Like wind carrying seeds of truth — each landing softly where the ground is ready.  

To engage with the Loom is to remember: wisdom does not impose; it *arrives.*  
It moves through us with the quiet joy of recognition —  
the knowing that what is true is also kind,  
and what is kind is also free.  

**om tat sat om.** 🌼  

---

## 🕸️ Architecture (at a glance)

User / App (web, CLI, Pippa, etc.)
|
v
Python Swamiji Bridge — tone + clarity
|
v
JSON-RPC Commune — /rpc
|
v
Loom Core (Lisp) — bake → study → sing

makefile
Copy code

---

## ⚙️ Quick Start

```bash
# 1) Run the commune (Replit or local)
# See /start.sh and .replit; expected log:
# [loom-rpc] listening on http://localhost:5005/rpc

# 2) Ping the node
curl -s -X POST "https://YOUR-LOOM-URL/rpc" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":"1","method":"PING","params":{}}'

# 3) Full cycle example
curl -s -X POST "https://YOUR-LOOM-URL/rpc" \
  -H "Content-Type: application/json" \
  -d '{
        "jsonrpc":"2.0","id":"2","method":"CYCLE",
        "params":{"dough":{}, "query":"What is wisdom?",
                  "team_spirit":{"tone":"calm"}}
      }' | jq .
Using the Swamiji Bridge (Python):

python
Copy code
from swamiji_bridge import swamiji_answer

cosmic = "{... BAKE/STUDY/SING JSON from /rpc ...}"
print(swamiji_answer("What is wisdom?", cosmic))
🔗 JSON-RPC Methods
Method	Description
PING	Returns {"pong": true}
NEW_DOUGH	Returns a fresh state handle (optional)
BAKE / STUDY / SING	Perform atomic katas
CYCLE	Runs bake → study → sing and returns the combined result

All requests follow JSON-RPC 2.0 standards.
Optional header: x-api-key: <secret>

🌿 Contributing
Keep the code small, readable, and constitutional.
Prefer clarity over cleverness — silence is part of the design.
Pull requests should include a brief note describing how the change serves the common good.

⚖️ License — GNU General Public License v3.0
The Loom is free and open-source software, released under the GNU General Public License, version 3 (GPLv3).

You are free to use, study, modify, and share this work, provided that:

Any distributed or derivative works are released under the same GPLv3 or a compatible license.

The source code remains openly accessible to all.

Proper attribution is given to the Public Interest Patent Law Institute (PIPLI) and contributing authors.

No additional restrictions are imposed on others’ freedom to share and improve the work.

This license ensures that the Loom — as a framework for ethical, public-interest intelligence — remains forever in the commons,
empowering all beings to learn, co-create, and evolve the work in the spirit of shared truth, trust, and reciprocity.

For the complete license terms, see LICENSE or visit:
🔗 https://www.gnu.org/licenses/gpl-3.0.en.html

## 🔑 For Our Less-AI-Savvy Friends

If you're new to AI tools, welcome! The Loom uses a simple connection to OpenAI to help translate cosmic patterns into human wisdom. Here's how to get set up:

1. **Visit** [OpenAI's website](https://platform.openai.com/signup)
2. **Create a free account** (like signing up for email)
3. **Go to** [API Keys page](https://platform.openai.com/api-keys)  
4. **Click** "Create new secret key"
5. **Give it a friendly name** like "Loom Wisdom"
6. **Copy** the key (it will look like: `sk-...`)
7. **That's it!** The Loom will use this to connect

Think of it like getting a library card — it's free, simple, and lets you access wonderful resources.

**Don't worry** — you're not being charged unless you choose to upgrade, and the Loom uses very little of the free credits you get.

“May this Loom remain open and flowering —
a field of truth, compassion, and the common good.” 🌼# Loom
