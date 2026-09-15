# Sphinx configuration for the Pygacq documentation
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "Pygacq"
author = "Olesja Smirnova"
copyright = "2026, AURA"
release = "0.2"
version = release

extensions = [
    "myst_parser",        # write pages in Markdown (MyST) as well as reStructuredText
]

# Both Markdown (.md) and reStructuredText (.rst) pages are accepted
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# MyST extras: ::: fenced directives (admonitions, figures) and definition lists
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "attrs_inline",       # {w=24px} after an image to set its size
]
# Anchors for headings down to #### so they can be linked to
myst_heading_anchors = 4

# _drafts holds unfinished pages that are kept in the repository but not built
exclude_patterns = ["_build", "_drafts", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_title = "Pygacq documentation"
html_static_path = []
