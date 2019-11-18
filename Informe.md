# Informe Trabajo Final

## Integrantes:
- Dante Moreno
- Natalia Maury
- Joaquín Galván

## Introducción:
Durante el ciclo se han visto diversos algoritmos para realizar programas eficientes y de complejidad baja en su peor caso. Para ello se utilizan estrategias como fuerza bruta, backtracking, programación dinámica, uso de grafos, etc. Por este motivo para resolver el problema de empaquetamiento propuesto en el trabajo final se utilizarán los algoritmos aprendidos durante el ciclo académico para que sea lo más eficiente posible. Cada integrante del grupo deberá presentar una solución diferente al mismo problema.

## Objetivo del Estudiante (Student Outcome)
Todos los integrantes del grupo estudian ciencias de la computación, por lo que el objetivo del estudiante es reconocer las responsabilidades profesionales y tomar decisiones informadas sobre prácticas de computación basadas en principios
legales y éticos.

## Estado del Arte: De los algoritmos revisados para el trabajo
El problema propuesto en el trabajo final es conocido con diversos nombres como el problema de la mochila, problema de embalaje de contenedores, problema de anidamiento, etc. Sin embargo, este problema fue propuesto por en los 21 problemas de NP-Completos de Richard Karp en el siglo XX. El problema en si consiste en maximizar el valor que se almacenará en el contenedor sin exceder el peso o capacidad máxima de este (Wikipedia; 2019). 

Para resolver este problema han surgido diversos algoritmos con diferentes técnicas pero la más óptima es la que utiliza programación dinámicao o algoritmos voraces. Este tipo de programación es como un divide y vencerás, pero la diferencia es que se evalua cada elemento una sola vez y si forma parte de la solución será considerado, pero en caso no lo forme será descartado de inmediato y ya no será tomado en cuenta para la solución al problema. También se puede resolver este problema en tiempo lineal utilizando optimizació (Wikipedia; 2019).

## Aporte: Demuestra ética profesional en el ejercicio de la profesión (analiza y muestra la importancia de hallar la complejidad algorítmica considerando a los algoritmos como tecnología)
Una de las formas de en las que se demuestra el profesionalismo es utilizando la herramienta GitHub. En esta herramienta se presentan los commits del trabajo periódicamente para demostrar el progreso. También se utilizan Milestones e issues que se le asignan a cada integrante del grupo para terminar el trabajo a tiempo. Con GitHub se puede facilitar el trabajo grupal y a la vez demostrar profesionalismo al hacerlo. 

La ética se demuestra con los commits donde se puede verificar el avance del trabajo y qué integrante realizó dicho avance. El trabajo debe ser avanzado y reportar los avances antes de que termine el Milestone. Al realizar los commits se demuestra compromiso y responsabilidad con el trabajo, además también demuestra puntualidad ya que se deben de realizar antes de que sea la fecha límite (Milestones). Si el trabajo se sube horas antes de la presentación, no demuestra ética ni profesionalismo porque sería un descuido por parte del equipo no reportar ningún avance, lo que puede generar dudas sobre su originalidad. Además, se realizó investigación de ciertos temas y para demostrar la honestidad y dar crédito al autor original al que le pertenece la información se utilizan las referencias cortas. 

## Diseño de Aplicativo para Pruebas: Presenta pseudocódigo de algoritmos que resuelvan el problema tratado, y demuestra responsabilidad en el diseño, implementación y validación de la solución y casos de prueba.
Debido a que el grupo está compuesto de tres integrantes, se deberá presentar una solución diferente por integrante. A continuación estarán los pseudocódigos de cada miembro del grupo y la lógica explicada de cada algorítmo.

### Algoritmo Natalia
Debido a que la solución más óptima utiliza programación dinámica, se implementará una solución que utiliza programación dinámica en su solución. La programación dinámica utiliza divide y vencerás donde superpone las soluciones a los subproblemas y así encontrar la solución al problema mayor de una forma más trivial. La lógica del algoritmo es que utilizará las matrices de los planos para verificar el espacio disponible en el contenedor. Si la caja no entra, será agregada al vector de cajas que no entraron en el contenedor que luego serán reevaluadas. En caso la caja sí entre en el contenedor será agregada al vector de cajas del contenedor. 

