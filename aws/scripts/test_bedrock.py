#!/usr/bin/env python3
"""
Test AWS Bedrock API access
Verifies that you can access Bedrock models
"""

import boto3
import json
from datetime import datetime

# Configuration
PROFILE = 'default'
REGION = 'us-east-1'  # Bedrock is available in specific regions

def create_bedrock_client(region='us-east-1'):
    """Create Bedrock Runtime client"""
    session = boto3.Session(profile_name=PROFILE)
    return session.client('bedrock-runtime', region_name=region)

def list_available_models():
    """List available Bedrock models"""
    print("\n📋 Checking available Bedrock models...")
    
    session = boto3.Session(profile_name=PROFILE)
    bedrock = session.client('bedrock', region_name=REGION)
    
    try:
        response = bedrock.list_foundation_models()
        models = response.get('modelSummaries', [])
        
        print(f"\n✅ Found {len(models)} available models:")
        
        # Group by provider
        providers = {}
        for model in models:
            provider = model.get('providerName', 'Unknown')
            if provider not in providers:
                providers[provider] = []
            providers[provider].append(model)
        
        for provider, provider_models in providers.items():
            print(f"\n  {provider}:")
            for model in provider_models[:3]:  # Show first 3 from each provider
                model_id = model.get('modelId', 'N/A')
                model_name = model.get('modelName', 'N/A')
                print(f"    - {model_name} ({model_id})")
        
        return True
    except Exception as e:
        print(f"❌ Error listing models: {e}")
        return False

def test_claude_model(bedrock_runtime):
    """Test Claude model (most common for RAG)"""
    print("\n🧪 Testing Claude model...")
    
    # Claude 3 Haiku (fastest, cheapest)
    model_id = "anthropic.claude-3-haiku-20240307-v1:0"
    
    prompt = "Hello! Please respond with 'Bedrock API is working!' if you can read this."
    
    # Claude 3 request format
    request_body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 100,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    
    try:
        response = bedrock_runtime.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body)
        )
        
        response_body = json.loads(response['body'].read())
        
        # Extract response text
        if 'content' in response_body and len(response_body['content']) > 0:
            response_text = response_body['content'][0]['text']
            print(f"✅ Claude Response: {response_text}")
            print(f"✅ Model: {model_id}")
            return True
        else:
            print(f"⚠️  Unexpected response format: {response_body}")
            return False
            
    except Exception as e:
        print(f"❌ Error invoking Claude: {e}")
        print(f"   Model ID tried: {model_id}")
        return False

def test_titan_embeddings(bedrock_runtime):
    """Test Titan Embeddings model"""
    print("\n🧪 Testing Titan Embeddings...")
    
    model_id = "amazon.titan-embed-text-v1"
    
    request_body = {
        "inputText": "This is a test sentence for embeddings."
    }
    
    try:
        response = bedrock_runtime.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body)
        )
        
        response_body = json.loads(response['body'].read())
        
        if 'embedding' in response_body:
            embedding = response_body['embedding']
            print(f"✅ Titan Embeddings working!")
            print(f"   Embedding dimension: {len(embedding)}")
            print(f"   Model: {model_id}")
            return True
        else:
            print(f"⚠️  Unexpected response format: {response_body}")
            return False
            
    except Exception as e:
        print(f"❌ Error invoking Titan Embeddings: {e}")
        print(f"   Model ID tried: {model_id}")
        return False

def test_region_availability():
    """Test which regions have Bedrock available"""
    print("\n🌍 Testing Bedrock availability in different regions...")
    
    regions_to_test = [
        'us-east-1',
        'us-west-2',
        'eu-west-1',
        'ap-southeast-1'
    ]
    
    session = boto3.Session(profile_name=PROFILE)
    available_regions = []
    
    for region in regions_to_test:
        try:
            bedrock = session.client('bedrock', region_name=region)
            bedrock.list_foundation_models()
            print(f"  ✅ {region}: Available")
            available_regions.append(region)
        except Exception as e:
            print(f"  ❌ {region}: Not available or no access")
    
    return available_regions

def main():
    """Run all Bedrock tests"""
    print("=" * 60)
    print("🚀 AWS Bedrock API Test")
    print("=" * 60)
    print(f"\n👤 Profile: {PROFILE}")
    print(f"🌍 Region: {REGION}")
    
    # Test 1: List available models
    models_ok = list_available_models()
    
    if not models_ok:
        print("\n⚠️  Could not list models. Checking region availability...")
        available_regions = test_region_availability()
        
        if available_regions:
            print(f"\n💡 Try using one of these regions: {', '.join(available_regions)}")
            print(f"   Update REGION in this script and run again.")
        else:
            print("\n❌ Bedrock may not be enabled in your account.")
            print("   Visit: https://console.aws.amazon.com/bedrock/")
            print("   Enable model access in the Bedrock console.")
        return
    
    # Create runtime client for testing
    bedrock_runtime = create_bedrock_client(REGION)
    
    # Test 2: Test Claude model
    claude_ok = test_claude_model(bedrock_runtime)
    
    # Test 3: Test Titan Embeddings
    titan_ok = test_titan_embeddings(bedrock_runtime)
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Test Summary")
    print("=" * 60)
    
    results = {
        "List Models": "✅" if models_ok else "❌",
        "Claude (Text Generation)": "✅" if claude_ok else "❌",
        "Titan Embeddings": "✅" if titan_ok else "❌"
    }
    
    for test, result in results.items():
        print(f"  {result} {test}")
    
    if all([models_ok, claude_ok, titan_ok]):
        print("\n🎉 All tests passed! Bedrock API is working!")
        print("\n📚 Next steps:")
        print("  1. Use Claude for text generation in your RAG system")
        print("  2. Use Titan Embeddings for document embeddings")
        print("  3. Check lessons/lesson6_generation/ for examples")
    elif models_ok and not (claude_ok or titan_ok):
        print("\n⚠️  Models are listed but invocation failed.")
        print("   You may need to request model access in Bedrock console:")
        print("   https://console.aws.amazon.com/bedrock/home#/modelaccess")
    else:
        print("\n❌ Some tests failed. Check the errors above.")
    
    print("=" * 60)

if __name__ == "__main__":
    main()

