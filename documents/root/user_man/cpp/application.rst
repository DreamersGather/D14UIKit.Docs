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

  * - int
    - :ref:`dpi<d14uikit-reference-cpp-ui_objects-application-isntm-dpi>` ()
    - const
  * - BitmapInterpMode
    - :ref:`bitmapInterpMode<d14uikit-reference-cpp-ui_objects-application-isntm-bitmap_interp_mode>` ()
    - const
  * - void
    - :ref:`setBitmapInterpMode<d14uikit-reference-cpp-ui_objects-application-isntm-set_bitmap_interp_mode>` (BitmapInterpMode mode)
    -
  * - int
    - :ref:`run<d14uikit-reference-cpp-ui_objects-application-isntm-run>` ()
    - const
  * - void
    - :ref:`exit<d14uikit-reference-cpp-ui_objects-application-isntm-exit>` ()
    - const
  * - bool
    - :ref:`visible<d14uikit-reference-cpp-ui_objects-application-isntm-visible>` ()
    - const
  * - void
    - :ref:`setVisible<d14uikit-reference-cpp-ui_objects-application-isntm-set_visible>` (bool value)
    -
  * - bool
    - :ref:`minimized<d14uikit-reference-cpp-ui_objects-application-isntm-minimized>` ()
    - const
  * - void
    - :ref:`setMinimized<d14uikit-reference-cpp-ui_objects-application-isntm-set_minimized>` (bool value)
    -
  * - bool
    - :ref:`maximized<d14uikit-reference-cpp-ui_objects-application-isntm-maximized>` ()
    - const
  * - void
    - :ref:`setMaximized<d14uikit-reference-cpp-ui_objects-application-isntm-set_maximized>` (bool value)
    -
  * - Size
    - :ref:`size<d14uikit-reference-cpp-ui_objects-application-isntm-size>` ()
    - const
  * - void
    - :ref:`setSize<d14uikit-reference-cpp-ui_objects-application-isntm-set_size>` (const Size& value)
    -
  * - int
    - :ref:`width<d14uikit-reference-cpp-ui_objects-application-isntm-width>` ()
    - const
  * - void
    - :ref:`setWidth<d14uikit-reference-cpp-ui_objects-application-isntm-set_width>` (int value)
    -
  * - int
    - :ref:`height<d14uikit-reference-cpp-ui_objects-application-isntm-height>` ()
    - const
  * - void
    - :ref:`setHeight<d14uikit-reference-cpp-ui_objects-application-isntm-set_height>` (int value)
    -
  * - Point
    - :ref:`position<d14uikit-reference-cpp-ui_objects-application-isntm-position>` ()
    - const
  * - void
    - :ref:`setPosition<d14uikit-reference-cpp-ui_objects-application-isntm-set_position>` (const Point& value)
    -
  * - int
    - :ref:`x<d14uikit-reference-cpp-ui_objects-application-isntm-x>` ()
    - const
  * - void
    - :ref:`setX<d14uikit-reference-cpp-ui_objects-application-isntm-set_x>` (int value)
    -
  * - int
    - :ref:`y<d14uikit-reference-cpp-ui_objects-application-isntm-y>` ()
    - const
  * - void
    - :ref:`setY<d14uikit-reference-cpp-ui_objects-application-isntm-set_y>` (int value)
    -
  * - Size
    - :ref:`minSize<d14uikit-reference-cpp-ui_objects-application-isntm-min_size>` ()
    - const
  * - void
    - :ref:`setMinSize<d14uikit-reference-cpp-ui_objects-application-isntm-set_min_size>` (const Size& value)
    -
  * - int
    - :ref:`minWidth<d14uikit-reference-cpp-ui_objects-application-isntm-min_width>` ()
    - const
  * - void
    - :ref:`setMinWidth<d14uikit-reference-cpp-ui_objects-application-isntm-set_min_width>` (int value)
    -
  * - int
    - :ref:`minHeight<d14uikit-reference-cpp-ui_objects-application-isntm-min_height>` ()
    - const
  * - void
    - :ref:`setMinHeight<d14uikit-reference-cpp-ui_objects-application-isntm-set_min_height>` (int value)
    -
  * - bool
    - :ref:`resizable<d14uikit-reference-cpp-ui_objects-application-isntm-resizable>` ()
    - const
  * - void
    - :ref:`setResizable<d14uikit-reference-cpp-ui_objects-application-isntm-set_resizable>` (bool value)
    -
  * - bool
    - :ref:`fullscreen<d14uikit-reference-cpp-ui_objects-application-isntm-fullscreen>` ()
    - const
  * - void
    - :ref:`setFullscreen<d14uikit-reference-cpp-ui_objects-application-isntm-set_fullscreen>` (bool value)
    -
  * - int
    - :ref:`fps<d14uikit-reference-cpp-ui_objects-application-isntm-fps>` ()
    - const
  * - std::unique_ptr<Image>
    - :ref:`capture<d14uikit-reference-cpp-ui_objects-application-isntm-capture>` ()
    - const
  * - TextAntialiasMode
    - :ref:`textAntialiasMode<d14uikit-reference-cpp-ui_objects-application-isntm-text_antialias_mode>` ()
    - const
  * - void
    - :ref:`setTextAntialiasMode<d14uikit-reference-cpp-ui_objects-application-isntm-set_text_antialias_mode>` (TextAntialiasMode mode)
    -
  * - RenderingMode
    - :ref:`renderingMode<d14uikit-reference-cpp-ui_objects-application-isntm-rendering_mode>` ()
    - const
  * - void
    - :ref:`setRenderingMode<d14uikit-reference-cpp-ui_objects-application-isntm-set_rendering_mode>` (RenderingMode mode)
    -
  * - int
    - :ref:`animCount<d14uikit-reference-cpp-ui_objects-application-isntm-anim_count>` ()
    - const
  * - bool
    - :ref:`animState<d14uikit-reference-cpp-ui_objects-application-isntm-anim_state>` ()
    - const
  * - void
    - :ref:`setAnimState<d14uikit-reference-cpp-ui_objects-application-isntm-set_anim_state>` (bool value)
    -
  * - Cursor*
    - :ref:`cursor<d14uikit-reference-cpp-ui_objects-application-isntm-cursor>` ()
    - const
  * - const std::wstring&
    - :ref:`themeMode<d14uikit-reference-cpp-ui_objects-application-isntm-theme_mode>` ()
    - const
  * - void
    - :ref:`setThemeMode<d14uikit-reference-cpp-ui_objects-application-isntm-set_theme_mode>` (const std::wstring& name)
    -
  * - Color
    - :ref:`themeColor<d14uikit-reference-cpp-ui_objects-application-isntm-theme_color>` ()
    - const
  * - void
    - :ref:`setThemeColor<d14uikit-reference-cpp-ui_objects-application-isntm-set_theme_color>` (const Color& value)
    -
  * - bool
    - :ref:`useSystemTheme<d14uikit-reference-cpp-ui_objects-application-isntm-use_system_theme>` ()
    - const
  * - void
    - :ref:`setUseSystemTheme<d14uikit-reference-cpp-ui_objects-application-isntm-set_use_system_theme>` (bool value)
    -
  * - const std::wstring&
    - :ref:`langLocale<d14uikit-reference-cpp-ui_objects-application-isntm-lang_locale>` ()
    - const
  * - void
    - :ref:`setLangLocale<d14uikit-reference-cpp-ui_objects-application-isntm-set_lang_locale>` (const std::wstring& name)
    -

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

    A DPI value that is not a multiple of 96 dpi may cause blurry display. The reason why we use "may" here is that it also depends on the actual size of the UI object. For example: at 125% scaling (i.e. 120 dpi), rendering a 100x100 dip image is based on a 125x125 px offscreen texture; however, for a 90x90 dip image, the texture size in theory is 112.5x112.5 px, and the actual size must be 112/113 px, which causes the image scaled and blurred.

    The tutorial :ref:`d14uikit-tutorials-beginner-dpi_adaption` gives a brief introduction to DPI.

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