Las estructuras a utilizar son:
* MyRec= vector que contiene todas las cajas.

* cc = vector que contiene las cajas que se han puesto en un contenedor

* cn = vector que contiene las cajas que no entraron en el contenedor y serán reevaluadas

* VecCont = Vector que contenga los "VecCajasCont" para tener cuántos contenedores se usaron.

* Vc = volumen de la caja actual a evaluar.

* avc = volumen de la caja del vector "cn" a evaluar

* Vol = volumen del contenedor disponible (Cada vez que se pone una caja, se el volumen de la caja con el volumen disponible para saber cuánto espacio disponible queda).

* PlanoXY = matriz que representa el plano xy del contenedor donde se considera su ancho (eje x) y el largo (eje y) del contenedor. La matriz está inicializada en 0 porque el contenedor está vacío. Cuando se se utiliza un espacio de la matriz se cambia el valor a 1.

* PlanoXZ = matriz que representa el plano xz del contenedor donde se considera su ancho (eje x) y el largo (eje y) del contenedor. La matriz está inicializada en 0 porque el contenedor está vacío. Cuando se se utiliza un espacio de la matriz se cambia el valor a 1.

* PlanoYZ = matriz que representa el plano yz del contenedor donde se considera su ancho (eje x) y el largo (eje y) del contenedor. La matriz está inicializada en 0 porque el contenedor está vacío. Cuando se se utiliza un espacio de la matriz se cambia el valor a 1.

A continuación se mostrará el pseudocódigo:

def AlgoritmoNatalia(MyRec, cc, cn):
    PlanoXY = [[0] * ancho for _ in range(largo)]
    PlanoXZ = [[0] * ancho for _ in range(alto)]
    PlanoYZ = [[0] * largo for _ in range(alto)]

    v = Ancho * Alto * Largo     
    vo = 0                       
    vd = v                       
    c = 1                        
    m = len(cc)                  
    dxy = 0                      
    dxz = 0                      
    dyz = 0

    for i in range(MyRec):
       vc = MyRec[i].ancho * MyRec[i].largo * MyRec[i].alto
       if vc <= vd:
           dxy = BuscarEspacioDisponible(PlanoXY, Ancho, Largo)
           dyz = BuscarEspacioDisponible(PlanoYZ, Largo, Alto)
           dxz = BuscarEspacioDisponible(PlanoXZ, Ancho, Alto)

           if MyRec[i].ancho <= dxy and MyRec[i].largo <= dyz and  MyRec[i].alto <= dxz:
                ColocarCaja(PlanoXY, Ancho, Largo, MyRec[i].ancho, MyRec[i].largo)
                ColocarCaja(PlanoYZ, Largo, Alto, MyRec[i].largo, MyRec[i].alto)
                ColocarCaja(PlanoXZ, Ancho, Largo, MyRec[i].ancho, MyRec[i].alto)
                cc.append(MyRec[i])
                vd -= vc
       else:
           for j in range(len(cn)):
                avc = cn[j].ancho * cn[j].alto * cn[j].largo
                if avc <= vd:
                    if cn[i].ancho <= dxy and cn[j].largo <= dyz and cn[i].alto <= dxz:
                        ColocarCaja(PlanoXY, Ancho, Largo, cn[i].ancho, cn[j].largo)
                        ColocarCaja(PlanoYZ, Largo, Alto, cn[i].largo, cn[j].largo)
                        ColocarCaja(PlanoXZ, Ancho, Alto, cn[i].ancho, cn[j].alto)
                        cc.append(cn[i])
                        del cn[i]
                        vd -= avc
                
                else:
                    cn.append(MyRec[i])
      vo = v - vd
          

### Algoritmo Dante
Debido a la elevada complejidad de resolver el problema de empaquetamiento en tres dimensiones de manera eficiente, el planteamiento que se ha tenido busca evitar elevar demasiado el tiempo de cálculo aplicando programación dinámica. Esto implica que se necesitará memoria.

Debido a que pueden existir distintas cajas del mismo modelo, se usa una indexación simple con un arreglo de identificadores:
arrID = [['A', (tamaño en x, tamaño en y, tamaño en z)],
         ['B', (tamaño en x, tamaño en y, tamaño en z)], ...] 
