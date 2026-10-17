# Investigación: Configuraciones de locomoción en robots móviles

**Matrícula:** 2630012  
**Nombre:** Sanchez Roman  
**Archivo:** `2630012_SanchezRoman.md`

---

## 1. Conceptos básicos

### ¿Qué es un robot móvil?

Un robot móvil es una máquina capaz de cambiar de posición dentro de un espacio mediante algún sistema de locomoción. En el caso de los robots con ruedas, los motores hacen girar las ruedas y el sistema de control coordina sus velocidades para producir el movimiento deseado.

### Diferencia entre un robot móvil y un robot manipulador fijo

Un robot móvil puede trasladarse de un lugar a otro porque su base no permanece anclada. Un manipulador fijo, en cambio, normalmente está instalado sobre una estructura o una base que permanece en una posición determinada. Un manipulador fijo puede tener varios grados de libertad en su brazo, pero eso no significa que toda la máquina pueda desplazarse por el entorno.

### Función del sistema de locomoción

El sistema de locomoción convierte la energía de los actuadores en movimiento del robot. Además, determina qué trayectorias puede seguir, qué tan fácil es girar y qué tan bien puede superar las restricciones del entorno.

### ¿Qué significa movilidad omnidireccional?

Significa que el robot puede controlar su movimiento en el plano en varias direcciones, incluyendo desplazarse hacia adelante, hacia atrás, lateralmente y girar. En una plataforma holonómica es posible combinar traslación y rotación de manera independiente dentro de los límites de velocidad y adherencia.

### Relación entre la disposición de las ruedas y el movimiento

La posición, orientación y tipo de rueda determinan la dirección de las fuerzas que pueden transmitirse al suelo. Por eso, cambiar una rueda convencional por una omni o Mecanum cambia completamente las posibilidades de movimiento. Las ruedas convencionales tienen restricciones laterales, mientras que las ruedas omnidireccionales utilizan rodillos para permitir deslizamiento controlado en una dirección.

### ¿Dónde se utilizan robots móviles?

Algunos ejemplos son:

- Almacenes y centros logísticos.
- Fábricas y líneas de producción.
- Hospitales.
- Laboratorios y universidades.
- Agricultura.
- Inspección de instalaciones.
- Transporte interno de materiales.
- Investigación y desarrollo de vehículos autónomos.
- Exploración de ambientes donde una persona no debería permanecer durante mucho tiempo.

---

## 2. Robot diferencial con rueda de castor

La configuración diferencial con castor utiliza normalmente **dos ruedas motrices independientes** colocadas a izquierda y derecha, más una o más ruedas de castor para mantener el equilibrio. Las dos ruedas motrices son las que controlan principalmente el movimiento y la orientación del robot.

### Colocación de las ruedas motrices

Las ruedas izquierda y derecha se colocan aproximadamente sobre el mismo eje transversal del robot. Cada una tiene su propio motor o control de velocidad.

### Función de la rueda de castor

La rueda de castor, también llamada rueda loca, soporta parte del peso y permite que la plataforma se mantenga estable. No necesita un motor de tracción y puede girar alrededor de su soporte para alinearse con el movimiento. Su presencia no determina directamente el sentido de giro del robot.

### Movimiento en línea recta

Si las dos ruedas motrices avanzan a la misma velocidad, el robot avanza aproximadamente en línea recta.

### Giro a izquierda o derecha

Si una rueda avanza más rápido que la otra, el robot describe una curva. Si la rueda izquierda gira más rápido que la derecha, el robot tiende a girar hacia la derecha. Si la derecha gira más rápido, tiende a girar hacia la izquierda.

### Giro sobre el propio eje

Para girar aproximadamente sobre el centro del eje que une las dos ruedas motrices, una rueda debe avanzar mientras la otra retrocede con velocidades de magnitud similar. Las fuerzas producen una rotación alrededor del centro del eje de las ruedas.

### Ventajas

- Mecánica relativamente sencilla.
- Solo necesita dos motores para la tracción principal.
- Control de movimiento fácil de implementar.
- Puede girar con radio muy pequeño.
- Es una buena configuración para aprender odometría y control.

### Limitaciones

