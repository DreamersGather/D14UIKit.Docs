D14UIKit
========

.. image:: https://media.githubusercontent.com/media/DreamersGather/D14UIKit.Res/main/logo.png
   :height: 41

Overview
--------

D14UIKit is a GUI development library, which supports C++ and Python languages, for modern Windows platform. D14UIKit implements high-performance graphics rendering based on DirectX, and its default appearance adapts to the Fluent Design style introduced in Windows 10/11. Furthermore, the modern Dark Mode theme is integrated as a basic feature in the library, which provides a seamless visual experience between the D14UIKit based and the native applications. Benefitted from various UI controls built in the library, it is easy for developers to build exciting GUI applications on modern Windows platform.

:download:`Download the latest D14UIKit library on GitHub <https://github.com/DreamersGather/D14UIKit/releases>`

.. image:: https://media.githubusercontent.com/media/DreamersGather/D14Docs.Res/main/d14uikit/overview.png

Next Step
---------

If you are new to D14UIKit, we recommend you to read the following tutorials that demonstrate the basic usages of D14UIKit:

* Elementary

  * :ref:`d14uikit-tutorials-elementary-hello_window`
  * :ref:`d14uikit-tutorials-elementary-dpi_adaption`

* Intermediate

  * :ref:`d14uikit-tutorials-intermediate-object_oriented`
  * :ref:`d14uikit-tutorials-intermediate-layout_control`
  * :ref:`d14uikit-tutorials-intermediate-basic_callback`
  * :ref:`d14uikit-tutorials-intermediate-modern_theme`

* Advanced

  * :ref:`d14uikit-tutorials-advanced-advanced_callback`

For the developers who want to learn more details of D14UIKit, here are the complete API references:

* :ref:`d14uikit-reference-cpp`
* :ref:`d14uikit-reference-python`

Features
--------

Imagine a common task that we want to add GUI support for an existing command-line program, and here are the triple dilemmas that we may face:

1. **Large and Numerous Dependencies**:

   In some situations, the existing command-line program is only a few MBs or hundreds of KBs in size, while the GUI library can be tens of MBs in size. In terms of the development environment, it can even reach a size of several GBs. Nowadays, software development pursues efficiency, and in order to accelerate the process of software construction, developers tend to choose universal solutions, which leads to a simple application occupying a large amount of storage space. Perhaps in the near future, with the improvement of hardware performance and optimization of system architecture, the application size is no longer worth optimizing; however, "Simple is better than complex" is always a good criterion.

2. **Sophisticated Environment Setup**:

   Due to various limitations, many GUI libraries have complex configuration steps. Take cross-platform development as an example, a GUI library may have to introduce many configuration parameters to provide a unified development process.

3. **Old and Outdated UI Appearances**:

   Started from XP version, several update iterations have been done on the appearance of Windows, and it is a normal phenomenon under the trend of constantly evolving of the visual styles in the UI design industry. For example, Realistic style was introduced from Vista version, and reached its peak in Windows 7; however, Windows 8 turned to Flat style and Windows 10 further improved it. The latest Windows 11 fully adapts Fluent Design style, which aims to provide a more modern user experience. For the GUI libraries on Windows, some are from official development teams, and is keeping updated with system upgrades; most of others either have their own appearance styles, or still stuck in the past instead of following the industry trend.

.. seealso::

   **Realistic** style (a.k.a `Skeuomorph <https://en.wikipedia.org/wiki/Skeuomorph>`__) and **Flat** style (a.k.a `Flat design <https://en.wikipedia.org/wiki/Flat_design>`__).

The core UI framework of D14UIKit is based on native Win32 APIs, and all graphics rendering is implemented through DirectX. There are no complex dependencies, and thus the exported library is lightweight enough. In terms of UI appearances, D14UIKit adapts well to modern UI design styles like Fluent Design and Dark Mode theme. If you want to add GUI support for a small-scale command-line program on Windows without an overwhelming UI library, D14UIKit is a worthwhile approach to consider.

.. list-table:: Comparison of UI Libraries on Modern Windows Platform
   :header-rows: 1
   :stub-columns: 1
   :width: 100%

   * - Property / Name
     - D14UIKit
     - Qt
     - WinUI
     - Electron
   * - Library Size
     - ■
     - ■■
     - ■■■
     - ■■■
   * - Dev Difficulty
     - ✦
     - ✦✦✦
     - ✦✦✦
     - ✦✦
   * - Performance
     - ★★★
     - ★★
     - ★★
     - ★
   * - System Adaption
     - ✓
     - ✗
     - ✓
     - ✗
   * - Customizable
     - ✗
     - ✓
     - ✓
     - ✓

Inspiration
-----------

There is a UIKit module in `D14Engine <https://github.com/DreamersGather/D14Engine>`__, which was originally developed to build the GUI of ``D14Engine::Editor``. However, as the project developed, we gradually discovered its potential as a high-performance UI library. ``D14Engine::UIKit`` is developed with native C++, and its architecture is designed for high-performance and customization. In order to utilize the module flexibly, developers not only need to have considerable C++ experience, but also need to have a certain understanding of development technologies such as COM and DirectX that are bound to the Windows platform. Extra knowledge about Modern Rendering Pipeline is required if developers are going to improve its performance furthermore.

On the one hand, these characteristics of UIKit make it difficult to get started easily. Even developers who are familiar with related technologies may not hesitate to choose more user-friendly UI libraries when building lightweight applications that do not require high-performance and customization. On the other hand, we still want to provide the powerful features of UIKit to everyone in a simpler way at the cost of a minimal performance loss. Therefore, D14UIKit was born. It has been modified and improved based on ``D14Engine::UIKit``, and is a wrapper of the latter.

.. toctree::
   :caption: Getting Started
   :hidden:

   tutorials/index

.. toctree::
   :caption: User's Manual
   :hidden:

   man/cpp/index
   man/python/index

.. toctree::
   :caption: Developer Guides
   :hidden:

   devs/build
