# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'toads-docs'
copyright = '2024, Docs By Toad114514'
author = 'Toad114514'
release = 'v0.114.5'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  'myst_parser',
  "sphinxcontrib.mermaid",
]

templates_path = ['_templates']
exclude_patterns = []

source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

myst_enable_extensions = [
    "tasklist",
    "deflist",
    "dollarmath",
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
# New Book theme config
html_theme_option = {
    "repository_url": "https://github.com/toad114514/toads-docs",
    "use_repository_button": True,
    "home_page_in_toc": True,
    "use_download_button": True,
    "use_fullscreen_button": True,
    "use_issues_button": True,
}

# readthedocs config
# html_theme_option = {
    # 'logo_only': True,
    # 'display_version': True,
    # 'prev_next_buttons_location': 'bottom',
    # 'style_external_links': False,
    # 'collapse_navigation': True,
    # 'sticky_navigation': True,
    # 'navigation_depth': 4,
    # 'includehidden': True,
    # 'titles_only': False
# }

html_static_path = ['_static']
html_search_language = 'zh'
html_favicon = "https://toads-docs.readthedocs.io/zh-cn/latest/_img/favicon.ico"
html_logo = "_img/logos.png"