.. _d14uikit-tutorials-intermediate-modern_theme:

Modern Theme
============

.. image:: https://media.githubusercontent.com/media/DreamersGather/D14Docs.Res/main/d14uikit/tutorials/modern_theme.png

.. note::

  The source code of the demo can be found in **d14uikit/demo**.

Dark Mode
---------

Many applications support switching between different UI themes, and the most important one is the switching between dark and light themes, which is also a basic feature of modern UI design. Many studies have shown that dark themes can help improve attention, increase immersion, and reduce visual fatigue. In addition, for certain kinds of electronic screens (such as OLED screens), dark themes may help save power. Nowadays, more and more electronic device users are accustomed to use different themes during the day and night, and even always use dark themes.

It is very straightforward to enable dark theme mode in D14UIKit:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      app->setThemeMode(L"Dark");

  .. tab:: Python

    .. sourcecode:: python

      app.themeMode = 'Dark'

where ``app`` is a reference to the global ``Application`` instance.

Simple Practice
---------------

In previous tutorials, we did not demonstrate how to switch the theme of an application, and D14UIKit defaults to making the application follow the system theme. Therefore, the appearance of the demo will be consistent with your system. In this section, we will create an application for switching themes.

First is ``app`` settings:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      app.setHeight(300);
      app.setMinSize(app.size());
      app.setResizable(true);

  .. tab:: Python

    .. sourcecode:: python

      app.height = 300
      app.minSize = app.size
      app.resizable = True

Next, initialize UI objects:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      MainWindow mwnd(DEMO_NAME);
      ConstraintLayout centerLayout;
      mwnd.setContent(&centerLayout);

      ConstraintLayout::GeoInfo geoInfo = {};

      Label themeLbl(L"Theme mode");
      themeLbl.setHeight(40);
      themeLbl.setHorzAlign(Label::HCenter);
      geoInfo = {};
      geoInfo.keepWidth = false;
      geoInfo.Left.ToLeft = 50;
      geoInfo.Right.ToLeft = 350;
      geoInfo.keepHeight = true;
      geoInfo.Top.ToTop = 100;
      centerLayout.addElement(&themeLbl, geoInfo);

      ComboBox themeSelector;
      themeSelector.setHeight(40);
      geoInfo = {};
      geoInfo.keepWidth = false;
      geoInfo.Left.ToRight = 350;
      geoInfo.Right.ToRight = 50;
      geoInfo.keepHeight = true;
      geoInfo.Top.ToTop = 100;
      centerLayout.addElement(&themeSelector, geoInfo);
      themeSelector.setRoundRadius(5);

      auto menu = themeSelector.dropDownMenu();

      ComboBoxItem items[3];
      items[0].setText(L"Light");
      items[1].setText(L"Dark");
      items[2].setText(L"Use system setting");

      std::list<MenuItem*> pItems;
      for (auto& item : items)
      {
          pItems.push_back(&item);
      }
      menu->appendItem(pItems);

      menu->setWidth(themeSelector.width());
      menu->setHeight(_countof(items) * 40);
      menu->setRoundExtension(5);

      themeSelector.setCurrSelected(2);

  .. tab:: Python

    .. sourcecode:: python

      mwnd = MainWindow(DEMO_NAME)
      centerLayout = ConstraintLayout()
      mwnd.content = centerLayout

      themeLbl = Label('Theme mode')
      themeLbl.height = 40
      themeLbl.horzAlign = Label.HCenter
      geoInfo = ConstraintLayout.GeoInfo()
      geoInfo.keepWidth = False
      geoInfo.Left.ToLeft = 50
      geoInfo.Right.ToLeft = 350
      geoInfo.keepHeight = True
      geoInfo.Top.ToTop = 100
      centerLayout.addElement(themeLbl, geoInfo)

      themeSelector = ComboBox()
      themeSelector.height = 40
      geoInfo = ConstraintLayout.GeoInfo()
      geoInfo.keepWidth = False
      geoInfo.Left.ToRight = 350
      geoInfo.Right.ToRight = 50
      geoInfo.keepHeight = True
      geoInfo.Top.ToTop = 100
      centerLayout.addElement(themeSelector, geoInfo)
      themeSelector.roundRadius = 5

      menu = themeSelector.dropDownMenu

      items = [ComboBoxItem() for i in range(3)]
      items[0].text = 'Light'
      items[1].text = 'Dark'
      items[2].text = 'Use system setting'

      menu.appendItem(items)

      menu.width = themeSelector.width
      menu.height = len(items) * 40
      menu.roundExtension = 5

      themeSelector.setCurrSelected(2)

Finally, set UI event callbacks:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      themeSelector.D14_onSelectedChange(ComboBox, obj, text)
      {
          auto app = Application::app();
          if (text == L"Light" || text == L"Dark")
          {
              app->setThemeMode(text);
          }
          else if (text == L"Use system setting")
          {
              app->setUseSystemTheme(true);
          }
      };

  .. tab:: Python

    .. sourcecode:: python

      def changeThemeMode(obj, text):
          app = Application.app
          if text == 'Light' or text == 'Dark':
              app.themeMode = text
          elif text == 'Use system setting':
              app.useSystemTheme = True
      themeSelector.f_onSelectedChange = changeThemeMode