- No puede desplazarse directamente de lado.
- La rueda de castor puede generar resistencia durante algunos giros.
- En superficies con poca adherencia puede existir deslizamiento.
- Para desplazamientos laterales necesita cambiar primero la orientación.

### Aplicaciones

Se utiliza en robots educativos, plataformas de investigación, robots de servicio, robots de almacén y bases móviles autónomas.

### Diagrama superior

```text
                    FRENTE
                      ↑
               Sentido de avance
                      │
        ┌─────────────────────────┐
        │                         │
        │   O                 O   │
        │  ← Rueda          Rueda →│
        │    izquierda       derecha│
        │                         │
        │          ●              │
        │      rueda de castor    │
        └─────────────────────────┘
                 ↺   │   ↻
                 Eje de giro
              aproximado en el
             centro de las ruedas
```

### Casos de movimiento

| Rueda izquierda | Rueda derecha | Movimiento del robot |
|---|---|---|
| Avanza | Avanza | Avanza en línea recta si las velocidades son iguales. |
| Detenida | Avanza | Gira hacia la izquierda alrededor de la rueda izquierda. |
| Avanza | Detenida | Gira hacia la derecha alrededor de la rueda derecha. |
| Avanza | Retrocede | Gira sobre su eje, aproximadamente. |
| Retrocede | Avanza | Gira sobre su eje en el sentido contrario. |
| Retrocede | Retrocede | Retrocede en línea recta si las velocidades son iguales. |

**Nota:** los sentidos de giro anteriores suponen que las ruedas tienen el mismo tamaño y que "avanza" significa producir desplazamiento hacia el frente del robot.

---

## 3. Robots omnidireccionales con ruedas Omni

### Funcionamiento de una rueda Omni

Una rueda Omni tiene una rueda principal y varios pequeños rodillos distribuidos alrededor de su periferia. La rueda puede transmitir fuerza principalmente en la dirección de giro de la rueda, mientras que los rodillos permiten que el contacto con el suelo se desplace lateralmente con mucha menor resistencia.

### Construcción

Su estructura está formada por:

1. Núcleo o cuerpo de la rueda.
2. Eje de giro.
3. Rodillos periféricos.
4. Soportes de los rodillos.

### Función de los rodillos

Los rodillos giran libremente. Por ello, cuando una fuerza intenta desplazar la rueda en la dirección perpendicular a su movimiento principal, los rodillos pueden girar en lugar de impedir completamente ese desplazamiento.

### ¿En qué dirección genera fuerza?

La rueda genera tracción principalmente en la dirección tangencial asociada con el giro de la rueda.

### ¿Por qué puede deslizarse en otra dirección?

Porque los rodillos no están rígidamente unidos al suelo. Pueden girar y permiten que la plataforma se desplace lateralmente respecto de la orientación de la rueda.

### Consecuencia para el robot

Al colocar varias ruedas Omni con diferentes orientaciones, las fuerzas de cada rueda se combinan. Así se pueden producir movimientos que una rueda convencional no permite, como una traslación lateral.

### Configuración de tres ruedas

Una configuración común coloca tres ruedas Omni alrededor de un centro, aproximadamente separadas **120°** entre sí. La documentación de ROS 2 describe la distribución angular de n ruedas mediante `2π/n`; para tres ruedas esto corresponde a 120°.

```text
                         FRENTE
                           ↑
                           │
                         [O]
                       /     \
                      /       \
                 [O]             [O]
                120°               120°
                    \             /
                     \     ●     /
                      \  centro /
```

Las ruedas deben orientarse de forma que sus direcciones de tracción sean tangenciales al movimiento deseado alrededor del centro. El controlador calcula las velocidades de las tres ruedas para obtener una velocidad lineal en X, una velocidad lateral en Y y una velocidad angular.

### Movimientos posibles

- **Adelante:** las tres ruedas reciben velocidades coordinadas para producir una componente de velocidad hacia el frente.
- **Atrás:** se invierten las velocidades correspondientes.
- **Lateral:** las tres ruedas giran a velocidades y sentidos que cancelan las componentes longitudinales y conservan una componente lateral.
- **Diagonal:** se combinan las componentes longitudinal y lateral.
- **Giro sobre el eje:** las ruedas se coordinan para que las fuerzas tangenciales produzcan un momento alrededor del centro.
- **Velocidades diferentes:** al modificar individualmente las velocidades se puede combinar traslación y rotación.

