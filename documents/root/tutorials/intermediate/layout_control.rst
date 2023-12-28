.. _d14uikit-tutorials-intermediate-layout_control:

Layout Control
==============

.. image:: https://media.githubusercontent.com/media/DreamersGather/D14Docs.Res/main/d14uikit/tutorials/layout_control.png

.. note::

  The source code of the demo can be found in **d14uikit/demo**.

Adaptive Layout
---------------

There are two ways to add new UI objects to a D14UIKit application: make it a child of a ``Panel``, or make it an element of a ``Layout``. The former way is relatively straightforward, and here we mainly introduce the usage of ``Layout``.

There are two built-in modes for layout control: Constraint and Grid. As the name suggests, Constraint achieves layout control by limiting the distance between elements and their master layout in each direction, while Grid achieves layout control by "stuffing" elements into pre-divided grids. The following figure is a visual comparison of these two methods:

.. image:: https://media.githubusercontent.com/media/DreamersGather/D14Docs.Res/main/d14uikit/tutorials/constraint_vs_grid.png

Simple Practice
---------------

Just as we can use a ``Panel`` as the content of ``MainWindow``, we can also use a ``Layout`` to fill the client area of the window. The default grid size of ``GridLayout`` is 1x1, and we set the number of horizontal grids as 2 to place the demonstration elements of Constraint and Grid respectively:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      MainWindow mwnd(DEMO_NAME);

      GridLayout centerLayout;
      mwnd.setContent(&centerLayout);

      centerLayout.setHorzCellCount(2);

  .. tab:: Python

    .. sourcecode:: python

      mwnd = MainWindow(DEMO_NAME)

      centerLayout = GridLayout()
      mwnd.content = centerLayout

      centerLayout.horzCellCount = 2

First, we create a container to demonstrate the usage of ``GridLayout``:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      GridLayout::GeoInfo geoInfo = {};

      ConstraintLayout layout1;
      geoInfo = {};
      geoInfo.x = { 0, 1 };
      geoInfo.y = { 0, 1 };
      centerLayout.addElement(&layout1, geoInfo);

      GridLayout layout2;
      geoInfo = {};
      geoInfo.x = { 1, 1 };
      geoInfo.y = { 0, 1 };
      centerLayout.addElement(&layout2, geoInfo);

  .. tab:: Python

    .. sourcecode:: python

      layout1 = ConstraintLayout()
      geoInfo = GridLayout.GeoInfo()
      geoInfo.x = Range(0, 1)
      geoInfo.y = Range(0, 1)
      centerLayout.addElement(layout1, geoInfo)

      layout2 = GridLayout()
      geoInfo = GridLayout.GeoInfo()
      geoInfo.x = Range(1, 1)
      geoInfo.y = Range(0, 1)
      centerLayout.addElement(layout2, geoInfo)

In order to add elements to ``GridLayout``, it is necessary to fill in the corresponding ``GeoInfo`` structures, which contain the geometry information of the UI objects to be added.

For ``GridLayout::GeoInfo``, the ``x`` and ``y`` fields are both ``Range`` structures, which can be used to specify the ``offset`` and ``count`` (unit: grid) of the UI objects in corresponding directions:

.. sourcecode::

  GridLayout::GeoInfo
  {
      bool fixedSize;
      Range x, y;
      Rect spacing;
  };

Next, we create an element to demonstrate the usage of ``ConstraintLayout``:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      Label lbl_c1(L"C1");
      ConstraintLayout::GeoInfo geoInfo1 = {};
      geoInfo1.keepWidth = false;
      geoInfo1.Left.ToLeft = 20;
      geoInfo1.Right.ToRight = 20;
      geoInfo1.keepHeight = false;
      geoInfo1.Top.ToTop = 20;
      geoInfo1.Bottom.ToTop = 120;
      layout1.addElement(&lbl_c1, geoInfo1);

      lbl_c1.setBkgnColor({ 0, 255, 0 });
      lbl_c1.setBkgnOpacity(0.5f);
      lbl_c1.setHorzAlign(Label::HCenter);

  .. tab:: Python

    .. sourcecode:: python

      lbl_c1 = Label('C1')
      geoInfo1 = ConstraintLayout.GeoInfo()
      geoInfo1.keepWidth = False
      geoInfo1.Left.ToLeft = 20
      geoInfo1.Right.ToRight = 20
      geoInfo1.keepHeight = False
      geoInfo1.Top.ToTop = 20
      geoInfo1.Bottom.ToTop = 120
      layout1.addElement(lbl_c1, geoInfo1)

      lbl_c1.bkgnColor = Color(0, 255, 0)
      lbl_c1.bkgnOpacity = 0.5
      lbl_c1.horzAlign = Label.HCenter

For ``ConstraintLayout::GeoInfo``, except for the ``Xxx.ToYyy`` fields, there are two options of ``keepWidth`` and ``keepHeight``: if they are true, the element to be added will always keep its original size, and ``Layout`` only changes its relative position:

