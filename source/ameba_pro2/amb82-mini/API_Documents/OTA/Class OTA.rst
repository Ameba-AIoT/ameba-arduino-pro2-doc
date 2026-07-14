Class OTA
==========

**OTA Class**
-------------

**Description**
~~~~~~~~~~~~~~~

A class used for updating firmware Over the Air (OTA) in local area network.
Supports both HTTP and HTTPS firmware updates.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  class OTA

**Members**
~~~~~~~~~~~

+----------------------------------------------+--------------------------------------------+
| **Public Constructors**                                                                   |
+==============================================+============================================+
| A public constructor should not be used as this class is intended to be a singleton class.|
| Access member functions using the object instance named OTA.                              |
+----------------------------------------------+--------------------------------------------+
| **Public Methods**                                                                        |
+----------------------------------------------+--------------------------------------------+
| OTA::start_OTA_threads                       | To begin threading tasks for OTA           |
|                                              | firmware update. Supports both HTTP and    |
|                                              | HTTPS.                                     |
+----------------------------------------------+--------------------------------------------+

**OTA::start_OTA_threads**
--------------------------

**Description**
~~~~~~~~~~~~~~~

To begin threading tasks for OTA firmware update. Supports both HTTP and
HTTPS connections.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  // HTTP mode (plain TCP, no encryption)
  void start_OTA_threads(int port, char* server);
  void start_OTA_threads(int port, char* server, WiFiClass &ota_wifi);

  // HTTPS mode (TLS encrypted)
  void start_OTA_threads(int port, char* server, bool useSSL);
  void start_OTA_threads(int port, char* server, WiFiClass &ota_wifi, bool useSSL);

**Parameters**
~~~~~~~~~~~~~~

port: port number for the OTA server (e.g., 3000 for HTTP, 443 for HTTPS)

\*server: pointer for OTA server IP address

useSSL: set to ``true`` to enable TLS/SSL (HTTPS), ``false`` for plain HTTP

ota_wifi: reference to a ``WiFiClass`` instance (optional; defaults to ``WiFi``)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `OTA <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/OTA/examples/OTA/OTA.ino>`_

.. code-block:: c++

   // HTTP
   ota.start_OTA_threads(3000, "192.168.1.100");

   // HTTPS
   ota.start_OTA_threads(443, "192.168.1.100", true);

.. note :: "OTA.h" must be included to use the function. When using HTTPS,
           ensure the server has a valid certificate (run ``setup-https.sh``
           in the ameba-OTA-UI directory).
