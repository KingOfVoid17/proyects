# Metodologías y marcos ágiles: Scrum, Kanban y Design Thinking

**Matrícula:** 2630012  
**Nombre:** Sanchez Roman  
**Archivo:** `2630012_SanchezRoman.md`

---

# 1. Resumen ejecutivo

El término **ágil** describe una forma de organizar el trabajo que busca entregar valor de manera frecuente, aprender a partir de la retroalimentación y adaptarse cuando cambian las necesidades. Surgió como respuesta a problemas de proyectos donde se intentaba definir todo desde el principio y los cambios posteriores resultaban costosos.

La idea no consiste simplemente en trabajar más rápido. Un enfoque ágil busca trabajar en ciclos pequeños, revisar los resultados y modificar el plan cuando la información nueva demuestra que es necesario hacerlo.

Este documento explica los principios de Agile y presenta tres enfoques relacionados:

- **Scrum:** útil para equipos que desarrollan productos mediante ciclos de trabajo definidos.
- **Kanban:** útil cuando existe un flujo continuo de trabajo y las prioridades pueden cambiar con frecuencia.
- **Design Thinking:** útil para comprender problemas y necesidades de los usuarios antes de invertir demasiado en una solución.

También se comparan sus ventajas y riesgos, se explican métricas de trabajo y se presenta un pequeño caso de aplicación relacionado con el desarrollo de software.

---

# 2. Principios ágiles

## 2.1 ¿Qué significa trabajar de manera ágil?

Trabajar de forma ágil significa organizar el desarrollo alrededor de entregas frecuentes, colaboración, aprendizaje y capacidad de adaptación. El **Manifiesto por el Desarrollo Ágil de Software**, publicado en 2001, plantea cuatro valores principales y doce principios. [1]

Los cuatro valores pueden entenderse de esta manera:

| Valor | Interpretación práctica |
|---|---|
| Individuos e interacciones sobre procesos y herramientas | Las herramientas ayudan, pero la comunicación entre las personas es fundamental. |
| Software funcionando sobre documentación exhaustiva | La documentación es útil, pero debe existir un producto que realmente funcione. |
| Colaboración con el cliente sobre negociación contractual | El usuario debe participar y proporcionar retroalimentación durante el desarrollo. |
| Responder al cambio sobre seguir un plan | El plan sirve como guía, pero puede modificarse cuando aparece nueva información. |

Esto **no significa que los elementos de la derecha sean inútiles**. La idea es dar mayor importancia al elemento de la izquierda cuando existe un conflicto entre ambos.

## 2.2 Principios clave

Los doce principios del Manifiesto pueden resumirse en ideas como:

1. Entregar valor al cliente de manera frecuente.
2. Aceptar cambios incluso cuando el proyecto ya está avanzado.
3. Entregar incrementos funcionales regularmente.
4. Mantener una comunicación cercana entre las personas involucradas.
5. Construir proyectos alrededor de personas motivadas.
6. Favorecer la comunicación directa.
7. Utilizar el software funcionando como una medida importante del progreso.
8. Mantener un ritmo de trabajo sostenible.
9. Prestar atención continua a la calidad técnica.
10. Buscar simplicidad.
11. Permitir que los equipos autoorganizados encuentren mejores soluciones.
12. Revisar periódicamente la forma de trabajo y realizar ajustes.

### Impacto en la gestión del trabajo

Estos principios cambian la forma tradicional de administrar un proyecto. En lugar de intentar controlar todos los detalles desde el inicio, el equipo establece una dirección, produce resultados pequeños, obtiene información y ajusta el trabajo.

```text
Plan inicial
     │
     ▼
Trabajo pequeño
     │
     ▼
Producto funcional
     │
     ▼
Retroalimentación
     │
     ▼
Aprendizaje
     │
     └──────────► Ajuste del siguiente ciclo
```

---

# 3. Panorama de marcos y enfoques ágiles

