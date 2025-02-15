.. _d14uikit-reference-cpp-ui_objects-panel:

Panel
=====

Overview
--------

.. list-table::
  :width: 100%
  :widths: 30, 70

  * - Header
    - Panel.h
  * - Inherits
    - NonCopyable

``Panel`` is the most derived UI object in D14UIKit. It represents a rectangular area on the screen, where we can draw an image or place other UI objects (as children).

Constructors
------------

.. list-table::
  :width: 100%

  * - :ref:`Panel<d14uikit-reference-cpp-ui_objects-panel-ctor-1>` ()

Instance Methods
----------------

.. list-table::
  :width: 100%
  :widths: 30, 60, 10

  * - bool
    - :ref:`release<d14uikit-reference-cpp-ui_objects-panel-isntm-release>` ()
    -
  * - bool
    - :ref:`visible<d14uikit-reference-cpp-ui_objects-panel-isntm-visible>` ()
    - const
  * - void
    - :ref:`setVisible<d14uikit-reference-cpp-ui_objects-panel-isntm-set_visible>` (bool value)
    -
  * - bool
    - :ref:`enabled<d14uikit-reference-cpp-ui_objects-panel-isntm-enabled>` ()
    - const
  * - void
    - :ref:`setEnabled<d14uikit-reference-cpp-ui_objects-panel-isntm-set_enabled>` (bool value)
    -
  * - Size
    - :ref:`size<d14uikit-reference-cpp-ui_objects-panel-isntm-size>` ()
    - const
  * - void
    - :ref:`setSize<d14uikit-reference-cpp-ui_objects-panel-isntm-set_size>` (const Size& value)
    -
  * - int
    - :ref:`width<d14uikit-reference-cpp-ui_objects-panel-isntm-width>` ()
    - const
  * - void
    - :ref:`setWidth<d14uikit-reference-cpp-ui_objects-panel-isntm-set_width>` (int value)
    -
  * - int
    - :ref:`height<d14uikit-reference-cpp-ui_objects-panel-isntm-height>` ()
    - const
  * - void
    - :ref:`setHeight<d14uikit-reference-cpp-ui_objects-panel-isntm-set_height>` (int value)
    -
  * - Point
    - :ref:`position<d14uikit-reference-cpp-ui_objects-panel-isntm-position>` ()
    - const
  * - Point
    - :ref:`absPosition<d14uikit-reference-cpp-ui_objects-panel-isntm-abs_position>` ()
    - const
  * - void
    - :ref:`setPosition<d14uikit-reference-cpp-ui_objects-panel-isntm-set_position>` (const Point& value)
    -
  * - int
    - :ref:`x<d14uikit-reference-cpp-ui_objects-panel-isntm-x>` ()
    - const
  * - int
    - :ref:`absX<d14uikit-reference-cpp-ui_objects-panel-isntm-abs_x>` ()
    - const
  * - void
    - :ref:`setX<d14uikit-reference-cpp-ui_objects-panel-isntm-set_x>` (int value)
    -
  * - int
    - :ref:`y<d14uikit-reference-cpp-ui_objects-panel-isntm-y>` ()
    - const
  * - int
    - :ref:`absY<d14uikit-reference-cpp-ui_objects-panel-isntm-abs_y>` ()
    - const
  * - void
    - :ref:`setY<d14uikit-reference-cpp-ui_objects-panel-isntm-set_y>` (int value)
    -
  * - Size
    - :ref:`minSize<d14uikit-reference-cpp-ui_objects-panel-isntm-min_size>` ()
    - const
  * - void
    - :ref:`setMinSize<d14uikit-reference-cpp-ui_objects-panel-isntm-set_min_size>` (const Size& value)
    -
  * - int
    - :ref:`minWidth<d14uikit-reference-cpp-ui_objects-panel-isntm-min_width>` ()
    - const
  * - void
    - :ref:`setMinWidth<d14uikit-reference-cpp-ui_objects-panel-isntm-set_min_width>` (int value)
    -
  * - int
    - :ref:`minHeight<d14uikit-reference-cpp-ui_objects-panel-isntm-min_height>` ()
    - const
  * - void
    - :ref:`setMinHeight<d14uikit-reference-cpp-ui_objects-panel-isntm-set_min_height>` (int value)
    -
  * - Size
    - :ref:`maxSize<d14uikit-reference-cpp-ui_objects-panel-isntm-max_size>` ()
    - const
  * - void
    - :ref:`setMaxSize<d14uikit-reference-cpp-ui_objects-panel-isntm-set_max_size>` (const Size& value)
    -
  * - int
    - :ref:`maxWidth<d14uikit-reference-cpp-ui_objects-panel-isntm-max_width>` ()
    - const
  * - void
    - :ref:`setMaxWidth<d14uikit-reference-cpp-ui_objects-panel-isntm-set_max_width>` (int value)
    -
  * - int
    - :ref:`maxHeight<d14uikit-reference-cpp-ui_objects-panel-isntm-max_height>` ()
    - const
  * - void
    - :ref:`setMaxHeight<d14uikit-reference-cpp-ui_objects-panel-isntm-set_max_height>` (int value)
    -
  * - Color
    - :ref:`color<d14uikit-reference-cpp-ui_objects-panel-isntm-color>` ()
    - const
  * - void
    - :ref:`setColor<d14uikit-reference-cpp-ui_objects-panel-isntm-set_color>` (const Color& value)
    -
  * - float
    - :ref:`opacity<d14uikit-reference-cpp-ui_objects-panel-isntm-opacity>` ()
    - const
  * - void
    - :ref:`setOpacity<d14uikit-reference-cpp-ui_objects-panel-isntm-set_opacity>` (float value)
    -
  * - int
    - :ref:`outlineWidth<d14uikit-reference-cpp-ui_objects-panel-isntm-outline_width>` ()
    - const
  * - void
    - :ref:`setOutlineWidth<d14uikit-reference-cpp-ui_objects-panel-isntm-set_outline_width>` (int value)
    -
  * - Color
    - :ref:`outlineColor<d14uikit-reference-cpp-ui_objects-panel-isntm-outline_color>` ()
    - const
  * - void
    - :ref:`setOutlineColor<d14uikit-reference-cpp-ui_objects-panel-isntm-set_outline_color>` (const Color& value)
    -
  * - float
    - :ref:`outlineOpacity<d14uikit-reference-cpp-ui_objects-panel-isntm-outline_opacity>` ()
    - const
  * - void
    - :ref:`setOutlineOpacity<d14uikit-reference-cpp-ui_objects-panel-isntm-set_outline_opacity>` (float value)
    -
  * - bool
    - :ref:`animState<d14uikit-reference-cpp-ui_objects-panel-isntm-anim_state>` ()
    - const
  * - void
    - :ref:`setAnimState<d14uikit-reference-cpp-ui_objects-panel-isntm-set_anim_state>` (bool value)
    -
  * - Image*
    - :ref:`image<d14uikit-reference-cpp-ui_objects-panel-isntm-image>` ()
    - const
  * - void
    - :ref:`setImage<d14uikit-reference-cpp-ui_objects-panel-isntm-set_image>` (Image* image)
    -
  * - float
    - :ref:`bitmapOpacity<d14uikit-reference-cpp-ui_objects-panel-isntm-bitmap_opacity>` ()
    - const
  * - void
    - :ref:`setBitmapOpacity<d14uikit-reference-cpp-ui_objects-panel-isntm-set_bitmap_opacity>` (float value)
    -
  * - BitmapInterpMode
    - :ref:`bitmapInterpMode<d14uikit-reference-cpp-ui_objects-panel-isntm-bitmap_interp_mode>` ()
    - const
  * - void
    - :ref:`setBitmapInterpMode<d14uikit-reference-cpp-ui_objects-panel-isntm-set_bitmap_interp_mode>` (BitmapInterpMode mode)
    -
  * - int
    - :ref:`roundRadius<d14uikit-reference-cpp-ui_objects-panel-isntm-round_radius>` ()
    - const
  * - void
    - :ref:`setRoundRadius<d14uikit-reference-cpp-ui_objects-panel-isntm-set_round_radius>` (int value)
    -
  * - void
    - :ref:`setGlobal<d14uikit-reference-cpp-ui_objects-panel-isntm-set_global>` (bool value)
    -
  * - void
    - :ref:`setPinned<d14uikit-reference-cpp-ui_objects-panel-isntm-set_pinned>` (bool value)
    -
  * - void
    - :ref:`setFocused<d14uikit-reference-cpp-ui_objects-panel-isntm-set_focused>` (bool value)
    -
  * - Panel*
    - :ref:`parent<d14uikit-reference-cpp-ui_objects-panel-isntm-parent>` ()
    - const
  * - void
    - :ref:`setParent<d14uikit-reference-cpp-ui_objects-panel-isntm-set_parent>` (Panel* uiobj)
    -
  * - void
    - :ref:`addChild<d14uikit-reference-cpp-ui_objects-panel-isntm-add_child>` (Panel* uiobj)
    -
  * - void
    - :ref:`removeChild<d14uikit-reference-cpp-ui_objects-panel-isntm-remove_child>` (Panel* uiobj)
    -
  * - void
    - :ref:`pinChild<d14uikit-reference-cpp-ui_objects-panel-isntm-pin_child>` (Panel* uiobj)
    -
  * - void
    - :ref:`unpinChild<d14uikit-reference-cpp-ui_objects-panel-isntm-unpin_child>` (Panel* uiobj)
    -
  * - void
    - :ref:`moveTopmost<d14uikit-reference-cpp-ui_objects-panel-isntm-move_topmost>` ()
    -
  * - void
    - :ref:`moveAbove<d14uikit-reference-cpp-ui_objects-panel-isntm-move_above>` (Panel* uiobj)
    -
  * - void
    - :ref:`moveBelow<d14uikit-reference-cpp-ui_objects-panel-isntm-move_below>` (Panel* uiobj)
    -

