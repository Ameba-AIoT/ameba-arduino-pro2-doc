Class UVCD
==========

.. contents::
  :local:
  :depth: 2

**UVCD Class**
--------------

**Description**
~~~~~~~~~~~~~~~

A class for USB UVC device API.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class UVCD

**Members**
~~~~~~~~~~~

+-----------------------------------+----------------------------------+
| **Public Constructors**                                              |
+===================================+==================================+
| UVCD::UVCD                        | Constructs a UVCD object.        |
|                                   | Initialize/Re-initialize of      |
|                                   | using USB UVC device.            |
+-----------------------------------+----------------------------------+
| **Public Methods**                                                   |
+-----------------------------------+----------------------------------+
| UVCD::isUsbUvcConnected           | Check if the UVC device          |
|                                   | is connected to PC and           |
|                                   | video stream.                    |
+-----------------------------------+----------------------------------+
| UVCD::configVideo                 | Start config video of using USB  |
|                                   | UVC device.                      |
+-----------------------------------+----------------------------------+
| UVCD::nnbegin                     | Begin video streaming of using   |
|                                   | USB UVC device for object        |
|                                   | detection.                       |
+-----------------------------------+----------------------------------+
| UVCD::begin                       | Begin video streaming of using   |
|                                   | USB UVC device.                  |
+-----------------------------------+----------------------------------+

**UVCD::UVCD**
--------------

**Description**
~~~~~~~~~~~~~~~

Constructs a UVCD object. Initialize/Re-initialize of using USB UVC device.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    UVCD(void);
    UVCD(const char *usb_uvcd_driver_name);

**Parameters**
~~~~~~~~~~~~~~

usb_uvcd_driver_name: A string of user defined USB UVC device driver name.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `UVC_Device <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/USB/examples/UVC_Device/UVC_Device.ino>`_

.. note :: "UVCD.h", "StreamIO.h" and "VideoStream.h" must be included to use the class function.

**UVCD::isUsbUvcConnected**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Check if the UVC device is connected to PC or video stream.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int isUsbUvcConnected(int uvcd_getctx_state);

**Parameters**
~~~~~~~~~~~~~~

uvcd_getctx_state: A return integer value of 1 if the UVC device is connected to PC, 0 otherwise.

**Returns**
~~~~~~~~~~~

This function returns 1 if the video stream module is initialized and UVC device is connected to PC, 0 otherwise.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `UVCDObjectDetectionLoop <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/UVCDObjectDetectionLoop/UVCDObjectDetectionLoop.ino>`_

.. note :: "UVCD.h" and "VideoStream.h" must be included to use the class function.

**UVCD::configVideo**
---------------------

**Description**
~~~~~~~~~~~~~~~

Start config video of using USB UVC device.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void configVideo(VideoSetting &config);

**Parameters**
~~~~~~~~~~~~~~

config: pointer of VideoSetting

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `UVC_Device <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/USB/examples/UVC_Device/UVC_Device.ino>`_

.. note :: "UVCD.h", "StreamIO.h" and "VideoStream.h" must be included to use the class function.

**UVCD::nnbegin**
-----------------

**Description**
~~~~~~~~~~~~~~~

Begin video streaming of using USB UVC device for object detection.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void nnbegin(const MMFModule &module_videocam, void *module_videolinker, int uvcd_channel, int nn_channel, int uvcd_getctx_check);

**Parameters**
~~~~~~~~~~~~~~

module_videocam: stream data from camera video.

module_videolinker: StreamIO object for uvcd.

uvcd_channel: video channel.

nn_channel: neural network channel.

uvcd_getctx_check: A return integer value of 1 if the UVC device is connected to PC, 0 otherwise.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `UVCDObjectDetectionLoop <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/UVCDObjectDetectionLoop/UVCDObjectDetectionLoop.ino>`_

.. note :: "UVCD.h", "StreamIO.h" and "VideoStream.h" must be included to use the class function.

**UVCD::begin**
---------------

**Description**
~~~~~~~~~~~~~~~

Begin video streaming of using USB UVC device.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void begin(const MMFModule &module_videocam, void *module_videolinker, int uvcd_channel);

**Parameters**
~~~~~~~~~~~~~~

module_videocam: stream data from camera video.

module_videolinker: StreamIO object for uvcd.

uvcd_channel: video channel.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `UVC_Device <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/USB/examples/UVC_Device/UVC_Device.ino>`_

.. note :: "UVCD.h", "StreamIO.h" and "VideoStream.h" must be included to use the class function.
