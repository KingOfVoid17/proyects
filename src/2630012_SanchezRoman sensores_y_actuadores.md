# Sensores y actuadores en sistemas mecatrónicos

**Matrícula:** 2630012  
**Nombre:** Sanchez Roman  
**Archivo:** `2630012_SanchezRoman.md`

---

## 1. Conceptos básicos

### ¿Qué es un sensor?

Un sensor es un dispositivo que detecta una característica física de su entorno y la convierte en una señal que un sistema electrónico puede interpretar. La característica puede ser temperatura, luz, distancia, presión, posición, velocidad, humedad o fuerza.

Por ejemplo, un sensor de temperatura no "entiende" que una habitación está caliente como lo haría una persona. Detecta una propiedad física relacionada con la temperatura y entrega una señal que el controlador puede convertir en un valor.

### ¿Qué es un actuador?

Un actuador es un dispositivo que recibe una orden y produce una acción física. Puede transformar energía eléctrica, neumática o hidráulica en movimiento, fuerza, desplazamiento, giro u otra acción.

Un motor eléctrico es un ejemplo sencillo: recibe energía eléctrica y produce movimiento rotatorio.

### Diferencia entre sensor y actuador

La diferencia principal está en la dirección de la información:

| Elemento | Función principal |
|---|---|
| Sensor | Obtiene información del entorno o del propio sistema. |
| Actuador | Ejecuta una acción física ordenada por el sistema de control. |

De manera sencilla:

**Sensor → información → controlador → orden → actuador → acción física**

### Función dentro de un sistema mecatrónico

Un sistema mecatrónico combina elementos mecánicos, electrónicos y de control. Los sensores permiten conocer qué está ocurriendo, mientras que los actuadores permiten modificar lo que está ocurriendo.

Por ejemplo, en una puerta automática:

- El **sensor** detecta que una persona se encuentra frente a la puerta.
- El **controlador** procesa esa información.
- El **actuador** mueve la puerta.
- Otro sensor puede comprobar si la puerta llegó a determinada posición.

La comunicación entre sensores, actuadores y sistemas de automatización es fundamental en sistemas industriales; tecnologías como IO-Link están diseñadas precisamente para conectar sensores y actuadores con los sistemas de control. [1]

### Ejemplo sencillo: aire acondicionado

Un aire acondicionado es un buen ejemplo de sistema mecatrónico.

```text
             ┌──────────────────┐
             │ Sensor de        │
             │ temperatura      │
             └────────┬─────────┘
                      │ temperatura medida
                      ▼
             ┌──────────────────┐
             │ Controlador      │
             │ electrónico      │
             └────────┬─────────┘
                      │ orden
                      ▼
             ┌──────────────────┐
             │ Actuador /       │
             │ motor del ventil.│
             └────────┬─────────┘
                      │
                      ▼
                Movimiento de
                  aire frío
```

El sensor detecta la temperatura del ambiente. El controlador compara esa temperatura con el valor deseado y, según el diseño del equipo, controla actuadores como el motor del ventilador, compresor o elementos de regulación.

---

# 2. Investigación de sensores

## Tabla comparativa de sensores

| Tipo de sensor | Variable que mide | Principio de funcionamiento | Ejemplo comercial o real | Aplicación |
|---|---|---|---|---|
| Temperatura | Temperatura | Cambia una propiedad eléctrica, como resistencia o tensión, en relación con la temperatura. | TI TMP235 / sensores de temperatura TI | Protección térmica y control HVAC |
| Luz | Intensidad de luz | Un elemento fotosensible cambia su corriente o resistencia cuando recibe luz. | Fotodiodo, LDR o sensor fotoeléctrico OMRON | Encendido automático de iluminación |
| Proximidad | Presencia o cercanía de un objeto | Detecta cambios producidos por un objeto sin necesidad de tocarlo; puede utilizar campos electromagnéticos o luz. | Sensor inductivo Balluff | Detección de piezas metálicas |
| Distancia | Distancia entre el sensor y un objeto | Emite una señal y determina la distancia a partir de su reflexión o tiempo de propagación. | Sensor ultrasónico | Evitación de obstáculos en robots |
| Presión | Presión de un gas o líquido | Una membrana o elemento sensible se deforma y esa deformación se transforma en señal eléctrica. | Sensor/transductor de presión industrial | Sistemas hidráulicos y neumáticos |
| Humedad | Humedad relativa del aire | Un material sensible cambia una propiedad eléctrica al absorber humedad. | Sensor de humedad digital | Control ambiental |
| Posición | Posición lineal o angular | Detecta la posición mediante un cambio magnético, inductivo, resistivo u óptico. | Balluff BIP002L | Control de posición de maquinaria |
| Velocidad o movimiento | Velocidad, giro o aceleración | Detecta cambios de posición en el tiempo, pulsos, campos magnéticos o aceleración. | Encoder rotatorio | Control de velocidad de motores |
| Fuerza o peso | Fuerza o carga | Una celda de carga se deforma ligeramente y cambia la señal de sus elementos extensométricos. | Celda de carga | Básculas y control de peso |

