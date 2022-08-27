# TCLAB_PYTHON_CAE
TCLab_CAE: Temperature Control Laboratory Control Automático Educación
=======================================================================


``TCLab_CAE`` proporciona una interfaz de Python modificada para el
`Temperature Control Lab <http://apmonitor.com/pdc/index.php/Main/ArduinoTemperatureControl>`_
implementado en un microcontrolador Arduino a través de una interfaz USB.
``TCLab_CAE`` se implementa como una clase de Python dentro
de ``tclab_cae``.  El paquete  ``tclab_cae`` incluye:

* ``clock`` Un generador de Python para la implementación suave en tiempo real de
   algoritmos de control de procesos.
* ``Historian`` Una clase de Python para registrar los resultados de un control de proceso
   experimento.
* ``Plotter`` Proporciona a un historiador trazado en tiempo real dentro de un
   cuaderno jupyter.
* ``TCLabModel`` Un modelo integrado del laboratorio de control de temperatura
   para simulación fuera de línea y más rápida que en tiempo real del control de procesos
   experimentos No es necesario conectar hardware para usar ``TCLabModel``.

The companion Arduino firmware for device operation is available at the
`TCLab-Sketch repository <https://github.com/jckantor/TCLab-sketch>`_.


Instalación Arduino
--------------------

El arduino debe tener instalado el programa para poder leer los nuevos sensores, cuyo repositorio esta disponible en 
<https://github.com/sergioacg/TCLAB_CAE>


Configuración de hardware
--------------

1. Conecte un dispositivo Arduino compatible (UNO, Leonardo, NHduino) con el
    lab conectado a su computadora a través de la conexión USB. Enchufe la CC
    adaptador de corriente en la pared.



Comprobando que todo funciona
------------------------------

Ejecuta el siguiente código ::

    import tclab
    with tclab.TCLab() as lab:
        print(lab.T1)

Si todo ha funcionado, debería ver el siguiente mensaje de salida::

    Connecting to TCLab
    TCLab Firmware Version 1.2.1 on NHduino connected to port XXXX
    21.54
    TCLab disconnected successfully.

El número devuelto es la temperatura del sensor T1 en °C.


Solución de problemas
---------------

Si algo salió mal en el proceso anterior, consulte nuestra guía de solución de problemas
en SOLUCIÓN DE PROBLEMAS.md.

Próximos pasos
----------

El directorio del cuaderno proporciona ejemplos sobre cómo usar el módulo TCLab.
La documentación más reciente está disponible en
`Lea los documentos <http://tclab.readthedocs.io/en/latest/index.html>`_.
