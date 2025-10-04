import os
from pathlib import Path
import re

def generate_index():
    # Define the base directory
    base_dir = Path("./root")
    
    # Start building the HTML content
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Knowledge Vault Index</title>
    <style>
        @font-face {
            font-family: 'ZedMono Nerd Font';
            src: url('./custom_fonts/ZedMonoNerdFont-Regular.ttf') format('truetype');
            font-weight: normal;
            font-style: normal;
        }
        
        @font-face {
            font-family: 'ZedMono Nerd Font';
            src: url('./custom_fonts/ZedMonoNerdFont-Bold.ttf') format('truetype');
            font-weight: bold;
            font-style: normal;
        }
        
        @font-face {
            font-family: 'ZedMono Nerd Font';
            src: url('./custom_fonts/ZedMonoNerdFont-Italic.ttf') format('truetype');
            font-weight: normal;
            font-style: italic;
        }
        
        @font-face {
            font-family: 'ZedMono Nerd Font';
            src: url('./custom_fonts/ZedMonoNerdFont-BoldItalic.ttf') format('truetype');
            font-weight: bold;
            font-style: italic;
        }
        
        :root {
            /* Gruvbox Dark */
            --dark-bg: #1d2021;
            --dark-bg-alt: #282828;
            --dark-bg-card: #32302f;
            --dark-text: #ebdbb2;
            --dark-text-secondary: #d5c4a1;
            --dark-accent: #83a598;
            --dark-accent-hover: #458588;
            --dark-border: #504945;
            --dark-code-bg: #282828;
            
            /* Gruvbox Light */
            --light-bg: #fbf1c7;
            --light-bg-alt: #f9f5d7;
            --light-bg-card: #ebdbb2;
            --light-text: #3c3836;
            --light-text-secondary: #665c54;
            --light-accent: #076678;
            --light-accent-hover: #458588;
            --light-border: #d5c4a1;
            --light-code-bg: #f2e5bc;
        }
        
        * {
            font-family: 'ZedMono Nerd Font', monospace !important;
        }
        
        body {
            font-family: 'ZedMono Nerd Font', monospace;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            transition: background-color 0.3s, color 0.3s;
        }
        
        body.dark {
            background-color: var(--dark-bg);
            color: var(--dark-text);
        }
        
        body.light {
            background-color: var(--light-bg);
            color: var(--light-text);
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        h1 {
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid;
            transition: border-color 0.3s;
            font-family: 'ZedMono Nerd Font', monospace;
            font-weight: bold;
        }
        
        body.dark h1 {
            color: var(--dark-text);
            border-color: var(--dark-accent);
        }
        
        body.light h1 {
            color: var(--light-text);
            border-color: var(--light-accent);
        }
        
        .theme-toggle {
            position: fixed;
            top: 20px;
            right: 20px;
            background: none;
            border: none;
            cursor: pointer;
            font-size: 1.5rem;
            padding: 10px;
            border-radius: 50%;
            transition: background-color 0.3s;
            font-family: 'ZedMono Nerd Font', monospace;
        }
        
        body.dark .theme-toggle {
            color: var(--dark-text);
            background-color: var(--dark-bg-alt);
        }
        
        body.light .theme-toggle {
            color: var(--light-text);
            background-color: var(--light-bg-alt);
        }
        
        .theme-toggle:hover {
            opacity: 0.8;
        }
        
        .directory {
            margin-bottom: 20px;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: background-color 0.3s, box-shadow 0.3s;
            font-family: 'ZedMono Nerd Font', monospace;
        }
        
        body.dark .directory {
            background-color: var(--dark-bg-card);
            box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        
        body.light .directory {
            background-color: var(--light-bg-card);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .directory-title {
            font-weight: bold;
            margin-top: 15px;
            font-size: 1.2em;
            display: flex;
            align-items: center;
            font-family: 'ZedMono Nerd Font', monospace;
        }
        
        .folder-icon {
            margin-right: 10px;
        }
        
        body.dark .folder-icon {
            color: #fabd2f;
        }
        
        body.light .folder-icon {
            color: #d79921;
        }
        
        ul {
            list-style-type: none;
            padding-left: 20px;
            font-family: 'ZedMono Nerd Font', monospace;
        }
        
        li {
            margin-bottom: 8px;
            font-family: 'ZedMono Nerd Font', monospace;
        }
        
        a {
            text-decoration: none;
            display: inline-block;
            padding: 5px 10px;
            border-radius: 4px;
            transition: background-color 0.3s, color 0.3s;
            font-family: 'ZedMono Nerd Font', monospace;
        }
        
        body.dark a {
            color: var(--dark-accent);
        }
        
        body.light a {
            color: var(--light-accent);
        }
        
        body.dark a:hover {
            background-color: var(--dark-bg-alt);
            color: var(--dark-accent-hover);
        }
        
        body.light a:hover {
            background-color: var(--light-bg-alt);
            color: var(--light-accent-hover);
        }
        
        .file-icon {
            margin-right: 8px;
        }
        
        body.dark .file-icon {
            color: #8ec07c;
        }
        
        body.light .file-icon {
            color: #689d6a;
        }
        
        .breadcrumb {
            margin-bottom: 20px;
            font-size: 0.9em;
            transition: color 0.3s;
            font-family: 'ZedMono Nerd Font', monospace;
        }
        
        body.dark .breadcrumb {
            color: var(--dark-text-secondary);
        }
        
        body.light .breadcrumb {
            color: var(--light-text-secondary);
        }
        
        .stats {
            margin-top: 30px;
            padding: 15px;
            border-radius: 8px;
            font-size: 0.9em;
            transition: background-color 0.3s, color 0.3s;
            font-family: 'ZedMono Nerd Font', monospace;
        }
        
        body.dark .stats {
            background-color: var(--dark-bg-alt);
            color: var(--dark-text-secondary);
        }
        
        body.light .stats {
            background-color: var(--light-bg-alt);
            color: var(--light-text-secondary);
        }
    </style>
</head>
<body class="dark">
    <button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme">
        <span id="theme-icon">🌙</span>
    </button>
    
    <div class="container">
        <h1>Knowledge Vault Index</h1>
        <div class="breadcrumb">Home / site-lib</div>
"""

    # Function to recursively process directories
    def process_directory(directory, level=0, breadcrumb="root"):
        nonlocal html_content
        
        # Get all items in the directory
        items = sorted(directory.iterdir())
        
        # Separate directories and files
        dirs = [item for item in items if item.is_dir()]
        files = [item for item in items if item.is_file() and item.suffix.lower() == '.html']
        
        # Add directory title if not the root
        if level > 0:
            dir_name = directory.name.replace('\\', '')
            html_content += f'<div class="directory" style="margin-left: {level * 20}px;">\n'
            html_content += f'<div class="directory-title"><span class="folder-icon">📁</span>{dir_name}</div>\n'
            html_content += f'<div class="breadcrumb">Home / {breadcrumb}</div>\n'
        
        # Add files
        if files:
            html_content += '<ul>\n'
            for file in files:
                file_path = file.relative_to(Path('.'))
                file_name = file.stem.replace('_', ' ').title()
                html_content += f'    <li><a href="{file_path}"><span class="file-icon">📄</span>{file_name}</a></li>\n'
            html_content += '</ul>\n'
        
        # Process subdirectories
        for subdir in dirs:
            new_breadcrumb = f"{breadcrumb} / {subdir.name.replace('\\', '')}"
            process_directory(subdir, level + 1, new_breadcrumb)
        
        # Close directory div if not the root
        if level > 0:
            html_content += '</div>\n'
    
    # Start processing from the base directory
    process_directory(base_dir)
    
    # Add stats section
    html_content += """
        <div class="stats">
            <p>Total directories and files: """ + str(len(list(base_dir.rglob("*")))) + """</p>
        </div>
    </div>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const themeToggle = document.getElementById('theme-toggle');
            const themeIcon = document.getElementById('theme-icon');
            const body = document.body;
            
            // Check for saved theme preference or default to dark
            const currentTheme = localStorage.getItem('theme') || 'dark';
            body.className = currentTheme;
            updateThemeIcon(currentTheme);
            
            themeToggle.addEventListener('click', function() {
                // Toggle between dark and light themes
                if (body.className === 'dark') {
                    body.className = 'light';
                    localStorage.setItem('theme', 'light');
                    updateThemeIcon('light');
                } else {
                    body.className = 'dark';
                    localStorage.setItem('theme', 'dark');
                    updateThemeIcon('dark');
                }
            });
            
            function updateThemeIcon(theme) {
                if (theme === 'dark') {
                    themeIcon.textContent = '🌙';
                } else {
                    themeIcon.textContent = '☀️';
                }
            }
        });
    </script>
</body>
</html>
"""
    
    # Write the HTML content to index.html
    with open('index.html', 'w') as f:
        f.write(html_content)
    
    print("index.html has been generated successfully!")

def add_custom_fonts_to_html():
    # Define the base directory
    base_dir = Path("./root")
    
    # Define the custom font CSS
    font_css = """
    <style>
        @font-face {
            font-family: 'ZedMono Nerd Font';
            src: url('/custom_fonts/ZedMonoNerdFont-Regular.ttf') format('truetype');
            font-weight: normal;
            font-style: normal;
        }
        
        @font-face {
            font-family: 'ZedMono Nerd Font';
            src: url('/custom_fonts/ZedMonoNerdFont-Bold.ttf') format('truetype');
            font-weight: bold;
            font-style: normal;
        }
        
        @font-face {
            font-family: 'ZedMono Nerd Font';
            src: url('/custom_fonts/ZedMonoNerdFont-Italic.ttf') format('truetype');
            font-weight: normal;
            font-style: italic;
        }
        
        @font-face {
            font-family: 'ZedMono Nerd Font';
            src: url('/custom_fonts/ZedMonoNerdFont-BoldItalic.ttf') format('truetype');
            font-weight: bold;
            font-style: italic;
        }
        
        * {
            font-family: 'ZedMono Nerd Font', monospace !important;
        }
    </style>
    """
    
    # Find all HTML files in the directory
    html_files = list(base_dir.rglob("*.html"))
    
    for html_file in html_files:
        # Read the HTML file
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if the font CSS is already added
        if "ZedMono Nerd Font" in content:
            print(f"Font already applied to {html_file}")
            continue
        
        # Find the position to insert the font CSS (after the <head> tag)
        head_match = re.search(r'<head[^>]*>', content)
        if head_match:
            insert_pos = head_match.end()
            # Insert the font CSS
            modified_content = content[:insert_pos] + font_css + content[insert_pos:]
            
            # Write the modified content back to the file
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            
            print(f"Font added to {html_file}")
        else:
            print(f"Could not find <head> tag in {html_file}")

if __name__ == "__main__":
    generate_index()
    add_custom_fonts_to_html()