| Enfoque | Idea principal | ¿Cuándo elegirlo? |
|---|---|---|
| Scrum | Desarrollo en ciclos llamados Sprints con responsabilidades y eventos definidos. | Cuando existe un producto que necesita evolucionar mediante iteraciones y un equipo dedicado. |
| Kanban | Gestionar el trabajo como un flujo continuo limitando el trabajo en progreso. | Cuando llegan tareas continuamente y las prioridades cambian con frecuencia. |
| Design Thinking | Comprender al usuario y experimentar con soluciones antes de construirlas completamente. | Cuando el problema todavía no está claro o existe alto riesgo de construir una solución que nadie necesita. |

Es importante distinguir **marco de trabajo** de **técnica de resolución de problemas**. Scrum y Kanban organizan principalmente el flujo de trabajo; Design Thinking se concentra en comprender problemas, usuarios y soluciones posibles.

---

# 4. Ventajas y riesgos

| Aspecto | Beneficio | Limitación o riesgo | Trade-off |
|---|---|---|---|
| Entregas frecuentes | Permiten recibir retroalimentación rápidamente. | Pueden aumentar la presión por entregar constantemente. | Rapidez vs. estabilidad |
| Adaptación | Facilita responder a cambios. | Cambiar continuamente puede provocar falta de dirección. | Flexibilidad vs. enfoque |
| Equipos autónomos | Aumentan la participación y responsabilidad. | Requieren personas capaces de tomar decisiones. | Autonomía vs. supervisión |
| Transparencia | Hace visible el estado del trabajo. | Puede exponer problemas que antes estaban ocultos. | Visibilidad vs. incomodidad |
| WIP limitado | Reduce multitarea y ayuda al flujo. | Puede sentirse restrictivo si el equipo no entiende el motivo. | Flujo vs. utilización individual |
| Prototipos | Permiten validar ideas temprano. | Un prototipo puede confundirse con un producto terminado. | Aprendizaje vs. perfección inicial |
| Métricas | Ayudan a identificar tendencias. | Pueden ser manipuladas si se convierten en objetivos. | Información vs. comportamiento artificial |

---

# 5. Scrum

## 5.1 Conceptos base

**Scrum** es un marco de trabajo para generar valor mediante soluciones adaptativas para problemas complejos. La Guía Scrum define elementos como responsabilidades, eventos y artefactos que ayudan a organizar el trabajo. [2]

Scrum puede ser adecuado cuando:

- El producto todavía necesita evolucionar.
- Existe incertidumbre sobre algunos requisitos.
- Se necesita retroalimentación frecuente.
- El equipo puede trabajar de manera colaborativa.
- Se pueden producir incrementos útiles en ciclos cortos.

Scrum no es simplemente una lista de reuniones. Su propósito es crear un sistema donde el equipo pueda inspeccionar el resultado y adaptarse.

---

## 5.2 Roles

En Scrum actual se habla de **accountabilities** o responsabilidades principales del Scrum Team: Product Owner, Scrum Master y Developers. En materiales anteriores puede aparecer el término "Development Team". [2]

### Product Owner

Su responsabilidad principal es maximizar el valor del producto y gestionar eficazmente el Product Backlog.

**Responsabilidades:**

- Definir y comunicar el Product Goal.
- Ordenar el Product Backlog.
- Aclarar qué valor tienen los elementos.
- Mantener visible el estado y dirección del producto.

**Errores frecuentes:**

- Convertirse en un jefe que asigna cada tarea individual.
- Cambiar prioridades sin explicar el objetivo.
- Tratar el backlog como una lista definitiva que nunca cambia.
- Medir el éxito solamente por cantidad de funcionalidades.

### Scrum Master

Ayuda a que Scrum se comprenda y se aplique correctamente. También ayuda a eliminar impedimentos y mejorar la efectividad del equipo.

**Responsabilidades:**

- Facilitar la comprensión de Scrum.
- Ayudar al equipo a mejorar su forma de trabajo.
- Promover la eliminación de impedimentos.
- Ayudar a mantener eventos productivos.

