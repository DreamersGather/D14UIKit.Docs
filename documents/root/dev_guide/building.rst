Building
========

Prerequisites
-------------

The development of D14UIKit is based on `Visual Studio`_ series tools, therefore the following components (community version is sufficient) need to be installed through Visual Studio Installer first:

* C++ Wrapper: **C++ Desktop Development** (Compiler, Linker and SDK etc.)
* Python Wrapper: **Python Development** with *Python native development tools*

.. seealso::

   More details about how to co-develop C++ and Python in Visual Studio can be found in this MSDN article: `Create a C++ extension for Python in Visual Studio`_.

In order to pack ``D14Engine::UIKit`` into D14UIKit, the following two technologies are mainly used:

* C++ Wrapper: `pimpl idiom`_, used to hide implementation, minimize coupling and separate interfaces
* Python Wrapper: `pybind11`_, used to export C++ project as Python compatible Dll (a.k.a pyd file)

D14UIKit is basically migrated from the Common, Renderer and UIKit modules of D14Engine with some necessary modifications. All of changed source files (in Src directory) are recorded in the **Src/sensitive.txt** file. In addition, a new folder **Exp** is created in the project root directory to store the extra wrapper code.

.. _Visual Studio: https://visualstudio.microsoft.com/
.. _Create a C++ extension for Python in Visual Studio: https://learn.microsoft.com/en-us/visualstudio/python/working-with-c-cpp-python-in-visual-studio?view=vs-2022
.. _pimpl idiom: https://learn.microsoft.com/en-us/cpp/cpp/pimpl-for-compile-time-encapsulation-modern-cpp
.. _pybind11: https://github.com/pybind/pybind11

Project Setup
-------------

Download the project repository from `GitHub`_ (optional ``--depth=1`` for reducing .git size):

.. sourcecode:: bat

   > git clone https://github.com/DreamersGather/D14UIKit.git --depth=1

We use `Git Large File Storage`_ system to help manage the binaries (like png files) in the project, and you may need to run an extra command ``git lfs fetch`` to download the lfs files. If you encounter any problems while downloading the lfs files, simply use the search box or propose an issue to `D14UIKit <https://github.com/DreamersGather/D14UIKit/issues>`__.

.. _GitHub: https://github.com/yiyaowen/D14UIKit
.. _Git Large File Storage: https://git-lfs.com

Everything is ready and we can start building D14UIKit. The project structure is as follows:

* **Bin** (Resource Files)

  * **Images**
  * **Shaders**

* **Dist** (Created after running pack.ps1)

* **Exp** (Wrapper Code of PIMPL)

  * **Inc** (C++ Interfaces)
  * **PyBind** (Python Interfaces)
  * **.h/.cpp** (Implementation)

* **Inc** (External Headers)
* **Int** (Build Intermediate Files)
* **Lib** (External Libraries)
* **Out** (Build Output Files)
* **Src** (Migrated from D14Engine)

  * **Common**
  * **Renderer**
  * **UIKit**
  * **sensitive.txt** (Diff-record of **Src**)

* **Test** (Copy D14UIKit.dll here)

  * **PyBind** (Copy D14UIKit.pyd here)

    * **scripts** (Demos for testing Python wrapper)

  * **sources** (Demos for testing C++ wrapper)

* **pack.ps1** (Used for packing wrappers to **Dist**)
* **Miscellaneous**

Open **D14UIKit.sln** in Visual Studio, and there are three projects in the explorer window:

.. tip::

  The explorer window can be found through *View* → *Solution Explorer*.

* **D14UIKit**

  The project for building C++ and Python wrappers. After the building is completed, the generated libraries will be copied to the testing directories, which is required for building **TestCpp** and **TestPyBind**.

* **TestCpp**

  The project for testing C++ wrapper, which includes some basic demos, and the necessary dependencies (``include_directories``, ``library_paths`` etc.) have already been configured.

* **TestPyBind**

  The project for testing Python wrapper, which includes some basic demos, and the environment has already been setup for debugging C++ and Python code together.

.. _d14uikit-devs-build_cpp_wrapper:

Build C++ Wrapper
-----------------

1. Select **D14UIKit** as the startup project.
2. Select one configuration from **(Debug/Rebug/Release) | (Win32/x64/x86)**.
3. Build the project, and the library files will be generated in **Out**.

.. important::

   .. list-table:: Comparison of Configurations in D14UIKit Project
      :header-rows: 1
      :width: 100%

      * - Configuration Name
        - Pre-definition
        - Optimization Level
        - Runtime Library
      * - Debug
        - _DEBUG
        - /Od
        - /MDd
      * - Rebug
        - NDEBUG
        - /O2
        - /MDd
      * - Release
        - NDEBUG
        - /O2
        - /MD

.. seealso::

  For more details about different runtime libraries, please refer to this `document page`_ of MSVC.

.. _document page: https://learn.microsoft.com/en-us/cpp/build/reference/md-mt-ld-use-run-time-library

Build Python Wrapper
--------------------

1. Select **D14UIKit** as the startup project.
2. Select one configuration from **(DPyBind/RPyBind) | (Win32/x64/x86)**.
3. Build the project, and the library files will be generated in **Out**.

.. note::

   You can use ``stubgen`` to generate a hint file for Python (D14UIKit.pyi):

   .. sourcecode:: bat

      > pip install mypy
      > stubgen -m D14UIKit -o .

Test C++ Wrapper
----------------

1. Select **TestCpp** as the startup project.
2. Select one configuration from **(Debug/Release) | (Win32/x64/x86)**.
3. Write a test program, for example:

   .. code-block:: c++

      #include "Application.h"
      #include "MainWindow.h"

      using namespace d14uikit;

      int main()
      {
          Application app;
          MainWindow mwnd;
          return app.run();
      }

4. Build and run the project.

Test Python Wrapper
-------------------
1. Select **TestPyBind** as the startup project.
2. Select one configuration from **(Debug/Release) | (Any CPU)**.
3. Write a test script, for example:

   .. code-block:: python

      from D14UIKit import Application, MainWindow

      app = Application()
      mwnd = MainWindow()
      app.run()

4. Run the project.

.. tip::

   To enable debugging C++ code while running the Python wrapper:

   1. Check `Download debugging symbols`_ option when installing Python interpreter.
   2. Check *Properties* → *Debug* → *Enable native code debugging* of the project.

.. _Download debugging symbols: https://learn.microsoft.com/en-us/visualstudio/python/debugging-symbols-for-mixed-mode-c-cpp-python

Pack Libraries
--------------

Run ``pack.ps1 v1.0`` in Windows PowerShell to generate/update **Dist**, where the version label ``v1.0`` will be used to name the zips (**d14uikit_cpp_v1.0.zip** and **d14uikit_python_v1.0.zip** in this case).

* **Dist**

  * **cpp** (C++ Wrapper)

    * **demo**
    * **include**
    * **lib**

      * **debug** (DLL with ``/MDd`` Runtime Library)
      * **release** (DLL with ``/MD`` Runtime Library)
      * **D14UIKit.lib**

  * **python** (Python Wrapper)

    * **demo**
    * **D14UIKit.pyd** (Python DLL)
    * **D14UIKit.pyi** (Python Stub File)

  * **d14uikit_cpp_v1.0.zip** (zip of **cpp**)
  * **d14uikit_python_v1.0.zip** (zip of **python**)

.. tip::

   You can also run the PowerShell script in Command Prompt:

   .. sourcecode:: bat

      > powershell -f pack.ps1 v1.0
