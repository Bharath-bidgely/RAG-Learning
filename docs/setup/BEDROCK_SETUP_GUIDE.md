# 🚀 AWS Bedrock Setup Guide

## ⚠️ Important: You DON'T Need "API Keys" from Discover Section!

The "API Keys" you saw in **Bedrock → Discover → API Keys** are for using **third-party APIs directly** (not AWS Bedrock).

**You already have AWS credentials configured** - that's all you need for Bedrock!

---

## ✅ What You Need to Do: Enable Model Access

### Step 1: Go to Bedrock Model Access Page

1. Open AWS Console: https://console.aws.amazon.com/bedrock/
2. Click **"Model access"** in the left sidebar (NOT "Discover")
3. Click **"Manage model access"** button

### Step 2: Enable Claude Models

Check these boxes:
- ✅ **Claude 3 Haiku** (fastest, cheapest - recommended for learning)
- ✅ **Claude 3 Sonnet** (balanced)
- ✅ **Claude 3.5 Sonnet** (most capable)
- ✅ **Titan Embeddings** (for document embeddings)

Click **"Request model access"** or **"Save changes"**

### Step 3: Wait for Approval (Usually Instant)

- Most models are approved instantly
- Status will change from "Available to request" → "Access granted"
- Refresh the page after a few seconds

---

## 🧪 Test Your Bedrock Access

Once models are enabled, run this test:

```bash
cd /Users/admin/RAG-Learning
source .venv/bin/activate
python test_bedrock_comprehensive.py
```

This will verify:
- ✅ Your AWS credentials work
- ✅ Bedrock is accessible
- ✅ Claude models are available
- ✅ You can send prompts and get responses

---

## 🔑 Authentication Methods Comparison

| Method | What It Is | Do You Need It? |
|--------|-----------|-----------------|
| **AWS Credentials** (AKIA...) | Your AWS access keys | ✅ YES - You have this |
| **Bedrock Model Access** | Enable which models to use | ✅ YES - Do this now |
| **API Keys from "Discover"** | Third-party provider keys | ❌ NO - Ignore this |

---

## 💡 Why You Don't Need "Discover → API Keys"

The **"Discover → API Keys"** section shows:
- How to use Anthropic API **directly** (not through AWS)
- How to use Cohere API **directly** (not through AWS)
- These are **alternative** approaches, not for AWS Bedrock

**You're using AWS Bedrock**, so you don't need those keys!

---

## 🎯 Quick Setup Checklist

- [x] AWS credentials configured (you have this)
- [ ] Enable model access in Bedrock console
- [ ] Run test script to verify
- [ ] Start using Bedrock in your RAG system

---

## 🚀 After Model Access is Enabled

Run the simple test:

```bash
python test_bedrock_prompt.py
```

You should see:
```
✅ Connected successfully!
⏳ Waiting for response...
✅ Response received!

🤖 MODEL RESPONSE:
Hello! Yes, I'm working perfectly...
```

---

## 🆘 Troubleshooting

### "Access Denied" Error
→ Go to Bedrock → Model access → Enable Claude models

### "Model not found" Error  
→ Check you're using the right region (us-east-1 or us-west-2)

### "Invalid credentials" Error
→ Your AWS credentials are not set up correctly
→ Run: `aws sts get-caller-identity --profile default`

---

## 📊 Cost Information

### AWS Bedrock Pricing (Pay per use)
- **Claude 3 Haiku**: $0.25 per 1M input tokens, $1.25 per 1M output tokens
- **Claude 3 Sonnet**: $3 per 1M input tokens, $15 per 1M output tokens
- **Titan Embeddings**: $0.10 per 1M tokens

### Example Costs
- 100 questions with Haiku: ~$0.05
- 1000 questions with Haiku: ~$0.50
- Learning/testing: < $5/month

**No monthly fees** - only pay for what you use!

---

## ✅ Next Steps

1. **Enable model access** in Bedrock console (5 minutes)
2. **Run test script** to verify it works
3. **Start building** your RAG system with Bedrock!

---

**Remember: You DON'T need the API keys from "Discover" section. Just enable model access and use your existing AWS credentials!** 🎯

