# 🧪 Tests

This folder contains test scripts for the RAG Learning project.

## Available Tests

### 1. `test_model_with_api_key.py`
**Purpose:** Test AWS Bedrock API access with your API key

**Usage:**
```bash
cd /Users/admin/RAG-Learning
source .venv/bin/activate
python tests/test_model_with_api_key.py
```

**What it tests:**
- ✅ API key authentication
- ✅ Model availability
- ✅ Prompt/response functionality
- ✅ Token usage tracking

**Configuration:**
Edit the script to set:
- `BEDROCK_API_KEY` - Your API key from Bedrock console
- `MODEL_ID` - Which model to use
- `PROMPT` - Test prompt to send

---

### 2. `test_installation.py`
**Purpose:** Verify all dependencies are installed correctly

**Usage:**
```bash
python tests/test_installation.py
```

**What it tests:**
- ✅ Python version
- ✅ PyTorch installation
- ✅ Transformers library
- ✅ ChromaDB
- ✅ Other dependencies

---

## Running All Tests

```bash
# Activate environment
source .venv/bin/activate

# Run installation test
python tests/test_installation.py

# Run API test
python tests/test_model_with_api_key.py
```

---

## Environment Variables

For `test_model_with_api_key.py`, you can use environment variables:

```bash
export AWS_BEARER_TOKEN_BEDROCK="your-api-key"
export MODEL_ID="us.anthropic.claude-3-5-haiku-20241022-v1:0"
export PROMPT="Your test prompt"
export AWS_REGION="us-east-1"

python tests/test_model_with_api_key.py
```

---

## Adding New Tests

When adding new test scripts:

1. Name them `test_*.py`
2. Place them in this `tests/` folder
3. Update this README
4. Include clear documentation in the script

---

## Quick Reference

| Test | Purpose | Time |
|------|---------|------|
| `test_installation.py` | Verify setup | ~5 sec |
| `test_model_with_api_key.py` | Test Bedrock API | ~2 sec |

---

**Keep tests organized here to maintain a clean project structure!** 🎯

