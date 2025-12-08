# Agent Instructions

## Project Overview
This is a Pelican static site generator project for Great CTO - a professional website for CTO coaching, fractional executive services, and technology consulting by Daniel Walters.

## Common Commands

### Development
- `pelican content` - Build the site
- `pelican --listen` - Build and serve locally
- `make html` - Build using Makefile
- `make serve` - Build and serve locally
- `make dev` - Build and serve with live reload

### Deployment
- `./push-to-github.sh` - Push changes and deploy to GitHub Pages
- `python deploy-github-api.py` - Deploy using GitHub API
- `./deploy-to-github.sh` - Interactive deployment guide

### Python Environment
- `pip install -r requirements.txt` - Install dependencies
- `python -m pelican --version` - Check Pelican version
- `export PATH=$PATH:/home/wioota/.local/bin` - Add Pelican to PATH

## Pre-Commit Checklist

Before committing any changes, **ALWAYS** run these checks:

### 1. Build Test (Required)
```bash
export PATH=$PATH:/home/wioota/.local/bin
pelican content -o output -s publishconf.py
```
**Expected**: `Done: Processed X articles, 0 drafts, 0 hidden articles, Y pages`
**If fails**: Fix build errors before committing

### 2. Local Preview (Required - User Must Approve)
```bash
cd output && python3 -m http.server 8000 &
# Visit http://localhost:8000
# Show preview to user
# Check homepage, services pages, blog articles
# WAIT FOR USER APPROVAL before proceeding to commit
pkill -f "python3 -m http.server"
```

### 3. Check for Common Issues
```bash
# Check for TODO comments
grep -r "TODO\|FIXME\|XXX" content/ themes/ plugins/ || echo "✓ No TODOs"

# Check for broken internal links (manual check needed)
# Verify all menu links work in preview

# Check for debug statements
grep -r "console.log\|print(" themes/ plugins/ || echo "✓ No debug statements"
```

### 4. Verify Configuration
```bash
# Check SITEURL is correct for production
grep SITEURL publishconf.py
# Should be: https://wioota.github.io/GreatCTObrochure

# Check Substack feed URL
grep SUBSTACK_FEED_URL pelicanconf.py
# Should be: https://greatcto.me/feed
```

## Post-Commit Deployment Workflow

After committing changes, **ALWAYS** deploy to make them live:

### Option 1: Automated Push Script (Recommended)
```bash
./push-to-github.sh
```
This script:
1. ✓ Extracts token from environment/configuration
2. ✓ Pushes to GitHub
3. ✓ Triggers automatic deployment
4. ✓ Cleans up credentials

### Option 2: Manual Push (If script fails)
```bash
# Set token from mcp-config.json
GITHUB_TOKEN=$(grep -o '"GITHUB_PERSONAL_ACCESS_TOKEN=[^"]*"' mcp-config.json | sed 's/"GITHUB_PERSONAL_ACCESS_TOKEN=\([^"]*\)"/\1/')

# Configure git remote with token
git remote set-url origin https://wioota:$GITHUB_TOKEN@github.com/wioota/GreatCTObrochure.git

# Push to GitHub
git push origin main

# Clean up (security!)
git remote set-url origin https://github.com/wioota/GreatCTObrochure.git
```

### Monitor Deployment
After pushing, monitor the deployment:
```bash
# Check GitHub Actions status
# Visit: https://github.com/wioota/GreatCTObrochure/actions

# Wait 2-3 minutes for build and deployment

# Verify site is updated
# Visit: https://wioota.github.io/GreatCTObrochure
```

## Complete Pre-Commit + Deploy Workflow

Here's the complete workflow to follow for any changes:

```bash
# 1. Make your changes to content, themes, or plugins
# ... edit files ...

# 2. Test the build
export PATH=$PATH:/home/wioota/.local/bin
pelican content -o output -s publishconf.py

# 3. Preview locally (REQUIRED - show user before committing)
cd output && python3 -m http.server 8000 &
# Visit http://localhost:8000
# Review changes with user
# Get user approval before proceeding
pkill -f "python3 -m http.server"
cd ..

# 4. ONLY AFTER USER APPROVAL - commit changes
git add .
git commit -m "Your descriptive commit message"

# 5. Deploy to GitHub Pages
./push-to-github.sh

# 6. Verify deployment
# Wait 2-3 minutes, then check: https://wioota.github.io/GreatCTObrochure
```

## Quick Reference Commands