### 2.1 Sensor de temperatura

**Variable:** temperatura.

**Principio:** dependiendo de la tecnología, la temperatura modifica la resistencia de un termistor, la tensión de salida de un circuito integrado o la señal producida por otros elementos como RTD y termopares. Los sensores integrados pueden tener salida analógica o interfaces digitales como I2C, SPI o UART. [2]

**Ejemplo:** TI TMP235, un sensor integrado de temperatura con salida analógica.

**Aplicación:** protección térmica de circuitos, sistemas HVAC, automóviles y equipos industriales.

### 2.2 Sensor de luz

**Variable:** cantidad o intensidad de luz.

**Principio:** un dispositivo fotosensible transforma la radiación luminosa en una variación eléctrica. En una LDR cambia la resistencia; en un fotodiodo cambia principalmente la corriente.

**Ejemplo:** fotodiodo o sensor fotoeléctrico industrial OMRON.

**Aplicación:** iluminación automática, detección de objetos y sistemas de conteo.

### 2.3 Sensor de proximidad

**Variable:** presencia o proximidad de un objeto.

**Principio:** el sensor genera un campo o utiliza una señal que cambia cuando un objeto entra en su zona de detección. En un sensor inductivo, por ejemplo, la presencia de un objeto metálico altera el campo electromagnético.

**Ejemplo:** sensores inductivos Balluff.

**Aplicación:** detectar que una pieza metálica llegó a una estación de una máquina.

Balluff ofrece sensores inductivos con salidas digitales, analógicas e interfaces como IO-Link, dependiendo del modelo. [3]

### 2.4 Sensor de distancia

**Variable:** distancia.

**Principio:** un sensor de distancia puede utilizar ultrasonido, luz infrarroja, láser u otra señal. El sistema analiza la señal emitida y recibida para estimar qué tan lejos se encuentra el objeto.

**Ejemplo:** sensor ultrasónico HC-SR04 en proyectos educativos.

**Aplicación:** robot móvil que necesita detectar una pared antes de chocar.

### 2.5 Sensor de presión

**Variable:** presión.

**Principio:** la presión actúa sobre un elemento sensible, normalmente una membrana, produciendo una deformación que puede convertirse en una señal eléctrica.

**Ejemplo:** transductor de presión industrial.

**Aplicación:** medir presión en sistemas hidráulicos, neumáticos, bombas o compresores.

### 2.6 Sensor de humedad

**Variable:** humedad relativa del aire.

**Principio:** el material sensible modifica una propiedad eléctrica según la cantidad de humedad que absorbe o detecta.

**Ejemplo:** sensor digital de temperatura y humedad DHT22/AM2302.

**Aplicación:** estaciones meteorológicas, control ambiental, invernaderos y sistemas de climatización.

### 2.7 Sensor de posición

**Variable:** posición lineal o angular.

**Principio:** puede detectar la posición mediante variaciones magnéticas, inductivas, ópticas o resistivas. El controlador interpreta esa señal como una posición.

**Ejemplo:** Balluff BIP002L, sensor inductivo de posición con rango de medición de 0 a 7 mm y salida analógica de 0 a 10 V. [4]

**Aplicación:** conocer la posición de una pieza móvil en una máquina.

### 2.8 Sensor de velocidad o movimiento

**Variable:** velocidad, giro, aceleración o movimiento.

**Principio:** un encoder puede generar pulsos cuando gira un eje; contando esos pulsos durante un intervalo se puede calcular la velocidad. Un acelerómetro, en cambio, detecta aceleraciones del cuerpo.

**Ejemplo:** encoder rotatorio.

**Aplicación:** controlar la velocidad de una rueda de un robot o de un motor industrial.

### 2.9 Sensor de fuerza o peso

**Variable:** fuerza o peso.

**Principio:** una celda de carga utiliza elementos extensométricos que cambian su resistencia cuando la estructura se deforma ligeramente debido a una carga.