Así, el parámetro de las funciones de cálculo reduce su tamaño, consistiendo de un cajas representadas como

caja = [(id, rotación), (posición en x, posición en y, posición en z)]

donde id es el índice en arrID que contiene la información de tamaño e identificador. El uso de duplas y tripletas propone evitar confusión en el acceso de datos del código.
El mayor problema con aplicar programación dinámica es el manejo de memoria.Por eso, en lugar de ocupar variables en las tablas que caracterizan este acercamiento a los problemas, se usarán archivos auxiliares que ocupan espacio en ROM, mas no en RAM. En estos archivos se guardarán las "pilas" de cajas hipotéticas.
Esto último se plantea con la matriz _waste_ para cada plancha; que tiene como dimensiones las cajas que se buscan ordenar y las 6 rotaciones posibles. Guarda el máximo espacio libre en x, y, z. 
Así, el algoritmo:
busca la primera opción (greedy) de la tabla con la que pueda entrar (su dimensión en x es menor al mayor espacio libre en X).
Luego, busca entrar en el contenedor, leyendo la información guardada en waste[n° de la última caja guardada][rotación de la nueva caja] como un string que indica la ruta del archivo que guarda las demás cajas en ese contenedor.
De no ser posible entrar, rota (avanza una columna en waste).
Si en ningún momento logró entrar, el algoritmo presenta una falla en la cual considera otro contenedor. Esto por la complejidad de aplicar backtracking más complejo.

### Algoritmo Joaquín
En base al problema dado, y a su gran complejidad, se han tomado una serie de decisiones que facilitaran la elección de las posiciones de las cajas. Las elecciones, estructuras y el orden son:
* El cambio en el sentido de los rectángulos: Lo primero que se debe hacer es cambiar el sentido de las "cajas" para que su dimensión X sea la mayor, seguida por la dimensión en Y. Como resultado de esto la dimensión Z siempre es la menor.
* Orden de los paralelepípedos: En segunda instancia, se debe ordenar el arreglo de rectángulos, llamado MyRec, según el tamaño en X. Esto nos permite estar seguros de que cada elemento es igual o mas pequeño que el anterior, en cuanto respecta a X.
* Se construyen las estructuras "Tower": Estos elementos se construyen apilando cajas una sobre otra hasta llegar al tope en Z. La creación de cada tower va de abajo para arriba. Para saber en donde se debe poner la primera caja se tiene un arreglo pos que tiene dentro una coordenada del plano, este comienza en (0,0,0). El programa ubica las cajas "bases" de las towers dimensión por dimensión. Es decir, cada vez que se elige el lugar de una base, al arreglo pos aumenta en su primer elemento, se le suma el lado de la caja que acaba de ser puesta, debido a que este le corresponde a X, el segundo a Y y el tercero a Z. Una vez que se llena el espacio disponible en x su variable correspondiente en el arreglo se reinicia y al segundo elemento de pos se le suma el ancho que tienen las cajas que tienen como parte de su coordenada x =0. El ciclo se repite hasta que acabe el espacio en y, no nos preocupamos por z ya que las torres ocupan ese espacio. Cuando se elige la base la torre se construye y una vez terminada busca el espacio para la siguiente base.

## Validación de Resultados y Discusión: Muestra tablas comparativas del consumo de recursos de memoria y tiempo.
Para realizar la validación de resultados se realizaran tablas comparativas del consumo de recursos como la memoria y el tiempo.

## Conclusiones y Trabajos Futuros: Emite juicios considerando el impacto de la solución propuesta en el contexto global, impacto social, ambiental y económico
La solución presentada tiene diversos impactos en diferentes ámbitos como el global, social, ambiental y económico, por lo que se explicará detalladamente cada uno de ellos a continuación:

### Impacto social:

### Impacto ambiental:
El problema de empaquetamiento se ve reflejado en la organización de paquetes en contenedores de cualquier tipo. Por ejemplo, en barcos que transportan carga internacional en grandes contenedores, una mejora en la administración de espacio no solo disminuiría los costos al poder llevar más carga. También reduciría la cantidad de viajes necesarios para llevar estos productos, disminuyendo consumo de combustibles, e incluso el riesgo de derrames contaminantes al tener menos tráfico en el mar.

