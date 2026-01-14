# Project Context & Progress Tracker

**Last Updated**: 2026-01-11 (Session 1 - Updated with beginner concepts)

---

## 🎯 Project Goal

Build a **production-grade RAG (Retrieval-Augmented Generation) learning system** that:
- Chunks large datasets from databases
- Finds relevant data using semantic search
- Passes only relevant context to LLM (avoiding token explosion)
- Uses AWS infrastructure (not local)
- Serves as both a POC and learning platform
- Maintains production-grade code quality

---

## 👤 User Profile & Requirements

### Learning Style
- **Beginner level** - treat as someone new to RAG
- **Step-by-step approach** - explain concept → show code → practice
- **Deep understanding** - architect-level design thinking
- **No rushing** - take time to learn properly
- **Hands-on** - learn by building

### Technical Preferences
- **Language**: Python
- **Framework**: FastAPI, LangChain
- **Cloud**: AWS (free tier where possible)
- **AWS Profile**: `AwsBedrock` (us-east-1)
- **Virtual Environment**: `.venv` for AWS deployment compatibility
- **Code Quality**: Production-grade, framework-based

### Key User Quotes
1. "This is for RAG learning with vector databases, semantic search with relevance and closeness/quality matching along with embeddings"
2. "Chunk a large dataset, find relevant data to pass to LLM instead of exploding tokens"
3. "Keep it product grade and framework based so I learn how to code in production"
4. "Use AWS account for infra and testing instead of local"
5. "Focus on vector, embedding, searching, chunking - just use AWS for infra"
6. "Keep folder structure clean and neat - product grade structure and good coding standards"
7. "I need to learn - explain concept first, then code, then move to next step slowly 1 by 1"
8. "Treat me as beginner"

---

## 📊 Current Progress

### ✅ Completed
1. **Project Setup**
   - Created `.venv` virtual environment
   - Set up `requirements.txt` organized by lesson
   - Configured `.env.example` with AWS settings
   - Created `.gitignore`
   - Created `CONTEXT.md` for session persistence

2. **Architecture Design**
   - Designed RAG system architecture diagram
   - Designed AWS cloud architecture (Bedrock, OpenSearch, RDS, ElastiCache, S3, ECS)
   - Created project structure diagram

3. **Project Restructure**
   - Cleaned up directories for fresh, learning-focused start
   - Created lesson-based learning structure (7 lessons)
   - Set up lesson folders: 01-rag-fundamentals through 07-production-system

4. **Lesson 1: RAG Fundamentals** ✅
   - Created `CONCEPTS.md` - **Beginner-friendly explanations** (vectors, cosine similarity, embeddings)
   - Created `README.md` - RAG overview and pipeline
   - Created `simple_example.py` - Working RAG demo (~150 lines)
   - Created `exercise.py` - Practice problem with TODOs
   - **Updated to use FREE tools** (Hugging Face instead of AWS Bedrock)
   - Covers: What is RAG, why use it, semantic search, embeddings basics

### 🔄 In Progress
- **User is now ready to start Lesson 1**
- Next: User reads README → runs example → does exercise

### ⏳ Pending
- Lesson 2: Text Chunking (fixed, recursive, semantic)
- Lesson 3: Embeddings (AWS Bedrock Titan)
- Lesson 4: Vector Databases (ChromaDB, OpenSearch)
- Lesson 5: Semantic Search (hybrid, re-ranking)
- Lesson 6: LLM Integration (AWS Bedrock Claude)
- Lesson 7: Production System (FastAPI, AWS deployment)
- AWS infrastructure deployment
- End-to-end testing

---

## 🏗️ Architecture Decisions

### 🎯 Key Decisions
1. **100% FREE Tools**: Using Hugging Face (sentence-transformers) instead of AWS Bedrock
2. **Beginner-Friendly**: Added CONCEPTS.md to explain vectors, embeddings, cosine similarity from scratch
3. **Learning-First**: 7 progressive lessons, each self-contained
4. **No Cloud Required**: ChromaDB (local), Hugging Face (free API), Ollama (local LLM)
5. **AWS Optional**: Lessons will show AWS alternatives, but not required

### Technology Stack (FREE Version)
- **Embeddings**: Sentence Transformers (Hugging Face) - FREE
- **Vector DB**: ChromaDB (local) - FREE
- **LLM**: Hugging Face Inference API or Ollama - FREE
- **Backend**: FastAPI (Lesson 7)
- **Optional AWS**: Bedrock, OpenSearch (for those who want cloud deployment)

---

## 📁 Current Project Structure

