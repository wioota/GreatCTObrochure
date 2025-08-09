#!/bin/bash

# Great CTO Website - GitHub Pages Deployment Script
# This script helps automate the GitHub repository creation and deployment

echo "🚀 Great CTO Website - GitHub Pages Deployment"
echo "=============================================="
echo ""

# Check if we're in the right directory
if [ ! -f "pelicanconf.py" ]; then
    echo "❌ Error: Please run this script from the GreatCTObrochure directory"
    exit 1
fi

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Error: Git repository not initialized"
    exit 1
fi

echo "📋 Pre-deployment checklist:"
echo "✅ Git repository initialized"
echo "✅ All files committed"
echo ""

echo "📝 Manual steps you need to complete:"
echo ""
echo "1. CREATE GITHUB REPOSITORY:"
echo "   - Go to https://github.com"
echo "   - Click '+' → 'New repository'"
echo "   - Repository name: 'GreatCTObrochure'"
echo "   - Make it PUBLIC (required for free GitHub Pages)"
echo "   - Don't initialize with README/gitignore (we have them)"
echo "   - Click 'Create repository'"
echo ""

echo "2. PUSH YOUR CODE:"
read -p "   Enter your GitHub username: " GITHUB_USERNAME
echo ""

if [ -z "$GITHUB_USERNAME" ]; then
    echo "❌ GitHub username is required"
    exit 1
fi

echo "   Run these commands:"
echo "   git remote add origin https://github.com/$GITHUB_USERNAME/GreatCTObrochure.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""

echo "3. ENABLE GITHUB PAGES:"
echo "   - Go to your repository → Settings → Pages"
echo "   - Source: 'Deploy from a branch'"
echo "   - Branch: 'gh-pages' (created by GitHub Action)"
echo "   - Click 'Save'"
echo ""

echo "4. YOUR SITE WILL BE LIVE AT:"
echo "   https://$GITHUB_USERNAME.github.io/GreatCTObrochure"
echo ""

read -p "Press Enter to see the git commands you need to run..."
echo ""
echo "🔧 Git commands to run:"
echo "======================"
echo "git remote add origin https://github.com/$GITHUB_USERNAME/GreatCTObrochure.git"
echo "git branch -M main" 
echo "git push -u origin main"
echo ""

echo "⏰ What happens next:"
echo "===================="
echo "• GitHub Action builds your site (2-3 minutes)"
echo "• Site goes live at https://$GITHUB_USERNAME.github.io/GreatCTObrochure"
echo "• Daily automatic imports from your Substack feed"
echo "• Automatic rebuilds when you push changes"
echo ""

echo "🎉 Your Great CTO website is ready for deployment!"