### Full Build and Deploy
```bash
# IMPORTANT: Only use after getting user approval for changes!
# One-liner for quick updates (after user approval)
export PATH=$PATH:/home/wioota/.local/bin && \
pelican content -o output -s publishconf.py && \
git add . && \
git commit -m "Update content" && \
./push-to-github.sh
```

### Emergency Rollback
```bash
# If deployment breaks the site
git revert HEAD
./push-to-github.sh
```

## Project Structure
- `content/` - Markdown source files
  - `blog/` - Blog posts (manual posts)
  - `pages/` - Static pages (About, Services, Contact, etc.)
  - `substack/` - Auto-imported Substack articles
  - `assets/` - Images and static files
  - `extras/` - robots.txt, .nojekyll, favicon
- `output/` - Generated static site (git ignored)
- `themes/cto-pro/` - Custom theme
  - `templates/` - Jinja2 templates
  - `static/` - CSS, JS, images
    - `images/` - Theme images (logos, icons)
- `plugins/` - Pelican plugins
  - `substack_importer.py` - Auto-imports from Substack RSS
- `pelicanconf.py` - Development configuration
- `publishconf.py` - Production configuration
- `.github/workflows/deploy.yml` - GitHub Actions deployment

## Logo and Asset Management

### Adding/Updating the Site Logo

The site logo is displayed in the top navigation bar. To update it:

1. **Download the new logo image** to `themes/cto-pro/static/images/logo.png`
2. **Update the navigation template** in `themes/cto-pro/templates/base.html`
   - Logo is referenced as: `<img src="{{ SITEURL }}/{{ THEME_STATIC_DIR }}/images/logo.png">`
   - Current implementation: 40px height with Bootstrap flex layout
3. **Test locally** using development config: `pelican content -o output -s pelicanconf.py`
4. **Test production build**: `pelican content -o output -s publishconf.py`
5. **Verify both configurations** work correctly before committing

**Important Notes:**
- Use `pelicanconf.py` (RELATIVE_URLS=True) for local testing
- Use `publishconf.py` for production builds (absolute URLs)
- Logo should be high-resolution PNG for best quality
- Test both desktop and mobile layouts

## Code Style Preferences
- Python: Follow PEP 8
- Markdown: Standard formatting
- Config files: Maintain existing structure
- Commit messages: Clear, descriptive, present tense
- **NEVER commit without user approval**
- Always test build before committing
- Always show preview to user before committing
- Always deploy after committing

## Important Notes
- **GitHub Pages source**: Set to "GitHub Actions" (not "Deploy from a branch")
- **Substack integration**: Auto-imports from https://greatcto.me/feed daily
- **Deployment**: Automatic via GitHub Actions on push to main branch
- **Security**: GitHub token managed through environment variables
- **Build time**: ~30 seconds locally, 2-3 minutes on GitHub Actions

## Troubleshooting

### Build Fails
```bash
# Check for syntax errors in markdown
find content/ -name "*.md" -exec python -m markdown {} \; > /dev/null

# Verify all dependencies are installed
pip install -r requirements.txt

# Check Pelican logs for specific errors
pelican content -o output -s publishconf.py --debug
```

### Deployment Fails
```bash
# Check GitHub Actions logs
# Visit: https://github.com/wioota/GreatCTObrochure/actions

# Common issues:
# - Substack feed timeout: Temporarily disable substack_importer plugin
# - Permission error: Verify GitHub Pages source is "GitHub Actions"
# - Jekyll conflict: Ensure .nojekyll file exists in output/
```

### Site Shows README Instead of Website
- Cause: GitHub Pages source set to "Deploy from a branch"
- Fix: Change to "GitHub Actions" in repository settings

## Testing Checklist

Before marking any task as complete, verify:

- [ ] Site builds without errors
- [ ] All pages load correctly in local preview
- [ ] Navigation links work
- [ ] Images and CSS load properly
- [ ] Blog articles display correctly
- [ ] Changes committed with clear message
- [ ] Changes pushed to GitHub
- [ ] GitHub Actions build succeeds
- [ ] Live site updated (check in browser)

## Key URLs

- **Live Site**: https://wioota.github.io/GreatCTObrochure
- **Repository**: https://github.com/wioota/GreatCTObrochure
- **GitHub Actions**: https://github.com/wioota/GreatCTObrochure/actions
- **Pages Settings**: https://github.com/wioota/GreatCTObrochure/settings/pages
- **Substack Feed**: https://greatcto.me/feed
