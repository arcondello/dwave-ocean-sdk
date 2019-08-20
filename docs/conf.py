# -*- coding: utf-8 -*-
#
# DWaveNetworkX documentation build configuration file, created by
# sphinx-quickstart on Wed Jul 26 10:55:26 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# -- General configuration ------------------------------------------------
# import sphinx
# if sphinx.__version__  # can check here

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages'
]

autosummary_generate = True

# templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser'}

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Ocean Documentation'
copyright = u'D-Wave Systems Inc'
author = u'D-Wave Systems Inc'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0.1'
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None


add_module_names = False
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Joel December 11, 2017: added for mathjax operator \vc
# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = ["."]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Joel April 2018: table widths bug in Read The Docs
# html_context = {
#     'css_files': [
#         '_static/theme_overrides.css',  # override wide tables in RTD theme
#         ],
#      }
def setup(app):
   #app.add_javascript("custom.js")
   app.add_stylesheet('theme_overrides.css')
   app.add_stylesheet('cookie_notice.css')
   app.add_javascript('cookie_notice.js')


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'docs'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).

latex_preamble = r"""
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsbsy}
\usepackage{braket}
\usepackage{circuitikz}

\newcommand{\vc}[1]{\pmb{#1}}
"""

latex_documents = [
    (master_doc, 'docs.tex', u'docs Documentation',
     u'D-Wave Systems Inc', 'manual'),
]

#
# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'docs', u'dock Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'dock', u'dock Documentation',
     author, 'dock', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# Joel May 16: WARNING: failed to reach any of the inventories with the following issues:
# WARNING: intersphinx inventory 'http://networkx.readthedocs.io/en/latest/objects.inv' not
# fetchable due to <class 'requests.exceptions.HTTPError'>: ('intersphinx inventory %r not
# fetchable due to %s: %s', 'http://networkx.readthedocs.io/en/latest/objects.inv', <class
# 'requests.exceptions.HTTPError'>, HTTPError(...))

# Example configuration for intersphinx: refer to the Python standard library.
#intersphinx_mapping = {'https://docs.python.org/': None,
#                       'http://networkx.readthedocs.io/en/latest/': None}
intersphinx_mapping = {'python': ('https://docs.python.org/', None),
    'dimod': ('https://docs.ocean.dwavesys.com/projects/dimod/en/latest/', None),
    'binarycsp': ('https://docs.ocean.dwavesys.com/projects/binarycsp/en/latest/', None),
    'cloud-client': ('https://docs.ocean.dwavesys.com/projects/cloud-client/en/latest/', None),
    'neal': ('https://docs.ocean.dwavesys.com/projects/neal/en/latest/', None),
    'networkx': ('https://docs.ocean.dwavesys.com/projects/dwave-networkx/en/latest/', None),
    'system': ('https://docs.ocean.dwavesys.com/projects/system/en/latest/', None),
    'penaltymodel': ('https://docs.ocean.dwavesys.com/projects/penaltymodel/en/latest/', None),
    'minorminer': ('https://docs.ocean.dwavesys.com/projects/minorminer/en/latest/', None),
    'hybrid': ('https://docs.ocean.dwavesys.com/projects/hybrid/en/latest/', None),
    'qbsolv': ('https://docs.ocean.dwavesys.com/projects/qbsolv/en/latest/', None),
    'tabu': ('https://docs.ocean.dwavesys.com/projects/tabu/en/latest/', None),
    'sysdocs_gettingstarted': ('https://docs.dwavesys.com/docs/latest/', None)}

# sort documentation they way the appear in the source file
autodoc_member_order = 'bysource'

# show inherited members
# autodoc_default_flags = ['members', 'undoc-members', 'inherited-members', 'show-inheritance']