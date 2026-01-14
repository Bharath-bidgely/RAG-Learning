# 🚀 AWS Infrastructure for RAG Learning

## Overview

This directory contains AWS infrastructure setup for your RAG learning project.

**AWS Account:** 827453154040  
**User:** bharath@bidgely.com  
**Profile:** default

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     RAG System on AWS                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐      ┌──────────────┐                    │
│  │   S3 Bucket  │      │  OpenSearch  │                    │
│  │  Documents   │      │ Vector Store │                    │
│  └──────────────┘      └──────────────┘                    │
│         │                      │                            │
│         └──────────┬───────────┘                            │
│                    │                                        │
│              ┌─────▼─────┐                                 │
│              │  Lambda   │  or  ┌──────────┐              │
│              │ Functions │      │   ECS    │              │
│              └───────────┘      │ Fargate  │              │
│                                 └──────────┘              │
│                                                              │
│  ┌──────────────────────────────────────────┐              │
│  │         API Gateway / ALB                 │              │
│  └──────────────────────────────────────────┘              │
└─────────────────────────────────────────────────────────────┘
```

## Services We'll Use

### 1. **S3** - Document Storage (FREE tier: 5GB)
- Store your documents
- Host embeddings
- Cheap and reliable

### 2. **OpenSearch Serverless** - Vector Database
- Managed vector search
- k-NN search built-in
- Alternative to ChromaDB for production

### 3. **Lambda** - Serverless Compute (FREE tier: 1M requests/month)
- Run embedding generation
- Handle API requests
- Pay only for what you use

### 4. **ECS Fargate** - Container Service (for larger workloads)
- Run FastAPI application
- Auto-scaling
- More control than Lambda

### 5. **Bedrock** - Managed LLMs (Optional)
- Claude, Llama models
- No infrastructure management
- Pay per token

## Cost Estimate

### Learning/Development (Minimal Usage)
- **S3:** ~$0.50/month (for 10GB storage)
- **Lambda:** FREE (within free tier)
- **OpenSearch Serverless:** ~$0 (we'll use local ChromaDB for learning)
- **Total:** < $5/month

### Production (Light Usage)
- **S3:** ~$2/month
- **Lambda/ECS:** ~$10-20/month
- **OpenSearch:** ~$50/month (if using managed)
- **Bedrock:** Pay per use (~$0.01-0.10 per request)
- **Total:** ~$60-100/month

## Setup Options

### Option 1: Hybrid (RECOMMENDED for Learning)
- **Local:** ChromaDB, embeddings, development
- **AWS:** S3 for documents, Lambda for deployment testing
- **Cost:** < $5/month
- **Best for:** Learning and experimentation

### Option 2: Full AWS (Production Ready)
- **AWS:** Everything on AWS
- **Cost:** ~$60-100/month
- **Best for:** Production deployment

### Option 3: Serverless Only
- **AWS:** S3 + Lambda + DynamoDB (instead of OpenSearch)
- **Cost:** ~$10-20/month
- **Best for:** Low-traffic production apps

## Quick Start

### 1. Install AWS Tools
```bash
pip install boto3 awscli
```

### 2. Verify AWS Access
```bash
aws sts get-caller-identity --profile default
```

### 3. Create S3 Bucket for Documents
```bash
python aws/setup_s3.py
```

### 4. Deploy Lambda Function
```bash
python aws/deploy_lambda.py
```

## Directory Structure

```
aws/
├── README.md                    # This file
├── setup_s3.py                  # Create S3 buckets
├── deploy_lambda.py             # Deploy Lambda functions
├── cloudformation/              # Infrastructure as Code
│   ├── s3-bucket.yaml
│   ├── lambda-function.yaml
│   └── opensearch.yaml
├── lambda/                      # Lambda function code
│   ├── embedding_function/
│   └── rag_api/
└── scripts/                     # Utility scripts
    ├── upload_documents.py
    └── test_deployment.py
```

## Next Steps

1. **Today:** Set up S3 bucket for document storage
2. **Tomorrow:** Deploy a simple Lambda function
3. **This Week:** Build complete RAG API on AWS
4. **Next Week:** Add monitoring and optimization

## Resources

- [AWS Free Tier](https://aws.amazon.com/free/)
- [OpenSearch Vector Search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/knn.html)
- [Lambda Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)