**Ejemplo:** celda de carga de una báscula electrónica.

**Aplicación:** básculas, robots que manipulan objetos y máquinas de medición.

---

# 3. Clasificación de sensores

## Sensores analógicos y digitales

La diferencia se encuentra principalmente en la forma de representar la información.

### Analógico

Un sensor analógico entrega una señal que puede tomar muchos valores dentro de un intervalo. Por ejemplo, un sensor podría entregar entre 0 y 5 V y el controlador interpreta diferentes voltajes como diferentes temperaturas.

**Característica que lo coloca en esta categoría:** la información de la variable se representa mediante un valor continuo dentro de un rango.

### Digital

Un sensor digital entrega información codificada en valores discretos. Puede ser simplemente una señal de encendido/apagado o una comunicación digital como I2C, SPI, UART o IO-Link.

**Característica:** la información se entrega mediante estados discretos o datos digitales.

TI ofrece sensores de temperatura tanto analógicos como digitales, mostrando claramente esta diferencia de interfaz. [2]

---

## Sensores de contacto y sin contacto

### De contacto

Necesitan que exista contacto físico con el objeto o superficie que se quiere detectar.

**Ejemplo:** un interruptor de límite que se activa cuando una pieza presiona mecánicamente su mecanismo.

**Característica:** la detección depende de una interacción física directa.

### Sin contacto

Pueden detectar una característica del objeto sin tocarlo.

**Ejemplos:** sensor inductivo, sensor fotoeléctrico y sensor ultrasónico.

**Característica:** utilizan un campo, radiación, sonido u otra señal para realizar la detección a distancia.

---

## Sensores activos y pasivos

### Activos

Un sensor activo necesita energía externa para generar o procesar la señal de detección.

Por ejemplo, un sensor ultrasónico necesita energía para producir una onda sonora y posteriormente analizar su retorno.

**Característica:** necesita alimentar electrónicamente el proceso de detección o excitación.

### Pasivos

Un sensor pasivo no necesita generar una señal de excitación propia para detectar la variable; aprovecha una propiedad física del elemento sensible.

Por ejemplo, un termistor cambia su resistencia debido a la temperatura y esa resistencia puede medirse desde un circuito externo.

**Característica:** la variable modifica una propiedad del sensor sin que el sensor tenga que generar por sí mismo la energía de medición.

---

# 4. Investigación de actuadores

| Actuador | Energía utilizada | Movimiento | Ventaja | Limitación | Aplicación |
|---|---|---|---|---|---|
| Motor DC | Eléctrica | Rotatorio | Simple y económico | No conoce su posición por sí mismo | Ruedas de robots |
| Servomotor | Eléctrica | Rotatorio controlado | Permite controlar posición | Rango y carga dependen del modelo | Articulación robótica |
| Motor paso a paso | Eléctrica | Rotatorio por pasos | Buen control de desplazamiento sin sensor en aplicaciones sencillas | Puede perder pasos si se sobrecarga | Impresora 3D/CNC |
| Solenoide | Eléctrica | Lineal corto | Respuesta sencilla y rápida | Recorrido limitado | Cerradura eléctrica |
| Cilindro neumático | Aire comprimido | Lineal | Rápido y robusto | Necesita compresor y válvulas | Empujar piezas |
| Cilindro hidráulico | Fluido hidráulico a presión | Lineal | Produce fuerzas muy grandes | Sistema más complejo y pesado | Maquinaria pesada |

### 4.1 Motor DC

**Energía:** eléctrica.

**Movimiento:** rotatorio.

**Funcionamiento:** la corriente eléctrica produce un campo magnético que interactúa con el sistema magnético del motor y genera un par que hace girar el eje. El sentido de giro puede cambiar invirtiendo la polaridad en un motor DC convencional.

**Ventaja:** es sencillo de controlar y existe una gran variedad de tamaños.

**Limitación:** un motor DC básico no sabe cuál es su posición angular. Para control de posición se puede agregar un encoder y un controlador.

**Aplicación:** ruedas de robots móviles.

Arduino también dispone de hardware específico para controlar motores DC, servomotores y motores paso a paso. [5]

### 4.2 Servomotor

**Energía:** eléctrica.

**Movimiento:** normalmente rotatorio y controlado en posición.

**Funcionamiento:** un servomotor combina un motor con electrónica de control y, en muchos modelos, un elemento de realimentación. El controlador compara la posición deseada con la posición detectada y corrige el motor.

**Ventaja:** facilita el control de posición.

