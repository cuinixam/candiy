# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "candiy"
copyright = "2022, cuinixam"
author = "cuinixam"
release = "0.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

# markdown to rst (m2r) config - @see https://pypi.org/project/m2r/
extensions.append("m2r")

# draw.io config - @see https://pypi.org/project/sphinxcontrib-drawio/
extensions.append("sphinxcontrib.drawio")
drawio_default_transparency = True

# The suffix of source filenames.
source_suffix = [
    ".rst",
    ".md",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
