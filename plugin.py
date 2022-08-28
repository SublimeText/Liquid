import sublime
from pathlib import Path

MD_TEMPLATE = """
%YAML 1.2
---
# http://www.sublimetext.com/docs/syntax.html
name: Markdown (Liquid)
scope: text.html.markdown.liquid
version: 2

extends: {base_syntax}

contexts:
  prototype:
    - meta_prepend: true
    - include: scope:source.liquid

  html-content:
    - include: scope:text.html.liquid#html
"""


def select_base_syntax():
    # prefer MarkdownEditing if present
    for base_syntax in sublime.find_syntax_by_name("Markdown"):
        if "MarkdownEditing" in base_syntax.path:
            return base_syntax.path
    # fallback to default markdown
    return "Packages/Markdown/Markdown.sublime-syntax"


def create_markdown_syntax():
    """
    Creates an inherit Markdown (Liquid).sublime-syntax.

    If present MarkdownEditing's Markdown.sublime-syntax is extended.
    Otherwise ST's Markdown package is used.
    """
    syntax_file = (
        Path(sublime.packages_path())
        / __package__
        / "Syntaxes/Markdown (Liquid).sublime-syntax"
    )
    syntax_content = MD_TEMPLATE.lstrip().format(base_syntax=select_base_syntax())

    # check existance and content to avoid touching unchanged files
    try:
        syntax_file.parent.mkdir(parents=True, exist_ok=True)
        with open(syntax_file) as f:
            if f.read() == syntax_content:
                return
    except FileNotFoundError:
        pass

    # create or update markdown syntax definition
    with open(syntax_file, "w") as f:
        f.write(syntax_content)


def plugin_loaded():
    create_markdown_syntax()
