Class VideoStream
=================

.. contents::
  :local:
  :depth: 2

**CameraSetting Class**
-----------------------

**Description**
~~~~~~~~~~~~~~~

A class used to configure parameters for the camera sensor.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class CameraSetting

**Members**
~~~~~~~~~~~

+---------------------------------+----------------------------------------+
| **Public Constructors**                                                  |
+=================================+========================================+
| CameraSetting::CameraSetting    | Constructs a CameraSetting object and  |
|                                 | set the parameters needed for camera   |
|                                 | sensor.                                |
+---------------------------------+----------------------------------------+
| **Public Methods**                                                       |
+---------------------------------+----------------------------------------+
| CameraSetting::setBrightness    | Set the brightness value of the image. |
+---------------------------------+----------------------------------------+
| CameraSetting::getBrightness    | Get the current brightness value.      |
+---------------------------------+----------------------------------------+
| CameraSetting::setContrast      | Set the contrast value of the image.   |
+---------------------------------+----------------------------------------+
| CameraSetting::getContrast      | Get the current contrast value.        |
+---------------------------------+----------------------------------------+
| CameraSetting::setSaturation    | Set the saturation value of the image. |
+---------------------------------+----------------------------------------+
| CameraSetting::getSaturation    | Get the current saturation value.      |
+---------------------------------+----------------------------------------+
| CameraSetting::setSharpness     | Set the sharpness value of the image.  |
+---------------------------------+----------------------------------------+
| CameraSetting::getSharpness     | Get the current sharpness value.       |
+---------------------------------+----------------------------------------+
| CameraSetting::setLDC           | Enable or Disable Lens Distortion      |
|                                 | Correction (LDC).                      |
+---------------------------------+----------------------------------------+
| CameraSetting::getLDC           | Get the current LDC value.             |
+---------------------------------+----------------------------------------+
| CameraSetting::setWDR           | Enable or Disable WDR mode.            |
+---------------------------------+----------------------------------------+
| CameraSetting::getWDR           | Get current WDR mode.                  |
+---------------------------------+----------------------------------------+
| CameraSetting::setWDRLevel      | Set WDR level.                         |
+---------------------------------+----------------------------------------+
| CameraSetting::getWDRLevel      | Get current WDR level.                 |
+---------------------------------+----------------------------------------+
| CameraSetting::setExposureMode  | Set Exposure mode in Auto or Manual    |
|                                 | mode.                                  |
+---------------------------------+----------------------------------------+
| CameraSetting::getExposureMode  | Get current exposure mode.             |
+---------------------------------+----------------------------------------+
| CameraSetting::setExposureTime  | Set exposure time.                     |
+---------------------------------+----------------------------------------+
| CameraSetting::getExposureTime  | Get current exposure time.             |
+---------------------------------+----------------------------------------+
| CameraSetting::setAEGain        | Set exposure gain value.               |
+---------------------------------+----------------------------------------+
| CameraSetting::getAEGain        | Get current exposure gain value.       |
+---------------------------------+----------------------------------------+
| CameraSetting::setPowerLineFreq | Enable or Disable Power Line Frequency |
|                                 | (Anti-flicker mode).                   |
+---------------------------------+----------------------------------------+
| CameraSetting::getPowerLineFreq | Get current Power Line Frequency.      |
+---------------------------------+----------------------------------------+
| CameraSetting::setAWB           | Set White Balance mode in Auto or      |
|                                 | Manual mode.                           |
+---------------------------------+----------------------------------------+
| CameraSetting::getAWB           | Get current White Balance mode.        |
+---------------------------------+----------------------------------------+
| CameraSetting::getWBTemp        | Get current White Balance Temperature. |
+---------------------------------+----------------------------------------+
| CameraSetting::setRedBalance    | Set red balance value.                 |
+---------------------------------+----------------------------------------+
| CameraSetting::getRedBalance    | Get red balance value.                 |
+---------------------------------+----------------------------------------+
| CameraSetting::setBlueBalance   | Set blue balance value.                |
+---------------------------------+----------------------------------------+
| CameraSetting::getBlueBalance   | Get blue balance value.                |
+---------------------------------+----------------------------------------+
| CameraSetting::setGrayMode      | Set Gray mode.                         |
+---------------------------------+----------------------------------------+
| CameraSetting::getGrayMode      | Get current mode, gray or color.       |
+---------------------------------+----------------------------------------+
| CameraSetting::setDayNightMode  | Set Day or Night mode.                 |
+---------------------------------+----------------------------------------+
| CameraSetting::getDayNightMode  | Get current mode, day, or night.       |
+---------------------------------+----------------------------------------+
| CameraSetting::reset            | Reset all the values to default value. |
+---------------------------------+----------------------------------------+