### Impacto global:
Todo lo que se quiera transportar se tiene que empaquetar. Es algo obvio y que se hace al rededor del mundo ya sea para celulares que se tienen que transportar desde una fabrica a sus tiendas respectivas o para enviar víveres a quienes más lo necesiten. Independientemente de ello, un empaquetamiento eficiente reduce el numero de entregas que se tienen que hacer juntos el costo de este. Esto facilita y mejora las conexiones entre cualquier entidad que que se encuentra a distancia de otra.

### Impacto económico:
Al realizar menos cantidad de viajes para transportar los elementos en un contenedor maximizando la mayor cantidad de elementos transportados la compañía puede ahorrar en temas de transporte y pagar menos contenedores para movilizar los elementos. Por ello, la solución al problema de empaquetamiento tiene un impacto positivo económicamente porque permitirá optimizar la cantidad de viajes realizados, también puede ahorrar en el combustible utilizado para transportar el material y no utilizar contenedores de más ello.

## Conclusiones (Indicando las ventajas y desventajas de los algoritmos considerados y brindando opiniones sobre los resultados obtenidos)
Debido a que el problema presentado forma parte de los 21 problemas NP completos de Richard Karp, aún no tiene una solución óptima. Por ello, en el algoritmo se intentó resolver el problema de la manera más eficiente posible intentando reducir su complejidad lo mayor que se puede. Para implementar la solución, cada uno de los algoritmos utilizó diferentes técnicas. El algoritmo Dante utiliza una combinación de backtracking y programación dinámica para implementar la solución.  La parte de backtracking está presente al momento de reevaluar la solución cuando el archivo "mistake" se crea, en ese momento el algoritmo sabe que no encontró una solución al momento de ordenar la caja anterior, así que tampoco podrá ordenar esta. Esto es un fallo ya que debería considerar saltar opciones, pero esta lógica lo evita. La programación dinámica se encuentra en que guarda los resultados obtenidos en un archivo donde guarda las soluciones obtenidas en ese momento. El algoritmo Natalia combina fuerza bruta y programación dinámica, donde el elemento de la fuerza bruta es que prueba todas las cajas para verificar que pueden entrar en el contenedor y que el algoritmo no es recursivo. No obstante, no se utiliza fuerza bruta al 100% porque es muy costoso y probar todas las posiciones posibles daría una complejidad muy alta, por ello, su presencia en el algoritmo se encuentra en probar todas las cajas a evaluar (vector MyRec) y las cajas a reevaluar (vector cn). La programación dinámica se encuentra en las matrices para colocar las cajas donde se almacenan las posiciones de las cajas puestas en el contenedor. El algoritmo Galván utiliza un algoritmo tipo greedy, en el cual se construyen las torres en la primera instancia que se vea posible. Una versión mejora implicaría el uso de de backtracking para, una vez formadas las torres, mover las bases hasta encontrar la mejor opción.

Cada uno de los algoritmos utilizados para intentar resolver el problema presenta desventajas su uso. La desventaja de utilizar el algoritmo Dante es que utiliza gran cantidad de recursos de memoria para su solución. Aunque se intentó utilizar archivos para reducir la cantidad de memoria utilizada en la RAM, se generaron muchos archivos lo que utiliza mucha memoria. La desventaja de utilizar el algoritmo Natalia es que sólo funciona para calcular un contenedor para transportar las cajas y utiliza muchos recursos para la solución como por ejemplo las 3 matrices para representar los planos. La desventaja de utilizar el algoritmo Galván es que al crearse las torres se deja una espacio vacío considerable entre las cajas más altas. Debido que estas se van haciendo más pequeñas y no ocupan todo el espacio disponible que queda entre ellas y las cajas mas altas de otras torres.

No obstante, cada uno de los algoritmos también tienen ventajas al utilizarlos. La ventaja del algoritmo Natalia es que al utilizar matrices que represente a cada uno de los planos se puede tener una forma bastante acertada sobre el uso del contenedor y cuánto espacio disponible tiene, aunque de forma costosa con la memoria. La ventaja de utilizar el algoritmo Dante es la variedad de casos que considera. La ventaja de utilizar el algoritmo Galván es. 

