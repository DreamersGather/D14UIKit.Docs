.. _d14uikit-tutorials-elementary-hello_window:

Hello Window
============

.. image:: https://media.githubusercontent.com/media/DreamersGather/D14Docs.Res/main/d14uikit/tutorials/hello_window.png

.. note::

  The source code of the demo can be found in **d14uikit/demo**.

Download Wrapper
----------------

:download:`Download the latest D14UIKit library on GitHub <https://github.com/DreamersGather/D14UIKit/releases>`

The directory structure is as follows:

.. tabs::

  .. tab:: C++

    * **d14uikit_cpp.zip**

      * **demo**
      * **include**
      * **lib**

        * **debug/D14UIKit.dll** (DLL with ``/MDd`` Runtime Library)
        * **release/D14UIKit.dll** (DLL with ``/MD`` Runtime Library)
        * **D14UIKit.lib**

    .. note::

        About the differences between the DLLs with ``/MDd`` and ``/MD`` runtime libraries, please refer to :ref:`d14uikit-devs-build_cpp_wrapper` in developer guides for a brief introduction. For users (rather than developers) of D14UIKit library, it is sufficient to make sure linking the correct DLLs for your targets respectively (i.e. ``/MDd`` for Debug, ``/MD`` for Release).

  .. tab:: Python

    * **d14uikit_python.zip**

      * **demo**
      * **D14UIKit.pyd** (Python DLL)
      * **D14UIKit.pyi** (Python Stub File)

    .. note::

        A pyd file is a Python DLL (Windows only) that can be imported by other Python code at runtime. For example, you can import **D14UIKit.pyd** in your scripts with ``import D14UIKit``.

Environment Setup
-----------------

The wrapper structure is relatively clear. To get started, you may just follow the basic development steps of common C++/Python projects. Here is a simple configuration example for your reference:

.. tabs::

  .. tab:: C++

    Copy **D14UIKit.lib** and **debug/D14UIKit.dll** to your workspace first, and then create a **HelloWindow.cpp** file in the same directory:

    .. sourcecode:: c++

      #include "Application.h"
      #include "MainWindow.h"

      using namespace d14uikit;

      int main()
      {
          Application app;
          MainWindow mwnd;
          return app.run();
      }

    Taking MSVC as an example, run the following command to build a Debug version of your application (for Release version, you need to use ``/MD`` instead of ``/MDd``):

    .. sourcecode:: bat

      > cl HelloWindow.cpp /std:c++20 /I path/to/d14uikit/include /link D14UIKit.lib /MDd

  .. tab:: Python

    Copy **D14UIKit.pyd** to your workspace first, and then create a **HelloWindow.py** script in the same directory:

    .. sourcecode:: python

      from D14UIKit import *

      app = Application()
      mwnd = MainWindow()
      app.run()

    Just run it with your ``python.exe``.