**Errores frecuentes:**

- Convertirse solamente en un secretario de reuniones.
- Asignar tareas a los Developers.
- Actuar como jefe tradicional del equipo.
- Pensar que su función es organizar reuniones y nada más.

### Developers

Son las personas que crean el incremento utilizable durante el Sprint.

**Responsabilidades:**

- Crear un Sprint Backlog.
- Mantener la calidad mediante la Definition of Done.
- Adaptar el plan diariamente hacia el Sprint Goal.
- Producir un incremento que cumpla la Definition of Done.

**Errores frecuentes:**

- Trabajar individualmente sin coordinación.
- Considerar terminado algo que no cumple los criterios de calidad.
- Optimizar únicamente su propia tarea en lugar del objetivo del Sprint.

---

# 6. Artefactos de Scrum

## 6.1 Product Backlog

Es la lista ordenada y evolutiva de todo lo que podría ser necesario para mejorar el producto. No es una simple lista de tareas: representa las necesidades y oportunidades que el producto debe atender.

## 6.2 Sprint Backlog

Es el conjunto de elementos seleccionados para el Sprint junto con el objetivo y el plan que utilizarán los Developers.

## 6.3 Increment

Es el resultado usable que cumple la **Definition of Done** y se suma a los incrementos anteriores. Un Sprint puede producir uno o varios incrementos.

### Definition of Done vs. criterios de aceptación

Estos conceptos pueden confundirse.

| Concepto | Qué responde | Ejemplo |
|---|---|---|
| Criterios de aceptación | ¿Qué debe cumplir esta funcionalidad específica para considerarse aceptable? | "El usuario puede iniciar sesión con correo y contraseña." |
| Definition of Done | ¿Qué condiciones generales debe cumplir cualquier incremento antes de considerarlo terminado? | Código revisado, pruebas ejecutadas, integración realizada y documentación necesaria actualizada. |

Los criterios de aceptación pertenecen a un elemento concreto del producto. La Definition of Done funciona como una norma general de calidad para el incremento.

---

# 7. Eventos de Scrum

| Evento | Objetivo | Duración sugerida / límite | Antipatrón típico |
|---|---|---|---|
| Sprint | Crear un incremento de valor y alcanzar el Sprint Goal. | Un mes o menos; comúnmente 1-2 semanas. | Convertirlo en una mini cascada con requisitos congelados sin aprendizaje. |
| Sprint Planning | Establecer qué se hará y cómo se realizará. | Hasta 8 h para Sprint de un mes; proporcionalmente menor para Sprints cortos. | Intentar planificar cada detalle técnico antes de comenzar. |
| Daily Scrum | Inspeccionar el progreso hacia el Sprint Goal y adaptar el plan. | 15 min. | Convertirlo en un reporte para el jefe. |
| Sprint Review | Revisar el resultado y discutir adaptaciones futuras. | Hasta 4 h para Sprint de un mes. | Hacer una presentación unilateral sin conversación. |
| Sprint Retrospective | Identificar mejoras para calidad y efectividad. | Hasta 3 h para Sprint de un mes. | Repetir quejas sin acordar acciones. |

Los límites anteriores se basan en la Scrum Guide y deben reducirse proporcionalmente cuando el Sprint es más corto. [2]

---

# 8. Métricas en Scrum

## Velocity

La velocity representa cuánto trabajo estima completar un equipo en un Sprint, normalmente usando puntos de historia u otra unidad acordada.

**Cómo interpretarla:**

- Sirve para observar tendencias internas.
- Puede ayudar a realizar previsiones cuando el contexto permanece relativamente estable.
- No demuestra por sí sola productividad o valor.

**Cómo no usarla:**

- No debe compararse entre equipos.
- No debe convertirse en una meta de "más puntos cada Sprint".
- No debe utilizarse para juzgar individualmente a los Developers.

