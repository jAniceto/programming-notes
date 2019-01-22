import os

# Configuration
TITLE = 'Programming Notes'

SUBTITLE = 'Programming notes, snippets and examples in one place.'

DISCLAIMER = """
These notes contain excerpts, code snippets and examples from various sources including, but not limited to, Python Docs, The Hitchhiker’s Guide to Python and Stack Overflow users. Sources were not collected as this notes were intended for personal use.
"""

EXCLUDE_DIRS = ['.git']


def get_md_files(directory):
    """Get all Markdown files in directory"""
    md_files = []
    for file in os.listdir(directory):
        if file.endswith(".md"):
            md_files.append(os.path.join(directory, file))
    return md_files


def get_article_title(filename):
    """Get article title"""
    with open(filename, 'r', encoding='utf-8') as f:
        title = f.readline()
    return title.replace('#', '').replace('\n', '').replace('\r', '').strip()


# Filter the result using os.path.isdir() (and use os.path.join() to get the real path):
sections = [ name for name in os.listdir('.') if os.path.isdir(os.path.join('.', name)) and name not in EXCLUDE_DIRS ]

index_str = ''
for section in sections:
    index_str += '## ' + section.replace('-', ' ').upper() + '\n'
    
    md_files = get_md_files(section)
    
    for md_file in md_files:
        title = get_article_title(md_file)
        index_str += f'* [{title}](/{md_file})\n'.replace('\\', '/')
    index_str += '\n'


# Build Readme.md

readme = f"""
# {TITLE}
{SUBTITLE}

{index_str}
{DISCLAIMER}
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)