### Configuración de cuatro ruedas Omni

En una plataforma de cuatro ruedas Omni, normalmente las ruedas se colocan cerca de las cuatro esquinas del chasis. Las ruedas se orientan para que sus componentes de tracción permitan combinar desplazamientos en X, Y y rotación.

La principal diferencia respecto a tres ruedas es que hay una rueda adicional, lo que puede mejorar el reparto de carga y la estabilidad mecánica, pero también aumenta el número de actuadores y exige una coordinación más precisa.

**Ventajas:**

- Buena capacidad de movimiento lateral.
- Puede combinar traslación y rotación.
- Cuatro ruedas pueden repartir mejor la carga.

**Limitaciones:**

- Mayor complejidad que un diferencial.
- Más motores y controladores.
- El comportamiento depende mucho de que las ruedas estén bien alineadas.
- Los rodillos producen pérdidas y pueden ser sensibles a irregularidades del piso.

---

## 4. Robot omnidireccional con ruedas Mecanum

Una rueda Mecanum tiene rodillos alrededor de la periferia, pero estos rodillos están colocados normalmente alrededor de **45° respecto al plano de la rueda**. Al combinar cuatro ruedas y controlar sus velocidades, las componentes de fuerza de los rodillos producen movimiento hacia adelante, lateral y rotacional.

### Construcción

Una Mecanum está formada por:

- Núcleo de rueda.
- Eje de transmisión.
- Rodillos periféricos.
- Soportes de los rodillos.
- Superficie de contacto de los rodillos.

### Diferencia entre Omni y Mecanum

Una rueda Omni convencional suele tener rodillos orientados para permitir deslizamiento lateral aproximadamente perpendicular a la tracción de la rueda. En la Mecanum, los rodillos están inclinados, generalmente 45°. Esa inclinación hace que cada rueda produzca una componente diagonal de fuerza.

### ¿Por qué se utilizan cuatro ruedas?

Cuatro ruedas permiten formar una plataforma rectangular estable y distribuir las fuerzas entre las esquinas. Las velocidades de las cuatro ruedas se combinan para controlar tres movimientos principales del chasis: velocidad longitudinal, velocidad lateral y velocidad angular.

### Orientación respecto al chasis

Una disposición típica se representa como una "X" cuando se observan las direcciones de los rodillos desde arriba:

```text
                         FRENTE
                            ↑

              DELANTERA IZQ.       DELANTERA DER.
                   ╲  ╲               ╱  ╱
                    ╲  ╲             ╱  ╱
                     [O]             [O]
                       ╲             ╱
                        ╲           ╱
                         ╲         ╱
                         ╱         ╲
                        ╱           ╲
                       ╱             ╲
                     [O]             [O]
                    ╱  ╱             ╲  ╲
                   ╱  ╱               ╲  ╲
              TRASERA IZQ.          TRASERA DER.

              Las direcciones de los rodillos
                    forman una configuración X.
```

> La orientación exacta puede cambiar según el fabricante y la convención de montaje. Lo importante es que las cuatro ruedas formen el patrón complementario necesario para que las componentes laterales se sumen correctamente.

### Combinación de movimientos

- **Avance:** las cuatro ruedas giran en el mismo sentido de tracción.
- **Retroceso:** las cuatro ruedas invierten el sentido.
- **Izquierda:** los pares de ruedas se hacen girar en sentidos opuestos según su posición, de manera que las componentes longitudinales se cancelan y las laterales se suman.
- **Derecha:** se invierte el patrón lateral.
- **Diagonal:** se pueden combinar avance y desplazamiento lateral.
- **Giro sobre el eje:** las ruedas de un lado y del otro trabajan en sentidos opuestos para crear un momento de giro.

### Tabla de sentidos de giro

La siguiente tabla usa `→` y `←` para indicar el sentido de giro **visto desde el lado exterior de cada rueda**. El sentido visual puede cambiar si se observa una rueda desde el lado opuesto; por eso, en una implementación real se debe seguir la convención del fabricante del motor.