## Burndown

Un burndown representa cuánto trabajo pendiente queda a lo largo del tiempo.

```text
Trabajo
  │\
  │ \
  │  \
  │   \
  │    \__
  │       \_
  └──────────── Tiempo
```

Una tendencia descendente puede mostrar que el trabajo restante está disminuyendo. Sin embargo, un burndown no explica por sí solo si se está generando valor ni si las estimaciones fueron buenas.

## Work in Progress (WIP)

El WIP representa el trabajo que ya comenzó pero todavía no terminó.

Un WIP demasiado alto puede indicar multitarea, esperas o bloqueos. Reducirlo puede ayudar a terminar trabajo antes de comenzar más tareas.

---

# 9. Kanban

## 9.1 Fundamentos

Kanban busca mejorar el flujo de trabajo mediante la visualización, límites de trabajo en progreso y mejora evolutiva. La guía oficial de Kanban University identifica prácticas como visualizar el trabajo, limitar WIP, gestionar el flujo, hacer explícitas las políticas y establecer bucles de retroalimentación. [3]

### Principios y prácticas

1. **Visualizar el trabajo:** hacer visible qué está pendiente, en proceso y terminado.
2. **Limitar WIP:** evitar comenzar demasiadas tareas al mismo tiempo.
3. **Gestionar el flujo:** observar cómo se mueve el trabajo y dónde aparecen esperas.
4. **Hacer explícitas las políticas:** definir reglas claras para mover elementos.
5. **Implementar bucles de retroalimentación:** revisar datos y comportamiento del sistema.
6. **Mejorar evolutivamente:** realizar cambios graduales en lugar de intentar transformar todo de una vez.

---

# 10. Tablero Kanban

Una propuesta para un equipo de desarrollo podría ser:

```text
┌───────────┬──────────────┬───────────────┬──────────────┬───────────┐
│ Backlog   │ Por hacer    │ Desarrollo    │ Revisión     │ Terminado │
│           │ WIP: 5       │ WIP: 3        │ WIP: 2       │           │
├───────────┼──────────────┼───────────────┼──────────────┼───────────┤
│ Historia  │ Historia A  │ Historia C    │ Historia F   │ Historia X│
│ Historia  │ Historia B  │ Historia D    │              │ Historia Y│
│ Historia  │ Historia E  │ Historia E    │              │           │
└───────────┴──────────────┴───────────────┴──────────────┴───────────┘
```

### Propuesta de límites

| Columna | WIP sugerido | Razón |
|---|---:|---|
| Backlog | Sin límite estricto | Contiene opciones futuras. |
| Por hacer | 5 | Evita preparar demasiadas tareas simultáneamente. |
| Desarrollo | 3 | Obliga a terminar antes de comenzar trabajo adicional. |
| Revisión | 2 | Evita acumular código esperando revisión. |
| Terminado | Sin límite práctico | Representa trabajo que ya salió del flujo activo. |

Los límites son ejemplos, no valores universales. Deben ajustarse según el tamaño y capacidad del equipo.

---

# 11. Métricas de flujo en Kanban

## Lead Time

Es el tiempo total que transcurre desde que una solicitud entra al sistema hasta que queda entregada.

**Ejemplo:** un cliente solicita una función el lunes y la recibe el viernes. El lead time es aproximadamente cuatro días hábiles.

## Cycle Time

Es el tiempo que tarda un elemento desde que comienza el trabajo activo hasta que termina.

Si una tarea permanece tres días esperando en una cola y luego tarda dos días en desarrollo, el cycle time puede ser de dos días mientras que el lead time será mayor.

## Throughput

Es la cantidad de elementos que terminan durante un período.

Ejemplo:

> El equipo terminó 20 historias durante un mes.

Esto es throughput.

## Diagrama de flujo acumulado

Un CFD representa cantidades de trabajo en diferentes estados a lo largo del tiempo.

