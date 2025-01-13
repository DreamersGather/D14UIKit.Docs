.. _d14uikit-tutorials-intermediate-frame_animation:

Frame Animation
===============

.. image:: https://media.githubusercontent.com/media/DreamersGather/D14Docs.Res/main/d14uikit/tutorials/frame_animation.png

.. note::

  The source code of the demo can be found in **d14uikit/demo**.

Do Something Fun
----------------

In the previous section, we introduced OOP-Style GUI building. Let's take a little break, and in this section, we'll do something interesting: implement a pixel-style frame animation "Running Sticky Boy".

Simple Practice
---------------

First, we set an appropriate size for the window. For example, if the frame image is scaled to display at 256x256 dip, the window size can be set to around 300 dip:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      app.setSize({ 300, 336 });

  .. tab:: Python

    .. sourcecode:: python

      app.size = Size(300, 336)

Next, let's do some basic setup:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      MainWindow mwnd(DEMO_NAME);
      mwnd.setMinimizeButton(false);
      mwnd.setMaximizeButton(false);

      Panel clntArea;
      mwnd.setContent(&clntArea);

  .. tab:: Python

    .. sourcecode:: python

      mwnd = MainWindow(DEMO_NAME)
      mwnd.minimizeButton = False
      mwnd.maximizeButton = False

      clntArea = Panel()
      mwnd.content = clntArea

As mentioned in the previous section, any UI object inherits from ``Panel``. D14UIKit provides a ``FrameAnimPanel`` for easily implementing frame animations. It represents a rectangular area on the screen where you can specify a series of frame images to display in a designated manner. We first create the ``FrameAnimPanel`` as follows:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      FrameAnimPanel animArea;
      animArea.setParent(&clntArea);
      animArea.setPosition({ 22, 22 });
      animArea.setSize({ 256, 256 });

  .. tab:: Python

    .. sourcecode:: python

      animArea = FrameAnimPanel()
      animArea.parent = clntArea
      animArea.position = Point(22, 22)
      animArea.size = Size(256, 256)

Next comes the main task: preparing all the frame images. Using C++ might be a bit cumbersome, but using Python's list comprehension is much more concise:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      std::vector<Image*> framePtrs;
      std::vector<std::unique_ptr<Image>> frames;
      for (int i = 0; i < 12; ++i)
      {
          auto frame = std::make_unique<Image>(L"images/stick_boy/" + std::to_wstring(i) + L".png");

          framePtrs.push_back(frame.get());
          frames.push_back(std::move(frame));
      }
      animArea.setFrames(framePtrs);

  .. tab:: Python

    .. sourcecode:: python

      animArea.frames = [Image(f'images/stick_boy/{i}.png') for i in range(12)]

The C++ API of D14UIKit only accepts parameters in the form of ``Object*``, which means that D14UIKit objects do not manage memory for you. Instead, they merely reference the objects as needed. Therefore, we create all ``Image`` objects on the heap and then pass the raw pointers.

.. important::

   Here is an important question:

   Suppose the ``Image`` objects passed to ``setFrames`` are **cleaned up**. Wouldn't the application **crash** when the ``FrameAnimPanel`` **references** the related ``Image`` objects?

   **Actually, it WON'T**, because D14UIKit still has a memory management mechanism for the so-called ``Private`` objects. For example, an ``Image`` object corresponds to an internal ``ImagePrivate`` object, and the actual data is retained by the ``Private`` object. D14UIKit objects merely reference their corresponding ``Private`` objects. Therefore, if an ``Image`` object is cleaned up, you can no longer reference the actual ``Private`` object, but the application itself won't crash. This also decouples the development code from D14UIKit.

   For example, you can try the following C++ code, and the application will still run normally, even if the ``std::vector<Image>`` on the stack has been cleaned up:

   .. sourcecode:: c++

    // other code
    {
        std::vector<Image*> framePtrs;
        std::vector<Image> frames;
        for (int i = 0; i < 12; ++i)
        {
            frames.emplace_back(L"images/stick_boy/" + std::to_wstring(i) + L".png");
            framePtrs.push_back(&frames[i]);
        }
        animArea.setFrames(framePtrs);
    }
    // other code

Next, set the frame interval and image scaling strategy. Since the original frames are pixel art, use Point-Sampler (a.k.a NearestNeighbor-Sampler) to maintain pixel clarity:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      animArea.setFrameInterpMode(BitmapInterpMode::NearestNeighbor);
      animArea.setFrameTimeSpan(0.06f);

  .. tab:: Python

    .. sourcecode:: python

      animArea.frameInterpMode = BitmapInterpMode.NearestNeighbor
      animArea.frameTimeSpan = 0.06

Then, set up the animation to start playing, and D14UIKit will render the frame animation at full speed:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      animArea.setAnimState(true);

  .. tab:: Python

    .. sourcecode:: python

      animArea.animState = True

.. note::

   D14UIKit operates in two modes:

   1. **Passive Mode**: When the animation state is false, similar to common GUI applications, D14UIKit uses a message queue for response and rendering, resulting in lower CPU/GPU usage and minimal power consumption.
   2. **Active Mode**: When the animation state is true, similar to real-time rendering games, D14UIKit continuously outputs refreshed frames through the high-speed graphics pipeline, enabling complex dynamic effects.

Finally, create a label to display the FPS and set up the relevant callback function:

.. tabs::

  .. tab:: C++

    .. sourcecode:: c++

      Label fpsLbl(L"FPS: None");
      fpsLbl.setParent(&clntArea);
      fpsLbl.setPosition({ 22, 22 });

      // This will be called before the renderer drawing each frame.
      fpsLbl.D14_onUpdate(p, &)
      {
          static int fps = 0;
          if (app.fps() != fps)
          {
              fps = app.fps();
              ((Label*)p)->setText(L"FPS: " + std::to_wstring(fps));
          }
      };

  .. tab:: Python

    .. sourcecode:: python

      fpsLbl = Label('FPS: None')
      fpsLbl.parent = clntArea
      fpsLbl.position = Point(22, 22)

      # This will be called before the renderer drawing each frame.
      def displayFPS(p):
          if app.fps != displayFPS.fps:
              displayFPS.fps = app.fps
              p.text = f'FPS: {displayFPS.fps}'

      displayFPS.fps = 0
      fpsLbl.f_onUpdate = displayFPS
