.. _d14uikit-tutorials-intermediate-basic_callback:

Basic Callback
==============

.. image:: https://media.githubusercontent.com/media/DreamersGather/D14Docs.Res/main/d14uikit/tutorials/basic_callback.png

.. note::

  The source code of the demo can be found in **d14uikit/demo**.

In this section, we will create an application for customizing the title of ``MainWindow`` to demonstrate the basic usage of callback functions in D14UIKit.

Initialize UI Objects
---------------------

Firstly, initialize ``Application`` and ``MainWindow`` (which is basically templated), and we set the height of the window to 380 dip to make it look better:

.. tabs::

  .. tab:: C++

    .. code-block:: c++
      :emphasize-lines: 19

      #include "Application.h"
      #include "Callback.h"
      #include "FlatButton.h"
      #include "MainWindow.h"
      #include "TextBox.h"

      using namespace d14uikit;

      #define DEMO_NAME L"BasicCallback"

      int main(int argc, char* argv[])
      {
          float dpi = 96.0f;
          if (argc >= 2 && strcmp(argv[1], "HighDPI") == 0)
          {
              dpi = 192.0f;
          }
          Application app(DEMO_NAME, dpi);
          app.setHeight(380);

          //------------------------------------------- Initialize UI objects.

          MainWindow mwnd(DEMO_NAME);
          Panel clntArea;
          mwnd.setContent(&clntArea);

          //------------------------------------------- Set UI event callbacks.

          return app.run();
      }

  .. tab:: Python

    .. code-block:: python
      :emphasize-lines: 13

      from sys import argv

      from D14UIKit import *

      DEMO_NAME = 'BasicCallback'

      if __name__ == '__main__':
          dpi = 96.0
          if len(argv) >= 2 and argv[1] == 'HighDPI':
              dpi = 192.0

          app = Application(DEMO_NAME, dpi)
          app.height = 380

          #------------------------------------------- Initialize UI objects.

          mwnd = MainWindow(DEMO_NAME)
          clntArea = Panel()
          mwnd.content = clntArea

          #------------------------------------------- Set UI event callbacks.

          exit(app.run())

Next, create a ``TextBox`` for customizing the window title; finally, create a ``FlatButton`` for restoring the window title to default:

.. tabs::

  .. tab:: C++

    .. code-block:: c++
      :emphasize-lines: 8

      TextBox titleInput;
      titleInput.setParent(&clntArea);
      titleInput.setSize({ 400, 50 });
      titleInput.setPosition({ 200, 100 });
      titleInput.setRoundRadius(5);
      titleInput.setTextRect({ 10, 5, 390, 45 });

      auto placer = titleInput.placeholder();
      placer->setText(L"Input window title...");

      FlatButton restoreButton;
      restoreButton.setParent(&clntArea);
      restoreButton.setSize({ 200, 50 });
      restoreButton.setPosition({ 300, 200 });
      restoreButton.setRoundRadius(5);
      restoreButton.setText(L"Restore default");

  .. tab:: Python

    .. code-block:: python
      :emphasize-lines: 8

      titleInput = TextBox()
      titleInput.parent = clntArea
      titleInput.size = Size(400, 50)
      titleInput.position = Point(200, 100)
      titleInput.roundRadius = 5
      titleInput.textRect = Rect(10, 5, 390, 45)

      placer = titleInput.placeholder
      placer.text = 'Input window title...'

      restoreButton = FlatButton()
      restoreButton.parent = clntArea
      restoreButton.size = Size(200, 50)
      restoreButton.position = Point(300, 200)
      restoreButton.roundRadius = 5
      restoreButton.text = 'Restore default'

In order to set the placeholder of ``TextBox``, we need to get the corresponding ``Label`` object inside the ``TextBox`` through the ``placeholder`` method/property, instead of directly calling a method provided by ``TextBox``. This OOP style usage is widely present in D14UIKit, as many built-in advanced UI controls often reuse other basic ones.

Set UI Event Callbacks
----------------------

In order to implement the function of changing the window title with input text, we need to set the ``onTextChange`` callback function of ``TextBox``. It will be called when the content changes:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      titleInput.callback().onTextChange =
      [&](RawTextInput* obj, const std::wstring& text)
      {
          mwnd.setTitle(text);
      };

  .. tab:: Python

    .. sourcecode:: python

      def changeMwndTitle(obj, text):
          mwnd.title = text

      titleInput.f_onTextChange = changeMwndTitle

Similarly, you can also set the ``onMouseButtonRelease`` callback function of ``FlatButton``, which will be called after the button is clicked (to continuously complete the press and release actions):

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      restoreButton.callback().onMouseButtonRelease =
      [&](ClickablePanel* clkp, MouseButtonClickEvent* e)
      {
          titleInput.setText(L"");
          mwnd.setTitle(DEMO_NAME);
      };

  .. tab:: Python

    .. sourcecode:: python

      def restoreMwndTitle(clkp, e):
          titleInput.text = ''
          mwnd.title = DEMO_NAME

      restoreButton.f_onMouseButtonRelease = restoreMwndTitle

Note that we must first clear the text box and then set the window title (but not vice versa), otherwise the ``onTextChange`` callback function will clear it again after setting the window title.

To Be More Elegant
------------------

Compared to concise callback function setting in Python, C++ developers may have noticed that the strict typing of C++ makes it a bit complicated. In order to write the corresponding callback function, we have to refer to the function prototype to copy relevant parameters and return value information. That is not elegant at all, and we provide a better solution in D14UIKit: There is a help-header **Callback.h** for C++ developers, which includes the signature-macros of built-in callback functions, and helps simplify the process of setting callback functions in C++:

.. sourcecode:: c++
  :emphasize-lines: 1

  #include "Callback.h"

  titleInput.D14_onTextChange(obj, text, &)
  {
      mwnd.setTitle(text);
  };
  restoreButton.D14_onMouseButtonRelease(clkp, e, &)
  {
      titleInput.setText(L"");
      mwnd.setTitle(DEMO_NAME);
  };

The last parameter of the signature-macros is a ``__VA_ARGS__`` (VAriable ARGumentS), which will be used to place the capture list of the expanded lambda.

In fact, in modern C++ standards (such as C++20), we can already use the ``auto`` keyword to enable the compiler to automatically infer the parameter list of lambda. For example, the callback function setting mentioned above can be further simplified as:

.. sourcecode:: c++

  titleInput.callback().onTextChange =
  [&](auto obj, auto text)
  {
      mwnd.setTitle(text);
  };
  restoreButton.callback().onMouseButtonRelease =
  [&](auto clkp, auto e)
  {
      titleInput.setText(L"");
      mwnd.setTitle(DEMO_NAME);
  };

However, some IDEs are unable to automatically infer the types of these parameters, which results in code completion not working. You can try the usage with your current IDE to test whether it is intelligent enough (Visual Studio does not support this =_=).