```
RAG-Learning/
├── .venv/                           # Virtual environment
├── lessons/                         # Learning modules (step-by-step)
│   ├── 01-rag-fundamentals/        # ✅ COMPLETE
│   │   ├── README.md               # Concept explanation
│   │   ├── START_HERE.md           # Quick start guide
│   │   ├── simple_example.py       # Working demo
│   │   └── exercise.py             # Practice problem
│   ├── 02-text-chunking/           # ⏳ Next
│   ├── 03-embeddings/
│   ├── 04-vector-databases/
│   ├── 05-semantic-search/
│   ├── 06-llm-integration/
│   └── 07-production-system/
├── .env.example                    # Environment template
├── .gitignore                      # Git ignore rules
├── requirements.txt                # Python dependencies (organized by lesson)
├── README.md                       # Project overview & learning path
├── CONTEXT.md                      # This file - session context
└── main.py                         # Original placeholder file
```

---

## 🎓 Learning Path

### Lesson Structure (Each Lesson)
1. **README.md** - Concept explanation (What & Why)
2. **simple_example.py** - Basic working code
3. **exercise.py** - Practice problem
4. **solution.py** - Production-grade implementation

### Lesson Topics
1. **RAG Fundamentals** - What is RAG? Why use it? The pipeline
2. **Text Chunking** - Fixed, Recursive, Semantic strategies
3. **Embeddings** - Vectors, similarity, AWS Bedrock Titan
4. **Vector Databases** - ChromaDB, OpenSearch, indexing
5. **Semantic Search** - Similarity, hybrid search, re-ranking
6. **LLM Integration** - AWS Bedrock Claude, prompts, tokens
7. **Production System** - FastAPI, AWS deployment, monitoring

---

## 🔑 Key Concepts to Cover

### Core RAG Components
1. **Chunking** - Breaking documents into searchable pieces
2. **Embeddings** - Converting text to vectors
3. **Vector Storage** - Efficient similarity search
4. **Retrieval** - Finding relevant chunks
5. **Generation** - LLM creates answer from context

### Why RAG?
- Avoids token limits (can't send 10,000 docs to LLM)
- Reduces cost (only send relevant chunks)
- Always up-to-date (no retraining needed)
- More accurate (focused context)

---

## 🔧 AWS Configuration

### Profile Details
- **Profile Name**: `AwsBedrock`
- **Region**: `us-east-1`
- **Access Key**: Configured via AWS CLI (stored in ~/.aws/credentials)

### Models to Use
- **LLM**: `anthropic.claude-3-sonnet-20240229-v1:0`
- **Embeddings**: `amazon.titan-embed-text-v2:0`

---

## 📝 Next Steps (When Resuming)

### If User Completed Lesson 1:
1. Ask if they understood the concepts
2. Review their exercise solution
3. Move to Lesson 2: Text Chunking
   - Create README.md explaining chunking strategies
   - Implement fixed_chunking.py
   - Implement recursive_chunking.py
   - Implement semantic_chunking.py
   - Create exercise

### If User Just Starting:
1. Direct them to: `lessons/01-rag-fundamentals/START_HERE.md`
2. Ensure they:
   - Read README.md (concepts)
   - Run simple_example.py (see it work)
   - Complete exercise.py (practice)
3. Answer any questions about RAG fundamentals

### Current Session Status:
- **Lesson 1 is ready** for user to start
- User should run: `cd lessons/01-rag-fundamentals && python simple_example.py`
- Dependencies needed: `pip install numpy==1.26.3`

---

## 💡 Important Notes

- **Learning pace**: Slow and thorough, not rushed
- **Code quality**: Production-grade, well-commented
- **Explanations**: Beginner-friendly with diagrams
- **AWS focus**: Use cloud services, not local-only solutions
- **Context preservation**: Update this file every 15 minutes

---

## 🗣️ User Feedback & Adjustments

- User wants concept-first, then code approach ✅
- User wants clean folder structure ✅
- User prefers AWS over local development ✅
- User wants to learn at architect level ✅

---

**Status**: ✅ Lesson 1 Complete - Ready for User to Start Learning
**Next Action**: User should start Lesson 1, then we build Lesson 2

---

## 📚 Lesson 1 Summary (For Quick Reference)

### What User Will Learn:
1. **The RAG Problem**: Why we can't send all documents to LLM
2. **The RAG Solution**: Smart search + focused context
3. **Embeddings**: Text → vectors for similarity search
4. **Semantic Search**: Finding by meaning, not keywords

### Files Created:
- `README.md` - Full concept explanation with examples
- `START_HERE.md` - Step-by-step instructions
- `simple_example.py` - Working RAG demo (100 lines, heavily commented)
- `exercise.py` - Practice building product search

### Key Code Concepts:
- `simple_embedding()` - Convert text to vector
- `cosine_similarity()` - Measure vector similarity
- `SimpleVectorDB` - In-memory vector storage
- `simple_rag()` - Complete RAG pipeline

### Success Criteria:
User can answer:
- What problem does RAG solve?
- What are embeddings?
- How does semantic search work?
- What are the two RAG phases?

