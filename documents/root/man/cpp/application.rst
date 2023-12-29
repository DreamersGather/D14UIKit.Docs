.. _d14uikit-reference-cpp-application:

Application
===========

Overview
--------

.. list-table::
  :width: 100%
  :widths: 30, 70

  * - Header
    - Application.h
  * - Inherits
    - NonCopyable

``Application`` is the core class for creating a typical D14UIKit application.

Constructors
------------

.. list-table::
  :width: 100%

  * - :ref:`Application<d14uikit-reference-cpp-application-ctor-1>` (const std::wstring& name = L"D14UIKit", const std::optional<float>& dpi = std::nullopt)

Static Methods
--------------

.. list-table::
  :width: 100%
  :widths: 30, 70

  * - Application*
    - :ref:`app<d14uikit-reference-cpp-application-sttcm-app>` ()

Instance Methods
----------------

.. list-table::
  :width: 100%
  :widths: 30, 60, 10

  * - Cursor*
    - :ref:`cursor<d14uikit-reference-cpp-application-isntm-cursor>` ()
    - const
  * - int
    - :ref:`run<d14uikit-reference-cpp-application-isntm-run>` ()
    - const
  * - void
    - :ref:`exit<d14uikit-reference-cpp-application-isntm-exit>` ()
    - const
  * - bool
    - :ref:`visible<d14uikit-reference-cpp-application-isntm-visible>` ()
    - const
  * - void
    - :ref:`setVisible<d14uikit-reference-cpp-application-isntm-set_visible>` (bool value)
    -
  * - bool
    - :ref:`minimized<d14uikit-reference-cpp-application-isntm-minimized>` ()
    - const
  * - void
    - :ref:`setMinimized<d14uikit-reference-cpp-application-isntm-set_minimized>` (bool value)
    -
  * - bool
    - :ref:`maximized<d14uikit-reference-cpp-application-isntm-maximized>` ()
    - const
  * - void
    - :ref:`setMaximized<d14uikit-reference-cpp-application-isntm-set_maximized>` (bool value)
    -
  * - Size
    - :ref:`size<d14uikit-reference-cpp-application-isntm-size>` ()
    - const
  * - void
    - :ref:`setSize<d14uikit-reference-cpp-application-isntm-set_size>` (const Size& value)
    -
  * - int
    - :ref:`width<d14uikit-reference-cpp-application-isntm-width>` ()
    - const
  * - void
    - :ref:`setWidth<d14uikit-reference-cpp-application-isntm-set_width>` (int value)
    -
  * - int
    - :ref:`height<d14uikit-reference-cpp-application-isntm-height>` ()
    - const
  * - void
    - :ref:`setHeight<d14uikit-reference-cpp-application-isntm-set_height>` (int value)
    -
  * - Point
    - :ref:`position<d14uikit-reference-cpp-application-isntm-position>` ()
    - const
  * - void
    - :ref:`setPosition<d14uikit-reference-cpp-application-isntm-set_position>` (const Point& value)
    -
  * - int
    - :ref:`x<d14uikit-reference-cpp-application-isntm-x>` ()
    - const
  * - void
    - :ref:`setX<d14uikit-reference-cpp-application-isntm-set_x>` (int value)
    -
  * - int
    - :ref:`y<d14uikit-reference-cpp-application-isntm-y>` ()
    - const
  * - void
    - :ref:`setY<d14uikit-reference-cpp-application-isntm-set_y>` (int value)
    -
  * - Size
    - :ref:`minSize<d14uikit-reference-cpp-application-isntm-min_size>` ()
    - const
  * - void
    - :ref:`setMinSize<d14uikit-reference-cpp-application-isntm-set_min_size>` (const Size& value)
    -
  * - int
    - :ref:`minWidth<d14uikit-reference-cpp-application-isntm-min_width>` ()
    - const
  * - void
    - :ref:`setMinWidth<d14uikit-reference-cpp-application-isntm-set_min_width>` (int value)
    -
  * - int
    - :ref:`minHeight<d14uikit-reference-cpp-application-isntm-min_height>` ()
    - const
  * - void
    - :ref:`setMinHeight<d14uikit-reference-cpp-application-isntm-set_min_height>` (int value)
    -
  * - bool
    - :ref:`resizable<d14uikit-reference-cpp-application-isntm-resizable>` ()
    - const
  * - void
    - :ref:`setResizable<d14uikit-reference-cpp-application-isntm-set_resizable>` (bool value)
    -
  * - bool
    - :ref:`fullscreen<d14uikit-reference-cpp-application-isntm-fullscreen>` ()
    - const
  * - void
    - :ref:`setFullscreen<d14uikit-reference-cpp-application-isntm-set_fullscreen>` (bool value)
    -
  * - int
    - :ref:`fps<d14uikit-reference-cpp-application-isntm-fps>` ()
    - const
  * - bool
    - :ref:`lowEnergy<d14uikit-reference-cpp-application-isntm-low_energy>` ()
    - const
  * - void
    - :ref:`setLowEnergy<d14uikit-reference-cpp-application-isntm-set_low_energy>` (bool value)
    -
  * - const std::wstring&
    - :ref:`themeMode<d14uikit-reference-cpp-application-isntm-theme_mode>` ()
    - const
  * - void
    - :ref:`setThemeMode<d14uikit-reference-cpp-application-isntm-set_theme_mode>` (const std::wstring& name)
    -
  * - Color
    - :ref:`themeColor<d14uikit-reference-cpp-application-isntm-theme_color>` ()
    - const
  * - void
    - :ref:`setThemeColor<d14uikit-reference-cpp-application-isntm-set_theme_color>` (const Color& value)
    -
  * - bool
    - :ref:`useSystemTheme<d14uikit-reference-cpp-application-isntm-use_system_theme>` ()
    - const
  * - void
    - :ref:`setUseSystemTheme<d14uikit-reference-cpp-application-isntm-set_use_system_theme>` (bool value)
    -
  * - const std::wstring&
    - :ref:`langLocale<d14uikit-reference-cpp-application-isntm-lang_locale>` ()
    - const
  * - void
    - :ref:`setLangLocale<d14uikit-reference-cpp-application-isntm-set_lang_locale>` (const std::wstring& name)
    -
  * - bool
    - :ref:`clearType<d14uikit-reference-cpp-application-isntm-clear_type>` ()
    - const
  * - void
    - :ref:`setClearType<d14uikit-reference-cpp-application-isntm-set_clear_type>` (bool value)
    -
  * - bool
    - :ref:`textVertSmooth<d14uikit-reference-cpp-application-isntm-text_vert_smooth>` ()
    - const
  * - void
    - :ref:`setTextVertSmooth<d14uikit-reference-cpp-application-isntm-set_text_vert_smooth>` (bool value)
    -
  * - bool
    - :ref:`bmpQualityInterp<d14uikit-reference-cpp-application-isntm-bmp_quality_interp>` ()
    - const
  * - void
    - :ref:`setBmpQualityInterp<d14uikit-reference-cpp-application-isntm-set_bmp_quality_interp>` (bool value)
    -
  * - std::unique_ptr<Image>
    - :ref:`capture<d14uikit-reference-cpp-application-isntm-capture>` ()
    - const

