#!/bin/bash
# Setup environment configuration

echo "🔧 Setting up environment configuration..."
echo ""

# Check if .env already exists
if [ -f .env ]; then
    echo "⚠️  .env file already exists!"
    read -p "Do you want to overwrite it? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ Setup cancelled. Keeping existing .env file."
        exit 0
    fi
fi

# Copy .env.example to .env
if [ -f .env.example ]; then
    cp .env.example .env
    echo "✅ Created .env file from .env.example"
else
    echo "❌ Error: .env.example not found!"
    exit 1
fi

echo ""
echo "📝 Next steps:"
echo "1. Edit .env file and add your secrets:"
echo "   nano .env"
echo ""
echo "2. Required values to fill in:"
echo "   - AWS_BEARER_TOKEN_BEDROCK (your Bedrock API key)"
echo "   - AWS_REGION (default: us-east-1)"
echo "   - MODEL_ID (default: us.anthropic.claude-3-5-haiku-20241022-v1:0)"
echo ""
echo "3. Get your Bedrock API key from:"
echo "   AWS Console → Bedrock → Discover → API Keys"
echo ""
echo "4. Test your setup:"
echo "   source .venv/bin/activate"
echo "   python tests/test_model_with_api_key.py"
echo ""
echo "✅ Setup complete!"

