#!/usr/bin/env python3
"""
Upload documents to S3 bucket
"""

import boto3
import json
import os
from pathlib import Path

def load_config():
    """Load S3 configuration"""
    config_path = Path(__file__).parent.parent / 'config.json'
    with open(config_path) as f:
        return json.load(f)

def upload_file(s3_client, bucket_name, file_path, s3_key):
    """Upload a single file to S3"""
    try:
        s3_client.upload_file(file_path, bucket_name, s3_key)
        print(f"✅ Uploaded: {file_path} → s3://{bucket_name}/{s3_key}")
        return True
    except Exception as e:
        print(f"❌ Error uploading {file_path}: {e}")
        return False

def upload_directory(s3_client, bucket_name, local_dir, s3_prefix='documents/raw/'):
    """Upload all files from a directory"""
    local_path = Path(local_dir)
    
    if not local_path.exists():
        print(f"❌ Directory not found: {local_dir}")
        return
    
    files = list(local_path.glob('**/*'))
    files = [f for f in files if f.is_file()]
    
    print(f"\n📤 Uploading {len(files)} files from {local_dir}...")
    
    success_count = 0
    for file_path in files:
        relative_path = file_path.relative_to(local_path)
        s3_key = f"{s3_prefix}{relative_path}"
        
        if upload_file(s3_client, bucket_name, str(file_path), s3_key):
            success_count += 1
    
    print(f"\n✅ Successfully uploaded {success_count}/{len(files)} files")

def main():
    """Main upload function"""
    print("=" * 60)
    print("📤 Upload Documents to S3")
    print("=" * 60)
    
    # Load configuration
    config = load_config()
    bucket_name = config['bucket_name']
    profile = config['profile']
    
    print(f"\n📦 Bucket: {bucket_name}")
    print(f"👤 Profile: {profile}")
    
    # Create S3 client
    session = boto3.Session(profile_name=profile)
    s3_client = session.client('s3')
    
    # Example: Upload sample documents
    print("\n📁 What would you like to upload?")
    print("  1. Single file")
    print("  2. Directory")
    print("  3. Sample documents (for testing)")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == '1':
        file_path = input("Enter file path: ").strip()
        s3_key = input("Enter S3 key (e.g., documents/raw/myfile.txt): ").strip()
        upload_file(s3_client, bucket_name, file_path, s3_key)
    
    elif choice == '2':
        dir_path = input("Enter directory path: ").strip()
        s3_prefix = input("Enter S3 prefix (e.g., documents/raw/): ").strip()
        upload_directory(s3_client, bucket_name, dir_path, s3_prefix)
    
    elif choice == '3':
        # Create sample documents
        sample_dir = Path('sample_documents')
        sample_dir.mkdir(exist_ok=True)
        
        samples = {
            'ai_basics.txt': 'Artificial Intelligence is the simulation of human intelligence by machines.',
            'ml_intro.txt': 'Machine Learning is a subset of AI that learns from data.',
            'rag_overview.txt': 'RAG combines retrieval and generation for better AI responses.'
        }
        
        for filename, content in samples.items():
            (sample_dir / filename).write_text(content)
        
        upload_directory(s3_client, bucket_name, str(sample_dir))
        print(f"\n🗑️  Cleaning up local sample files...")
        for filename in samples:
            (sample_dir / filename).unlink()
        sample_dir.rmdir()
    
    print("\n✅ Upload complete!")

if __name__ == "__main__":
    main()