.. sourcecode::

  ConstraintLayout::GeoInfo
  {
      bool keepWidth;

      HorzDistance
      {
          optional int ToLeft;
          optional int ToRight;
      }
      Left, Right;

      bool keepHeight;

      VertDistance
      {
          optional int ToTop;
          optional int ToBottom;
      }
      Top, Bottom;
  };

It is worth noting that ``Xxx.ToYyy`` fields are all optional, and for fields that are not specified, ``Layout`` simply does not constrain the corresponding distance. Besides, contradictory constraints are allowed. For example, when specifying both ``Top.ToTop`` and ``Top.ToBottom`` as the same value, ``Layout`` will only use one of them (depending on specific implementation). It is recommended to intentionally avoid contradictory constraints rather than let D14UIKit decide.

Finally, the complete demo code (so much repetitive creation and layout work) is as follows. Note that ``app.resizable`` is set as true to help observe the adaptive layout as window size changes:

.. tabs::

  .. tab:: C++

    .. code-block:: c++
      :emphasize-lines: 19, 20

      #include "Application.h"
      #include "ConstraintLayout.h"
      #include "GridLayout.h"
      #include "Label.h"
      #include "MainWindow.h"

      using namespace d14uikit;

      #define DEMO_NAME L"LayoutControl"

      int main(int argc, char* argv[])
      {
          float dpi = 96.0f;
          if (argc >= 2 && strcmp(argv[1], "HighDPI") == 0)
          {
              dpi = 192.0f;
          }
          Application app(DEMO_NAME, dpi);
          app.setMinSize(app.size());
          app.setResizable(true);

          //------------------------------------------- Initialize UI objects.

          MainWindow mwnd(DEMO_NAME);
          GridLayout centerLayout;
          mwnd.setContent(&centerLayout);
          centerLayout.setHorzCellCount(2);

          GridLayout::GeoInfo geoInfo = {};

          ConstraintLayout layout1;
          geoInfo = {};
          geoInfo.x = { 0, 1 };
          geoInfo.y = { 0, 1 };
          centerLayout.addElement(&layout1, geoInfo);

          ConstraintLayout::GeoInfo geoInfo1 = {};

          Label lbl_c1(L"C1");
          geoInfo1 = {};
          geoInfo1.keepWidth = false;
          geoInfo1.Left.ToLeft = 20;
          geoInfo1.Right.ToRight = 20;
          geoInfo1.keepHeight = false;
          geoInfo1.Top.ToTop = 20;
          geoInfo1.Bottom.ToTop = 120;
          layout1.addElement(&lbl_c1, geoInfo1);
          lbl_c1.setBkgnColor({ 0, 255, 0 });
          lbl_c1.setBkgnOpacity(0.5f);
          lbl_c1.setHorzAlign(Label::HCenter);

          Label lbl_c2(L"C2");
          lbl_c2.setHeight(400);
          geoInfo1 = {};
          geoInfo1.keepWidth = false;
          geoInfo1.Left.ToLeft = 20;
          geoInfo1.Right.ToRight = 20;
          geoInfo1.keepHeight = true;
          geoInfo1.Bottom.ToBottom = 20;
          layout1.addElement(&lbl_c2, geoInfo1);
          lbl_c2.setBkgnColor({ 0, 255, 255 });
          lbl_c2.setBkgnOpacity(0.5f);
          lbl_c2.setHorzAlign(Label::HCenter);

          GridLayout layout2;
          geoInfo = {};
          geoInfo.x = { 1, 1 };
          geoInfo.y = { 0, 1 };
          centerLayout.addElement(&layout2, geoInfo);
          layout2.setHorzCellCount(4);
          layout2.setVertCellCount(4);
          layout2.setHorzMargin(20);
          layout2.setVertMargin(20);

          GridLayout::GeoInfo geoInfo2 = {};

          Label lbl_g1(L"G1");
          geoInfo2 = {};
          geoInfo2.x = { 0, 1 };
          geoInfo2.y = { 0, 1 };
          layout2.addElement(&lbl_g1, geoInfo2);
          lbl_g1.setBkgnColor({ 255, 0, 0 });
          lbl_g1.setBkgnOpacity(0.5f);
          lbl_g1.setHorzAlign(Label::HCenter);

          Label lbl_g2(L"G2");
          geoInfo2 = {};
          geoInfo2.x = { 1, 3 };
          geoInfo2.y = { 0, 2 };
          layout2.addElement(&lbl_g2, geoInfo2);
          lbl_g2.setBkgnColor({ 0, 255, 0 });
          lbl_g2.setBkgnOpacity(0.5f);
          lbl_g2.setHorzAlign(Label::HCenter);

          Label lbl_g3(L"G3");
          geoInfo2 = {};
          geoInfo2.x = { 0, 1 };
          geoInfo2.y = { 1, 3 };
          geoInfo2.spacing.top = 10;
          geoInfo2.spacing.right = 10;
          layout2.addElement(&lbl_g3, geoInfo2);
          lbl_g3.setBkgnColor({ 255, 0, 255 });
          lbl_g3.setBkgnOpacity(0.5f);
          lbl_g3.setHorzAlign(Label::HCenter);

          Label lbl_g4(L"G4");
          lbl_g4.setSize({ 200, 200 });
          geoInfo2 = {};
          geoInfo2.fixedSize = true;
          geoInfo2.x = { 1, 3 };
          geoInfo2.y = { 2, 2 };
          layout2.addElement(&lbl_g4, geoInfo2);
          lbl_g4.setBkgnColor({ 0, 255, 255 });
          lbl_g4.setBkgnOpacity(0.5f);
          lbl_g4.setHorzAlign(Label::HCenter);

          //------------------------------------------- Set UI event callbacks.

          return app.run();
      }

  .. tab:: Python

    .. code-block:: python
      :emphasize-lines: 13, 14

      from sys import argv

      from D14UIKit import *

      DEMO_NAME = 'DemoTemplate'

      if __name__ == '__main__':
          dpi = 96.0
          if len(argv) >= 2 and argv[1] == 'HighDPI':
              dpi = 192.0

          app = Application(DEMO_NAME, dpi)
          app.minSize = app.size
          app.resizable = True

          #------------------------------------------- Initialize UI objects.

          mwnd = MainWindow(DEMO_NAME)
          centerLayout = GridLayout()
          mwnd.content = centerLayout
          centerLayout.horzCellCount = 2

          layout1 = ConstraintLayout()
          geoInfo = GridLayout.GeoInfo()
          geoInfo.x = Range(0, 1)
          geoInfo.y = Range(0, 1)
          centerLayout.addElement(layout1, geoInfo)

          lbl_c1 = Label('C1')
          geoInfo1 = ConstraintLayout.GeoInfo()
          geoInfo1.keepWidth = False
          geoInfo1.Left.ToLeft = 20
          geoInfo1.Right.ToRight = 20
          geoInfo1.keepHeight = False
          geoInfo1.Top.ToTop = 20
          geoInfo1.Bottom.ToTop = 120
          layout1.addElement(lbl_c1, geoInfo1)
          lbl_c1.bkgnColor = Color(0, 255, 0)
          lbl_c1.bkgnOpacity = 0.5
          lbl_c1.horzAlign = Label.HCenter

          lbl_c2 = Label('C2')
          lbl_c2.height = 400
          geoInfo1 = ConstraintLayout.GeoInfo()
          geoInfo1.keepWidth = False
          geoInfo1.Left.ToLeft = 20
          geoInfo1.Right.ToRight = 20
          geoInfo1.keepHeight = True
          geoInfo1.Bottom.ToBottom = 20
          layout1.addElement(lbl_c2, geoInfo1)
          lbl_c2.bkgnColor = Color(0, 255, 255)
          lbl_c2.bkgnOpacity = 0.5
          lbl_c2.horzAlign = Label.HCenter

          layout2 = GridLayout()
          geoInfo = GridLayout.GeoInfo()
          geoInfo.x = Range(1, 1)
          geoInfo.y = Range(0, 1)
          centerLayout.addElement(layout2, geoInfo)
          layout2.horzCellCount = 4
          layout2.vertCellCount = 4
          layout2.horzMargin = 20
          layout2.vertMargin = 20

          lbl_g1 = Label('G1')
          geoInfo2 = GridLayout.GeoInfo()
          geoInfo2.x = Range(0, 1)
          geoInfo2.y = Range(0, 1)
          layout2.addElement(lbl_g1, geoInfo2)
          lbl_g1.bkgnColor = Color(255, 0, 0)
          lbl_g1.bkgnOpacity = 0.5
          lbl_g1.horzAlign = Label.HCenter

          lbl_g2 = Label('G2')
          geoInfo2 = GridLayout.GeoInfo()
          geoInfo2.x = Range(1, 3)
          geoInfo2.y = Range(0, 2)
          layout2.addElement(lbl_g2, geoInfo2)
          lbl_g2.bkgnColor = Color(0, 255, 0)
          lbl_g2.bkgnOpacity = 0.5
          lbl_g2.horzAlign = Label.HCenter

          lbl_g3 = Label('G3')
          geoInfo2 = GridLayout.GeoInfo()
          geoInfo2.x = Range(0, 1)
          geoInfo2.y = Range(1, 3)
          geoInfo2.spacing.top = 10
          geoInfo2.spacing.right = 10
          layout2.addElement(lbl_g3, geoInfo2)
          lbl_g3.bkgnColor = Color(255, 0, 255)
          lbl_g3.bkgnOpacity = 0.5
          lbl_g3.horzAlign = Label.HCenter

          lbl_g4 = Label('G4')
          lbl_g4.size = Size(200, 200)
          geoInfo2 = GridLayout.GeoInfo()
          geoInfo2.fixedSize = True
          geoInfo2.x = Range(1, 3)
          geoInfo2.y = Range(2, 2)
          layout2.addElement(lbl_g4, geoInfo2)
          lbl_g4.bkgnColor = Color(0, 255, 255)
          lbl_g4.bkgnOpacity = 0.5
          lbl_g4.horzAlign = Label.HCenter

          #------------------------------------------- Set UI event callbacks.

          exit(app.run())
