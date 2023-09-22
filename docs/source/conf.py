# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'TestingTesting'
copyright = '2023'
author = 'Martin'

release = '0.1'
version = '0.1.0'

# -- General configuration
matlab_src_dir = '.'
matlab_show_property_default_value = True
matlab_short_links = True

extensions = [
    'sphinx.ext.viewcode',   
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinxcontrib.matlab',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    # 'sphinx_rtd_theme'
]

import os
matlab_src_dir = os.path.abspath('..')

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

primary_domain = "mat"

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