Callback Functions
------------------

.. list-table::
  :width: 100%
  :widths: 30, 70

  * - virtual void
    - :ref:`onUpdate<d14uikit-reference-cpp-ui_objects-panel-virtm-on_update>` ()
  * - virtual void
    - :ref:`onSize<d14uikit-reference-cpp-ui_objects-panel-virtm-on_size>` (SizeEvent* event)
  * - virtual void
    - :ref:`onMove<d14uikit-reference-cpp-ui_objects-panel-virtm-on_move>` (MoveEvent* event)
  * - virtual void
    - :ref:`onChangeTheme<d14uikit-reference-cpp-ui_objects-panel-virtm-on_change_theme>` (const std::wstring& name)
  * - virtual void
    - :ref:`onChangeLangLocale<d14uikit-reference-cpp-ui_objects-panel-virtm-on_change_lang_locale>` (const std::wstring& name)
  * - virtual void
    - :ref:`onGetFocus<d14uikit-reference-cpp-ui_objects-panel-virtm-on_get_focus>` ()
  * - virtual void
    - :ref:`onLoseFocus<d14uikit-reference-cpp-ui_objects-panel-virtm-on_lose_focus>` ()
  * - virtual void
    - :ref:`onMouseEnter<d14uikit-reference-cpp-ui_objects-panel-virtm-on_mouse_enter>` (MouseMoveEvent* event)
  * - virtual void
    - :ref:`onMouseMove<d14uikit-reference-cpp-ui_objects-panel-virtm-on_mouse_move>` (MouseMoveEvent* event)
  * - virtual void
    - :ref:`onMouseLeave<d14uikit-reference-cpp-ui_objects-panel-virtm-on_mouse_leave>` (MouseMoveEvent* event)
  * - virtual void
    - :ref:`onMouseButton<d14uikit-reference-cpp-ui_objects-panel-virtm-on_mouse_button>` (MouseButtonEvent* event)
  * - virtual void
    - :ref:`onMouseWheel<d14uikit-reference-cpp-ui_objects-panel-virtm-on_mouse_wheel>` (MouseWheelEvent* event)
  * - virtual void
    - :ref:`onKeyboard<d14uikit-reference-cpp-ui_objects-panel-virtm-on_keyboard>` (KeyboardEvent* event)

