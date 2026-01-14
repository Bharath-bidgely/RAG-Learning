# Lesson 1: RAG Fundamentals

**Time**: 30-45 minutes

## 🚀 Quick Start

### Option A: Simple Version (No Dependencies)
```bash
# 1. Read concepts
cat CONCEPTS.md

# 2. Run simple example (uses fake embeddings for learning)
python simple_example.py
```

### Option B: Real Hugging Face Embeddings
```bash
# 1. Install dependencies
pip install sentence-transformers

# 2. Run with REAL embeddings
python real_embeddings_example.py

# 3. See what happens inside the model
python embedding_internals.py
```

### Then Practice
```bash
python exercise.py
```

---

## 🎯 What You'll Learn

1. What problem RAG solves
2. How RAG works (the pipeline)
3. When to use RAG vs other approaches
4. The key components of a RAG system

---

## 📖 The Problem: Information Overload

### Scenario

You work at a company with **10,000 documents** (policies, manuals, FAQs, etc.).
A customer asks: **"What is your refund policy?"**

You want to use an LLM (like GPT-4 or Claude) to answer, but you face these challenges:

### ❌ Challenge 1: Token Limits

**LLMs have input limits:**
- GPT-4 Turbo: ~128,000 tokens (~100 pages)
- Claude 3: ~200,000 tokens (~150 pages)

**Your 10,000 documents** = ~5,000,000 tokens

**Problem**: You can't fit all documents into the LLM!

### ❌ Challenge 2: Cost

Even if you could fit everything:
- GPT-4: $0.01 per 1,000 input tokens
- 5,000,000 tokens = **$50 per question!**

### ❌ Challenge 3: Accuracy

When you give an LLM too much information:
- It gets confused ("lost in the middle" problem)
- It may miss the relevant part
- Response quality decreases

### ❌ Challenge 4: Freshness

If you fine-tune the LLM on your documents:
- Costs $10,000+
- Takes weeks
- When documents update, you must retrain
- Old information gets "baked in"

---

## ✅ The Solution: RAG (Retrieval-Augmented Generation)

**RAG = Smart Search + LLM**

Instead of sending ALL documents, RAG:
1. **Finds** the 5 most relevant paragraphs (retrieval)
2. **Sends** only those 5 paragraphs to the LLM (augmented)
3. **Generates** an answer based on that context (generation)

### The Magic

```
10,000 documents (5M tokens) → RAG → 5 paragraphs (2,000 tokens)
```

**Cost**: $0.02 instead of $50 ✅
**Speed**: 2 seconds instead of 30 seconds ✅
**Accuracy**: Higher (focused context) ✅
**Freshness**: Always current (no retraining) ✅

---

## 🔄 How RAG Works: The Two-Phase Pipeline

### Phase 1: Indexing (One-Time Setup)

This happens ONCE when you add documents to your system:

```
┌─────────────┐
│  Document   │  "Our refund policy allows returns within 30 days..."
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Chunk     │  Split into smaller pieces (we'll learn why in Lesson 2)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Embed     │  Convert text to numbers (vectors) - Lesson 3
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Store     │  Save in vector database - Lesson 4
└─────────────┘
```

**Result**: Your documents are now "searchable by meaning"

### Phase 2: Querying (Every User Question)

This happens EVERY TIME a user asks a question:

```
┌─────────────┐
│  Question   │  "What's the refund policy?"
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Embed     │  Convert question to vector
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Search    │  Find similar vectors in database
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Retrieve   │  Get top 5 most relevant chunks
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ LLM + Context│ "Based on these 5 paragraphs, answer: ..."
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Answer    │  "Our refund policy allows..."
└─────────────┘
```

---

## 🧠 Key Concept: Semantic Search

**Traditional Search (Keyword Matching)**
```
Question: "How do I get my money back?"
Search: Looks for exact words "money" and "back"
Result: ❌ Misses documents about "refunds" and "returns"
```

**Semantic Search (Meaning Matching)**
```
Question: "How do I get my money back?"
Embedding: [0.2, 0.8, 0.1, ...] (vector representing meaning)
Search: Finds vectors with similar meaning
Result: ✅ Finds "refund policy", "return process", "reimbursement"
```

**This is the power of embeddings!** (We'll learn how in Lesson 3)

---

## 📊 RAG vs Alternatives

| Approach | Cost | Speed | Accuracy | Freshness | Use Case |
|----------|------|-------|----------|-----------|----------|
| **RAG** | $ | Fast | High | Always current | ✅ Most cases |
| Fine-tuning | $$$$ | Slow | High | Stale | Specialized domains |
| Prompt stuffing | $$$ | Slow | Low | Current | Small datasets |
| No context | $ | Fast | Low | N/A | General knowledge |

---

## 🎓 What You'll Build

In `simple_example.py`, you'll build a minimal RAG system that:
1. Takes 3 sample documents
2. Chunks them
3. Creates embeddings (using AWS Bedrock)
4. Stores in a simple in-memory database
5. Answers questions by retrieving relevant chunks

**Next**: Open `simple_example.py` to see RAG in action!

