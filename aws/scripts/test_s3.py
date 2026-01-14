#!/usr/bin/env python3
"""
Test S3 bucket access and functionality
"""

import boto3
import json
from pathlib import Path

def load_config():
    """Load S3 configuration"""
    config_path = Path(__file__).parent.parent / 'config.json'
    with open(config_path) as f:
        return json.load(f)

def test_bucket_access(s3_client, bucket_name):
    """Test if we can access the bucket"""
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        print("✅ Bucket access: OK")
        return True
    except Exception as e:
        print(f"❌ Bucket access failed: {e}")
        return False

def test_list_objects(s3_client, bucket_name):
    """Test listing objects in bucket"""
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name, MaxKeys=10)
        count = response.get('KeyCount', 0)
        print(f"✅ List objects: OK ({count} objects found)")
        
        if count > 0:
            print("\n📄 Sample objects:")
            for obj in response.get('Contents', [])[:5]:
                print(f"  - {obj['Key']} ({obj['Size']} bytes)")
        
        return True
    except Exception as e:
        print(f"❌ List objects failed: {e}")
        return False

def test_upload_download(s3_client, bucket_name):
    """Test upload and download"""
    test_key = 'test/test_file.txt'
    test_content = 'Hello from RAG Learning!'
    
    try:
        # Upload
        s3_client.put_object(
            Bucket=bucket_name,
            Key=test_key,
            Body=test_content.encode('utf-8')
        )
        print("✅ Upload test: OK")
        
        # Download
        response = s3_client.get_object(Bucket=bucket_name, Key=test_key)
        downloaded_content = response['Body'].read().decode('utf-8')
        
        if downloaded_content == test_content:
            print("✅ Download test: OK")
        else:
            print("❌ Download test: Content mismatch")
            return False
        
        # Cleanup
        s3_client.delete_object(Bucket=bucket_name, Key=test_key)
        print("✅ Cleanup: OK")
        
        return True
    except Exception as e:
        print(f"❌ Upload/Download test failed: {e}")
        return False

def get_bucket_size(s3_client, bucket_name):
    """Calculate total bucket size"""
    try:
        total_size = 0
        total_objects = 0
        
        paginator = s3_client.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=bucket_name):
            for obj in page.get('Contents', []):
                total_size += obj['Size']
                total_objects += 1
        
        size_mb = total_size / (1024 * 1024)
        print(f"📊 Bucket stats:")
        print(f"  - Total objects: {total_objects}")
        print(f"  - Total size: {size_mb:.2f} MB")
        
        return True
    except Exception as e:
        print(f"⚠️  Could not calculate bucket size: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("🧪 Testing S3 Configuration")
    print("=" * 60)
    
    # Load configuration
    try:
        config = load_config()
        bucket_name = config['bucket_name']
        profile = config['profile']
        region = config['region']
    except Exception as e:
        print(f"❌ Could not load config: {e}")
        print("Run 'python aws/setup_s3.py' first!")
        return
    
    print(f"\n📦 Bucket: {bucket_name}")
    print(f"🌍 Region: {region}")
    print(f"👤 Profile: {profile}")
    
    # Create S3 client
    session = boto3.Session(profile_name=profile)
    s3_client = session.client('s3', region_name=region)
    
    # Run tests
    print("\n🧪 Running tests...\n")
    
    tests = [
        ("Bucket Access", lambda: test_bucket_access(s3_client, bucket_name)),
        ("List Objects", lambda: test_list_objects(s3_client, bucket_name)),
        ("Upload/Download", lambda: test_upload_download(s3_client, bucket_name)),
        ("Bucket Stats", lambda: get_bucket_size(s3_client, bucket_name)),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        results.append(test_func())
    
    # Summary
    print("\n" + "=" * 60)
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"✅ All tests passed! ({passed}/{total})")
    else:
        print(f"⚠️  Some tests failed ({passed}/{total} passed)")
    
    print("=" * 60)

if __name__ == "__main__":
    main()

