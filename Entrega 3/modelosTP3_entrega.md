# Resolución del Problema Utilizando Programación Lineal Entera
## Enunciado
 - Una lavandería tiene que lavar prendas, algunas pueden ir juntas y otras no (destiñen).
 - El tiempo de cada lavado es el tiempo que lleva lavar la prenda más sucia de ese lavado.

## Análisis del problema
Se trata de una variación del problema de coloración de grafos. Es decir, un problema de solución no polinómica que deberá ser resuelto utilizando Programación Lineal Entera.
Se tendrá entonces un grafo para el que deberán colorearse sus vértices, respetando que ningún adyacente comparta tinte; minimizando entonces el máximo valor de cada color.
Para modelizar la situación, se supondrá cada prenda como un vértice del grafo (con su valor siendo su tiempo de lavado), cada desteñido como una arista, y cada lavado como un color distinto.

## Objetivo
Determinar cuáles prendas y en qué número de lavado asearlas para un intervalo de tiempo p,con el objetivo de minimizar la suma total de tiempos de lavado, en base a las restricciones de desteñido.
## Hipótesis y Supuestos
 - Toda prenda deberá pertenecer a un lavado.
 - Se supondrá que la suciedad de una prenda está completamente relacionada con su tiempo de lavado, por lo que "la prenda más sucia de ese lavado" _(enunciado)_ se tomará como sinónimo de "la prenda con mayor tiempo de lavado".
 - Se buscará evitar completamente el desteñimiento. Si no se logra, se considerará que no es una solución al problema.
 - El tiempo de lavado de una prenda será una constante, y no se verá afectada por ningún factor (como, por ejemplo, la cantidad de prendas con las que comparte lavado).
 - El tiempo de un lavado respetará a rajatabla el enunciado, y no se verá afectado por ningún factor (como, por ejemplo, el cargado de jabón según la cantidad de prendas que contenga). 
 - Un lavado no podrá fallar.
 - Un lavado tendrá capacidad infinita: siempre y cuando se cumplan las restricciones, podrá contener cualquier cantidad de prendas.
 - La cantidad total de lavados no se considerará a minimizar.
 - No se considerarán gastos por electricidad, agua, etcétera.
 - Siendo $n$ la candidad de prendas por lavar, el modelo "verá" $n$ lavados. Un lavado con tiempo cero representará entonces un lavado no efectuado.
 - Una vez una prenda forma parte de un lavado, esta
    - Tendrá que lavarse durante todo su tiempo de lavado 
    - No podrá ser realocada hacia otro lavado ("lavarse de a partes")
 - A la hora de minimizar, no se considerará la posibilidad de realizar múltiples lavados a la vez. Es decir, se minimizará el tiempo de lavado efectivo, independientemente de si es en paralelo con múltiples lavadoras o no.

## Definición de Variables y Constantes
 - $i = 1, 2, ..., n$
 - $j = 1, 2, ..., n$
 - $C_{i}$: Tiempo de lavado de una prenda $i$ [min/p; **constante**]
 - $L_{ij}$: Representa que una prenda $i$ forma parte de un lavado $j$ [bivalente]
 - $T_{j}$: Tiempo que tarda en realizarse un lavado $j$ [min/p]
 - $Y_{ij}$: Representa que la prenda $i$ es la que tiene el máximo tiempo de limpieza de su lavado $j$ [bivalente]

## Funcional
Como se busca minimizar el tiempo total de lavados, el funcional entonces será:

$$Min\\;\\:Z = \displaystyle\sum_{j=1}^{n} T_{j}$$



## Restricciones

1) Cada prenda $i$ no podrá formar parte de más de un lavado, y tendrá que sí o sí pertenecer a uno. La siguientes restricciones lo asegurarán:

$$\displaystyle\sum_{j=1}^{n} L_{ij} = 1;\\;\\;\forall i = 1, ... ,n$$

2) Por cada prenda $k$ que sería desteñida si fuera lavada junto a $l$, deberá existir la siguiente restricción para asegurar que nunca compartan lavado:
    $$L_{kj} + L_{lj} \leq 1; \\;\\; \forall j = 1, ... ,n$$
    
    Esta restricción también podría, con el afán de no escribir manualmente cada ecuación, definirse utilizando una **constante** $D_{ik}$ (que represente que las prendas $i$ y $k$ serán desteñidas si son lavadas juntas), tal que:
    $$L_{ij} + L_{kj} \leq 1 + M(1-D_{ik}); \\;\\; \forall i,j, k = 1, ... ,n;\\;\\; i \neq k$$
    
    Nótese que de esta última forma la cantidad de ecuaciones resultantes sería, en la gran mayoría de los casos, mucho mayor.
    
3) La variable $T_{j}$ deberá tomar el valor máximo (operación $max$) entre el tiempo de lavado de todas sus prendas. Entonces:
    $$\displaystyle\sum_{i=1}^{n} Y_{ij} = 1; \\;\\; \forall j = 1, ... ,n$$
    $$L_{ij}C_{i} \leq T_{j} \leq L_{ij}C_{i} + M(1 - Y_{ij});\\;\\; \forall i, j = 1, ... ,n$$
    
    Nótese que $C_{i}$ es una constante, por lo que puede multiplicarse por variables sin perder linealidad.
