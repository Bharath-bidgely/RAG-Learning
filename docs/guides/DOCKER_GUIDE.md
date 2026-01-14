# 🐳 Docker Setup Guide

Run the entire RAG learning environment in Docker - no need to install anything on your laptop!

---

## 🚀 Quick Start

### Option 1: Docker Compose (Recommended)

```bash
# Build and start the container
docker-compose up -d rag-learning

# Enter the container
docker-compose exec rag-learning bash

# Now you're inside the container! Run any lesson:
cd lessons/01-rag-fundamentals
python simple_example.py
python real_embeddings_example.py
```

### Option 2: Docker Only

```bash
# Build the image
docker build -t rag-learning .

# Run the container
docker run -it -v $(pwd):/app rag-learning

# You're now inside the container
python lessons/01-rag-fundamentals/simple_example.py
```

---

## 📦 What's Included

The Docker image includes:
- ✅ Python 3.11
- ✅ All dependencies from `requirements.txt`
- ✅ Hugging Face models (cached)
- ✅ NumPy, Sentence Transformers, PyTorch
- ✅ ChromaDB, FastAPI, and more

**No installation needed on your laptop!**

---

## 🎯 Common Commands

### Start the Environment
```bash
# Start all services (RAG learning + ChromaDB + Ollama)
docker-compose up -d

# Start only RAG learning environment
docker-compose up -d rag-learning
```

### Enter the Container
```bash
# Interactive shell
docker-compose exec rag-learning bash

# Run a specific script
docker-compose exec rag-learning python lessons/01-rag-fundamentals/simple_example.py
```

### Stop the Environment
```bash
# Stop all services
docker-compose down

# Stop and remove volumes (clean slate)
docker-compose down -v
```

### View Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f rag-learning
```

---

## 📚 Running Lessons in Docker

### Lesson 1: RAG Fundamentals
```bash
# Enter container
docker-compose exec rag-learning bash

# Inside container:
cd lessons/01-rag-fundamentals

# Simple example (no downloads)
python simple_example.py

# Real embeddings (downloads model first time ~80MB)
python real_embeddings_example.py

# Deep dive
python embedding_internals.py
```

### Lesson 4: Vector Databases
```bash
# ChromaDB is already running on port 8000
# Your code can connect to: http://chromadb:8000

# Or from your laptop: http://localhost:8000
```

### Lesson 6: LLM Integration
```bash
# Ollama is running on port 11434

# Pull a model (inside ollama container)
docker-compose exec ollama ollama pull llama2

# Use it in your code
# Connect to: http://ollama:11434
```

---

## 🔧 Advanced Usage

### Rebuild After Changing Dependencies
```bash
# Rebuild the image
docker-compose build rag-learning

# Restart
docker-compose up -d rag-learning
```

### Access Jupyter Notebook (Optional)
```bash
# Install Jupyter in container
docker-compose exec rag-learning pip install jupyter

# Start Jupyter
docker-compose exec rag-learning jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

# Access at: http://localhost:8888
```

### Mount Custom Data
```bash
# Edit docker-compose.yml and add:
volumes:
  - ./data:/app/data
  - ./models:/app/models
```

---

## 🗂️ Docker Services

### 1. `rag-learning` (Main Container)
- **Purpose**: Run all Python code
- **Volumes**: Project mounted at `/app`
- **Cache**: Hugging Face models cached

### 2. `chromadb` (Vector Database)
- **Purpose**: Store embeddings (Lesson 4+)
- **Port**: 8000
- **Access**: `http://localhost:8000`

### 3. `ollama` (Local LLM)
- **Purpose**: Run LLMs locally (Lesson 6)
- **Port**: 11434
- **Access**: `http://localhost:11434`

---

## 💾 Data Persistence

Docker volumes ensure data persists:
- `huggingface-cache`: Downloaded models (won't re-download)
- `chromadb-data`: Vector database storage
- `ollama-data`: LLM models

**Your code changes are immediately reflected** (project is mounted as volume)

---

## 🐛 Troubleshooting

### Container won't start
```bash
# Check logs
docker-compose logs rag-learning

# Rebuild
docker-compose build --no-cache rag-learning
```

### Out of disk space
```bash
# Clean up unused images
docker system prune -a

# Remove volumes (WARNING: deletes data)
docker-compose down -v
```

### Model download fails
```bash
# Enter container
docker-compose exec rag-learning bash

# Manually download
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"
```

### Permission issues
```bash
# Run as your user (add to docker-compose.yml)
user: "${UID}:${GID}"
```

---

## 🎓 Workflow Example

```bash
# 1. Start everything
docker-compose up -d

# 2. Enter the learning environment
docker-compose exec rag-learning bash

# 3. Navigate to lesson
cd lessons/01-rag-fundamentals

# 4. Run examples
python simple_example.py
python real_embeddings_example.py

# 5. Edit code on your laptop (changes reflect immediately)
# (Use your favorite editor - VS Code, PyCharm, etc.)

# 6. Run again to see changes
python real_embeddings_example.py

# 7. When done
exit
docker-compose down
```

---

## 🔑 Key Benefits

✅ **Clean laptop** - Nothing installed locally  
✅ **Consistent environment** - Same setup everywhere  
✅ **Easy cleanup** - `docker-compose down -v`  
✅ **Isolated** - Won't mess with your system  
✅ **Reproducible** - Same results every time  
✅ **Includes databases** - ChromaDB, Ollama ready to use  

---

## 📝 Next Steps

1. **Start the environment**: `docker-compose up -d`
2. **Enter the container**: `docker-compose exec rag-learning bash`
3. **Start learning**: `cd lessons/01-rag-fundamentals && python simple_example.py`

**Your laptop stays clean, everything runs in Docker!** 🎉