## Anexos
### Profesionalismo:
Según Concepto.de, profesionalismo es la forma de desarrollar una actividad profesional con un compromiso total, siguiendo pautas preestablecidas socialmente, responsabilidad y mesura. Para considerar que una persona ha realizado un trabajo de manera profesional se deben cumplir diversos requisitos. Uno de los requisitos es demostrar un compromiso mayor a lo normal en el trabajo. Otro de ellos es el uso del vocabulario adecuado en la comunicación, la puntualidad con las fechas establecidas, y ética profesional (Concepto.de; S/F).

### Ética:
Según Concepto.de, la ética profesional se basa en el conjunto de normas y valores para mejorar el desarrollo de las actividades profesionales. Se encarga de desarrollar las pautas del desarrollo laboral mediante valores universales como la puntualidad, responsabilidad, estudio, constancia, concentración, carácter, etc. Dichos valores son centrados para la práctica laboral. Si se cumplen con todos los valores y normas, se demostrará que el trabajo realizado es digno, probando su honestidad y moral, lo que es importante para el futuro. La ética profesional también puede ser complementada con los valores individuales del profesional y el código oficial de ética permitiendo al individuo tomar mejores decisiones en el trabajo (Concepto.de; S/F).

### Fuerza Bruta:
Esta es una de las técnicas aplicadas para resolver problemas en espacios de búsqueda. Fuerza Bruta prueba todas las opciones posibles para resolver el problema y aquí se mide la fuerza de la computadora. Se recomienda utilizar en problemas de menor escala porque se basa en probar todas las posibles opciones para resolver el problema. Por ello, si se aplica en un problema de una escala mayor, como probará todas las opciones para resolver el problema su complejidad en su peor caso aumentará.

### Backtracking:
Es una técnica utilizada para resolver problemas que requieren un espacio de búsqueda. Esta técnica utiliza los legales para verificar si el estado es posible, y en caso sea continúa recursivamente para ver si por ese estado se puede llegar al estado objetivo. En caso se llegue a un estado en el que no se llegará a la solución, regresa al estado anterior para probar siguiente estado. Se recomienda utilizar mayormente en problemas de mayor escala porque se basa en la recursividad para resolver el problema. Por ello, si se aplica en un problema de una escala menor o muy pequeña, por la recursividad hará que la complejidad del problema en su peor caso aumente. Para calcular la complejidad se debe de utilizar el teorema maestro para el caso de la recursividad.

### Divide y vencerás:
Si un problema al dividirlo, los sub-problemas son iguales al problema inicial; entonces el problema inicial puede resolverse al resolver los sub-problemas. Para poder realizar esto, los sub-problemas deben ser resueltos de forma recursiva y luego combinarlos para poder resolver el problema inicial planteado.

### Programación dinámica:
Según Cormen, Leiserson, Rivest y Stein, esta estrategia utiliza el concepto de divide y vencerás que es dividir el problema en subproblemas para hallar la solución al problema principal. No obstante, a diferencia de divide y vencerás, no combina los subproblemas para encontrar la solución al problema principal. Programación dinámica resuelve cada subproblema una vez y guarda la solución en una tabla, por ello, es que cuando se encuentra un subproblema que comparte una solución que ya ha encontrado antes, no la computa de nuevo porque ya la tiene en una tabla por lo que evita realizar cálculos u operaciones de más. La programación dinámica se aplica principalmente a problemas de optimización. Cuando se desarrolla un algoritmo que utiliza programación dinámica sigue una secuencia de 4 pasos. El primer paso es definir la estructura de la solución más óptima. El segundo paso es recursivamente definir la solución óptima. El tercer paso es computar del valor de una solución óptima. El último paso es construir la solución óptima con la información ya computada (Cormen, Leiserson, Rivest, Stein; 2009).

## Bibliografía
Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C. (2009). Introduction to Algorithms, 3rd Edition. MIT Press

Concepto.de (S/F). Ética profesional. Recuperado de https://concepto.de/etica-profesional/ [Consultado el 17 de octubre del 2019].

Concepto.de (S/F). Profesionalismo. Recuperado de https://concepto.de/profesionalismo/ [Consultado el 17 de octubre del 2019].

Wikipedia (2019). Problema de la mochila. Recuperado de https://es.wikipedia.org/wiki/Problema_de_la_mochila [Consultado el 21 de octubre del 2019]
