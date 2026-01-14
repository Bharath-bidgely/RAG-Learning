#!/bin/bash
# Verify no secrets are in the code before committing

echo "🔍 Checking for secrets in code..."
echo ""

FOUND_ISSUES=0

# Check for Bedrock API keys (ABSK...)
echo "Checking for hardcoded Bedrock API keys..."
if git ls-files | xargs grep -l "ABSK[A-Za-z0-9+/=]\{50,\}" 2>/dev/null; then
    echo "❌ Found hardcoded Bedrock API key!"
    FOUND_ISSUES=1
else
    echo "✅ No hardcoded Bedrock API keys found"
fi

echo ""

# Check for AWS access keys
echo "Checking for AWS access keys..."
if git ls-files | xargs grep -l "AKIA[A-Z0-9]\{16\}" 2>/dev/null; then
    echo "❌ Found AWS access key!"
    FOUND_ISSUES=1
else
    echo "✅ No AWS access keys found"
fi

echo ""

# Check for AWS secret keys (common patterns)
echo "Checking for AWS secret keys..."
if git ls-files | xargs grep -l "aws_secret_access_key.*=.*[A-Za-z0-9/+=]\{40\}" 2>/dev/null; then
    echo "❌ Found AWS secret key!"
    FOUND_ISSUES=1
else
    echo "✅ No AWS secret keys found"
fi

echo ""

# Check if .env is in .gitignore
echo "Checking .gitignore..."
if grep -q "^\.env$" .gitignore; then
    echo "✅ .env is in .gitignore"
else
    echo "❌ .env is NOT in .gitignore!"
    FOUND_ISSUES=1
fi

echo ""

# Check if .env file exists and is not tracked
if [ -f .env ]; then
    if git ls-files --error-unmatch .env 2>/dev/null; then
        echo "❌ .env file is tracked by git!"
        FOUND_ISSUES=1
    else
        echo "✅ .env file exists and is not tracked"
    fi
else
    echo "⚠️  .env file does not exist (create from .env.example)"
fi

echo ""

# Check if .env.example exists and has no real secrets
if [ -f .env.example ]; then
    if grep -q "your-.*-key-here\|your-.*-token-here\|PASTE_YOUR_KEY" .env.example; then
        echo "✅ .env.example has placeholder values"
    else
        echo "⚠️  .env.example might contain real secrets"
    fi
else
    echo "⚠️  .env.example does not exist"
fi

echo ""
echo "=========================================================="

if [ $FOUND_ISSUES -eq 0 ]; then
    echo "✅ ALL CHECKS PASSED - Safe to commit!"
    echo "=========================================================="
    exit 0
else
    echo "❌ ISSUES FOUND - DO NOT COMMIT!"
    echo "=========================================================="
    echo ""
    echo "Fix the issues above before committing."
    exit 1
fi

