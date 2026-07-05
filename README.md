# MemoryOS-Project
MemoryOS is an intelligent memory system designed to store, structure, and surface your ideas, notes, conversations, and context when you need them.
# 📖 Study Buddy — AI-Powered Notes Q&A

> **Hackathon Submission** — "The Hangover Part AI: Where's My Context?" by WeMakeDevs × Cognee

---

## 🧠 The Problem

Standard AI chatbots suffer from **AI Amnesia** — every session starts from zero. You upload your notes, ask questions, close the tab, and tomorrow it remembers nothing. Students have to re-upload, re-explain, and re-query everything from scratch, every single time.

## 💡 The Solution

**Study Buddy** gives AI a permanent memory for your notes using [Cognee](https://cognee.ai).

Load your notes once → Ask questions forever. Cognee builds a knowledge graph from your documents that persists across every session. Your Study Buddy never forgets.

---

## 🎯 How It Works

```
Your Notes (.txt files)
        ↓
  cognee.remember()       ← Ingests, chunks, extracts entities, builds knowledge graph
        ↓
  Permanent Memory        ← Stored as a hybrid graph-vector knowledge store
        ↓
  cognee.recall()         ← Searches memory with natural language questions
        ↓
    Your Answer ✅
```

---

## ✨ Features

- **Load any `.txt` notes** — biology, history, math, anything
- **Ask questions in plain English** — no commands, no syntax
- **Persistent memory** — notes stay in the knowledge graph forever, no re-uploading
- **Powered by Cognee** — uses `remember()` and `recall()` from Cognee's memory lifecycle API

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/study-buddy.git
cd study-buddy
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
Create a file called `.env` in the project folder:
```
OPENAI_API_KEY=your_openai_api_key_here
```
Get a free API key at [platform.openai.com](https://platform.openai.com)

### 4. Add your notes
Put your `.txt` note files inside the `notes/` folder.
A sample biology notes file is included to try immediately.

### 5. Run Study Buddy
```bash
python study_buddy.py
```

---

## 📋 Usage

```
==================================================
  📖 STUDY BUDDY — AI-Powered Notes Q&A
  Powered by Cognee Memory
==================================================

What would you like to do?
  1 → Load / Reload my notes into memory
  2 → Ask a question about my notes
  3 → Exit
```

**Step 1:** Choose `1` to load your notes (only needs to be done once)

**Step 2:** Choose `2` and ask any question:
```
Ask your question: What is the powerhouse of the cell?

💡 Answer:
──────────────────────────────────────────────────
The mitochondria is the powerhouse of the cell.
It produces energy (ATP) through cellular respiration.
──────────────────────────────────────────────────
```

**Step 3:** Next time you run the app — your notes are already in memory. Just ask!

---

## 🧩 Cognee Memory Lifecycle Used

| Cognee Operation | Where Used |
|---|---|
| `cognee.remember()` | Ingesting note files into the knowledge graph |
| `cognee.recall()` | Answering natural language questions from memory |

---

## 📁 Project Structure

```
study-buddy/
├── study_buddy.py          # Main application
├── requirements.txt        # Dependencies
├── .env                    # Your API key (NOT uploaded to GitHub)
├── .gitignore              # Keeps .env safe
├── README.md               # This file
└── notes/
    └── sample_biology_notes.txt   # Sample notes to try
```

---

## 🔮 Future Scope

- Add `cognee.improve()` to enrich the knowledge graph as more notes are added
- Web UI with Streamlit for non-technical users
- Support for PDF note uploads
- Integration with Cognee Cloud for cross-device memory sync
- Connect with Codex agent for automatic note-taking during study sessions

---

## 🛠️ Tech Stack

- **Python** — core language
- **Cognee** — AI memory layer (graph-vector knowledge store)
- **OpenAI** — LLM and embeddings backend
- **python-dotenv** — environment variable management

---

## ⚠️ AI Disclosure

This project was built with assistance from **Claude (Anthropic)** as an AI coding mentor and pair programmer, in accordance with the hackathon's AI disclosure rules.

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

*Built for "The Hangover Part AI: Where's My Context?" Hackathon by WeMakeDevs × Cognee*
*Your AI woke up in Vegas with no memory. Study Buddy never will.* 🎰
