#!/bin/bash

# GitHub Push Script
echo "🚀 Pushing Great CTO Website to GitHub"
echo "======================================"

# Check if mcp-config.json exists and has token
if [ ! -f "mcp-config.json" ]; then
    echo "❌ mcp-config.json not found"
    echo "   Please create it with your GitHub token"
    exit 1
fi

# Extract token from config
GITHUB_TOKEN=$(grep -o '"GITHUB_PERSONAL_ACCESS_TOKEN=[^"]*"' mcp-config.json | sed 's/"GITHUB_PERSONAL_ACCESS_TOKEN=\([^"]*\)"/\1/')

if [ -z "$GITHUB_TOKEN" ]; then
    echo "❌ GitHub token not found in mcp-config.json"
    echo "   Please add your token to the file"
    exit 1
fi

echo "✅ GitHub token found"

# Configure git with token
git remote set-url origin https://wioota:$GITHUB_TOKEN@github.com/wioota/GreatCTObrochure.git

# Push changes
echo "📤 Pushing to GitHub..."
git push origin main

if [ $? -eq 0 ]; then
    echo "✅ Successfully pushed to GitHub!"
    echo ""
    echo "🔄 GitHub Actions will now:"
    echo "  1. Build your website (2-3 minutes)"
    echo "  2. Deploy to GitHub Pages"
    echo "  3. Make it live at: https://wioota.github.io/GreatCTObrochure"
    echo ""
    echo "📊 Monitor progress at:"
    echo "  https://github.com/wioota/GreatCTObrochure/actions"
else
    echo "❌ Failed to push to GitHub"
    echo "   Please check your token and network connection"
fi

# Reset git remote to not leak token in git config
git remote set-url origin https://github.com/wioota/GreatCTObrochure.git
