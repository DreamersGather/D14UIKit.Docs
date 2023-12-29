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
    - :ref:`destroy<d14uikit-reference-cpp-ui_objects-panel-isntm-destroy>` ()
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
  * - Image*
    - :ref:`image<d14uikit-reference-cpp-ui_objects-panel-isntm-image>` ()
    - const
  * - void
    - :ref:`setImage<d14uikit-reference-cpp-ui_objects-panel-isntm-set_image>` (Image* image)
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

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-destroy:

  **bool destroy()**

Decreases the reference count of the panel. If the reference count becomes zero, the panel will be destroyed and the method returns true; otherwise the method returns false.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-visible:

  **bool visible() const**

Returns whether the panel is visible.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_visible:

  **void setVisible(bool value)**

Changes whether the panel is visible.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-enabled:

  **bool enabled() const**

Returns whether the panel is enabled.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_enabled:

  **void setEnabled(bool value)**

Changes whether the panel is enabled.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-size:

  **Size size() const**

Returns the size (DIP) of the panel.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_size:

  **void setSize(const Size& value)**

Changes the size (DIP) of the panel.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-width:

  **int width() const**

Returns the width (DIP) of the panel.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_width:

  **void setWidth(int value)**

Changes the width (DIP) of the panel.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-height:

  **int height() const**

Returns the height (DIP) of the panel.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_height:

  **void setHeight(int value)**

Changes the height (DIP) of the panel.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-position:

  **Point position() const**

Returns the position (DIP) of the panel in the parent coordinate.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-abs_position:

  **Point absPosition() const**

Returns the position (DIP) of the panel in the application coordinate.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_position:

  **void setPosition(const Point& value)**

Changes the position (DIP) of the panel in the parent coordinate.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-x:

  **int x() const**

Returns the x-offset (DIP) of the panel in the parent coordinate.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-abs_x:

  **int absX() const**

Returns the x-offset (DIP) of the panel in the application coordinate.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_x:

  **void setX(int value)**

Changes the x-offset (DIP) of the panel in the parent coordinate.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-y:

  **int y() const**

Returns the y-offset (DIP) of the panel in the parent coordinate.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-abs_y:

  **int absY() const**

Returns the y-offset (DIP) of the panel in the application coordinate.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_y:

  **void setY(int value)**

Changes the y-offset (DIP) of the panel in the parent coordinate.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-color:

  **Color color() const**

Returns the color of the solid background.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_color:

  **void setColor(const Color& value)**

Changes the color of the solid background.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-opacity:

  **float opacity() const**

Returns the opacity of the solid background.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_opacity:

  **void setOpacity(float value)**

Changes the opacity of the solid background.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-outline_width:

  **int outlineWidth() const**

Returns the width (DIP) of the outline.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_outline_width:

  **void setOutlineWidth(int value)**

Changes the width (DIP) of the outline.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-outline_color:

  **Color outlineColor() const**

Returns the color of the outline.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_outline_color:

  **void setOutlineColor(const Color& value)**

Changes the color of the outline.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-outline_opacity:

  **float outlineOpacity() const**

Returns the opacity of the outline.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_outline_opacity:

  **void setOutlineOpacity(float value)**

Changes the opacity of the outline.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-image:

  **Image* image() const**

Returns the image of the background, or ``nullptr`` if not set.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_image:

  **void setImage(Image* image)**

Changes the image of the background; pass ``nullptr`` to reset.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-round_radius:

  **int roundRadius() const**

Returns the round radius (DIP) of the panel.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_round_radius:

  **void setRoundRadius(int value)**

Changes the round radius (DIP) of the panel.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_global:

  **void setGlobal(bool value)**

Changes whether the panel is a global UI object.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_focused:

  **void setFocused(bool value)**

Changes whether the panel can be focused.

* **Notes**

  It is only when the UI object can be focused that its ``onGetFocus`` and ``onLoseFocus`` callback functions are possible to be triggered.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-parent:

  **Panel* parent() const**

Returns the parent of the panel, or ``nullptr`` if not set.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-set_parent:

  **void setParent(Panel* uiobj)**

Changes the parent of the panel; pass ``nullptr`` to reset.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-add_child:

  **void addChild(Panel* uiobj)**

Adds ``uiobj`` to the child-set of the panel.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-remove_child:

  **void removeChild(Panel* uiobj)**

Removes ``uiobj`` from the child-set of the panel.

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-move_topmost:

  **void moveTopmost()**

Moves the panel to the topmost (i.e. gives the highest priority).

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-move_above:

  **void moveAbove(Panel* uiobj)**

Moves the panel above ``uiobj`` (i.e. set its priority to ``uiobj``'s - 1).

.. _d14uikit-reference-cpp-ui_objects-panel-isntm-move_below:

  **void moveBelow(Panel* uiobj)**

Moves the panel below ``uiobj`` (i.e. set its priority to  ``uiobj``'s + 1).

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