| Movimiento | Delantera izquierda | Delantera derecha | Trasera izquierda | Trasera derecha |
|---|---:|---:|---:|---:|
| Avanzar | → | → | → | → |
| Retroceder | ← | ← | ← | ← |
| Desplazarse a la izquierda | ← | → | → | ← |
| Desplazarse a la derecha | → | ← | ← | → |
| Girar a la izquierda | ← | → | ← | → |
| Girar a la derecha | → | ← | → | ← |

Para movimiento diagonal se combina la orden de avance con la orden lateral. Por ejemplo, para avanzar y desplazarse hacia la izquierda al mismo tiempo se suma matemáticamente la velocidad de avance con la velocidad lateral.

---

## 5. Robot con dirección Ackermann

La geometría Ackermann se utiliza en automóviles y robots móviles que deben desplazarse de una forma parecida a un automóvil. Normalmente existen cuatro ruedas, dos delanteras y dos traseras.

### Distribución

Las ruedas están colocadas en dos ejes:

- Eje delantero.
- Eje trasero.

Las ruedas delanteras suelen ser las que cambian de orientación para dirigir el vehículo.

### Dirección y tracción

En un vehículo convencional, las ruedas delanteras pueden encargarse de la dirección y las ruedas motrices pueden estar adelante, atrás o en ambos ejes. En un robot autónomo, la tracción puede depender de la arquitectura elegida.

### ¿Por qué las ruedas interior y exterior tienen ángulos diferentes?

Durante una curva, la rueda interior recorre un círculo de menor radio que la rueda exterior. Para que ambas ruedas rueden aproximadamente sin arrastrarse lateralmente, sus líneas de orientación deben apuntar hacia un centro común de giro. Por eso la rueda interior necesita un ángulo mayor que la exterior.

### Radio de giro

Es la distancia aproximada entre el centro instantáneo de rotación del vehículo y el punto de referencia que se esté utilizando, normalmente cerca del centro del eje trasero en un modelo simplificado.

### ¿Por qué no puede moverse directamente hacia un costado?

Las ruedas convencionales de un vehículo Ackermann están orientadas para rodar hacia adelante o hacia atrás. No poseen rodillos laterales como una rueda Omni o Mecanum. Para cambiar la posición lateral, el vehículo necesita avanzar o retroceder siguiendo una trayectoria curva.

### Semejanza con un automóvil

La semejanza principal es que la dirección cambia el ángulo de las ruedas delanteras y el vehículo sigue una trayectoria curva. Por eso Ackermann es una opción natural para robots que necesitan comportarse como automóviles.

### Diagrama de curva

```text
                         FRENTE
                            ↑
                   Rueda exterior
                         ╲
                          ╲
                           ╲
                            ╲
                             ╲
                              ●  Centro
                             /   aproximado
                            /    de giro
                           /
                    Rueda interior
                         ╱

        ┌──────────────────────────────┐
        │          CHASIS              │
        └──────────────────────────────┘
                 ↗ Dirección de avance

La rueda interior sigue un radio menor.
La rueda exterior sigue un radio mayor.
```

### Ejemplos

Robots móviles autónomos para exteriores, vehículos de investigación y plataformas tipo automóvil pueden utilizar esta geometría. También existen controladores de Ackermann en ecosistemas de robótica como ROS/ROS 2.

---

## 6. Comparación de configuraciones

| Configuración | Número típico de ruedas | Movimiento lateral | Giro sobre su eje | Complejidad mecánica | Complejidad de control | Aplicaciones |
|---|---:|---|---|---|---|---|
| Diferencial + castor | 3 | No directo | Sí | Baja | Baja | Educación, robots de servicio, investigación |
| Omni de 3 ruedas | 3 | Sí | Sí | Media | Media | Plataformas compactas, investigación |
| Omni de 4 ruedas | 4 | Sí | Sí | Media-alta | Media-alta | Transporte interno, plataformas industriales |
| Mecanum | 4 | Sí | Sí | Media-alta | Alta | Logística, almacenes, manipulación móvil |
| Ackermann | 4 | No directo | No | Media | Media | Vehículos autónomos, robots tipo automóvil |

### ¿Qué configuración elegiría?

**Robot pequeño para aprender programación y control:**  
Elegiría **diferencial + castor**. Solo requiere dos motores de tracción y permite aprender control de velocidad, encoders, odometría y navegación sin que la cinemática sea demasiado complicada.

