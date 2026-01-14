# RAG Learning - Production-Grade System

Learn **Retrieval-Augmented Generation (RAG)** from scratch with hands-on lessons.

---

## 🚀 Quick Start

### Option A: Docker (Recommended - Clean & Isolated)
```bash
# Start the environment
docker-compose up -d rag-learning

# Enter the container
docker-compose exec rag-learning bash

# Inside container - start learning!
cd lessons/01-rag-fundamentals
python simple_example.py
python real_embeddings_example.py
```

**See [docs/guides/DOCKER_GUIDE.md](docs/guides/DOCKER_GUIDE.md) for complete Docker instructions**

### Option B: Local Installation
```bash
# 1. Activate environment
source .venv/bin/activate

# 2. Install all dependencies
pip install -r requirements.txt

# 3. Start learning
cd lessons/01-rag-fundamentals
python simple_example.py
```

---

## 📚 Learning Path

```
lessons/
├── 01-rag-fundamentals/     ← START HERE
├── 02-text-chunking/
├── 03-embeddings/
├── 04-vector-databases/
├── 05-semantic-search/
├── 06-llm-integration/
└── 07-production-system/
```

**Each lesson has:**
- `README.md` - Concepts explained
- `simple_example.py` - Working code
- `exercise.py` - Practice problem

---

## 📖 What You'll Learn

1. **RAG Fundamentals** - What, why, and how
2. **Text Chunking** - Split documents intelligently
3. **Embeddings** - Convert text to vectors (Hugging Face - FREE)
4. **Vector Databases** - Store and search efficiently (ChromaDB - FREE)
5. **Semantic Search** - Find by meaning, not keywords
6. **LLM Integration** - Generate answers (Hugging Face/Ollama - FREE)
7. **Production** - Deploy with FastAPI (optional: AWS)

**Time**: 4-6 hours total | 30-60 min per lesson
**Cost**: 100% FREE (using open-source tools)

---

## 🔧 Setup

**Prerequisites:**
- Python 3.11+
- Virtual environment: `.venv` (already created)
- **No AWS account needed!** (100% free, open-source)

**🔐 Security Note:**
- This repo is PUBLIC - never commit secrets!
- Use `.env` file for API keys (see [docs/setup/SECRETS_MANAGEMENT.md](docs/setup/SECRETS_MANAGEMENT.md))
- `.env` is already in `.gitignore`

**Dependencies** (installed per lesson):
- Lesson 1: `numpy`
- Lesson 3: `sentence-transformers` (Hugging Face embeddings)
- Lesson 4: `chromadb` (local vector database)
- Lesson 6: `huggingface-hub` or Ollama (free LLMs)
- Lesson 7: `fastapi`, `uvicorn`

---

## 📝 Important Files

- **`README.md`** (this file) - Project overview
- **`START_HERE.md`** - Quick start guide (read this first!)
- **`docs/`** - All documentation (setup guides, references)
- **`tests/`** - Test scripts
- **`lessons/`** - Learning materials
- **`requirements.txt`** - All dependencies

---

## 🎯 Learning Philosophy

**Concept → Code → Practice → Production**

1. Understand WHY before HOW
2. See working examples
3. Build it yourself
4. Learn best practices

---

---

## 📚 Documentation

All documentation is organized in the `docs/` folder:

- **[START_HERE.md](START_HERE.md)** - Quick start guide
- **[docs/guides/QUICKSTART.md](docs/guides/QUICKSTART.md)** - Command reference
- **[docs/setup/](docs/setup/)** - Setup guides (AWS, Bedrock, API keys)
- **[docs/README.md](docs/README.md)** - Complete documentation index

---

**Ready?** Start with **[START_HERE.md](START_HERE.md)**

**Need help?** Check **[docs/README.md](docs/README.md)** for all guides

