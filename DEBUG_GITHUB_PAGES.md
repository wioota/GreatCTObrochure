# GitHub Pages Debugging Guide

## 🔍 Common Issues and Solutions

### 1. Check GitHub Actions Build Status

**Go to**: `https://github.com/wioota/GreatCTObrochure/actions`

**Look for**:
- ✅ Green checkmark = Build successful
- ❌ Red X = Build failed
- 🟡 Yellow circle = Build in progress

### 2. If Build is Failing

**Click on the failed action** to see error details:

**Common issues**:
- **Dependencies missing**: Check if `requirements.txt` has all packages
- **Substack feed error**: Feed might be temporarily unavailable
- **Pelican build error**: Check content syntax

**Quick fix for Substack issues**:
```python
# In pelicanconf.py, temporarily disable Substack import:
PLUGINS = [
    'neighbors',
    'sitemap',
    # 'substack_importer',  # Comment this out temporarily
]
```

### 3. Check GitHub Pages Configuration

**Go to**: `https://github.com/wioota/GreatCTObrochure/settings/pages`

**Verify**:
- Source: "Deploy from a branch"
- Branch: "gh-pages" 
- Folder: "/ (root)"
- Custom domain: Leave blank for now

### 4. Check if gh-pages Branch Exists

**Go to**: `https://github.com/wioota/GreatCTObrochure/branches`

**You should see**:
- `main` branch (your source code)
- `gh-pages` branch (auto-created by GitHub Action)

**If gh-pages branch is missing**:
- The GitHub Action hasn't run successfully yet
- Check Actions tab for errors

### 5. DNS/URL Issues

**Expected URL**: `https://wioota.github.io/GreatCTObrochure`

**If URL returns 404**:
- Wait 5-10 minutes after successful build
- Check Pages settings are correct
- Verify repository name matches URL path

### 6. Force Rebuild

**Trigger a new build**:
1. Go to Actions tab
2. Click "Build and Deploy CTO Coach Website"
3. Click "Run workflow" button
4. Select "main" branch
5. Click "Run workflow"

### 7. Check Build Output

**In the GitHub Action logs, look for**:
```
Done: Processed X articles, 0 drafts, 0 hidden articles, Y pages
```

**Should see**:
- 11 articles (2 manual + 9 Substack)
- 7 pages (About, Contact, Services, etc.)

### 8. Test Local Build

**Run locally to debug**:
```bash
cd /home/wioota/Dev/GreatCTObrochure

# Test production build
export PATH=$PATH:/home/wioota/.local/bin
pelican content -o output -s publishconf.py

# Check for errors
echo $?  # Should be 0

# Test server
cd output && python3 -m http.server 8000
# Visit http://localhost:8000
```

### 9. Repository Permissions

**Check if repository is**:
- ✅ Public (required for free GitHub Pages)
- ✅ Has Pages enabled
- ✅ Actions enabled

### 10. Alternative: Manual Deployment

**If GitHub Actions keeps failing**:
1. Build locally: `pelican content -o output -s publishconf.py`
2. Go to your repository
3. Create new branch: `gh-pages`
4. Upload contents of `output/` folder to `gh-pages` branch
5. Enable Pages from `gh-pages` branch

## 🚨 Emergency Fixes

### Fix 1: Disable Substack Import Temporarily
```python
# In pelicanconf.py
PLUGINS = [
    'neighbors',
    'sitemap',
    # 'substack_importer',  # Comment out
]
```

### Fix 2: Simplified GitHub Action
Create `.github/workflows/simple-deploy.yml`:
```yaml
name: Simple Deploy
on:
  push:
    branches: [ main ]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    - run: |
        pip install pelican[markdown] beautifulsoup4
        pelican content -o output -s publishconf.py
    - uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./output
```

### Fix 3: Check Specific Error Messages

**Common errors in Actions**:
- `ModuleNotFoundError`: Missing dependency in requirements.txt
- `TemplateNotFound`: Theme template issue  
- `UnicodeError`: Content encoding issue
- `ConnectionError`: Substack feed unreachable

## 📞 Status Check Commands

**Check your deployment status**:
```bash
# Check if site is live
curl -I https://wioota.github.io/GreatCTObrochure

# Should return: HTTP/2 200
```

## 🎯 Expected Timeline

**After pushing to GitHub**:
- **0-2 minutes**: Action starts
- **2-5 minutes**: Build completes
- **5-10 minutes**: Pages available at URL
- **First build may take longer**

Let me know which step is failing and I'll help debug further!
