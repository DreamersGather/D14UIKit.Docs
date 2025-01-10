.. _d14uikit-tutorials-intermediate-object_oriented:

Object Oriented
===============

.. image:: https://media.githubusercontent.com/media/DreamersGather/D14Docs.Res/main/d14uikit/tutorials/object_oriented.png

.. note::

  The source code of the demo can be found in **d14uikit/demo**.

UI Object
---------

``Panel`` is the most derived UI object in D14UIKit. It represents a rectangular area on the screen, where we can draw an image or place other UI objects (as children). Let's start with ``MainWindow``:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      MainWindow mwnd(DEMO_NAME);

  .. tab:: Python

    .. sourcecode:: python

      mwnd = MainWindow(DEMO_NAME)

As mentioned above, ``MainWindow`` is derived from ``Panel``, and its rectangular area is divided into two parts: the non-client and the client area. The non-client area contains a caption and a decorative bar, and the center of the window is the client area:

.. note::

  There is a sizing frame around the window, which also belongs to the non-client area.

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      Panel clntArea;
      mwnd.setContent(&clntArea);

  .. tab:: Python

    .. sourcecode:: python

      clntArea = Panel()
      mwnd.content = clntArea

Non-UI Object
-------------

In addition to UI objects derived from ``Panel``, there are also non-UI objects in D14UIKit, which are not directly displayed on the screen, such as ``Image`` and ``Font``.

To display an image on the screen, we first need to create an ``Image`` object with target bitmap, and then create a ``Panel`` object for displaying the image:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      Image img(L"test.png");

      Panel imgArea;
      imgArea.setParent(&clntArea);
      imgArea.setSize(img.size());
      imgArea.setPosition({ 20, 0 });
      imgArea.setImage(&img);

  .. tab:: Python

    .. sourcecode:: python

      img = Image('test.png')

      imgArea = Panel()
      imgArea.parent = clntArea
      imgArea.size = img.size
      imgArea.position = Point(20, 0)
      imgArea.image = img

Similarly, in order to draw text, we need to create a ``Label`` object and associate it with a ``Font`` object (optional, there is a global default ``Font`` for ``Label``):

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      Label textArea;

      textArea.setParent(&clntArea);
      textArea.setSize({ 200, 100 });
      textArea.setPosition({ 400, 100 });
      textArea.setOutlineWidth(5);
      textArea.setOutlineColor({ 255, 0, 0 });
      textArea.setOutlineOpacity(0.5);
      textArea.setText(L"This is a label");
      textArea.setHorzAlign(Label::HCenter);

      auto font1 = Font::load(
          L"MyFont",
          L"Times New Roman",
          20,
          L"en-us",
          Font::ExtraBold,
          Font::Italic,
          Font::Expanded);

      auto font2 = Font(L"MyFont");

      textArea.setFont(&font1);
      //textArea.setFont(&font2);

  .. tab:: Python

    .. sourcecode:: python

      textArea = Label()

      textArea.parent = clntArea
      textArea.size = Size(200, 100)
      textArea.position = Point(400, 100)
      textArea.outlineWidth = 5
      textArea.outlineColor = Color(255, 0, 0)
      textArea.outlineOpacity = 0.5
      textArea.text = 'This is a label'
      textArea.horzAlign = Label.HCenter

      font1 = Font.load( \
          "MyFont", \
          "Times New Roman", \
          20, "en-us", \
          Font.ExtraBold, \
          Font.Italic, \
          Font.Expanded)

      font2 = Font('MyFont')

      textArea.font = font1
      #textArea.font = font2

It is worth noting that ``Font::load`` only needs to be called once for each customized font type. In fact, the actual font entity has already been created by calling ``Font::load``, and creating a ``Font`` object just makes a reference to the global entity, which helps improve performance.

Alternatively, we can use the default font directly to avoid creating customized font objects:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      Label busyArea;
      busyArea.setParent(&clntArea);
      busyArea.setSize({ 760, 240 });
      busyArea.setPosition({ 20, 300 });
      busyArea.setBkgnColor({ 128, 128, 128 });
      busyArea.setBkgnOpacity(0.5f);
      busyArea.setText(L"Try moving cursor in this area");
      busyArea.setHorzAlign(Label::HCenter);

      busyArea.setFontSize(20);

  .. tab:: Python

    .. sourcecode:: python

      busyArea = Label()
      busyArea.parent = clntArea
      busyArea.size = Size(760, 240)
      busyArea.position = Point(20, 300)
      busyArea.bkgnColor = Color(128, 128, 128)
      busyArea.bkgnOpacity = 0.5
      busyArea.text = 'Try moving cursor in this area'
      busyArea.horzAlign = Label.HCenter

      busyArea.fontSize = 20

Note that for performance considerations, the text in D14UIKit is rendered using predetermined text layout data. Therefore, when the ``Label``'s text changes, some of the properties of the original text layout (such as font size) will be reset. This is why the text setting should be placed last.

.. note::

   If you want to retain the original properties after the text changes, you need to replace the font (which will change the default text layout data) instead of directly setting the font properties.

In addition to images and fonts, each callback function/event of UI objects is also a non-UI object. It is basically implemented with the concept of functor in modern C++/Python languages:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      auto setBusyCursor = [](Panel* p, MouseMoveEvent* e)
      {
          auto cursor = Application::app()->cursor();
          cursor->setIcon(Cursor::Busy);
      };
      busyArea.callback().onMouseMove = setBusyCursor;

  .. tab:: Python

    .. sourcecode:: python

      def setBusyCursor(p, e):
          cursor = Application.app.cursor
          cursor.setIcon(Cursor.Busy)

      busyArea.f_onMouseMove = setBusyCursor
