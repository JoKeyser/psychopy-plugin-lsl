===============================
Development and setup guide
===============================

This guide explains how to work with the plugin scaffolding in this repository. It is adapted from the `PsychoPy plugin template <https://github.com/psychopy/psychopy-plugin-template>`_.

.. warning::

   This project is still in the planning stage. The example code and setup steps below do not provide the planned LSL messaging function.

Setting up a development environment
====================================

Use a supported Python installation and create a virtual environment for development. From the repository root, install the project in editable mode with its test dependencies::

    python -m venv .venv
    # Activate the environment, then:
    python -m pip install --upgrade pip
    python -m pip install -e ".[tests]"

The test extra installs PsychoPy and pytest. To build the documentation as well, install the docs extra::

    python -m pip install -e ".[docs]"
    sphinx-build docs_src docs -b dirhtml

Writing plugin code
===================

A PsychoPy plugin is a Python package with entry points that let PsychoPy discover its components and other extensions. The ``psychopy_plugin_template`` directory contains template examples, including a Builder Component, a Standalone Routine, hardware classes, visual classes, and app ribbon contributions. These are example scaffolding only; they are not the planned LSL messaging feature.

For an introduction to PsychoPy plugin development, see the `PsychoPy plugin development guide <https://psychopy.org/developers/pluginDevGuide.html>`_. The structure and implementation of the LSL function have not yet been decided.

Configuring ``pyproject.toml``
==============================

The root ``pyproject.toml`` contains package metadata, dependencies, optional development dependencies, and PsychoPy entry points. When the project moves beyond its current scaffolding, keep these areas aligned with the implementation:

* **Name and version:** The distribution is currently named ``psychopy-plugin-lsl`` and starts at ``0.0.0``. The Python import package is still named ``psychopy_plugin_template``; changing that requires updating the package directory, entry-point targets, and package version lookup together.
* **Description and authors:** Keep these accurate as the project and its contributors evolve.
* **Dependencies:** Add runtime dependencies only when the implementation requires packages that are not already provided by PsychoPy.
* **Project URLs:** Keep the repository and changelog links current, and add documentation links when the published documentation is available.
* **Entry points:** These are how PsychoPy discovers plugin extensions. Update them to match real implemented classes; the existing entries point to template examples.

Installing locally for testing
==============================

An editable install (``python -m pip install -e ".[tests]"``) makes changes in this checkout available in the active environment without reinstalling after each edit. Run the test suite from the repository root with::

    python -m pytest

This verifies the current template scaffolding, not the not-yet-implemented LSL messaging behavior.

Publishing
==========

The repository includes a PyPI publishing workflow, but this project is not yet ready to publish as a usable LSL plugin. Do not create a public release that implies the planned functionality is available.

When the project is ready to publish, the workflow in ``.github/workflows/pypi.yaml`` uses PyPI trusted publishing. Configure a PyPI trusted publisher for this GitHub repository with workflow name ``pypi.yaml`` and environment ``pypi``, and create a GitHub environment named ``pypi``. Publishing is triggered by a version tag; ensure the tag matches the version in ``pyproject.toml``. Review the workflow and package contents before enabling or using publishing.
