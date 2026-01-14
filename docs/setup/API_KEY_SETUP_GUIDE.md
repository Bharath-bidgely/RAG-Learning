# 🔑 API Key Setup Guide

## For Users Who Want to Use Anthropic API Keys (from Bedrock Discover)

This guide is for users who want to use **Anthropic API keys** obtained from the AWS Bedrock "Discover" section.

---

## 📋 Step 1: Get Your Anthropic API Key

### Option A: From AWS Bedrock Console (Recommended)

1. Go to **AWS Bedrock Console**: https://console.aws.amazon.com/bedrock/
2. Navigate to: **Discover → API Keys → Long-term API Keys**
3. Click **"Create API Key"** for Anthropic
4. Copy the API key (starts with `sk-ant-...`)
5. **Save it securely** - you won't see it again!

### Option B: From Anthropic Console Directly

1. Go to: https://console.anthropic.com/
2. Sign up or log in
3. Navigate to **Settings → API Keys**
4. Click **"Create Key"**
5. Copy the key (starts with `sk-ant-...`)

---

## 🧪 Step 2: Test Your API Key

### Quick Test

1. Open the test script:
   ```bash
   cd /Users/admin/RAG-Learning
   nano test_model_with_api_key.py
   ```

2. Find this line (around line 18):
   ```python
   ANTHROPIC_API_KEY = "sk-ant-YOUR-API-KEY-HERE"
   ```

3. Replace with your actual key:
   ```python
   ANTHROPIC_API_KEY = "sk-ant-api03-abc123xyz..."
   ```

4. Make sure METHOD is set to "anthropic":
   ```python
   METHOD = "anthropic"
   ```

5. Save and run:
   ```bash
   source .venv/bin/activate
   python test_model_with_api_key.py
   ```

### Expected Output

```
🧪 AI Model API Test
======================================================================
Method: ANTHROPIC

🚀 Testing Anthropic API (Direct)
======================================================================

📡 Connecting to Anthropic API...
   Model: claude-3-haiku-20240307
   API Key: sk-ant-api03-abc123...
   ⏳ Sending request...
   ✅ Response received!

======================================================================
📨 PROMPT:
======================================================================
Hello! Please respond with:
1. Confirmation that you're working
2. What model you are
3. A brief fun fact about AI

======================================================================
🤖 RESPONSE:
======================================================================
Hello! Here's my response:

1. ✅ I'm working perfectly!
2. I'm Claude 3 Haiku, Anthropic's fastest model
3. Fun fact: The first chatbot, ELIZA, was created in 1966!

======================================================================
📊 USAGE:
======================================================================
   Input tokens: 45
   Output tokens: 52

✅ SUCCESS - Anthropic API is working!
```

---

## 🎯 Step 3: Use in Your RAG System

Once your API key works, you can use it in your RAG applications:

```python
import requests
import json

def ask_claude(prompt, api_key):
    """Send a prompt to Claude via Anthropic API"""
    
    url = "https://api.anthropic.com/v1/messages"
    
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    
    data = {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 1000,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    
    return result['content'][0]['text']

# Usage
api_key = "sk-ant-your-key-here"
answer = ask_claude("What is RAG?", api_key)
print(answer)
```

---

## 💰 Pricing (Anthropic API Direct)

| Model | Input (per 1M tokens) | Output (per 1M tokens) |
|-------|----------------------|------------------------|
| Claude 3 Haiku | $0.25 | $1.25 |
| Claude 3 Sonnet | $3.00 | $15.00 |
| Claude 3.5 Sonnet | $3.00 | $15.00 |
| Claude 3 Opus | $15.00 | $75.00 |

**Example costs:**
- 100 questions (Haiku): ~$0.05
- 1000 questions (Haiku): ~$0.50
- Learning/testing: < $5/month

---

## 🔄 AWS Bedrock vs Direct Anthropic API

| Feature | AWS Bedrock | Direct Anthropic API |
|---------|-------------|---------------------|
| **Authentication** | AWS credentials | Anthropic API key |
| **Billing** | Through AWS | Through Anthropic |
| **Setup** | Enable model access | Create API key |
| **Integration** | AWS services | Any platform |
| **Best for** | AWS users | Non-AWS users |

---

## 🆘 Troubleshooting

### Error: "Invalid API key"

**Solution:**
- Check the key is copied correctly (no spaces)
- Verify it starts with `sk-ant-`
- Make sure the key is active in Anthropic console

### Error: "Rate limit exceeded"

**Solution:**
- You're sending too many requests
- Wait a few minutes and try again
- Upgrade your Anthropic plan if needed

### Error: "Model not found"

**Solution:**
- Check the model name is correct
- Use: `claude-3-haiku-20240307` (not the Bedrock version)

---

## 📚 Configuration Options

Edit `test_model_with_api_key.py` to customize:

```python
# Choose method
METHOD = "anthropic"  # or "bedrock"

# Anthropic API settings
ANTHROPIC_API_KEY = "sk-ant-your-key"
ANTHROPIC_MODEL = "claude-3-haiku-20240307"  # or sonnet, opus

# Change the test prompt
TEST_PROMPT = """Your custom prompt here"""
```

---

## ✅ Quick Reference

### For Anthropic API Users:

1. Get API key from Bedrock Discover or Anthropic console
2. Set `METHOD = "anthropic"`
3. Set `ANTHROPIC_API_KEY = "sk-ant-..."`
4. Run: `python test_model_with_api_key.py`

### For AWS Bedrock Users:

1. Enable model access in Bedrock console
2. Set `METHOD = "bedrock"`
3. Configure AWS credentials
4. Run: `python test_model_with_api_key.py`

---

## 🎉 You're Ready!

Once the test passes, you can:
- ✅ Use the API in your RAG system
- ✅ Build AI applications
- ✅ Integrate with your projects
- ✅ Share this script with your team

**Happy building! 🚀**