**Robot para un almacén con espacios reducidos:**  
Elegiría **Mecanum** u Omni. La posibilidad de desplazarse lateralmente facilita entrar y salir de espacios estrechos sin tener que hacer muchas maniobras.

**Plataforma que necesita moverse lateralmente sin cambiar su orientación:**  
Elegiría **Omni o Mecanum**, porque permiten producir una velocidad lateral directamente.

**Vehículo autónomo similar a un automóvil:**  
Elegiría **Ackermann**, porque su geometría se parece a la de un automóvil y representa mejor las restricciones de dirección de un vehículo convencional.

**Robot para una competencia donde sea necesario cambiar rápidamente de dirección:**  
Elegiría **Mecanum** si el piso es relativamente uniforme, debido a que permite combinar desplazamiento y giro de manera muy flexible.

**Robot móvil sencillo con únicamente dos motores:**  
Elegiría **diferencial + castor**, porque las dos ruedas motrices pueden ser controladas independientemente con dos motores.

---

## 7. Análisis del movimiento

### Diferencial

Para girar sobre su propio eje, las dos ruedas motrices deben producir velocidades de igual magnitud pero sentidos opuestos. Por ejemplo, si la izquierda avanza y la derecha retrocede, las fuerzas longitudinales generan un momento alrededor del centro del robot. Al estar las ruedas separadas, ese momento hace girar el chasis.

### Omni

Los rodillos permiten movimiento lateral porque reducen la resistencia al desplazamiento en una dirección perpendicular a la tracción principal de la rueda. Cuando varias ruedas están colocadas con diferentes orientaciones, sus fuerzas se combinan para generar una velocidad lateral resultante.

### Mecanum

El robot puede desplazarse lateralmente aunque ninguna rueda apunte directamente hacia el costado porque los rodillos están inclinados. Cada rueda produce una fuerza con componentes en dos direcciones. El controlador combina esas componentes y hace que las fuerzas longitudinales se cancelen mientras las componentes laterales se suman.

### Ackermann

El vehículo necesita avanzar o retroceder para cambiar de posición lateral porque las ruedas convencionales no pueden generar una velocidad lateral independiente. Al girar las ruedas directrices, el vehículo cambia el radio de su trayectoria y obtiene un desplazamiento lateral como consecuencia de seguir una curva.

---

## 8. Aplicación en un robot real

### Robot seleccionado: RB-KAIROS de Robotnik

El **RB-KAIROS** es un robot móvil autónomo industrial de Robotnik diseñado para aplicaciones de interior. Utiliza una base omnidireccional con cuatro ruedas Mecanum.

### Características principales

| Característica | RB-KAIROS |
|---|---|
| Fabricante | Robotnik |
| Tipo | Robot móvil autónomo industrial |
| Locomoción | Omnidireccional |
| Ruedas | 4 ruedas Mecanum |
| Motores de tracción | 4 servomotores de 500 W con freno |
| Sensores principales | 2 escáneres LiDAR 2D de seguridad, cámara RGBD, IMU |
| Localización | SLAM |
| Control | Arquitectura ROS |
| Aplicaciones | Logística, transporte de mercancías, metrología y alimentación de piezas |
| Entorno | Interior |

Robotnik indica que el RB-KAIROS puede transportar cargas de hasta 250 kg según la configuración y que su locomoción omnidireccional le permite moverse en distintas direcciones, algo especialmente útil en espacios con obstáculos.

### Imagen del robot