**Limitación:** los servos pequeños tienen límites de torque, velocidad y recorrido.

**Aplicación:** mover una articulación pequeña de un robot.

Arduino muestra ejemplos de control de posición de servomotores y de barrido de aproximadamente 0° a 180° en servos de hobby. [6]

### 4.3 Motor paso a paso

**Energía:** eléctrica.

**Movimiento:** rotatorio en pasos discretos.

**Funcionamiento:** sus bobinas se energizan en una secuencia para que el rotor avance de una posición a otra. La cantidad de pasos enviados determina aproximadamente cuánto gira.

**Ventaja:** permite realizar movimientos angulares controlados de manera sencilla.

**Limitación:** si la carga o aceleración son demasiado altas, puede perder sincronización y pasos.

**Aplicación:** impresoras 3D, máquinas CNC y mecanismos de posicionamiento.

Arduino proporciona una biblioteca para controlar motores paso a paso unipolares y bipolares. [7]

### 4.4 Solenoide

**Energía:** eléctrica.

**Movimiento:** lineal, normalmente de recorrido corto.

**Funcionamiento:** una bobina crea un campo magnético cuando circula corriente. Ese campo atrae o mueve un núcleo ferromagnético.

**Ventaja:** diseño sencillo y accionamiento rápido.

**Limitación:** normalmente tiene un recorrido corto y puede consumir bastante corriente mientras permanece activado.

**Aplicación:** cerraduras eléctricas, válvulas y mecanismos de bloqueo.

### 4.5 Cilindro neumático

**Energía:** aire comprimido.

**Movimiento:** lineal.

**Funcionamiento:** una válvula dirige aire comprimido a uno de los lados del pistón. La presión produce una fuerza que desplaza el pistón y su vástago.

**Ventaja:** es rápido, resistente y apropiado para movimientos repetitivos.

**Limitación:** necesita una fuente de aire comprimido y el aire es compresible, por lo que el posicionamiento muy preciso puede ser más complicado.

Parker clasifica los cilindros como actuadores lineales y describe el uso de aire comprimido como el medio más común de los cilindros neumáticos. [8]

**Aplicación:** empujar una pieza en una línea de producción.

### 4.6 Cilindro hidráulico

**Energía:** energía hidráulica mediante fluido a presión.

**Movimiento:** lineal.

**Funcionamiento:** el fluido a presión entra en una cámara y actúa sobre un pistón. La fuerza resultante desplaza el vástago. Parker describe estos cilindros como dispositivos que convierten presión y flujo del fluido en fuerza y movimiento lineal. [9]

**Ventaja:** puede producir fuerzas muy elevadas y soportar trabajos pesados.

**Limitación:** requiere bomba, válvulas, tuberías y mantenimiento del fluido; el sistema suele ser más complejo que uno eléctrico sencillo.

**Aplicación:** maquinaria de construcción, prensas y sistemas industriales de alta fuerza.

---

# 5. Comparación de actuadores

## Motor DC vs. servomotor

Un motor DC básico está pensado principalmente para producir rotación. Para conocer y controlar su posición normalmente se necesita agregar realimentación, por ejemplo mediante un encoder.

Un servomotor ya está pensado para formar un sistema de control de posición o velocidad, dependiendo del modelo.

**Elegiría motor DC:** para mover las ruedas de un robot pequeño donde solamente necesito controlar velocidad y sentido.

**Elegiría servomotor:** para una articulación donde necesito ordenar una posición determinada, como mover una pinza a cierto ángulo.

---

## Servomotor vs. motor paso a paso

Un servomotor utiliza realimentación en muchas aplicaciones para corregir su posición, mientras que un motor paso a paso avanza siguiendo una secuencia de pasos y puede funcionar sin sensor de posición en aplicaciones donde se acepta ese método.

**Elegiría servomotor:** para una articulación que necesita corregir errores de posición y responder rápidamente.

**Elegiría paso a paso:** para un mecanismo de posicionamiento como una impresora 3D, donde los movimientos por pasos resultan convenientes y el sistema puede diseñarse dentro de sus límites.

---

## Actuador neumático vs. actuador hidráulico

Ambos utilizan un fluido para generar movimiento lineal, pero el neumático utiliza normalmente aire comprimido y el hidráulico utiliza un líquido a presión.

**Elegiría neumático:** para mover rápidamente piezas relativamente ligeras en una línea de producción.

**Elegiría hidráulico:** cuando se necesita una fuerza mucho mayor, por ejemplo para una máquina pesada.