Remarks
-------

For a typical D14UIKit application, creating an ``Application`` instance is the first necessary step. When drafting a brand new D14UIKit based GUI project, the following template can be used:

.. code-block:: c++
  :emphasize-lines: 9

  #include "Application.h"

  using namespace d14uikit;

  int main(int argc, char* argv[])
  {
      Application app;

      // Add code here.

      return app.run();
  }

Details
-------

.. _d14uikit-reference-cpp-application-ctor-1:

  **explicit Application(const std::wstring& name = L"D14UIKit", const std::optional<float>& dpi = std::nullopt)**

* **Params**

  * ``name``

    Type: **const std::wstring&**

    Default Value: **L"D14UIKit"**

    The name of the application, which is also used as the name of the underlying Win32 window. Therefore, it is also the text displayed for the program in the taskbar thumbnail, task manager and other system interfaces.

  * ``dpi``

    Type: **const std::optional<float>&**

    Default Value: **std::nullopt**

    The DPI of the application. This can be any positive value within ``float`` range, or empty to follow the system DPI. The typical DPI settings are as follows:

    .. list-table::
      :header-rows: 1
      :width: 100%

      * - Display Scale
        - DPI value
      * - 100%
        - 96 dpi
      * - 150%
        - 144 dpi
      * - 200%
        - 192 dpi

    A DPI value that is not a multiple of 96 dpi may cause blurry display. The reason why we use "may" here is that it also depends on the actual size of the UI object. For example: at 125% scaling (i.e. 120 dpi), rendering a 100 dip ⨉ 100 dip image is based on a 125 px ⨉ 125 px offscreen texture; however, for a 90 dip ⨉ 90 dip image, the texture size in theory is 112.5 px ⨉ 112.5 px, and the actual size must be 112/113 px, which causes the image scaled and blurred.

    The tutorial :ref:`d14uikit-tutorials-elementary-dpi_adaption` gives a brief introduction to DPI.

.. _d14uikit-reference-cpp-application-sttcm-app:

  **static Application* app()**

Returns a pointer to the global ``Application`` instance.

