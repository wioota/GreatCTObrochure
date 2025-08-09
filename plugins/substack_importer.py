"""
Substack RSS Importer Plugin for Pelican

This plugin imports articles from a Substack RSS feed and creates Pelican articles.
"""

import logging
import os
import requests
import feedparser
from datetime import datetime
from pelican import signals
from pelican.readers import MarkdownReader
from pelican.utils import slugify
from markdownify import markdownify
import re

logger = logging.getLogger(__name__)

class SubstackImporter:
    def __init__(self, settings):
        self.settings = settings
        self.substack_url = settings.get('SUBSTACK_FEED_URL', '')
        self.substack_cache_dir = settings.get('SUBSTACK_CACHE_DIR', 'content/substack')
        self.import_limit = settings.get('SUBSTACK_IMPORT_LIMIT', 10)
        self.public_only = settings.get('SUBSTACK_PUBLIC_ONLY', True)
        
    def import_substack_posts(self, pelican):
        """Import posts from Substack RSS feed"""
        if not self.substack_url:
            logger.info("No Substack feed URL configured")
            return
            
        logger.info(f"Importing Substack posts from: {self.substack_url}")
        
        # Ensure cache directory exists
        os.makedirs(self.substack_cache_dir, exist_ok=True)
        
        try:
            # Fetch the RSS feed
            response = requests.get(self.substack_url, timeout=10)
            response.raise_for_status()
            
            # Parse the feed
            feed = feedparser.parse(response.content)
            
            if feed.bozo:
                logger.warning(f"RSS feed may have issues: {feed.bozo_exception}")
            
            imported_count = 0
            
            for entry in feed.entries[:self.import_limit]:
                if self._import_entry(entry):
                    imported_count += 1
                    
            logger.info(f"Successfully imported {imported_count} Substack posts")
            
        except requests.RequestException as e:
            logger.error(f"Failed to fetch Substack feed: {e}")
        except Exception as e:
            logger.error(f"Error importing Substack posts: {e}")
    
    def _import_entry(self, entry):
        """Import a single RSS entry as a Pelican article"""
        try:
            # Extract metadata
            title = entry.title
            pub_date = datetime(*entry.published_parsed[:6])
            link = entry.link
            
            # Create slug from title
            slug = slugify(title)
            
            # Skip if already imported
            article_path = os.path.join(self.substack_cache_dir, f"{slug}.md")
            if os.path.exists(article_path):
                return False
            
            # Extract content
            content = self._extract_content(entry)
            
            # Skip if no content
            if not content:
                logger.warning(f"No content found for: {title}")
                return False
            
            # Check if public only
            if self.public_only and self._is_paywalled(content):
                logger.info(f"Skipping paywalled article: {title}")
                return False
            
            # Create the markdown content
            markdown_content = self._create_markdown_content(
                title, pub_date, content, link, entry
            )
            
            # Write to file
            with open(article_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            logger.info(f"Imported: {title}")
            return True
            
        except Exception as e:
            logger.error(f"Error importing entry '{entry.title}': {e}")
            return False
    
    def _extract_content(self, entry):
        """Extract and clean content from RSS entry"""
        # Try content first, fall back to summary
        content = getattr(entry, 'content', [])
        if content:
            html_content = content[0].value
        else:
            html_content = getattr(entry, 'summary', '')
        
        if not html_content:
            return ''
        
        # Convert HTML to Markdown
        markdown_content = markdownify(html_content, heading_style="ATX")
        
        # Clean up the markdown
        markdown_content = self._clean_markdown(markdown_content)
        
        return markdown_content
    
    def _clean_markdown(self, content):
        """Clean up converted markdown content"""
        # Remove excessive newlines
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        # Remove empty links
        content = re.sub(r'\[\]\([^)]*\)', '', content)
        
        # Clean up whitespace
        content = content.strip()
        
        return content
    
    def _is_paywalled(self, content):
        """Check if content appears to be paywalled"""
        paywall_indicators = [
            'subscribe to read',
            'upgrade to paid',
            'become a paid subscriber',
            'this post is for paying subscribers',
            'paywall'
        ]
        
        content_lower = content.lower()
        return any(indicator in content_lower for indicator in paywall_indicators)
    
    def _create_markdown_content(self, title, pub_date, content, link, entry):
        """Create the complete markdown content with metadata"""
        # Extract tags if available
        tags = []
        if hasattr(entry, 'tags'):
            tags = [tag.term for tag in entry.tags]
        
        # Create metadata
        metadata = [
            f"Title: {title}",
            f"Date: {pub_date.strftime('%Y-%m-%d %H:%M')}",
            f"Category: Blog",
            f"Tags: {', '.join(tags) if tags else 'substack'}",
            f"Slug: {slugify(title)}",
            f"Source: Substack",
            f"Original-URL: {link}",
            f"Summary: {self._create_summary(content)}"
        ]
        
        # Combine metadata and content
        markdown_content = '\n'.join(metadata) + '\n\n' + content
        
        # Add source attribution
        markdown_content += f"\n\n---\n\n*Originally published on [Substack]({link})*"
        
        return markdown_content
    
    def _create_summary(self, content):
        """Create a summary from the content"""
        # Remove markdown formatting for summary
        text = re.sub(r'[#*`_\[\]()]', '', content)
        # Get first paragraph or 160 characters
        lines = text.split('\n')
        summary = ''
        for line in lines:
            line = line.strip()
            if line:
                summary = line
                break
        
        if len(summary) > 160:
            summary = summary[:157] + '...'
        
        return summary

def initialize_substack_importer(pelican):
    """Initialize the Substack importer"""
    importer = SubstackImporter(pelican.settings)
    importer.import_substack_posts(pelican)

def register():
    """Register the plugin with Pelican"""
    signals.initialized.connect(initialize_substack_importer)
