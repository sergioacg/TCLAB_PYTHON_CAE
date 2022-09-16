# TCLAB_PYTHON_CAE
TCLab_CAE: Temperature Control Laboratory Control Automático Educación
=======================================================================


``TCLab_CAE`` proporciona una interfaz de Python modificada para el `Temperature Control Lab <http://apmonitor.com/pdc/index.php/Main/ArduinoTemperatureControl>`_ implementado en un microcontrolador Arduino a través de una interfaz USB. ``TCLab_CAE`` se implementa como una clase de Python dentro de ``tclab_cae``.  El paquete  ``tclab_cae`` incluye:

* ``clock`` Un generador de Python para la implementación suave en tiempo real de    algoritmos de control de procesos.
* ``Historian`` Una clase de Python para registrar los resultados de un control de proceso experimento.
* ``Plotter`` Proporciona a un historiador trazado en tiempo real dentro de un cuaderno jupyter.
* ``TCLabModel`` Un modelo integrado del laboratorio de control de temperatura para simulación fuera de línea y más rápida que en tiempo real del control de procesos experimentos No es necesario conectar hardware para usar ``TCLabModel``.

El repositorio en PyPi es: <https://pypi.org/project/tclab-cae/>

Cursos de Control en Sistemas Embebidos
--------------------

Si esta interesado en realizar cursos de control sin necesidad de usar Python o Matlab, sino que desea saber como programar los controladores directamente en el microcontrolador Arduino o en un microcontrolador PIC de Microchip empleando el PIC C Compiler, puede acceder a los siguientes cursos con un Cupon de Descuento en el sitio web de **Control Automático Educación**

`Implementación de Controladores en Dispositivos Embebidos usando el TCLAB_CAE <https://controlautomaticoeducacion.com/sistemas-de-control-en-dispositivos-embebidos/>`_ 

Instalación Arduino
--------------------

El arduino debe tener instalado el programa para poder leer los nuevos sensores, cuyo repositorio esta disponible en 
<https://github.com/sergioacg/TCLAB_CAE>

Instalación de la Bilioteca TCLab_CAE
--------------------

La instalación del TCLAB se hace en el terminal usando el manejador de paquetes ``pip`` si tienes Python o usando ``conda`` si tienes anaconda (en el caso de Anaconda abra el programa como administrador en Windows para una correcta instalación de los paquetes):

``pip install tclab-cae``

Si hay problemas con los permisos se puede intentar el comando:

``pip install tclab-cae --user``

Posteriormente, deberemos instalar la biblioteca de comunicación serial pyserial:

``pip install pyserial``
``conda install pyserial``


Configuración de hardware
--------------

1. Conecte un dispositivo Arduino compatible (UNO, Leonardo, MEGA, NHduino) con el TCLab conectado a su computadora a través de la conexión USB y enchufe el adaptador de CC a un toma corriente en la pared.


Comprobando que todo funciona
------------------------------

Ejecuta el siguiente código :

    import tclab_cae.tclab_cae as tclab   
    with tclab.TCLab_CAE() as lab:
        print(lab.T1)

Si todo ha funcionado, debería ver el siguiente mensaje de salida::

    Connecting to TCLab
    TCLab Firmware Version X.X.X on NHduino connected to port XXXX
    XX.XX
    TCLab disconnected successfully.

El número devuelto es la temperatura del sensor T1 en °C.