.. _d14uikit-reference-cpp-ui_objects-application-isntm-dpi:

  **int dpi() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-bitmap_interp_mode:

  **BitmapInterpMode bitmapInterpMode() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_bitmap_interp_mode:

  **void setBitmapInterpMode(BitmapInterpMode mode)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-run:

  **int run() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-exit:

  **void exit() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-visible:

  **bool visible() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_visible:

  **void setVisible(bool value)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-minimized:

  **bool minimized() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_minimized:

  **void setMinimized(bool value)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-maximized:

  **bool maximized() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_maximized:

  **void setMaximized(bool value)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-size:

  **Size size() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_size:

  **void setSize(const Size& value)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-width:

  **int width() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_width:

  **void setWidth(int value)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-height:

  **int height() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_height:

  **void setHeight(int value)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-position:

  **Point position() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_position:

  **void setPosition(const Point& value)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-x:

  **int x() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_x:

  **void setX(int value)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-y:

  **int y() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_y:

  **void setY(int value)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-min_size:

  **Size minSize() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_min_size:

  **void setMinSize(const Size& value)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-min_width:

  **int minWidth() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_min_width:

  **void setMinWidth(int value)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-min_height:

  **int minHeight() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_min_height:

  **void setMinHeight(int value)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-resizable:

  **bool resizable() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_resizable:

  **void setResizable(bool value)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-fullscreen:

  **bool fullscreen() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_fullscreen:

  **void setFullscreen(bool value)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-fps:

  **int fps() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-capture:

  **std::unique_ptr<Image> capture() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-text_antialias_mode:

  **TextAntialiasMode textAntialiasMode() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_text_antialias_mode:

  **void setTextAntialiasMode(TextAntialiasMode mode)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-rendering_mode:

  **RenderingMode renderingMode() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_rendering_mode:

  **void setRenderingMode(RenderingMode mode)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-anim_count:

  **int animCount() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-anim_state:

  **bool animState() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_anim_state:

  **void setAnimState(bool value)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-cursor:

  **Cursor* cursor() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-theme_mode:

  **const std::wstring& themeMode() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_theme_mode:

  **void setThemeMode(const std::wstring& name)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-theme_color:

  **Color themeColor() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_theme_color:

  **void setThemeColor(const Color& value)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-use_system_theme:

  **bool useSystemTheme() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_use_system_theme:

  **void setUseSystemTheme(bool value)**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-lang_locale:

  **const std::wstring& langLocale() const**

.. _d14uikit-reference-cpp-ui_objects-application-isntm-set_lang_locale:

  **void setLangLocale(const std::wstring& name)**
