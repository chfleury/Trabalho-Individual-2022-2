import sys
import os

project = 'tf-gces'
copyright = '2023, Christian Fleury'
author = 'Christian Fleury'

sys.path.append("/home/chfleury/Music/breathe-4.34.0/breathe")

extensions = ['breathe' ]


breathe_projects = {"myproject": os. getcwd() +"/xml"}

breathe_default_project = "myproject"# Configuration file for the Sphinx documentation builder.



 
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ptbr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
