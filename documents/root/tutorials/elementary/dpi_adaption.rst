.. _d14uikit-tutorials-elementary-dpi_adaption:

DPI Adaption
============

.. image:: https://media.githubusercontent.com/media/DreamersGather/D14Docs.Res/main/d14uikit/tutorials/hello_window_dpi.png

.. note::

  The source code of the demo can be found in **d14uikit/demo**.

Display Scale
-------------

Windows 10/11 users may be familiar with the following option:

.. image:: https://media.githubusercontent.com/media/DreamersGather/D14Docs.Res/main/d14uikit/tutorials/display_scaling.png

For Windows 7 and older versions, the option can be found in control panel (high-DPI scaling is supported starting from Windows XP). In general, 100% scaling is displayed in 96 dpi (120 dpi for 125% scaling and so on). In terms of GUI appearance, as the scaling ratio increases, the size of a UI control will increase, and bitmap images may become blurry (while vector images keep sharp).

DPI: Dots Per Inch
------------------

DPI stands for "Dots Per Inch". As we all known, "Inch" is a physical unit of length. In similar, "Dot" is a virtual unit of length on bitmap plane, and it can refer to a pixel on bitmap screen or an ink dot on printing paper. Therefore, DPI is a bridge connecting the physical world and the virtual screen. After determining the DPI, the number of pixels occupied by a display-object can be calculated from its physical size, and vice versa. For example, in 96 dpi, a 1 inch line would occupy 96 pixels on screen or 96 ink dots on paper.

In fact, DPI is often used to describe the sensitivity of electronic devices. For example, considering a 1000 dpi mouse, its cursor moves 1000 pixels on screen every time the related device moves 1 inch on physical plane. In addition, on Windows platform, there is a concept called Device Independent Pixel (DIP), which is easily confused with Dots Per Inch (DPI). DIP is a pixel unit in logical space, and it is often mapped to multiple pixels in physical space. Applying DIP coordinates provides great convenience for GUI development, as Windows automatically converts logical pixels into physical pixels according to different DPI settings, which ensures the object can be displayed correctly on screens of different sizes and resolutions.

For example, a 100 dip line would occupy 100 physical pixels on a 96 dpi screen, while on a 120 dpi screen it would occupy 100*(120/96)=125 physical pixels. More details can be found in this `article`_ on MSDN, where the content of Direct2D and hig-DPI is also helpful for development.

.. _article: https://learn.microsoft.com/en-us/windows/win32/direct2d/direct2d-and-high-dpi#what-is-a-dip

DPI in D14UIKit
---------------

Setting the DPI of an application in D14UIKit is very straightforward:

.. tabs::

  .. tab:: C++

    .. code-block:: c++
      :emphasize-lines: 15

      #include "Application.h"
      #include "MainWindow.h"

      using namespace d14uikit;

      #define DEMO_NAME L"HelloWindowDPI"

      int main(int argc, char* argv[])
      {
          float dpi = 96.0f;
          if (argc >= 2 && strcmp(argv[1], "HighDPI") == 0)
          {
              dpi = 192.0f;
          }
          Application app(DEMO_NAME, dpi);
          MainWindow mwnd(DEMO_NAME);
          return app.run();
      }

  .. tab:: Python

    .. code-block:: python
      :emphasize-lines: 12

      from sys import argv

      from D14UIKit import *

      DEMO_NAME = 'HelloWindowDPI'

      if __name__ == '__main__':
          dpi = 96.0
          if len(argv) >= 2 and argv[1] == 'HighDPI':
              dpi = 192.0

          app = Application(DEMO_NAME, dpi)
          mwnd = MainWindow(DEMO_NAME)
          exit(app.run())
