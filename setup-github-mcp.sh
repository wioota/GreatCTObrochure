#!/bin/bash

# GitHub MCP Server Setup Script
echo "🔧 GitHub MCP Server Setup"
echo "========================="
echo ""

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

echo "✅ Docker is running"

# Check if GitHub MCP image is available
if docker images | grep -q "github-mcp-server"; then
    echo "✅ GitHub MCP Server image found"
else
    echo "📥 Pulling GitHub MCP Server image..."
    docker pull ghcr.io/github/github-mcp-server
fi

echo ""
echo "📝 To complete setup:"
echo "1. Edit mcp-config.json"
echo "2. Replace 'YOUR_TOKEN_HERE' with your GitHub Personal Access Token"
echo "3. Run: export GITHUB_TOKEN=your_token_here"
echo "4. Test with: docker run -i --rm -e GITHUB_PERSONAL_ACCESS_TOKEN=\$GITHUB_TOKEN ghcr.io/github/github-mcp-server"
echo ""

echo "🔑 Your GitHub Token needs these permissions:"
echo "- repo (Full control of private repositories)"
echo "- workflow (Update GitHub Action workflows)"
echo "- write:packages (Upload packages to GitHub Package Registry)"
echo ""

echo "📍 Get your token at: https://github.com/settings/tokens"
echo ""

# Create environment file template
cat > .env.example << 'EOF'
# GitHub Personal Access Token
# Get yours at: https://github.com/settings/tokens
# Required scopes: repo, workflow, write:packages
GITHUB_TOKEN=ghp_your_token_here
EOF

echo "✅ Created .env.example template"
echo "✅ Created MCP configuration files"
echo ""
echo "🚀 Next: Add your GitHub token to complete setup!"