```text
Cantidad
  │              Terminado
  │            ┌──────────────
  │         ┌──┘
  │      ┌──┘  Revisión
  │   ┌──┘
  │ ┌─┘ Desarrollo
  │─┘
  └──────────────────────── Tiempo
```

### Cómo leerlo

- El eje horizontal representa el tiempo.
- El eje vertical representa cantidad de elementos.
- Cada banda representa un estado.
- Una banda que aumenta mucho puede indicar acumulación.
- El ancho horizontal de una banda puede ayudar a observar cuánto tiempo permanecen los elementos en ese estado.
- Si el flujo se estabiliza, el sistema puede estar procesando trabajo de manera relativamente constante.

---

# 12. Políticas y clases de servicio

Las **políticas explícitas** indican bajo qué condiciones una tarea puede entrar, salir o cambiar de columna.

Ejemplos:

- Una tarea no entra a Desarrollo si no tiene información suficiente.
- Una tarea no pasa a Terminado si las pruebas fallan.
- Una tarea bloqueada debe marcarse visualmente.
- Una revisión de código debe realizarse antes de cerrar la tarea.

## Clases de servicio

Una clase de servicio es una forma de diferenciar cómo se debe tratar un tipo de trabajo.

| Clase | Ejemplo | Cuándo usarla |
|---|---|---|
| Expedite | Falla crítica en producción | Cuando esperar el flujo normal genera un impacto muy alto. |
| Fixed Date | Requisito legal que debe estar listo antes de una fecha | Cuando existe una fecha externa real. |
| Standard | Funcionalidad normal | Para la mayoría del trabajo. |
| Intangible | Mejora técnica o deuda técnica | Cuando el beneficio puede ser importante pero no es urgente. |

Las clases de servicio deben utilizarse con cuidado. Si todo se marca como urgente, dejan de cumplir su propósito.

---

# 13. ¿Cuándo usar Kanban?

Kanban resulta especialmente conveniente cuando:

- Las solicitudes llegan continuamente.
- Las prioridades cambian con frecuencia.
- El trabajo tiene tamaños diferentes.
- Existen tickets de soporte, mantenimiento o incidencias.
- El equipo necesita mejorar el flujo sin adoptar necesariamente un marco con Sprints.

Por ejemplo, un equipo de soporte de software podría recibir errores de usuarios durante toda la semana. En este escenario, un flujo Kanban puede ser más natural que obligar cada incidencia a esperar hasta el siguiente Sprint.

---

# 14. Design Thinking

## 14.1 Visión general

**Design Thinking** es un enfoque para resolver problemas centrado en las personas. Su objetivo es comprender las necesidades reales antes de comprometer demasiado tiempo y recursos en una solución.

En software puede utilizarse antes o durante el desarrollo para descubrir:

- Qué problema tiene realmente el usuario.
- Qué necesidades son importantes.
- Qué solución podría ser útil.
- Qué supuestos necesitan validarse.

El enfoque popularizado por instituciones como Stanford d.school utiliza actividades de empatía, definición, ideación, prototipado y prueba. [4]

---

# 15. Fases de Design Thinking

| Fase | Objetivo | Técnicas sugeridas | Entregable mínimo |
|---|---|---|---|
| Empatizar | Comprender al usuario y su contexto. | Entrevistas, observación, mapas de empatía. | Hallazgos y necesidades principales. |
| Definir | Convertir los hallazgos en un problema claro. | Punto de vista, preguntas "¿Cómo podríamos...?" | Declaración del problema. |
| Idear | Generar varias soluciones posibles. | Lluvia de ideas, sketching, SCAMPER. | Lista priorizada de ideas. |
| Prototipar | Crear una representación económica de una solución. | Bocetos, wireframes, prototipos de papel. | Prototipo de baja o media fidelidad. |
| Probar | Obtener evidencia con usuarios. | Pruebas de usabilidad, entrevistas, observación. | Resultados y aprendizajes. |

