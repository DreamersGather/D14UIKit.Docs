.. _d14uikit-tutorials-advanced-advanced_callback:

Advanced Callback
=================

.. image:: https://media.githubusercontent.com/media/DreamersGather/D14Docs.Res/main/d14uikit/tutorials/advanced_callback.png

.. note::

  The source code of the demo can be found in **d14uikit/demo**.

In this section, we will create a simple yet complete **paint.exe** to demonstrate the advanced usage of callback functions in D14UIKit.

Final Test
----------

Readers who have reached this section must already be familiar with the development of D14UIKit, so you can consider the demo in this section as a final test. The demo source **d14uikit/demo/AdvancedCallback.cpp** have detailed comments. If you can fully understand the meaning of each code in the program, then congratulations: you have just entered the world of D14UIKit development.

Next Steps
----------

As a drawing program, this demo is still in a relatively raw stage. For example, it does not support changing the brush color, and the brush stroke does not look very real. We have summarized some points to improve, and you can continue to develop the program if interested:

1. **Support Different Brush Colors**:

   The current program can only use the system theme color as the brush color. Perhaps we can design a ``Panel`` that uses the brush color as its background, and when we click on it, a dialog box will pop up for us to choose another color. It seems easy to achieve this function by writing some callback functions. As for the modal dialog box, perhaps a combination of an invisible ``Panel`` (used to intercept UI events) and an upper Window (used as a dialog box) can be somehow useful.

2. **Support More Real Brush Stroke**:

   As a drawing program, having only one type of brush stroke (Pencil) seems kind of boring, and the current drawing logic is relatively ugly (just generating a solid color square around the stroke). Under this logic, the ink line often breaks due to the discrete mouse movement events. Perhaps this problem can be solved by directly drawing continuous lines/curves with ``cursorPoint`` and ``lastCursorPoint`` methods/properties of ``Application``. How to map an abstract geometry shape to discrete pixels on the screen is a fundamental problem in CG (Computer Graphics). For readers who are not familiar with related knowledge, it is great to start by learning the basic line generation algorithms (such as the Bresenham algorithm).

3. **Even Create an Adobe Photoshop**:

   The canvas is implemented by an ``Image`` object, and the ``Image`` in D14UIKit supports effective memory mapping and copying between 2U (CPU & GPU). Therefore, we can implement various fantastic digital image processing algorithms, and even create an Adobe Photoshop!