* **Notes**

  This method is often used in callback functions when no ``app`` can be captured:

  .. code-block:: c++
    :emphasize-lines: 3

    button.D14_onMouseButtonRelease(clkp, e, )
    {
        Application::app()->exit();
    };

  The macro ``D14_onMouseButtonRelease`` expands to a lambda. If you do not want to use the static ``Application::app()``, it is necessary to make the lambda capture an ``app`` instance:

  .. code-block:: c++
    :emphasize-lines: 3

    Application app;

    button.D14_onMouseButtonRelease(clkp, e, &)
    {
        app.exit(); // capture by reference
    };

.. _d14uikit-reference-cpp-application-isntm-cursor:

  **Cursor* cursor() const**

Returns a pointer to the global ``Cursor`` instance.

.. _d14uikit-reference-cpp-application-isntm-run:

  **int run() const**

Launches the application.

* **Return**

  Type: **int**

  The exit code of the application.

.. _d14uikit-reference-cpp-application-isntm-exit:

  **void exit() const**

Notifies the application to exit.

.. _d14uikit-reference-cpp-application-isntm-visible:

  **bool visible() const**

Returns whether the main window is visible.

.. _d14uikit-reference-cpp-application-isntm-set_visible:

  **void setVisible(bool value)**

Changes whether the main window is visible.

.. _d14uikit-reference-cpp-application-isntm-minimized:

  **bool minimized() const**

Returns whether the main window is minimized.

.. _d14uikit-reference-cpp-application-isntm-set_minimized:

  **void setMinimized(bool value)**

Changes whether the main window is minimized.

* **Notes**

  ``setMinimized(false)`` has different effects based on the state of the main window:

  .. list-table::
    :header-rows: 1
    :width: 100%

    * - Original State
      - Function Effect
    * - Minimized
      - The main window will be restored to normal.
    * - Normal, Maximized
      - The main window will keep the original state.

.. _d14uikit-reference-cpp-application-isntm-maximized:

  **bool maximized() const**

Returns whether the main window is maximized.

.. _d14uikit-reference-cpp-application-isntm-set_maximized:

  **void setMaximized(bool value)**

Changes whether the main window is maximized.

* **Notes**

  ``setMaximized(false)`` has different effects based on the state of the main window:

  .. list-table::
    :header-rows: 1
    :width: 100%

    * - Original State
      - Function Effect
    * - Maximized
      - The main window will be restored to normal.
    * - Normal, Minimized
      - The main window will keep the original state.

.. _d14uikit-reference-cpp-application-isntm-size:

  **Size size() const**

Returns the size (DIP) of the main window.

.. _d14uikit-reference-cpp-application-isntm-set_size:

  **void setSize(const Size& value)**

Changes the size (DIP) of the main window.

.. _d14uikit-reference-cpp-application-isntm-width:

  **int width() const**

Returns the width (DIP) of the main window.

.. _d14uikit-reference-cpp-application-isntm-set_width:

  **void setWidth(int value)**

Changes the width (DIP) of the main window.

.. _d14uikit-reference-cpp-application-isntm-height:

  **int height() const**

Returns the height (DIP) of the main window.

.. _d14uikit-reference-cpp-application-isntm-set_height:

  **void setHeight(int value)**

Changes the height (DIP) of the main window.

.. _d14uikit-reference-cpp-application-isntm-position:

  **Point position() const**

Returns the position (DIP) of the main window in the screen coordinate.

.. _d14uikit-reference-cpp-application-isntm-set_position:

  **void setPosition(const Point& value)**

Changes the position (DIP) of the main window in the screen coordinate.

.. _d14uikit-reference-cpp-application-isntm-x:

  **int x() const**

Returns the x-offset (DIP) of the main window in the screen coordinate.

.. _d14uikit-reference-cpp-application-isntm-set_x:

  **void setX(int value)**

Changes the x-offset (DIP) of the main window in the screen coordinate.

.. _d14uikit-reference-cpp-application-isntm-y:

  **int y() const**

Returns the y-offset (DIP) of the main window in the screen coordinate.

.. _d14uikit-reference-cpp-application-isntm-set_y:

  **void setY(int value)**

Changes the y-offset (DIP) of the main window in the screen coordinate.

.. _d14uikit-reference-cpp-application-isntm-min_size:

  **Size minSize() const**

Returns the minimal size (DIP) of the main window.

.. _d14uikit-reference-cpp-application-isntm-set_min_size:

  **void setMinSize(const Size& value)**

Changes the minimal size (DIP) of the main window.

.. _d14uikit-reference-cpp-application-isntm-min_width:

  **int minWidth() const**

Returns the minimal width (DIP) of the main window.

.. _d14uikit-reference-cpp-application-isntm-set_min_width:

  **void setMinWidth(int value)**

Changes the minimal width (DIP) of the main window.

.. _d14uikit-reference-cpp-application-isntm-min_height:

  **int minHeight() const**

Returns the minimal height (DIP) of the main window.