Estas fases no tienen que ejecutarse como una línea rígida. Los resultados de una prueba pueden obligar a volver a definir el problema o generar nuevas ideas.

---

# 16. Mini-caso: aplicación móvil para reservar laboratorios

## Problema

En una institución educativa, los estudiantes necesitan utilizar laboratorios para realizar prácticas. Actualmente deben preguntar presencialmente si el laboratorio está disponible, lo que provoca pérdida de tiempo.

## Empatizar

Actividades:

- Entrevistar a estudiantes.
- Entrevistar a profesores.
- Observar cómo se solicita actualmente un laboratorio.
- Identificar los momentos en que ocurren conflictos de horarios.

**Hallazgos hipotéticos:**

- Los estudiantes no saben qué horarios están disponibles.
- Los profesores necesitan evitar reservas duplicadas.
- Algunos estudiantes solo necesitan consultar disponibilidad.

## Definir

Problema:

> Los estudiantes necesitan conocer rápidamente qué laboratorios están disponibles y reservar un horario sin tener que acudir físicamente con un encargado.

## Idear

Se proponen varias ideas:

1. Aplicación móvil.
2. Página web.
3. Pantalla ubicada en el laboratorio.
4. Sistema de mensajes.

Se selecciona una aplicación móvil porque permitiría consultar disponibilidad desde cualquier lugar.

## Prototipar

Se crea un prototipo de baja fidelidad:

```text
┌──────────────────────────┐
│     LABORATORIOS         │
├──────────────────────────┤
│ Fecha: 15 / 10 / 2026    │
│                          │
│ Laboratorio 1            │
│ 10:00  DISPONIBLE        │
│ [ Reservar ]             │
│                          │
│ Laboratorio 2            │
│ 10:00  OCUPADO           │
│                          │
│ Laboratorio 3            │
│ 12:00  DISPONIBLE        │
│ [ Reservar ]             │
└──────────────────────────┘
```

El prototipo permite discutir la idea antes de programar toda la aplicación.

## Probar

Se pide a cinco estudiantes que intenten:

1. Encontrar un laboratorio.
2. Seleccionar una hora.
3. Realizar una reserva.
4. Cancelarla.

Se observa dónde tienen dificultades.

### Resultado hipotético

Si varios estudiantes no encuentran fácilmente el botón de reserva, se modifica el diseño antes de comenzar el desarrollo completo.

---

# 17. Relación entre Design Thinking, SDLC y Agile

Design Thinking puede reducir el riesgo de **construir correctamente algo que en realidad no resuelve el problema correcto**.

El SDLC normalmente incluye actividades como análisis, diseño, desarrollo, pruebas, despliegue y mantenimiento. Design Thinking puede intervenir especialmente antes y durante el análisis para validar necesidades.

```text
Design Thinking
        │
        ▼
Comprender problema
        │
        ▼
Prototipo / validación
        │
        ▼
Requisitos mejor informados
        │
        ▼
       Scrum
  ┌─────┴─────┐
  │ Sprint    │
  │ desarrollo│
  │ prueba    │
  │ revisión  │
  └─────┬─────┘
        │
        ▼
Producto
        │
        ▼
Retroalimentación
        │
        └──────► nueva investigación / mejora
```

### Design Thinking + Scrum

Design Thinking puede ayudar a descubrir y validar problemas y soluciones. Scrum puede utilizarse posteriormente para convertir las soluciones seleccionadas en incrementos de producto mediante Sprints.

### Design Thinking + Kanban

Kanban puede utilizarse para administrar de manera continua las actividades de investigación, diseño, desarrollo y mantenimiento. Esto resulta especialmente útil cuando las solicitudes cambian constantemente.

### Ejemplo

Para la aplicación de laboratorios:

- Design Thinking ayuda a descubrir qué necesitan estudiantes y profesores.
- Scrum puede organizar el desarrollo de la aplicación en Sprints.
- Kanban puede administrar posteriormente las solicitudes de mantenimiento y errores.

---

