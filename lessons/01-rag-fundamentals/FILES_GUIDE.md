# 📚 File Guide - Which File to Use?

This lesson has multiple files. Here's what each one does and when to use it.

---

## 📖 Learning Materials

### 1. `CONCEPTS.md` ⭐ START HERE
**What**: Beginner-friendly explanations of core concepts  
**Topics**:
- What are vectors/embeddings?
- How are vectors created?
- What is cosine similarity?
- Trigonometry refresher (sin, cos, tan)
- Complete math formulas with examples

**When to read**: Before running any code, especially if you're new to embeddings

---

### 2. `MATH_CHEATSHEET.md`
**What**: Quick reference for formulas  
**Topics**:
- Cosine similarity formula
- Step-by-step calculations
- Python implementations
- Common trigonometry values

**When to use**: Keep open while coding as a reference

---

### 3. `README.md`
**What**: RAG system overview  
**Topics**:
- What problem does RAG solve?
- The two-phase pipeline (indexing + querying)
- RAG vs alternatives
- When to use RAG

**When to read**: After CONCEPTS.md, before running examples

---

## 💻 Code Examples

### 4. `simple_example.py` ⭐ RUN THIS FIRST
**What**: Educational RAG demo with simplified embeddings  
**Dependencies**: Only `numpy` (already installed)  
**Embeddings**: Fake/simplified (keyword counting)  
**Purpose**: Learn RAG concepts without complexity

**Pros**:
- ✅ No downloads, runs instantly
- ✅ Easy to understand (simple keyword matching)
- ✅ Shows RAG pipeline clearly

**Cons**:
- ❌ Not production-quality
- ❌ Embeddings are simplified

**Run**:
```bash
python simple_example.py
```

---

### 5. `real_embeddings_example.py` ⭐ RUN THIS SECOND
**What**: RAG demo with REAL Hugging Face embeddings  
**Dependencies**: `sentence-transformers` (80MB download)  
**Embeddings**: Real neural network (all-MiniLM-L6-v2)  
**Purpose**: See how production RAG actually works

**Pros**:
- ✅ Real embeddings (384 dimensions)
- ✅ Accurate semantic search
- ✅ Production-quality results
- ✅ FREE (Hugging Face)

**Cons**:
- ❌ Requires download (~80MB first time)
- ❌ Slightly slower

**Install & Run**:
```bash
pip install sentence-transformers
python real_embeddings_example.py
```

---

### 6. `embedding_internals.py` ⭐ ADVANCED
**What**: Deep dive into what happens inside the embedding model  
**Dependencies**: `sentence-transformers`, `transformers`  
**Purpose**: Understand tokenization, token IDs, neural network processing

**Shows**:
- ✅ Tokenization step-by-step
- ✅ Token → ID conversion
- ✅ What happens in the neural network
- ✅ Normalization process
- ✅ Similarity calculations

**Run**:
```bash
pip install sentence-transformers transformers
python embedding_internals.py
```

---

### 7. `exercise.py`
**What**: Practice building your own RAG system  
**Dependencies**: `numpy`  
**Purpose**: Hands-on practice

**Task**: Build a product search system using what you learned

**Run**:
```bash
python exercise.py
```

---

## 🎯 Recommended Learning Path

### For Beginners (No ML Background)
```
1. Read CONCEPTS.md          (30 min) - Understand vectors, embeddings, math
2. Read README.md             (15 min) - Understand RAG
3. Run simple_example.py      (5 min)  - See basic RAG
4. Install sentence-transformers
5. Run real_embeddings_example.py (5 min) - See real RAG
6. Run embedding_internals.py (10 min) - Understand internals
7. Do exercise.py             (30 min) - Practice
```

### For Experienced Developers
```
1. Skim CONCEPTS.md           (10 min)
2. Run real_embeddings_example.py (5 min)
3. Run embedding_internals.py (10 min)
4. Do exercise.py             (20 min)
```

### For Quick Demo
```
1. Run simple_example.py      (2 min)
2. Run real_embeddings_example.py (5 min)
```

---

## 📊 File Comparison

| File | Dependencies | Embeddings | Purpose | Time |
|------|-------------|------------|---------|------|
| `simple_example.py` | numpy | Fake (keywords) | Learn concepts | 5 min |
| `real_embeddings_example.py` | sentence-transformers | Real (384D) | See production | 5 min |
| `embedding_internals.py` | sentence-transformers | Real (384D) | Deep dive | 10 min |
| `exercise.py` | numpy | You implement! | Practice | 30 min |

---

## 🔧 Installation Commands

### Minimal (Simple Example Only)
```bash
# Already installed
# Just run: python simple_example.py
```

### Full (All Examples)
```bash
pip install sentence-transformers transformers
```

### Individual
```bash
# For real_embeddings_example.py
pip install sentence-transformers

# For embedding_internals.py
pip install sentence-transformers transformers
```

---

## 💡 Which File Answers Your Question?

| Question | File |
|----------|------|
| What are vectors? | `CONCEPTS.md` |
| How is text converted to vectors? | `CONCEPTS.md`, `embedding_internals.py` |
| What is cosine similarity? | `CONCEPTS.md`, `MATH_CHEATSHEET.md` |
| How does RAG work? | `README.md` |
| Show me a simple RAG demo | `simple_example.py` |
| Show me real embeddings | `real_embeddings_example.py` |
| What happens inside the model? | `embedding_internals.py` |
| How do I build my own? | `exercise.py` |

---

**Start with**: `CONCEPTS.md` → `simple_example.py` → `real_embeddings_example.py`

**Then explore**: `embedding_internals.py` for deep understanding!

