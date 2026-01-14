#!/usr/bin/env python3
"""
Setup S3 buckets for RAG Learning project
Creates buckets for documents and embeddings storage
"""

import boto3
import json
from datetime import datetime

# Configuration
PROFILE = 'default'
REGION = 'us-east-1'  # Change if you prefer another region
BUCKET_PREFIX = 'rag-learning-bharath'  # Will add timestamp for uniqueness

def create_s3_client():
    """Create S3 client with default profile"""
    session = boto3.Session(profile_name=PROFILE)
    return session.client('s3', region_name=REGION)

def create_bucket(s3_client, bucket_name, region):
    """Create S3 bucket with proper configuration"""
    try:
        if region == 'us-east-1':
            # us-east-1 doesn't need LocationConstraint
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        
        print(f"✅ Created bucket: {bucket_name}")
        return True
    except s3_client.exceptions.BucketAlreadyOwnedByYou:
        print(f"ℹ️  Bucket already exists: {bucket_name}")
        return True
    except Exception as e:
        print(f"❌ Error creating bucket {bucket_name}: {e}")
        return False

def enable_versioning(s3_client, bucket_name):
    """Enable versioning on bucket"""
    try:
        s3_client.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={'Status': 'Enabled'}
        )
        print(f"✅ Enabled versioning on {bucket_name}")
    except Exception as e:
        print(f"⚠️  Could not enable versioning: {e}")

def add_lifecycle_policy(s3_client, bucket_name):
    """Add lifecycle policy to reduce costs"""
    lifecycle_policy = {
        'Rules': [
            {
                'Id': 'DeleteOldVersions',
                'Status': 'Enabled',
                'NoncurrentVersionExpiration': {'NoncurrentDays': 30},
                'AbortIncompleteMultipartUpload': {'DaysAfterInitiation': 7}
            }
        ]
    }
    
    try:
        s3_client.put_bucket_lifecycle_configuration(
            Bucket=bucket_name,
            LifecycleConfiguration=lifecycle_policy
        )
        print(f"✅ Added lifecycle policy to {bucket_name}")
    except Exception as e:
        print(f"⚠️  Could not add lifecycle policy: {e}")

def create_folder_structure(s3_client, bucket_name):
    """Create folder structure in bucket"""
    folders = [
        'documents/raw/',
        'documents/processed/',
        'embeddings/',
        'models/',
        'outputs/'
    ]
    
    for folder in folders:
        try:
            s3_client.put_object(Bucket=bucket_name, Key=folder)
            print(f"  📁 Created folder: {folder}")
        except Exception as e:
            print(f"  ⚠️  Could not create folder {folder}: {e}")

def save_config(bucket_name):
    """Save bucket configuration to file"""
    config = {
        'bucket_name': bucket_name,
        'region': REGION,
        'profile': PROFILE,
        'created_at': datetime.now().isoformat()
    }
    
    with open('aws/config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"✅ Saved configuration to aws/config.json")

def main():
    """Main setup function"""
    print("=" * 60)
    print("🚀 Setting up S3 for RAG Learning")
    print("=" * 60)
    
    # Create S3 client
    print(f"\n📡 Connecting to AWS (Profile: {PROFILE}, Region: {REGION})...")
    s3_client = create_s3_client()
    
    # Generate unique bucket name
    timestamp = datetime.now().strftime('%Y%m%d')
    bucket_name = f"{BUCKET_PREFIX}-{timestamp}"
    
    print(f"\n📦 Creating bucket: {bucket_name}")
    
    # Create bucket
    if not create_bucket(s3_client, bucket_name, REGION):
        print("\n❌ Failed to create bucket. Exiting.")
        return
    
    # Configure bucket
    print("\n⚙️  Configuring bucket...")
    enable_versioning(s3_client, bucket_name)
    add_lifecycle_policy(s3_client, bucket_name)
    
    # Create folder structure
    print("\n📁 Creating folder structure...")
    create_folder_structure(s3_client, bucket_name)
    
    # Save configuration
    print("\n💾 Saving configuration...")
    save_config(bucket_name)
    
    # Summary
    print("\n" + "=" * 60)
    print("✅ S3 Setup Complete!")
    print("=" * 60)
    print(f"\n📦 Bucket Name: {bucket_name}")
    print(f"🌍 Region: {REGION}")
    print(f"🔗 Console URL: https://s3.console.aws.amazon.com/s3/buckets/{bucket_name}")
    print("\n📚 Next steps:")
    print("  1. Upload documents: python aws/scripts/upload_documents.py")
    print("  2. Test access: python aws/scripts/test_s3.py")
    print("  3. Continue with lessons!")

if __name__ == "__main__":
    main()