# 18. Comparación general

| Característica | Scrum | Kanban | Design Thinking |
|---|---|---|---|
| Enfoque principal | Desarrollo iterativo | Flujo continuo | Descubrimiento y solución de problemas |
| Unidad de trabajo | Sprint | Elemento de flujo | Problema/hipótesis/prototipo |
| Planificación | Al inicio de cada Sprint | Continua | Iterativa |
| WIP | Limitado de forma indirecta por capacidad del Sprint | Se limita explícitamente | Depende del proyecto |
| Retroalimentación | Review y Retrospective | Bucles de feedback | Pruebas con usuarios |
| Cambio de prioridades | Normalmente entre Sprints | Puede ocurrir continuamente según políticas | Puede cambiar la dirección según aprendizajes |
| Mejor escenario | Producto complejo en evolución | Tickets y trabajo continuo | Problema incierto y centrado en usuario |

---

# 19. Conclusiones

Los enfoques ágiles no representan una única receta para desarrollar proyectos. Scrum, Kanban y Design Thinking resuelven problemas diferentes y también pueden combinarse.

**Scrum** me parece adecuado para proyectos académicos de desarrollo de software donde existe un equipo pequeño y se quiere trabajar por etapas. Por ejemplo, una aplicación móvil podría dividirse en Sprints: primero autenticación, después interfaz, posteriormente base de datos y finalmente pruebas.

**Kanban** sería especialmente útil para administrar tareas que llegan continuamente, como errores, solicitudes de mantenimiento o actividades de soporte. La visualización del trabajo y los límites WIP ayudan a evitar que el equipo comience demasiadas tareas sin terminar las anteriores.

**Design Thinking** sería muy útil al inicio de un proyecto cuando todavía no está completamente claro qué necesita el usuario. Para un estudiante que desarrolla una aplicación, entrevistar primero a los usuarios y probar un prototipo sencillo puede ahorrar mucho trabajo posteriormente.

En un contexto académico y profesional, considero que lo más importante no es utilizar una metodología porque esté de moda, sino seleccionar las prácticas que resuelvan el problema real del equipo. Un proyecto puede utilizar Design Thinking para descubrir la necesidad, Scrum para construir el producto y Kanban para administrar posteriormente su mantenimiento.

La principal enseñanza de los enfoques ágiles es que el desarrollo no debería depender únicamente de un plan inicial. El equipo debe observar los resultados, escuchar a los usuarios, medir el flujo y utilizar esa información para mejorar continuamente.

---

# Referencias

1. **Agile Alliance.** *Manifesto for Agile Software Development.* 2001.  
   https://agilemanifesto.org/

2. **Schwaber, K. y Sutherland, J.** *The Scrum Guide: The Definitive Guide to Scrum: The Rules of the Game.* 2020.  
   https://scrumguides.org/scrum-guide.html

3. **Kanban University.** *The Kanban Guide.* Kanban University, 2025.  
   https://kanban.university/kanban-guide/

4. **Stanford d.school.** *Design Thinking Bootleg.* Stanford University, Hasso Plattner Institute of Design.  
   https://dschool.stanford.edu/resources/design-thinking-bootleg

5. **Project Management Institute (PMI).** *Agile Practice Guide.* PMI, 2017.  
   https://www.pmi.org/pmbok-guide-standards/practice-guides/agile

6. **Atlassian.** *What is Kanban?* Atlassian Agile resources, consulta 2026.  
   https://www.atlassian.com/agile/kanban

7. **Scrum.org.** *What is Scrum?* Scrum.org, consulta 2026.  
   https://www.scrum.org/resources/what-is-scrum

---

# Cierre

La gestión ágil puede resumirse como un ciclo de **crear, observar, aprender y adaptar**. Scrum estructura ese ciclo mediante Sprints; Kanban busca que el flujo sea estable y visible; y Design Thinking ayuda a asegurar que el equipo esté resolviendo un problema que realmente importa al usuario.
