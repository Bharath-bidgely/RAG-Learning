# 🚀 Quick Start Guide

## ✅ Installation Complete!

Your RAG Learning environment is now set up and ready to use!

## 📦 What's Installed

- **Python 3.13** with virtual environment
- **PyTorch** - Deep learning framework
- **Transformers** - Hugging Face models
- **ChromaDB** - Vector database (local, FREE)
- **Sentence Transformers** - Embeddings
- **FastAPI** - Web framework
- All development tools (pytest, black, ruff)

## 🎯 Next Steps

### 1. Activate Your Environment

Every time you work on this project, activate the virtual environment:

```bash
cd /Users/admin/RAG-Learning
source .venv/bin/activate
```

### 2. Start Learning!

The lessons are organized in the `lessons/` directory:

```
lessons/
├── lesson1_embeddings/          # Start here!
├── lesson2_semantic_search/
├── lesson3_chunking/
├── lesson4_vector_databases/
├── lesson5_retrieval/
├── lesson6_generation/
└── lesson7_production/
```

### 3. Run Your First Example

```bash
# Activate environment
source .venv/bin/activate

# Navigate to lesson 1
cd lessons/lesson1_embeddings

# Run the example
python basic_embeddings.py
```

## 📚 Learning Path

1. **Lesson 1: Embeddings** - Understand how text becomes vectors
2. **Lesson 2: Semantic Search** - Find similar documents
3. **Lesson 3: Chunking** - Split documents intelligently
4. **Lesson 4: Vector Databases** - Store and query embeddings
5. **Lesson 5: Retrieval** - Build a retriever
6. **Lesson 6: Generation** - Add LLM generation
7. **Lesson 7: Production** - Deploy your RAG system

## 🔧 Useful Commands

```bash
# Activate environment
source .venv/bin/activate

# Deactivate environment
deactivate

# Run tests
pytest

# Format code
black .

# Lint code
ruff check .

# Install new packages
pip install <package-name>
```

## 💡 Tips

- **Always activate the virtual environment** before working
- **Start with Lesson 1** - they build on each other
- **Run the examples** - hands-on learning is best
- **Experiment** - modify the code and see what happens
- **Check the README** in each lesson for detailed explanations

## 🆘 Troubleshooting

### Virtual Environment Not Activated?
```bash
# You should see (.venv) in your terminal prompt
# If not, run:
source .venv/bin/activate
```

### Import Errors?
```bash
# Make sure you're in the virtual environment
# Then reinstall requirements:
pip install -r requirements.txt
```

### Need to Start Fresh?
```bash
# Remove virtual environment
rm -rf .venv

# Create new one
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 🎓 Ready to Learn!

You're all set! Head to `lessons/lesson1_embeddings/` and start your RAG journey!

```bash
cd lessons/lesson1_embeddings
cat README.md  # Read the lesson overview
python basic_embeddings.py  # Run your first example
```

Happy learning! 🚀

