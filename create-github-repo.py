#!/usr/bin/env python3
"""
GitHub Repository Creator for Great CTO Website
Uses GitHub API to create repository and push code
"""

import os
import sys
import subprocess
import requests
import json

def check_requirements():
    """Check if we have everything needed"""
    if not os.path.exists('pelicanconf.py'):
        print("❌ Error: Run this script from the GreatCTObrochure directory")
        sys.exit(1)
    
    if not os.path.exists('.git'):
        print("❌ Error: Git repository not initialized")
        sys.exit(1)
    
    print("✅ All requirements met")

def get_github_token():
    """Get GitHub token from user"""
    token = input("Enter your GitHub Personal Access Token: ").strip()
    if not token:
        print("❌ GitHub token is required")
        sys.exit(1)
    return token

def get_username():
    """Get GitHub username"""
    username = input("Enter your GitHub username: ").strip()
    if not username:
        print("❌ GitHub username is required")
        sys.exit(1)
    return username

def create_repository(token, username, repo_name):
    """Create GitHub repository"""
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    data = {
        'name': repo_name,
        'description': 'Great CTO - Professional website for CTO coaching and resources',
        'private': False,  # Must be public for free GitHub Pages
        'has_issues': True,
        'has_projects': False,
        'has_wiki': False,
        'auto_init': False  # We already have files
    }
    
    response = requests.post(
        'https://api.github.com/user/repos',
        headers=headers,
        json=data
    )
    
    if response.status_code == 201:
        print(f"✅ Repository created: https://github.com/{username}/{repo_name}")
        return True
    elif response.status_code == 422:
        error = response.json()
        if 'already exists' in str(error):
            print(f"⚠️  Repository already exists: https://github.com/{username}/{repo_name}")
            return True
        else:
            print(f"❌ Error creating repository: {error}")
            return False
    else:
        print(f"❌ Error creating repository: {response.status_code} - {response.text}")
        return False

def setup_git_remote(username, repo_name):
    """Setup git remote and push"""
    try:
        # Check if remote already exists
        result = subprocess.run(['git', 'remote', 'get-url', 'origin'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("⚠️  Remote 'origin' already exists")
            print(f"Current remote: {result.stdout.strip()}")
            
            update = input("Update remote URL? (y/n): ").strip().lower()
            if update == 'y':
                subprocess.run(['git', 'remote', 'set-url', 'origin', 
                              f'https://github.com/{username}/{repo_name}.git'])
                print("✅ Remote URL updated")
        else:
            # Add new remote
            subprocess.run(['git', 'remote', 'add', 'origin', 
                          f'https://github.com/{username}/{repo_name}.git'])
            print("✅ Remote added")
        
        # Push to GitHub
        print("📤 Pushing to GitHub...")
        subprocess.run(['git', 'branch', '-M', 'main'])
        
        push_result = subprocess.run(['git', 'push', '-u', 'origin', 'main'], 
                                   capture_output=True, text=True)
        
        if push_result.returncode == 0:
            print("✅ Code pushed successfully!")
            return True
        else:
            print(f"❌ Error pushing: {push_result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error with git operations: {e}")
        return False

def enable_github_pages_message(username, repo_name):
    """Show instructions for enabling GitHub Pages"""
    print("\n🔧 FINAL STEP - Enable GitHub Pages:")
    print("=====================================")
    print(f"1. Go to https://github.com/{username}/{repo_name}/settings/pages")
    print("2. Under 'Source', select 'Deploy from a branch'")
    print("3. Select branch 'gh-pages' (will be created by GitHub Action)")
    print("4. Click 'Save'")
    print(f"\n🌐 Your site will be live at: https://{username}.github.io/{repo_name}")
    print("\n⏰ The GitHub Action will build your site in 2-3 minutes")
    print("📅 New Substack posts will be imported daily at 3 AM UTC")

def main():
    print("🚀 Great CTO Website - GitHub Repository Creator")
    print("===============================================\n")
    
    check_requirements()
    
    token = get_github_token()
    username = get_username()
    repo_name = "GreatCTObrochure"
    
    print(f"\n📁 Creating repository: {username}/{repo_name}")
    
    if create_repository(token, username, repo_name):
        if setup_git_remote(username, repo_name):
            enable_github_pages_message(username, repo_name)
            print("\n🎉 Deployment complete! Your website is ready!")
        else:
            print("\n❌ Failed to push code. Please run git commands manually.")
    else:
        print("\n❌ Failed to create repository. Please create manually on GitHub.")

if __name__ == "__main__":
    main()