Parker señala que los cilindros neumáticos e hidráulicos tienen aplicaciones y características diferentes, y que la selección depende de factores como fuerza, carrera, velocidad y condiciones de trabajo. [8][9]

---

# 6. Sensores y actuadores en un sistema real

## Sistema seleccionado: robot móvil

Para este apartado seleccioné un **robot móvil autónomo de almacén** como sistema mecatrónico. Es un ejemplo adecuado porque integra sensores para conocer el entorno, un controlador para tomar decisiones y actuadores para mover la plataforma.

### Elementos principales

| Elemento | Tipo | Función |
|---|---|---|
| LiDAR | Sensor | Detecta obstáculos y permite obtener información de la geometría del entorno. |
| Encoder de ruedas | Sensor | Mide el giro de las ruedas para estimar desplazamiento y velocidad. |
| IMU | Sensor | Mide aceleraciones y velocidades angulares para estimar el movimiento del robot. |
| Sensor de batería | Sensor | Permite conocer el estado eléctrico de la batería. |
| Computadora/controlador | Control | Procesa las mediciones y calcula las órdenes de movimiento. |
| Motores DC/BLDC | Actuadores | Producen el giro de las ruedas. |
| Driver de motores | Actuador/control de potencia | Entrega la corriente necesaria a los motores y controla su sentido y velocidad. |
| Ruedas | Elementos mecánicos | Transforman la rotación de los motores en desplazamiento del robot. |

### Diagrama del sistema

```text
                    ENTORNO
                       │
            ┌──────────┴──────────┐
            │                     │
         Obstáculos          Posición/movimiento
            │                     │
            ▼                     ▼
         ┌───────┐           ┌────────┐
         │ LiDAR │           │  IMU   │
         └───┬───┘           └───┬────┘
             │                   │
             └────────┬──────────┘
                      │
                      ▼
               ┌─────────────┐
               │ CONTROLADOR │
               │ / COMPUTAD. │
               └──────┬──────┘
                      │
                órdenes de control
                      │
                      ▼
              ┌───────────────┐
              │ DRIVER MOTORES│
              └───────┬───────┘
                      │
             ┌────────┴────────┐
             ▼                 ▼
       ┌──────────┐      ┌──────────┐
       │ Motor izq│      │ Motor der│
       └────┬─────┘      └────┬─────┘
            │                 │
            └────────┬────────┘
                     ▼
                  RUEDAS
                     │
                     ▼
             Movimiento del robot
                     │
                     └───────► nuevo estado
```

Este esquema muestra el ciclo básico de un sistema mecatrónico: **medir → procesar → actuar → volver a medir**.

---

# 7. Selección de componentes

| Situación | Componente seleccionado | Tipo | Razón |
|---|---|---|---|
| Detectar si una persona se encuentra frente a una puerta automática | Sensor fotoeléctrico o sensor de presencia | Sensor | Puede detectar a la persona sin necesidad de contacto físico. |
| Medir la temperatura dentro de un salón | Sensor de temperatura digital, por ejemplo TMP1075 | Sensor | Entrega una medición que el controlador puede utilizar para regular el ambiente. |
| Detectar el nivel de agua de un depósito | Sensor ultrasónico de nivel | Sensor | Permite medir el nivel sin colocar un componente eléctrico dentro del agua. |
| Mover una rueda de un robot móvil | Motor DC con driver y encoder | Actuador + sensor | El motor genera la rotación y el encoder permite conocer la velocidad o desplazamiento. |
| Controlar con precisión el ángulo de una pequeña articulación robótica | Servomotor | Actuador | Está diseñado para controlar la posición angular mediante su sistema de control. |
| Empujar una pieza en una línea de producción | Cilindro neumático | Actuador | Produce un movimiento lineal rápido y adecuado para empujar piezas repetitivamente. |
| Medir la distancia entre un robot y una pared | Sensor ultrasónico o LiDAR | Sensor | Mide la separación sin contacto físico. |
| Detectar si una habitación está iluminada | Sensor de luz / fotodiodo / LDR | Sensor | Su señal cambia de acuerdo con la cantidad de luz que recibe. |

---

# Reflexión final

### ¿Qué diferencia encuentro entre medir una variable y realizar una acción física?

Medir una variable significa obtener información sobre el estado de algo, por ejemplo saber que una habitación está a 25 °C o que un robot está a 40 cm de una pared. Realizar una acción física significa modificar el estado del sistema, como encender un motor, mover una puerta o empujar una pieza.

