#!/bin/bash
# Fresh start - Remove all git history and start clean

cd "$(dirname "$0")/../.." || exit 1

echo "🔄 FRESH START: Clean repository (remove all history)"
echo "======================================================"
echo ""
echo "⚠️  This will REMOVE ALL git history and create fresh commit"
echo ""
read -p "Continue? (yes/no): " -r
[[ ! $REPLY == "yes" ]] && exit 1

echo "🔧 Backing up..."
cp -r .git .git.backup

echo "🔧 Removing history..."
rm -rf .git

echo "🔧 Creating fresh repo..."
git init
git branch -M main
git add -A
git commit -m "Initial commit - RAG Learning project"

echo "🔧 Adding remote..."
git remote add origin https://github.com/Bharath-bidgely/RAG-Learning.git

echo ""
echo "✅ Ready to push!"
echo ""
read -p "Force push to GitHub? (yes/no): " -r
if [[ $REPLY == "yes" ]]; then
    git push -u origin main --force
    echo "✅ Done! Check: https://github.com/Bharath-bidgely/RAG-Learning/commits/main"
else
    echo "Run: git push -u origin main --force"
fi

echo ""
echo "⚠️  IMPORTANT: Rotate your API key in AWS Console!"

