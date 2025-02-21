import os

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Learn Multibody Dynamics'
html_title = project
copyright = '2022, Jason K. Moore'
author = 'Jason K. Moore'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_togglebutton',  # this has to be first so that the material css doesn't clobber its css
    'jupyter_sphinx',
    'sphinx.ext.graphviz',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

if "ONGITHUB" not in os.environ:
    # Display TODO notes.
    todo_include_todos = True

# This configures sphinx to number figures and allow referencing them, if
# labeled, using :numref:`my_figure`.
numfig = True

# Sphinx >=4 default to MathJax v3, but v3 does not support wrapping lines. So
# force Sphinx to use v2 and config MathJax to wrap long lines.
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
mathjax2_config = {
    "HTML-CSS": {
        "linebreaks": {"automatic": True}
    }
}

# Setup intersphinx so that we can reference the SymPy documentation.
# :external:py:func:`~sympy.physics.vector.functions.dot` for example.
intersphinx_mapping = {
    'sympy': ('https://docs.sympy.org/latest/', None),
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html",
           "searchbox.html"]

}
html_theme_options = {
    'base_url': 'https://moorepants.github.io/learn-multibody-dynamics/',
    'color_primary': 'teal',
    'color_accent': 'deep-orange',  # hover color of hyperlinks
    # could do this if it is a GH pages build, takes too long for autobuild
    #'css_minify': True,
    #'html_minify': True,
    'repo_name': 'Learn Multibody Dynamics',
    'repo_url': 'https://github.com/moorepants/learn-multibody-dynamics/',
    "logo_icon": "&#xe52f",
    'master_doc': False,  # Doesn't show duplicate title
    'nav_links': [{"href": "index", "internal": True, "title": "Home"}],
}
html_css_files = ['css/custom.css']  # seems to load after the material css

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Options for jupyter-sphinx

jupyter_execute_data_priority = [
    'application/vnd.jupyter.widget-view+json',
    'text/html',
    'text/latex',  # put latex before png so sympy displays mathjax
    'image/svg+xml',
    'image/png',
    'image/jpeg',
    'text/plain',
]