Remarks
-------

* **Appearance**

  The background of ``Panel`` can be a solid color:

  .. sourcecode:: c++

    panel.setColor({ 255, 0, 0 });
    panel.setOpacity(1.0f);

  or an image:

  .. sourcecode:: c++

    Image img(L"background.png");
    panel.setImage(&img);

  We can set both a solid color and an image at the same time, and the image will be displayed on the solid color background, which is very useful for displaying an image with an Alpha channel. In addition to the background, we can also set the outline of ``Panel``:

  .. sourcecode:: c++

    panel.setOutlineColor({ 0, 255, 0 });
    panel.setOutlineOpacity(1.0f);

  The outline will be displayed on the image and solid color background.

* **Priority**

  ``Panel`` can be a global UI object:

  .. sourcecode:: c++

    panel.setGlobal(true);

  or a child object of another ``Panel``:

  .. sourcecode:: c++

    panel.setGlobal(false);

  It is worth noting that global objects do not refer to the children of the main window, but rather the objects directly managed by the application. In general, the main window should be created as a global object. If you want a higher priority of a UI object than the main window (such as a dialog box), you should set it as a global object.

  For objects at the same layer (all are global objects or children of another object), D14UIKit also supports different priorities. For example, to make ``a`` display above ``b``:

  .. code-block:: c++
    :emphasize-lines: 4

    a.setParent(&panel);
    b.setParent(&panel);

    a.moveAbove(&b);

  or simply move it to the topmost:

  .. sourcecode:: c++

    a.moveTopmost();

  In D14UIKit, a smaller value corresponds to a higher priority, so the topmost's priority is 0.