Por eso un sensor está relacionado principalmente con la **información**, mientras que un actuador está relacionado con la **acción**.

### ¿Por qué un sistema mecatrónico normalmente necesita sensores y actuadores?

Porque un sistema automático necesita saber qué está ocurriendo y después responder. Sin sensores, el controlador tendría poca información sobre el entorno o sobre el propio mecanismo. Sin actuadores, el sistema podría detectar y procesar información, pero no tendría una forma física de modificar su estado.

La combinación de ambos permite implementar sistemas de control y retroalimentación.

### ¿Qué sensor o actuador me pareció más interesante y por qué?

El componente que me pareció más interesante fue el **servomotor**, porque integra movimiento y control de posición en un mismo conjunto. Es especialmente útil en robótica porque permite transformar una orden electrónica en un movimiento angular controlado.

También me parece interesante el sensor LiDAR porque permite que un robot obtenga información espacial de su entorno y pueda utilizarla para navegación y evitación de obstáculos.

---

# Referencias

1. **Siemens AG.** *IO-Link: Communication technology that bridges the gap between sensors, actuators, and automation systems.* Siemens, consulta 2026.  
   https://www.siemens.com/en-us/products/sirius/io-link/

2. **Texas Instruments.** *Temperature Sensors.* TI, consulta 2026. Incluye sensores de temperatura analógicos y digitales y diferentes interfaces de comunicación.  
   https://www.ti.com/product-category/sensors/temperature/overview.html

3. **Balluff GmbH.** *Products and Services Volume 1 – Sensors.* Balluff, catálogo técnico. Incluye sensores inductivos, capacitivos, fotoeléctricos y sensores de distancia.  
   https://assets.balluff.com/WebBinary1/LIT_CAT_CATALOG_VOLUME_SENSORS_1_EN_A19_DRW_942496_00_000.pdf

4. **Balluff GmbH.** *BIP002L – Inductive position sensor.* Balluff Mexico, documentación del producto.  
   https://www.balluff.com/en-mx/products/BIP002L

5. **Arduino.** *MKR Motor Carrier.* Arduino Documentation, consulta 2026. Documentación para el control de motores DC, servomotores y motores paso a paso.  
   https://docs.arduino.cc/hardware/mkr-motor-carrier

6. **Arduino.** *Servo Motor Basics with Arduino.* Arduino Documentation, revisión 2024.  
   https://docs.arduino.cc/learn/electronics/servo-motors/

7. **Arduino.** *Stepper Library.* Arduino Documentation, versión 1.1.3, 2026.  
   https://docs.arduino.cc/libraries/stepper/

8. **Parker Hannifin Corporation.** *Application Engineering Guide – Cylinder Operating Principles.* Parker, documentación técnica. Explica principios de funcionamiento de cilindros neumáticos e hidráulicos.  
   https://www.parker.com/parkerimages/cylinder/miller/cat/App_Eng_3-02.pdf

9. **Parker Hannifin Corporation.** *Hydraulic Cylinder Specification Guide.* Parker, consulta 2026. Información sobre cilindros hidráulicos y selección de actuadores.  
   https://discover.parker.com/hydraulic-cylinder-specification-LP

10. **Texas Instruments, Manny Soltero.** *What Are You Sensing? Pros and Cons of Four Temperature Sensor Types.* Technical Article, 2015.  
    https://www.ti.com/document-viewer/lit/html/SSZTCA2

11. **OMRON Corporation.** *Photoelectric Sensors – E3FA/E3RA/E3FB/E3RB Datasheet.* OMRON Automation and Safety.  
    https://assets.omron.com/m/048d74e345093d86/original/E3FA_E3RA_E3FB_E3RB_datasheet_en_201401_E53I-E-03-pdf.pdf

12. **Parker Hannifin Corporation.** *Actuator Central Training.* Material de capacitación sobre cilindros y actuadores neumáticos e hidráulicos.  
    https://discover.parker.com/Cylindercentral-training

---

## Conclusión

Los sensores y actuadores cumplen funciones opuestas pero complementarias dentro de un sistema mecatrónico. Los sensores permiten obtener información de variables físicas y convertirla en señales que el controlador puede procesar. Los actuadores reciben órdenes y transforman energía en acciones físicas.

La elección del componente depende de la aplicación. No es lo mismo detectar una persona que medir una temperatura, ni mover una rueda que empujar una pieza con mucha fuerza. Por eso conocer las características de cada sensor y actuador es importante para diseñar sistemas mecatrónicos eficientes, seguros y adecuados para su propósito.
