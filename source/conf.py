# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'D14Project'
author = 'yiyaowen'
copyright = '2023, yiyaowen'
version = 'alpha && beta'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_tabs.tabs']

sphinx_tabs_disable_tab_closing = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_logo = 'https://media.githubusercontent.com/media/DreamersGather/D14Docs.Res/main/logo.png'
html_favicon = 'https://media.githubusercontent.com/media/DreamersGather/D14Project.Res/main/logo.png'
