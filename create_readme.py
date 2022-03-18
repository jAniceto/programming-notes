# import os
from pathlib import Path


# Configuration
TITLE = 'Programming Notes'
SUBTITLE = 'Programming notes, snippets and examples.'
DISCLAIMER = 'These notes contain excerpts, code snippets and examples from various sources including, but not limited to, Python Docs, The Hitchhiker’s Guide to Python, Real Python and Stack Overflow users.'
EXCLUDE_DIRS = ['.git', '.github', '.idea', '__pycache__', 'articles', 'docs']


def get_directories():
    """Get directories in current folder. 

    RETURNS
        list of pathlib.Path
    """
    cwd = Path.cwd()
    return [p for p in cwd.iterdir() if p.is_dir() and p.name not in EXCLUDE_DIRS]


def get_md_files(path):
    """Get all Markdown files in directory and sort. 

    ARGUMENTS
        path : pathlib.Path

    RETURNS
        list of pathlib.Path
    """
    return [p for p in path.iterdir() if p.is_file() and p.suffix == '.md']


def get_article_title(filename):
    """Get article title"""
    with open(filename, 'r', encoding='utf-8') as f:
        title = f.readline()
    return title.replace('#', '').replace('\n', '').replace('\r', '').strip()


def main():
    sections = get_directories()

    index_str = ''
    for section in sections:
        index_str += '## ' + section.stem.replace('-', ' ').upper() + '\n'

        md_files = get_md_files(section)

        for md_file in md_files:
            title = get_article_title(md_file)
            index_str += f"- [{title}](/{md_file.parent.name}/{md_file.name})\n"
        index_str += '\n'

    # Build Readme.md
    readme = f"""# {TITLE}
{SUBTITLE}
    
{index_str}
{DISCLAIMER}
"""

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme)

    print('readme.md updated!')


if __name__ == "__main__":
    main()