![Robot móvil RB-KAIROS de Robotnik](https://robotnik.eu/wp-content/uploads/2024/09/Robotnik_Datasheet_RB-KAIROS_2024_EN.pdf)

**Fuente de la imagen y datos técnicos:** Robotnik, ficha técnica del RB-KAIROS.

### ¿Por qué Mecanum resulta adecuada?

La configuración Mecanum es apropiada porque el robot puede acercarse a una posición de trabajo desde diferentes direcciones sin tener que realizar una maniobra larga para cambiar de orientación. Esto es especialmente útil en logística y en líneas de producción donde los pasillos pueden ser estrechos.

Robotnik también presenta aplicaciones donde el RB-KAIROS+ necesita desplazarse por pasillos estrechos y posicionarse con precisión frente a estaciones de trabajo. En este tipo de escenario, la movilidad omnidireccional facilita la colocación de la plataforma.

---

# Reflexión final

La configuración que me pareció más sencilla de comprender fue la **diferencial con rueda de castor**, porque solamente se necesita entender la relación entre la velocidad de la rueda izquierda y la derecha. También es una configuración sencilla para construir un primer prototipo con dos motores.

La configuración que ofrece mayor libertad de movimiento entre las estudiadas es la **omnidireccional**, especialmente Mecanum u Omni, porque permite controlar una componente lateral además del avance y la rotación.

Para construir mi primer robot móvil utilizaría **diferencial + castor**. Esta opción requiere menos motores, tiene una mecánica sencilla y permite aprender conceptos importantes como PWM, control de motores, encoders, odometría y navegación.

No existe una sola configuración adecuada para todos los robots porque cada aplicación tiene diferentes necesidades. Un vehículo que circula como automóvil necesita una geometría diferente de una plataforma que debe moverse lateralmente dentro de un almacén. Además, influyen factores como el costo, la carga, el tipo de suelo, el consumo de energía, la precisión, la velocidad y la complejidad del control.

---

# Referencias

1. K. M. Lynch y F. C. Park, *Modern Robotics: Wheeled Mobile Robots*, Northwestern University. Material educativo sobre cinemática, robots móviles con ruedas y robots omnidireccionales.  
   https://modernrobotics.northwestern.edu/nu-gm-book-resource/13-1-wheeled-mobile-robots/

2. ROS 2 Control, *Wheeled Mobile Robot Kinematics*, documentación técnica, 2026. Describe la cinemática de robots con ruedas Omni y la relación entre la geometría de las ruedas y las velocidades del robot.  
   https://control.ros.org/master/doc/ros2_controllers/doc/mobile_robot_kinematics.html

3. ROS 2 Control, *Controllers Index*, documentación técnica. Incluye controladores para diferencial, Mecanum, Omni y Ackermann.  
   https://control.ros.org/master/doc/ros2_controllers/doc/controllers_index.html

4. Robotnik, *RB-KAIROS+ Mobile Manipulator*, documentación del fabricante. Información sobre ruedas Mecanum, sensores, motores, ROS y aplicaciones industriales.  
   https://robotnik.eu/products/mobile-manipulators/rb-kairos/

5. Robotnik, *RB-KAIROS Autonomous Mobile Robot*, ficha técnica. Información sobre locomoción omnidireccional, cuatro ruedas Mecanum, sensores, motores y aplicaciones.  
   https://robotnik.eu/wp-content/uploads/2024/09/Robotnik_Datasheet_RB-KAIROS_2024_EN.pdf

6. Robotnik, *Use of robotics in gear manufacturing plant*, caso de aplicación industrial del RB-KAIROS+. Explica el uso de ruedas Mecanum para maniobrar en pasillos y posicionarse frente a estaciones de trabajo.  
   https://robotnik.eu/uses-of-robotic-in-gear-manufacturing-plant/

7. J. Arrizabalaga, N. Van Duijkeren, M. Ryll y R. Lange, *A caster-wheel-aware MPC-based motion planner for mobile robotics*, Technical University of Munich / Robert Bosch GmbH, 2022. Estudia el efecto de las ruedas de castor en robots móviles diferenciales.  
   https://portal.fis.tum.de/en/publications/a-caster-wheel-aware-mpc-based-motion-planner-for-mobile-robotics/

8. IEEE, *Comparative Analysis of Ackermann and Differential-Drive Kinematics for Autonomous Mobile Robots*, 2026. Comparación de las restricciones y características cinemáticas de Ackermann y diferencial.  
   https://ieeexplore.ieee.org/abstract/document/11604417

9. D. S. y colaboradores, *Generalized Kinematic Modeling of Wheeled Mobile Robots: A Unified Framework for Heterogeneous Architectures*, Mathematics, vol. 14, no. 3, 415, 2026. Presenta modelos de robots diferencial, Ackermann, omnidireccional de tres ruedas y Mecanum.  
   https://doi.org/10.3390/math14030415