Details
-------

.. _d14uikit-reference-cpp-ui_objects-panel-ctor-1:

  **Panel()**

Constructs a panel with size of (0,0) and position of (0,0), and a black transparent background and outline, and the lowest priority.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-release:

  **bool release()**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-visible:

  **bool visible() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_visible:

  **void setVisible(bool value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-enabled:

  **bool enabled() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_enabled:

  **void setEnabled(bool value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-size:

  **Size size() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_size:

  **void setSize(const Size& value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-width:

  **int width() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_width:

  **void setWidth(int value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-height:

  **int height() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_height:

  **void setHeight(int value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-position:

  **Point position() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-abs_position:

  **Point absPosition() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_position:

  **void setPosition(const Point& value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-x:

  **int x() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-abs_x:

  **int absX() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_x:

  **void setX(int value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-y:

  **int y() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-abs_y:

  **int absY() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_y:

  **void setY(int value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-min_size:

  **Size minSize() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_min_size:

  **void setMinSize(const Size& value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-min_width:

  **int minWidth() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_min_width:

  **void setMinWidth(int value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-min_height:

  **int minHeight() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_min_height:

  **void setMinHeight(int value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-max_size:

  **Size maxSize() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_max_size:

  **void setMaxSize(const Size& value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-max_width:

  **int maxWidth() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_max_width:

  **void setMaxWidth(int value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-max_height:

  **int maxHeight() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_max_height:

  **void setMaxHeight(int value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-color:

  **Color color() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_color:

  **void setColor(const Color& value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-opacity:

  **float opacity() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_opacity:

  **void setOpacity(float value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-outline_width:

  **int outlineWidth() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_outline_width:

  **void setOutlineWidth(int value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-outline_color:

  **Color outlineColor() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_outline_color:

  **void setOutlineColor(const Color& value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-outline_opacity:

  **float outlineOpacity() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_outline_opacity:

  **void setOutlineOpacity(float value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-anim_state:

  **bool animState() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_anim_state:

  **void setAnimState(bool value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-image:

  **Image* image() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_image:

  **void setImage(Image* image)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-bitmap_opacity:

  **float bitmapOpacity() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_bitmap_opacity:

  **void setBitmapOpacity(float value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-bitmap_interp_mode:

  **BitmapInterpMode bitmapInterpMode() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_bitmap_interp_mode:

  **void setBitmapInterpMode(BitmapInterpMode mode)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-round_radius:

  **int roundRadius() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_round_radius:

  **void setRoundRadius(int value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_global:

  **void setGlobal(bool value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_pinned:

  **void setPinned(bool value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_focused:

  **void setFocused(bool value)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-parent:

  **Panel* parent() const**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_parent:

  **void setParent(Panel* uiobj)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-add_child:

  **void addChild(Panel* uiobj)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-remove_child:

  **void removeChild(Panel* uiobj)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-pin_child:

  **void pinChild(Panel* uiobj)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-unpin_child:

  **void unpinChild(Panel* uiobj)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-move_topmost:

  **void moveTopmost()**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-move_above:

  **void moveAbove(Panel* uiobj)**

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-move_below:

  **void moveBelow(Panel* uiobj)**

.. _d14uikit-reference-cpp-ui_objects-panel-virtm-on_update:

  **virtual void onUpdate()**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - trigger
    - when processing the update stage in each frame
  * - functor
    - .. sourcecode:: c++

        std::function<void(Panel*)> onUpdate = {};

  * - lambda templates
    - general:

      .. sourcecode:: c++

        XXXX.Panel::callback().onUpdate =
        [/*capture list*/](Panel* p)
        {
            // add code here
        };

      with Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onUpdate(p, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_objects-panel-virtm-on_size:

  **virtual void onSize(SizeEvent* event)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - trigger
    - when the size of the panel changes
  * - functor
    - .. sourcecode:: c++

        std::function<void(Panel*, SizeEvent*)> onSize = {};

  * - lambda templates
    - general:

      .. sourcecode:: c++

        XXXX.Panel::callback().onSize =
        [/*capture list*/](Panel* p, SizeEvent* e)
        {
            // add code here
        };

      with Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onSize(p, e, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_objects-panel-virtm-on_move:

  **virtual void onMove(MoveEvent* event)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - trigger
    - when the position of the panel changes
  * - functor
    - .. sourcecode:: c++

        std::function<void(Panel*, MoveEvent*)> onMove = {};

  * - lambda templates
    - general:

      .. sourcecode:: c++

        XXXX.Panel::callback().onMove =
        [/*capture list*/](Panel* p, MoveEvent* e)
        {
            // add code here
        };

      with Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onMove(p, e, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_objects-panel-virtm-on_change_theme:

  **virtual void onChangeTheme(const std::wstring& name)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - trigger
    - when the theme of the application changes
  * - functor
    - .. sourcecode:: c++

        std::function<void(Panel*, const std::wstring&)> onChangeTheme = {};

  * - lambda templates
    - general:

      .. sourcecode:: c++

        XXXX.Panel::callback().onChangeTheme =
        [/*capture list*/](Panel* p, const std::wstring& name)
        {
            // add code here
        };

      with Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onChangeTheme(p, name, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_objects-panel-virtm-on_change_lang_locale:

  **virtual void onChangeLangLocale(const std::wstring& name)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - trigger
    - when the language-locale of the application changes
  * - functor
    - .. sourcecode:: c++

        std::function<void(Panel*, const std::wstring&)> onChangeLangLocale = {};

  * - lambda templates
    - general:

      .. sourcecode:: c++

        XXXX.Panel::callback().onChangeLangLocale =
        [/*capture list*/](Panel* p, const std::wstring& name)
        {
            // add code here
        };

      with Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onChangeLangLocale(p, name, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_objects-panel-virtm-on_get_focus:

  **virtual void onGetFocus()**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - trigger
    - when the panel gets focus
  * - functor
    - .. sourcecode:: c++

        std::function<void(Panel*)> onGetFocus = {};

  * - lambda templates
    - general:

      .. sourcecode:: c++

        XXXX.Panel::callback().onGetFocus =
        [/*capture list*/](Panel* p)
        {
            // add code here
        };

      with Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onGetFocus(p, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_objects-panel-virtm-on_lose_focus:

  **virtual void onLoseFocus()**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - trigger
    - when the panel loses focus
  * - functor
    - .. sourcecode:: c++

        std::function<void(Panel*)> onLoseFocus = {};

  * - lambda templates
    - general:

      .. sourcecode:: c++

        XXXX.Panel::callback().onLoseFocus =
        [/*capture list*/](Panel* p)
        {
            // add code here
        };

      with Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onLoseFocus(p, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_objects-panel-virtm-on_mouse_enter:

  **virtual void onMouseEnter(MouseMoveEvent* event)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - trigger
    - when the mouse cursor enters the panel
  * - functor
    - .. sourcecode:: c++

        std::function<void(Panel*, MouseMoveEvent*)> onMouseEnter = {};

  * - lambda templates
    - general:

      .. sourcecode:: c++

        XXXX.Panel::callback().onMouseEnter =
        [/*capture list*/](Panel* p, MouseMoveEvent* e)
        {
            // add code here
        };

      with Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onMouseEnter(p, e, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_objects-panel-virtm-on_mouse_move:

  **virtual void onMouseMove(MouseMoveEvent* event)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - trigger
    - when the mouse cursor moves in the panel
  * - functor
    - .. sourcecode:: c++

        std::function<void(Panel*, MouseMoveEvent*)> onMouseMove = {};

  * - lambda templates
    - general:

      .. sourcecode:: c++

        XXXX.Panel::callback().onMouseMove =
        [/*capture list*/](Panel* p, MouseMoveEvent* e)
        {
            // add code here
        };

      with Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onMouseMove(p, e, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_objects-panel-virtm-on_mouse_leave:

  **virtual void onMouseLeave(MouseMoveEvent* event)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - trigger
    - when the mouse cursor leaves the panel
  * - functor
    - .. sourcecode:: c++

        std::function<void(Panel*, MouseMoveEvent*)> onMouseLeave = {};

  * - lambda templates
    - general:

      .. sourcecode:: c++

        XXXX.Panel::callback().onMouseLeave =
        [/*capture list*/](Panel* p, MouseMoveEvent* e)
        {
            // add code here
        };

      with Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onMouseLeave(p, e, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_objects-panel-virtm-on_mouse_button:

  **virtual void onMouseButton(MouseButtonEvent* event)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - trigger
    - when any mouse button is used in the panel
  * - functor
    - .. sourcecode:: c++

        std::function<void(Panel*, MouseButtonEvent*)> onMouseButton = {};

  * - lambda templates
    - general:

      .. sourcecode:: c++

        XXXX.Panel::callback().onMouseButton =
        [/*capture list*/](Panel* p, MouseButtonEvent* e)
        {
            // add code here
        };

      with Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onMouseButton(p, e, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_objects-panel-virtm-on_mouse_wheel:

  **virtual void onMouseWheel(MouseWheelEvent* event)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - trigger
    - when the mouse wheel is used in the panel
  * - functor
    - .. sourcecode:: c++

        std::function<void(Panel*, MouseWheelEvent*)> onMouseWheel = {};

  * - lambda templates
    - general:

      .. sourcecode:: c++

        XXXX.Panel::callback().onMouseWheel =
        [/*capture list*/](Panel* p, MouseWheelEvent* e)
        {
            // add code here
        };

      with Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onMouseWheel(p, e, /*capture list*/)
        {
            // add code here
        };

.. _d14uikit-reference-cpp-ui_objects-panel-virtm-on_keyboard:

  **virtual void onKeyboard(KeyboardEvent* event)**

.. list-table::
  :width: 100%
  :stub-columns: 1

  * - trigger
    - when the keyboard is used in the panel
  * - functor
    - .. sourcecode:: c++

        std::function<void(Panel*, KeyboardEvent*)> onKeyboard = {};

  * - lambda templates
    - general:

      .. sourcecode:: c++

        XXXX.Panel::callback().onKeyboard =
        [/*capture list*/](Panel* p, KeyboardEvent* e)
        {
            // add code here
        };

      with Callback.h:

      .. sourcecode:: c++

        XXXX.D14_onKeyboard(p, e, /*capture list*/)
        {
            // add code here
        };
