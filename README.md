# CTO Coach Website

A professional static website for CTO coaching, fractional executive services, and technology consulting built with Pelican static site generator.

## Features

- **Professional Design**: Clean, conversion-focused design with compelling service pages
- **Substack Integration**: Automatically imports blog posts from your Substack RSS feed
- **Static Security**: Zero server-side vulnerabilities with static hosting
- **SEO Optimized**: Meta tags, Open Graph, schema markup, and sitemap
- **Mobile Responsive**: Mobile-first design that works on all devices
- **Fast Performance**: Optimized for speed with CDN-ready static files

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Customize Configuration

Edit `pelicanconf.py` to customize:

```python
AUTHOR = 'Your Name'
SITENAME = 'Your Site Name'
SUBSTACK_FEED_URL = 'https://yoursubstack.substack.com/feed'
```

### 3. Update Content

- Edit service pages in `content/pages/`
- Update your bio in `content/pages/about.md`
- Add your contact information in `content/pages/contact.md`

### 4. Build and Serve

```bash
# Development server with live reload
make dev

# Build for production
make publish
```

## Customization Guide

### Personal Information

1. **Update Author Info**: Edit `AUTHOR` in `pelicanconf.py`
2. **Social Links**: Update `SOCIAL` tuple in `pelicanconf.py`
3. **Contact Details**: Edit `content/pages/contact.md`

### Service Configuration

Edit the service pages in `content/pages/`:
- `services.md` - Overview of all services
- `cto-coach.md` - CTO coaching details and pricing
- `fractional-cto.md` - Fractional CTO service details
- `consulting.md` - Consulting service details

### Substack Integration

1. **Set Feed URL**: Update `SUBSTACK_FEED_URL` in `pelicanconf.py`
2. **Configure Import**: Adjust `SUBSTACK_IMPORT_LIMIT` and `SUBSTACK_PUBLIC_ONLY`
3. **Test Import**: Build the site to import latest posts

### Styling

- **Colors**: Edit CSS variables in `themes/cto-pro/static/css/style.css`
- **Fonts**: Update font links in `themes/cto-pro/templates/base.html`
- **Logo**: Add your logo to `content/assets/images/`

### Analytics

#### Plausible Analytics (Recommended)
```python
# In publishconf.py
PLAUSIBLE_ANALYTICS = {
    'domain': 'your-domain.com'
}
```

#### Google Analytics
```python
# In publishconf.py
GOOGLE_ANALYTICS = "G-XXXXXXXXXX"
```

## Deployment Options

### GitHub Pages (Free)

1. **Push to GitHub**: Create a repository and push your code
2. **Enable GitHub Pages**: In repository settings, enable Pages from `gh-pages` branch
3. **Automatic Deployment**: The included GitHub Action will build and deploy automatically

### Netlify (Recommended for Custom Domains)

1. **Connect Repository**: Link your GitHub repository to Netlify
2. **Configure Build**: Use build command `pelican content -o output -s publishconf.py`
3. **Set Environment Variables**: Add any required environment variables
4. **Custom Domain**: Configure your custom domain in Netlify settings

### Manual Deployment

```bash
# Build the site
make publish

# Upload the output/ directory to your web server
rsync -avz output/ user@server:/path/to/webroot/
```

## Content Management

### Blog Posts

- **Manual Posts**: Create `.md` files in `content/blog/`
- **Substack Import**: Automatic import from your Substack RSS feed
- **Post Format**: Include title, date, category, tags, and slug metadata

### Service Pages

Each service page should include:
- Compelling headline and value proposition
- Clear description of benefits
- Pricing information (if appropriate)
- Call-to-action buttons
- Client testimonials or case studies

### SEO Optimization

- **Page Titles**: Use descriptive, keyword-rich titles
- **Meta Descriptions**: Write compelling descriptions under 160 characters
- **Headers**: Use H1, H2, H3 structure for content hierarchy
- **Internal Linking**: Link between related pages and services

## Development Commands

```bash
# Install dependencies
make setup

# Development server with live reload
make dev

# Build for production
make publish

# Clean build directory
make clean

# Run with debugging
make html DEBUG=1
```

## File Structure

```
├── content/
│   ├── blog/              # Blog posts
│   ├── pages/             # Static pages
│   ├── assets/            # Images and static files
│   └── extras/            # robots.txt, favicon, etc.
├── themes/cto-pro/        # Custom theme
│   ├── templates/         # Jinja2 templates
│   └── static/           # CSS, JS, images
├── plugins/               # Custom Pelican plugins
├── .github/workflows/     # GitHub Actions
└── output/               # Generated site (git ignored)
```

## Troubleshooting

### Build Errors

1. **Template Errors**: Check Jinja2 syntax in theme templates
2. **Missing Dependencies**: Run `pip install -r requirements.txt`
3. **Plugin Errors**: Verify plugin configuration in `pelicanconf.py`

### Substack Import Issues

1. **Feed URL**: Verify your Substack RSS feed URL is correct
2. **Network Issues**: Check internet connection and firewall settings
3. **Content Parsing**: Some Substack formatting may need manual adjustment

### Deployment Issues

1. **GitHub Actions**: Check Actions tab for build errors
2. **Netlify**: Review deploy logs in Netlify dashboard
3. **DNS**: Verify domain DNS settings point to hosting provider

## Support

For questions or issues:

1. **Documentation**: Check Pelican documentation at https://docs.getpelican.com/
2. **Issues**: Create an issue in the repository
3. **Professional Help**: Contact for consulting assistance

## License

This project is open source. Feel free to customize and use for your own CTO coaching website.

<!-- Deployment trigger: Sat Aug  9 11:29:38 UTC 2025 -->