**CameraSetting::setBrightness**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Set the brightness value of the image.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setBrightness (int value);

**Parameters**
~~~~~~~~~~~~~~

value: Preferred brightness value.

- -64 to 64 (Default value is 0)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/ImageTuning <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::getBrightness**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the current brightness value.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setBrightness (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/ImageTuning <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::setContrast**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Set the contrast value of the image.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setContrast (int value);

**Parameters**
~~~~~~~~~~~~~~

value: Preferred contrast value.

- 0 to 100 (Default value is 50)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/ImageTuning <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::getContrast**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the current contrast value.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void getContrast (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/ImageTuning <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::setSaturation**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Set the saturation value of the image.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setSaturation (int value);

**Parameters**
~~~~~~~~~~~~~~

value: Preferred saturation value.

- 0 to 100 (Default value is 50)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/ImageTuning <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::getSaturation**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the current saturation value.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void getSaturation (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/ImageTuning <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::setSharpness**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Set the sharpness value of the image.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setSharpness (int value);

**Parameters**
~~~~~~~~~~~~~~

value: Preferred sharpness value.

- 0 to 100 (Default value is 50)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/ImageTuning <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::getSharpness**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the current sharpness value.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void getSharpness (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/ImageTuning <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::setLDC**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Enable or Disable Lens Distortion Correction (LDC).

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setLDC (int enable);

**Parameters**
~~~~~~~~~~~~~~

enable: Enable or Disable LDC.

- 0 (Disabled. Default value)

- 1 (Enabled)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/ImageTuning <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::getLDC**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Get the current LDC value.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void getLDC (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/ImageTuning <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::setWDR**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Enable or Disable WDR mode.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setWDR (int enable);

**Parameters**
~~~~~~~~~~~~~~

enable: Preferred WDR mode. If WDR mode is enabled, Manual or Auto mode can be chosen. 

- 0 (Disabled. Default value)

- 1 (Manual)

- 2 (Auto)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/WideDynamicRange <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WideDynamicRange/WideDynamicRange.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::getWDR**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Get current WDR mode.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void getWDR (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/WideDynamicRange <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WideDynamicRange/WideDynamicRange.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::setWDRLevel**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Set WDR level.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setWDRLevel (int value);

**Parameters**
~~~~~~~~~~~~~~

value: Preferred WDR level.

- 50 - 100 (Default value is 50)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/WideDynamicRange <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WideDynamicRange/WideDynamicRange.ino>`_

.. note :: "VideoStream.h" must be included to use the class function. WDR level can only be modified, and changes can be seen on image if WDR mode is set to manual mode before calling setWDRLevel() function.

**CameraSetting::getWDRLevel**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Get current WDR level.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void getWDRLevel (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/WideDynamicRange <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WideDynamicRange/WideDynamicRange.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::setExposureMode**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Set Exposure mode in Auto or Manual mode.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setExposureMode (int enable);

**Parameters**
~~~~~~~~~~~~~~

enable: Enable exposure mode in Manual or Auto mode.

- 0 (Manual)

- 1 (Auto. Default value)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/Exposure <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Exposure/Exposure.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::getExposureMode**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Get current exposure mode.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void getExposureMode (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/Exposure <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Exposure/Exposure.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::setExposureTime**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Set exposure time.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setExposureTime (int time);

**Parameters**
~~~~~~~~~~~~~~

time: Preferred exposure time in us.

- time <= 33333

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/Exposure <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Exposure/Exposure.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::getExposureTime**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Get current exposure time.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void getExposureTime (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/Exposure <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Exposure/Exposure.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::setAEGain**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Set exposure gain value.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setAEGain (int value);

**Parameters**
~~~~~~~~~~~~~~

value: Preferred exposure gain.

- 256 to 32768

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/Exposure <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Exposure/Exposure.ino>`_

.. note :: "VideoStream.h" must be included to use the class function. AE gain can only be modified, and changes can be seen on image if Exposure mode is set to manual mode before calling setAEGain() function.

**CameraSetting::getAEGain**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Get current exposure gain value.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void getAEGain (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/Exposure <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Exposure/Exposure.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::setPowerLineFreq**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Enable or Disable Power Line Frequency (Anti-flicker mode).

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setPowerLineFreq (int enable);

**Parameters**
~~~~~~~~~~~~~~

enable: Enable or disable power line frequency. If power line frequency is enabled, power line frequency can be set as auto or choose from different frequencies (50Hz, 60Hz).

- 0 (Disable)

- 1 (50Hz)

- 2 (60Hz)

- 3 (Auto. Default value)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/Exposure <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Exposure/Exposure.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::getPowerLineFreq**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Get current Power Line Frequency.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void getPowerLineFreq (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/Exposure <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Exposure/Exposure.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::setAWB**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Set White Balance mode in Auto or Manual mode.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setAWB (int enable);

**Parameters**
~~~~~~~~~~~~~~

enable: Enable white balance mode in Manual or Auto mode.

- 0 (Manual Temperature)

- 1 (Auto. Default value)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/WhiteBalance <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WhiteBalance/WhiteBalance.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::getAWB**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Get current White Balance mode.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void getAWB (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/WhiteBalance <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WhiteBalance/WhiteBalance.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::getWBTemp**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Get current White Balance Temperature.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void getWBTemp (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/WhiteBalance <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WhiteBalance/WhiteBalance.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::setRedBalance**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Set red balance value.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setRedBalance (int value);

**Parameters**
~~~~~~~~~~~~~~

value: Preferred red balance value based on 256.

- 256 to 2047

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/WhiteBalance <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WhiteBalance/WhiteBalance.ino>`_

.. note :: "VideoStream.h" must be included to use the class function. Red Balance value can only be modified, and changes can be seen on image if white balance mode is set to manual mode before calling setRedBalance() function.

**CameraSetting::getRedBalance**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Get current red balance value.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void getRedBalance (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/WhiteBalance <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WhiteBalance/WhiteBalance.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::setBlueBalance**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Set blue balance value.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setBlueBalance (int value);

**Parameters**
~~~~~~~~~~~~~~

value: Preferred blue balance value based on 256.

- 256 to 2047

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/WhiteBalance <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WhiteBalance/WhiteBalance.ino>`_

.. note :: "VideoStream.h" must be included to use the class function. Blue Balance value can only be modified, and changes can be seen on image if white balance mode is set to manual mode before calling setBlueBalance() function.

**CameraSetting::getBlueBalance**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Get current blue balance value.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void getBlueBalance (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/WhiteBalance <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WhiteBalance/WhiteBalance.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::setGrayMode**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Set Gray mode.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setGrayMode (int enable);

**Parameters**
~~~~~~~~~~~~~~

enable: Enable gray mode.

- 0 (Color mode. Default value)

- 1 (Gray mode)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/Mode <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Mode/Mode.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::getGrayMode**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Get current mode, gray or color.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void getGrayMode (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/Mode <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Mode/Mode.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::setDayNightMode**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Set Day or Night mode.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setDayNightMode (int enable);

**Parameters**
~~~~~~~~~~~~~~

enable: Enable day or night mode.

- 0 (Day mode. Default value)

- 1 (Night mode)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/Mode <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Mode/Mode.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::getDayNightMode**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Get current mode, day or night.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void getDayNightMode (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/Mode <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Mode/Mode.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**CameraSetting::reset**
------------------------

**Description**
~~~~~~~~~~~~~~~

Reset all the values to default value.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void reset (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ISPControl/Mode <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Mode/Mode.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**VideoSetting Class**
----------------------

**Description**
~~~~~~~~~~~~~~~

A class used to configure parameters for video streams.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class VideoSetting

**Members**
~~~~~~~~~~~

+------------------------------+-----------------------------------------+
| **Public Constructors**                                                |
+------------------------------+-----------------------------------------+
| VideoSetting::VideoSetting   | Constructs a VideoSetting object and    |
|                              | set the parameters needed for video     |
|                              | streams.                                |
+------------------------------+-----------------------------------------+
| **Public Methods**                                                     |
+------------------------------+-----------------------------------------+
| VideoSetting::setBitrate     | Configure bitrate for H264 and H265     |
|                              | video encoder.                          |
+------------------------------+-----------------------------------------+
| VideoSetting::setJpegQuality | Configure quality level for JPEG        |
|                              | snapshots.                              |
+------------------------------+-----------------------------------------+
| VideoSetting::setRotation    | Configure orientation for H264, H265    |
|                              | video and JPEG encoders.                |
+------------------------------+-----------------------------------------+
| VideoSetting::width          | Get current configured video stream     |
|                              | width.                                  |
+------------------------------+-----------------------------------------+
| VideoSetting::height         | Get current configured video stream     |
|                              | height.                                 |
+------------------------------+-----------------------------------------+
| VideoSetting::fps            | Get current configured video stream fps |
|                              | (frame per second).                     |
+------------------------------+-----------------------------------------+

**VideoSetting::VideoSetting**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a VideoSetting object and sets the parameters needed for video streams, such as resolution, frame rate per second (fps), bit rate per second (bps), encoder type.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    VideoSetting(uint8_t preset);
    VideoSetting(uint8_t resolution, uint8_t fps, uint8_t encoder, uint8_t snapshot);
    VideoSetting(uint16_t w, uint16_t h, uint8_t fps, uint8_t encoder, uint8_t snapshot);

**Parameters**
~~~~~~~~~~~~~~

preset: Select one out of 3 preset video stream settings.

- 0 (Default value)

- 1

- 2

resolution: Video resolution.

- VIDEO_HD

- VIDEO_FHD

fps: Frame rate in frames per second.

encoder: Video encoder format to use.

- VIDEO_HEVC

- VIDEO_H264

- VIDEO_JPEG

snapshot: Enable or disable snapshot function.

w: Width in pixels.

h: Height in pixels.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `StreamRTSP/VideoOnly <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/VideoOnly/VideoOnly.ino>`_

.. note ::

    "VideoStream.h" must be included to use the class function.

    Preset configurations:

    **Preset 0:**
    resolution: VIDEO_FHD
    fps: 30
    bps: 2 * 1024 * 1024
    encoder: VIDEO_H264
    snapshot: 0

    **Preset 1:**
    resolution: VIDEO_HD
    fps: 30
    bps: 2 * 1024 * 1024
    encoder: VIDEO_H264
    snapshot: 0

    **Preset 2:**
    resolution: VIDEO_FHD
    fps: 30
    bps: 2 * 1024 * 1024
    encoder: VIDEO_JPEG
    snapshot: 0

**VideoSetting::setBitrate**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Configure bitrate for H264 and H265 video encoder.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setBitrate(uint32_t bitrate);

**Parameters**
~~~~~~~~~~~~~~

bitrate: desired video encoder bitrate. Values range from 1Mbps (1024 * 1024) to 50Mbps (50 * 1024 * 1024).

- 1 to 50 (Default value is 4Mbps)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `StreamRTSP/VideoOnly <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/VideoOnly/VideoOnly.ino>`_

.. note :: "VideoStream.h" must be included to use the class function. The default value of 4Mbps is a suitable balance of video quality and file size. For RTSP streaming, it is recommended that the bitrate is lowered to 2Mbps to account for possible network congestion.

**VideoSetting::setJpegQuality**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Configure quality level for JPEG snapshots.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setJpegQuality(uint8_t quality);

**Parameters**
~~~~~~~~~~~~~~

quality: desired JPEG image quality level. 

- 1 to 9 (Worst to best. Default value is 5)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "VideoStream.h" must be included to use the class function. A lower quality results in a reduced file size, while a quality level of 9 may result in large file sizes without a significant improvements in image quality.

**VideoSetting::setRotation**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Configure orientation for H264, H265 video and JPEG encoders.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setRotation(int angle);

**Parameters**
~~~~~~~~~~~~~~

angle: desired rotation angle represented by numerical values.

- 0 (No rotation. Default value)

- 1 (90 degree to right)

- 2 (90 degree to left)

- 3 (180 degree)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "VideoStream.h" must be included to use the class function.

**VideoSetting::width**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Get current configured video stream width.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint16_t width(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the current configured video stream width.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MotionDetection/LoopPostProcessing <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**VideoSetting::height**
------------------------

**Description**
~~~~~~~~~~~~~~~

Get current configured video stream height.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint16_t height(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the current configured video stream height.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MotionDetection/LoopPostProcessing <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**VideoSetting::fps**
---------------------

**Description**
~~~~~~~~~~~~~~~

Get current configured video stream fps (frame per second).

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint16_t fps(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the current configured video stream fps.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "VideoStream.h" must be included to use the class function.

**Video Class**
---------------

**Description**
~~~~~~~~~~~~~~~

A class used to configure and initialize the camera to generate video data streams.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class Video

**Members**
~~~~~~~~~~~

+----------------------------+-----------------------------------------+
| **Public Constructors**                                              |
+----------------------------+-----------------------------------------+
| Video::Video               | Construct a Video object.               |
+----------------------------+-----------------------------------------+
| **Public Methods**                                                   |
+----------------------------+-----------------------------------------+
| Video::configVideoChannel  | Configure video stream channel.         |
+----------------------------+-----------------------------------------+
| Video::camInit             | Initialization of camera sensor using   |
|                            | existing configurations.                |
+----------------------------+-----------------------------------------+
| Video::camDeinit           | Deinitialization of camera sensor       |
+----------------------------+-----------------------------------------+
| Video::videoInit           | Initialization of video streams using   |
|                            | existing configurations.                |
+----------------------------+-----------------------------------------+
| Video::videoDeinit         | Deinitialization of video stream module |
|                            | for a specific channel.                 |
+----------------------------+-----------------------------------------+
| Video::channelBegin        | Start video streaming on a specific     |
|                            | channel.                                |
+----------------------------+-----------------------------------------+
| Video::channelEnd          | Stop video streaming on a specific      |
|                            | channel.                                |
+----------------------------+-----------------------------------------+
| Video::getStream           | Get video data stream to provide as an  |
|                            | input for other data stream consumers.  |
+----------------------------+-----------------------------------------+
| Video::getImage            | Enable snapshot function.               |
+----------------------------+-----------------------------------------+
| Video::setFPS              | Set camera video max FPS.               |
+----------------------------+-----------------------------------------+
| Video::printInfo           | Print out current configuration of      |
|                            | video channels.                         |
+----------------------------+-----------------------------------------+
| Video::videostream_status  | Retrieve video stream module contents   |
|                            | from specific channel and pass for      |
|                            | checking on UVC connection status.      |
+----------------------------+-----------------------------------------+

**Video::configVideoChannel**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Configure video stream channel parameters using VideoSetting class object.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void configVideoChannel(int ch, VideoSetting& config);

**Parameters**
~~~~~~~~~~~~~~

ch: Channel to configure.

- 0

- 1

- 2

config: VideoSetting object.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `StreamRTSP/VideoOnly <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/VideoOnly/VideoOnly.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**Video::camInit**
------------------

**Description**
~~~~~~~~~~~~~~~

Initialize camera sensor using configuration from CameraSetting object.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void cameraInit(CameraSetting& config);

**Parameters**
~~~~~~~~~~~~~~

config: CameraSetting object.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "VideoStream.h" must be included to use the class function.

**Video::camDeinit**
--------------------

**Description**
~~~~~~~~~~~~~~~

Deinitialize camera sensor.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void cameraDeinit(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "VideoStream.h" must be included to use the class function.

**Video::videoInit**
--------------------

**Description**
~~~~~~~~~~~~~~~

Initialization of video streams from camera using existing configurations.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void videoInit(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `StreamRTSP/VideoOnly <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/VideoOnly/VideoOnly.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**Video::videoDeinit**
----------------------

**Description**
~~~~~~~~~~~~~~~

Deinitialization of all video streams.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void videoDeinit(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "VideoStream.h" must be included to use the class function.

**Video::channelBegin**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Start video streaming on a specific channel.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void channelBegin(int ch);

**Parameters**
~~~~~~~~~~~~~~

ch: channel to start streaming. Default channel is 0.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `StreamRTSP/VideoOnly <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/VideoOnly/VideoOnly.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**Video::channelEnd**
---------------------

**Description**
~~~~~~~~~~~~~~~

Stop video streaming on a specific channel.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void channelEnd(int ch);

**Parameters**
~~~~~~~~~~~~~~

ch: channel to stop streaming. Default channel is 0.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "VideoStream.h" must be included to use the class function.

**Video::getStream**
--------------------

**Description**
~~~~~~~~~~~~~~~

Get video data stream to provide as an input for other data stream consumers.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    MMFModule getStream(int ch);

**Parameters**
~~~~~~~~~~~~~~

ch: channel to get data stream of. Default channel is 0.

**Returns**
~~~~~~~~~~~

This function returns the video data stream.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `StreamRTSP/VideoOnly <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/VideoOnly/VideoOnly.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**Video::getImage**
-------------------

**Description**
~~~~~~~~~~~~~~~

Take a snapshot.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void getImage(int ch, uint32_t* addr, uint32_t* len);

**Parameters**
~~~~~~~~~~~~~~

ch: Video stream channel to take a snapshot from.

addr: A pointer to a 32-bit unsigned integer to store the image address.

len: A pointer to a 32-bit unsigned integer to store the image length.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `CaptureJPEG/HTTPDisplayJPEG <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/CaptureJPEG/HTTPDisplayJPEG/HTTPDisplayJPEG.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**Video::setFPS**
-----------------

**Description**
~~~~~~~~~~~~~~~

Set camera video max FPS.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setFPS(int fps);

**Parameters**
~~~~~~~~~~~~~~

fps: max frame rate in frames per second for camera.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "VideoStream.h" must be included to use the class function.

**Video::printInfo**
--------------------

**Description**
~~~~~~~~~~~~~~~

Print out current configuration of video channels.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void printInfo(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `StreamRTSP/VideoOnly <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/VideoOnly/VideoOnly.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.

**Video::videostream_status**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Retrieve video stream module contents from specific channel and pass for checking on UVC connection status.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int videostream_status(int ch);

**Parameters**
~~~~~~~~~~~~~~

ch: Channel to configure.

- 0    

**Returns**
~~~~~~~~~~~

This function returns 1 if the UVC device is connected to PC, 0 otherwise.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `UVCDObjectDetectionLoop <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/UVCDObjectDetectionLoop/UVCDObjectDetectionLoop.ino>`_

.. note :: "VideoStream.h" must be included to use the class function.
