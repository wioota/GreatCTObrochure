#!/usr/bin/env python3
"""
GitHub Repository Creator for Great CTO Website
Usage: GITHUB_TOKEN=your_token GITHUB_USERNAME=your_username python3 deploy-github-api.py
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

def get_credentials():
    """Get GitHub credentials from environment or command line"""
    token = os.environ.get('GITHUB_TOKEN')
    username = os.environ.get('GITHUB_USERNAME')
    
    if not token:
        print("❌ GITHUB_TOKEN environment variable is required")
        print("   Set it with: export GITHUB_TOKEN=your_token")
        print("   Or create one at: https://github.com/settings/tokens")
        sys.exit(1)
    
    if not username:
        print("❌ GITHUB_USERNAME environment variable is required")
        print("   Set it with: export GITHUB_USERNAME=your_username")
        sys.exit(1)
    
    return token, username

def test_github_auth(token):
    """Test if GitHub token is valid"""
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    response = requests.get('https://api.github.com/user', headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        print(f"✅ GitHub authentication successful for user: {user_data['login']}")
        return True
    else:
        print(f"❌ GitHub authentication failed: {response.status_code}")
        print("   Please check your GitHub token")
        return False

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
        if any('already exists' in str(err) for err in error.get('errors', [])):
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
            
            # Update remote URL
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
        subprocess.run(['git', 'branch', '-M', 'main'], check=True)
        
        push_result = subprocess.run(['git', 'push', '-u', 'origin', 'main'], 
                                   capture_output=True, text=True)
        
        if push_result.returncode == 0:
            print("✅ Code pushed successfully!")
            return True
        else:
            print(f"❌ Error pushing: {push_result.stderr}")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Error with git operations: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def enable_github_pages_api(token, username, repo_name):
    """Try to enable GitHub Pages via API"""
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # Check if Pages is already enabled
    response = requests.get(
        f'https://api.github.com/repos/{username}/{repo_name}/pages',
        headers=headers
    )
    
    if response.status_code == 200:
        pages_info = response.json()
        print(f"✅ GitHub Pages already enabled: {pages_info['html_url']}")
        return True
    
    # Try to enable Pages with gh-pages branch
    data = {
        'source': {
            'branch': 'gh-pages',
            'path': '/'
        }
    }
    
    response = requests.post(
        f'https://api.github.com/repos/{username}/{repo_name}/pages',
        headers=headers,
        json=data
    )
    
    if response.status_code == 201:
        pages_info = response.json()
        print(f"✅ GitHub Pages enabled: {pages_info['html_url']}")
        return True
    else:
        print("⚠️  Could not enable GitHub Pages automatically")
        print("   The gh-pages branch will be created by the GitHub Action")
        return False

def show_final_instructions(username, repo_name):
    """Show final instructions"""
    print(f"\n🎉 DEPLOYMENT SUCCESSFUL!")
    print("=" * 50)
    print(f"📍 Repository: https://github.com/{username}/{repo_name}")
    print(f"🌐 Website URL: https://{username}.github.io/{repo_name}")
    print("\n📋 What happens next:")
    print("• GitHub Action builds your site (2-3 minutes)")
    print("• Site goes live automatically")
    print("• Daily Substack imports at 3 AM UTC")
    print("• Automatic rebuilds on code changes")
    
    print(f"\n🔧 If Pages isn't enabled automatically:")
    print(f"1. Go to https://github.com/{username}/{repo_name}/settings/pages")
    print("2. Source: 'Deploy from a branch'")
    print("3. Branch: 'gh-pages'")
    print("4. Click 'Save'")
    
    print(f"\n📊 Monitor deployment:")
    print(f"• Actions: https://github.com/{username}/{repo_name}/actions")
    print(f"• Pages: https://github.com/{username}/{repo_name}/settings/pages")

def main():
    print("🚀 Great CTO Website - Automated GitHub Deployment")
    print("=" * 50)
    print()
    
    check_requirements()
    
    try:
        token, username = get_credentials()
        
        if not test_github_auth(token):
            sys.exit(1)
        
        repo_name = "GreatCTObrochure"
        
        print(f"\n📁 Creating repository: {username}/{repo_name}")
        
        if create_repository(token, username, repo_name):
            if setup_git_remote(username, repo_name):
                enable_github_pages_api(token, username, repo_name)
                show_final_instructions(username, repo_name)
            else:
                print("\n❌ Failed to push code. Check git configuration.")
                sys.exit(1)
        else:
            print("\n❌ Failed to create repository.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n❌ Deployment cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
