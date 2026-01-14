#!/usr/bin/env python3
"""
Test AWS Bedrock API with Bearer Token Authentication

This script tests the Bedrock API using credentials from .env file.
Make sure to copy .env.example to .env and fill in your credentials.
"""

import os
import json
import requests
from pathlib import Path

# Load environment variables from .env file
def load_env_file():
    """Load environment variables from .env file if it exists"""
    env_path = Path(__file__).parent.parent / '.env'

    if not env_path.exists():
        print("⚠️  Warning: .env file not found!")
        print(f"   Expected location: {env_path}")
        print("   Copy .env.example to .env and fill in your credentials.")
        print()
        return False

    # Simple .env parser
    with open(env_path, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue
            # Parse KEY=VALUE
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                # Only set if not already in environment
                if key not in os.environ:
                    os.environ[key] = value

    return True

# Load .env file
load_env_file()

# ---- CONFIG ----
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

# IMPORTANT: Use inference profile ARN for on-demand throughput
# Format: {region}.{provider}.{model-version}
MODEL_ID = os.getenv("MODEL_ID", "us.anthropic.claude-3-5-haiku-20241022-v1:0")

# Your Bedrock API Key from .env file
# Get from: AWS Console → Bedrock → Discover → API Keys
BEDROCK_API_KEY = os.getenv("AWS_BEARER_TOKEN_BEDROCK")

PROMPT = os.getenv("PROMPT", "Are you active? Reply briefly.")
# -----------------

def main():
    print("=" * 70)
    print("🧪 AWS Bedrock API Test")
    print("=" * 70)
    print()

    if not BEDROCK_API_KEY or BEDROCK_API_KEY == "your-bedrock-api-key-here":
        print("❌ Missing Bedrock API key!")
        print()
        print("📝 Setup Instructions:")
        print("1. Copy .env.example to .env:")
        print("   cp .env.example .env")
        print()
        print("2. Edit .env and add your Bedrock API key:")
        print("   AWS_BEARER_TOKEN_BEDROCK=your-actual-key")
        print()
        print("3. Get your API key from:")
        print("   AWS Console → Bedrock → Discover → API Keys")
        print()
        return

    url = f"https://bedrock-runtime.{AWS_REGION}.amazonaws.com/model/{MODEL_ID}/converse"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {BEDROCK_API_KEY}"
    }

    payload = {
        "messages": [
            {"role": "user", "content": [{"text": PROMPT}]}
        ]
    }

    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=30)

        # Try parsing JSON response
        data = resp.json()

        # If Bedrock returned an error, print it
        if resp.status_code != 200:
            print("❌ Request failed")
            print("HTTP Status:", resp.status_code)
            print("Response JSON:\n", json.dumps(data, indent=2))
            return

        # Success case: print assistant text
        text = data["output"]["message"]["content"][0]["text"]
        print("✅ Success")
        print("Model:", MODEL_ID)
        print("Response:", text)

    except Exception as e:
        print("❌ Exception while calling Bedrock:", str(e))

if __name__ == "__main__":
    main()