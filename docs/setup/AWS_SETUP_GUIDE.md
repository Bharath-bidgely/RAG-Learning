# 🚀 AWS Setup Guide for RAG Learning

## ✅ Current Status

Your AWS credentials are configured and working!

- **AWS Account:** 827453154040
- **User:** bharath@bidgely.com
- **Profile:** default
- **Tools Installed:** boto3, awscli

## 🎯 Recommended Approach: Hybrid Learning

### Why Hybrid?

**Learn Locally, Deploy to AWS**

1. **Local Development (FREE)**
   - Use ChromaDB for vector storage
   - Run embeddings on your machine
   - Fast iteration and learning
   - No AWS costs during learning

2. **AWS Deployment (When Ready)**
   - Store documents in S3
   - Deploy API to Lambda/ECS
   - Production-ready infrastructure
   - Scalable and reliable

### Cost Comparison

| Approach | Monthly Cost | Best For |
|----------|-------------|----------|
| **Local Only** | $0 | Learning, development |
| **Hybrid (Recommended)** | < $5 | Learning + AWS practice |
| **Full AWS** | $60-100 | Production deployment |

## 🚀 Quick Start with AWS

### Step 1: Create S3 Bucket (5 minutes)

```bash
# Activate your environment
source .venv/bin/activate

# Create S3 bucket for documents
python aws/setup_s3.py
```

This will:
- Create a unique S3 bucket
- Set up folder structure
- Enable versioning
- Add lifecycle policies (cost optimization)
- Save configuration to `aws/config.json`

### Step 2: Test S3 Access (2 minutes)

```bash
python aws/scripts/test_s3.py
```

This will verify:
- ✅ Bucket access
- ✅ Upload/download
- ✅ List objects
- ✅ Bucket statistics

### Step 3: Upload Sample Documents (Optional)

```bash
python aws/scripts/upload_documents.py
```

Choose from:
1. Upload a single file
2. Upload a directory
3. Create and upload sample documents

## 📚 Learning Path with AWS

### Phase 1: Learn Locally (Lessons 1-4)
**Focus:** Understanding RAG fundamentals  
**Tools:** Local ChromaDB, sentence-transformers  
**Cost:** $0

```bash
cd lessons/lesson1_embeddings
python basic_embeddings.py
```

### Phase 2: Hybrid Setup (Lesson 5-6)
**Focus:** Building complete RAG system  
**Tools:** Local processing + S3 storage  
**Cost:** < $5/month

```bash
# Store documents in S3
python aws/scripts/upload_documents.py

# Process locally, save to S3
python lessons/lesson5_retrieval/s3_integration.py
```

### Phase 3: AWS Deployment (Lesson 7)
**Focus:** Production deployment  
**Tools:** Lambda, API Gateway, S3  
**Cost:** ~$10-20/month (light usage)

```bash
# Deploy to Lambda
python aws/deploy_lambda.py

# Test production API
curl https://your-api.execute-api.us-east-1.amazonaws.com/prod/query
```

## 🛠️ AWS Services Overview

### 1. S3 - Document Storage
**What:** Object storage for documents and embeddings  
**Cost:** ~$0.023/GB/month (first 50TB)  
**Free Tier:** 5GB for 12 months  
**Use Case:** Store PDFs, text files, embeddings

### 2. Lambda - Serverless Compute
**What:** Run code without managing servers  
**Cost:** $0.20 per 1M requests  
**Free Tier:** 1M requests/month forever  
**Use Case:** Embedding generation, API endpoints

### 3. OpenSearch - Vector Database
**What:** Managed search with k-NN vector search  
**Cost:** ~$50/month (minimum)  
**Free Tier:** None  
**Use Case:** Production vector search (later)

### 4. Bedrock - Managed LLMs
**What:** Access to Claude, Llama, etc.  
**Cost:** Pay per token (~$0.01-0.10 per request)  
**Free Tier:** None  
**Use Case:** LLM generation (optional)

## 💡 Best Practices

### Cost Optimization
1. **Use S3 Lifecycle Policies** - Auto-delete old versions
2. **Lambda Memory** - Start with 512MB, adjust as needed
3. **Monitor Usage** - Set up billing alerts
4. **Free Tier** - Maximize free tier usage

### Security
1. **IAM Roles** - Use least privilege access
2. **Bucket Policies** - Restrict public access
3. **Encryption** - Enable S3 encryption
4. **Secrets** - Use AWS Secrets Manager for API keys

### Development Workflow
1. **Develop Locally** - Fast iteration
2. **Test with S3** - Verify AWS integration
3. **Deploy to Lambda** - Production testing
4. **Monitor** - CloudWatch logs and metrics

## 🎓 When to Use What

### Use Local ChromaDB When:
- ✅ Learning RAG concepts
- ✅ Developing and testing
- ✅ Small datasets (< 1GB)
- ✅ Single user/developer

### Use AWS S3 When:
- ✅ Storing large document collections
- ✅ Sharing data across team
- ✅ Need backup and versioning
- ✅ Preparing for production

### Use AWS Lambda When:
- ✅ Building APIs
- ✅ Serverless deployment
- ✅ Low to medium traffic
- ✅ Cost-sensitive projects

### Use AWS OpenSearch When:
- ✅ Production workloads
- ✅ High query volume
- ✅ Need managed service
- ✅ Budget allows ($50+/month)

## 📖 Next Steps

### Today (Optional)
```bash
# Set up S3 bucket
python aws/setup_s3.py

# Test access
python aws/scripts/test_s3.py
```

### This Week
- Complete Lessons 1-3 (local only)
- Understand embeddings and chunking
- Build semantic search

### Next Week
- Integrate S3 for document storage
- Build complete RAG pipeline
- Test with real documents

### Later
- Deploy to Lambda
- Add monitoring
- Optimize costs

## 🆘 Troubleshooting

### AWS Credentials Not Working?
```bash
aws sts get-caller-identity --profile default
```

### S3 Bucket Already Exists?
The script adds a timestamp to make it unique. If it still fails, check the AWS console.

### Permission Denied?
Make sure your IAM user has S3 permissions:
- s3:CreateBucket
- s3:PutObject
- s3:GetObject
- s3:ListBucket

## 📊 Cost Monitoring

Set up a billing alert:
1. Go to AWS Billing Console
2. Create a budget
3. Set alert at $5, $10, $20
4. Get email notifications

**Recommended:** Set a $10/month budget alert while learning.

---

**You're ready to use AWS! Start with local learning, then gradually integrate AWS services. 🚀**

