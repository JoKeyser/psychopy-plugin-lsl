===============================
Development and setup guide
===============================

This guide covers developing and testing this template with PsychoPy Studio as a Linux AppImage.
It is adapted from the `PsychoPy plugin template <https://github.com/psychopy/psychopy-plugin-template>`_.
For general plugin guidance, see the `PsychoPy plugin development guide <https://psychopy.org/developers/pluginDevGuide.html>`_.

The template is a helpful starting point, though some of its setup guidance still reflects the older wxPython app.
PsychoPy Studio is the newer Svelte/Electron rewrite, first released in 2026, and is intended to replace that app; these instructions adapt this project to this transition and focus on Studio for now.
See the `Studio project overview <https://github.com/psychopy/psychopy-studio#readme>`_ and the `PsychoPy App overview <https://github.com/psychopy/psychopy-app#readme>`_.

.. warning::

   This project is still a scaffold. It does not implement the planned LSL messaging feature.

Set up the development environment
==================================

For now, this project deliberately uses one Studio-managed Python environment for plugin development, tests, documentation, and Builder integration.
This keeps the workflow simple and ensures tests use the same PsychoPy version as Studio, at the cost of keeping development tools in that environment instead of isolating them separately.
The steps below use the AppImage's portable-config mode to keep this development environment separate from Studio's regular user configuration.

.. note::

   All paths and the Studio version shown below are examples from the verified setup.
   Replace them with the AppImage location and version on your machine.

#. Set the path to the Studio AppImage and create a portable config directory.
   This command creates the sidecar directory and exits without launching Studio::

       APPIMAGE="$HOME/apps/PsychoPy_Studio_2026.2.4.AppImage"
       "$APPIMAGE" --appimage-portable-config

#. Launch the AppImage normally.
   While the sidecar directory exists, AppImageKit automatically uses it as ``XDG_CONFIG_HOME``::

       "$APPIMAGE"

#. On first launch, choose Studio's **User folder** for Python environments.
   Studio creates the managed environment under
   ``<AppImage path>.config/psychopy4/.python/<PsychoPy version>/``.
   Close Studio before installing development dependencies.
#. From the repository root, set the interpreter path and install the project and its test/documentation extras::

       APPIMAGE="$HOME/apps/PsychoPy_Studio_2026.2.4.AppImage"
       STUDIO_VERSION=2026.2.4
       STUDIO_PYTHON="${APPIMAGE}.config/psychopy4/.python/${STUDIO_VERSION}/bin/python"
       uv pip install --python "$STUDIO_PYTHON" --editable ".[tests,docs]"

The editable install makes source changes available in Studio's environment without reinstalling.
The ``tests`` extra provides pytest; the ``docs`` extra provides Sphinx and its theme.
Run the checks with the same interpreter::

    "$STUDIO_PYTHON" -m pytest
    "$STUDIO_PYTHON" -m sphinx docs_src docs -b dirhtml

The tests cover the current scaffold, not the planned LSL functionality.

Writing plugin code
===================

A PsychoPy plugin is a Python package with entry points that let PsychoPy discover its components and extensions.
The ``psychopy_plugin_template`` package contains example Builder, routine, visual, and hardware classes; these are scaffold only.

For an introduction to PsychoPy plugin development, see the `PsychoPy plugin development guide <https://psychopy.org/developers/pluginDevGuide.html>`_.
The structure of the planned LSL feature has not yet been decided.

Project metadata
================

The root ``pyproject.toml`` defines package metadata, dependencies, and entry points.
The distribution is ``psychopy-plugin-lsl``; its Python package is still named ``psychopy_plugin_template``.
Keep entry-point targets aligned with the implemented classes. For Studio AppImage, use ``psychopy.*`` entry points; do not add ``psychopy_app.*`` unless that module exists in the target environment.

Developing with PsychoPy Studio on Linux
========================================

The AppImage is the application bundle, not its Python environment.
Studio stores its configuration and managed Python environments separately from the AppImage.
With default settings, the environment is under ``$HOME/.config/psychopy4/.python/<PsychoPy version>/``.
The portable-config steps above create a separate environment alongside the AppImage and leave the default environment untouched.

.. note::

   Verified with PsychoPy Studio 2026.2.4: the default environment is ``$HOME/.config/psychopy4/.python/2026.2.4/`` and uses Python 3.11.13.
   The portable environment is separate; its interpreter also uses Python 3.11.13 and imports PsychoPy 2026.2.4.

After installing the editable project, restart the portable Studio instance.

Now, in Builder's **Custom** category, you should see the **Example** component (class ``ExampleComponent``) and **Example Standalone** as a separate routine.
Reinstall after changing entry points or package metadata.

To remove the development install from the portable environment::

    uv pip uninstall --python "$STUDIO_PYTHON" psychopy-plugin-lsl

Legacy ribbon example
======================

The template retains an old-app ribbon example in ``psychopy_plugin_template/app/ribbon.py``.
It imports ``FrameRibbonPluginSection`` from ``psychopy_app.ribbon`` and adds a convenience button to the old wxPython app's ribbons.
Studio is a separate Svelte/Electron application and does not provide that Python module or consume the old ``psychopy_app.*`` entry points.
In Studio 2026.2.4, those entry points caused PsychoPy to fail activation of the entire plugin because ``psychopy_app`` was unavailable.
The entry points are therefore removed; the ribbon code remains only as inactive template material and does not add a button to Studio.

Publishing
==========

The repository has a PyPI publishing workflow using trusted publishing, but the project is not ready for release.
Do not publish until the planned LSL functionality is implemented and the package contents and version tag have been reviewed.