.. _d14uikit-reference-cpp-application-isntm-set_min_height:

  **void setMinHeight(int value)**

Changes the minimal height (DIP) of the main window.

.. _d14uikit-reference-cpp-application-isntm-resizable:

  **bool resizable() const**

Returns whether the main window is resizable.

.. _d14uikit-reference-cpp-application-isntm-set_resizable:

  **void setResizable(bool value)**

Changes whether the main window is resizable.

.. _d14uikit-reference-cpp-application-isntm-fullscreen:

  **bool fullscreen() const**

Returns whether the application is displayed in fullscreen mode.

.. _d14uikit-reference-cpp-application-isntm-set_fullscreen:

  **void setFullscreen(bool value)**

Changes whether the application is displayed in fullscreen mode.

.. _d14uikit-reference-cpp-application-isntm-fps:

  **int fps() const**

Returns the refresh rate of the application.

.. _d14uikit-reference-cpp-application-isntm-low_energy:

  **bool lowEnergy() const**

Returns whether the application is working in low-energy mode.

* **Notes**

  For the application working in low-energy mode, the renderer outputs a new frame only when the user or the program itself triggers any UI event that causes the main window to repaint. When the application is idle in the background, it helps to reduce the CPU usage and saves power energy.

.. _d14uikit-reference-cpp-application-isntm-set_low_energy:

  **void setLowEnergy(bool value)**

Changes whether the application is working in low-energy mode.

.. _d14uikit-reference-cpp-application-isntm-theme_mode:

  **const std::wstring& themeMode() const**

Returns the theme mode of the application.

.. _d14uikit-reference-cpp-application-isntm-set_theme_mode:

  **void setThemeMode(const std::wstring& name)**

Changes the theme mode of the application.

* **Notes**

  Currently only "Dark" and "Light" theme modes are available.

.. _d14uikit-reference-cpp-application-isntm-theme_color:

  **Color themeColor() const**

Returns the theme color of the application.

.. _d14uikit-reference-cpp-application-isntm-set_theme_color:

  **void setThemeColor(const Color& value)**

Changes the theme color of the application.

.. _d14uikit-reference-cpp-application-isntm-use_system_theme:

  **bool useSystemTheme() const**

Returns whether the theme of the application follows the system setting.

.. _d14uikit-reference-cpp-application-isntm-set_use_system_theme:

  **void setUseSystemTheme(bool value)**

Changes whether the theme of the application follows the system setting.

.. _d14uikit-reference-cpp-application-isntm-lang_locale:

  **const std::wstring& langLocale() const**

Returns the language-locale setting of the application.

* **Return**

  Type: **const std::wstring&**

  A locale code formed by combining the ISO 639-1 language code and the ISO 3166-1 region code:

  .. list-table::
    :width: 100%

    * - en-us
      - English in United States
    * - zh-cn
      - Simplified Chinese in Chain

.. _d14uikit-reference-cpp-application-isntm-set_lang_locale:

  **void setLangLocale(const std::wstring& name)**

Changes the language-locale setting of the application.

.. _d14uikit-reference-cpp-application-isntm-clear_type:

  **bool clearType() const**

Returns whether the application uses ClearType to improve the readability of text.

.. seealso::

  More details about ClearType can be found `here`_.

.. _here: https://learn.microsoft.com/en-us/typography/cleartype/

.. _d14uikit-reference-cpp-application-isntm-set_clear_type:

  **void setClearType(bool value)**

Changes whether the application uses ClearType to improve the readability of text.

.. _d14uikit-reference-cpp-application-isntm-text_vert_smooth:

  **bool textVertSmooth() const**

Returns whether the application smooths text in vertical direction.

.. _d14uikit-reference-cpp-application-isntm-set_text_vert_smooth:

  **void setTextVertSmooth(bool value)**

Changes whether the application smooths text in vertical direction.

.. _d14uikit-reference-cpp-application-isntm-bmp_quality_interp:

  **bool bmpQualityInterp() const**

Returns whether the application uses high-quality cubic algorithm for bitmap interpolation.

.. _d14uikit-reference-cpp-application-isntm-set_bmp_quality_interp:

  **void setBmpQualityInterp(bool value)**

Changes whether the application uses high-quality cubic algorithm for bitmap interpolation.

.. _d14uikit-reference-cpp-application-isntm-capture:

  **std::unique_ptr<Image> capture() const**

Returns the last frame presented by the renderer.

* **Return**

  Type: **std::unique_ptr<Image>**

  A screenshot of the main window.

* **Notes**

  This method can capture a screenshot with high-performance, and below is a usage example:

  .. code-block:: c++
    :emphasize-lines: 3

    button.D14_onMouseButtonRelease(clkp, e, )
    {
        auto frame = Application::app()->capture();

        // some intermediate operation

        frame->save(L"Screenshot.png");
    };
