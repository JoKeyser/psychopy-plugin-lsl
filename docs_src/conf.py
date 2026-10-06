# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PsychoPy plugin for LSL'
copyright = '2026, Johannes Keyser'
author = 'Johannes Keyser'
release = '0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

# BF: Mock gltools so the docs build does not segfault.
# See explanation in upstream PR, https://github.com/psychopy/psychopy-plugin-template/pull/9
# This is a temporary workaround. It should be removed once psychopy.tools.gltools
# no longer queries OpenGL at import time (which triggers this crash).
import sys
from unittest import mock

sys.modules['psychopy.tools.gltools'] = mock.MagicMock()


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'psychopy'
