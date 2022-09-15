# Instructivo de Uso

## Uso Simple
<br>
Para ejecutar el algoritmo una única vez, se procede con
la línea:

```bash
$ python3 modelosTP2_entrega.py
```

Lo cual puede tener dos resultados posibles:

### El algoritmo encuentra un nuevo máximo

Se imprimirá por consola cual fue el máximo, junto con
su semilla para replicarlo. Por ejemplo:

```
Nuevo minimo encontrado! => 488
Con la semilla: 0.9728406867979249
El la ejecucion n° 1

El mejor tiempo fue 488; con la semilla: 0.9728406867979249
 - Ejecucion finalizada!
```
Esto llevará a que un archivo metadata_mejorlavadoTP2.txt sea
creado, que servirá para que el programa tenga guardado este
último máximo para ejecuciones futuras, y quede accesible la semilla para replicarlo.
También será creado un archivo modelosTP2_Result.txt, con el
formato de solución pedido.

### El algoritmo no encuentra un nuevo máximo

Imrpimirá por consola el resultado de esta ejecución con
su semilla, sin realizar ningún cambio en archivos.

```
El mejor tiempo fue 528; con la semilla: 0.2061375398509141
 - Ejecucion finalizada!
```

## Uso Múltiple

<br>
Para ejecutar el algoritmo una varias veces, se procede con
la línea simple, pero con un número entero (ej, 100) de la forma:

```bash
$ python3 modelosTP2_entrega.py 100
```

El programa nos avisará cada vez que un nuevo mínimo
sea encontrado de forma similar a la ejecución simple
(modificando también los archivos de solución y metadata),
a la vez que también un indicador de porcentaje de ejecución
total:

```
 - Ejecucion n° 0, 0%

Nuevo minimo encontrado! => 487
Con la semilla: 0.780192438883334
El la ejecucion n° 10


Nuevo minimo encontrado! => 483
Con la semilla: 0.10883752294732796
El la ejecucion n° 16

 - Ejecucion n° 25, 25%
 - Ejecucion n° 50, 50%

Nuevo minimo encontrado! => 482
Con la semilla: 0.36795581291347756
El la ejecucion n° 60


Nuevo minimo encontrado! => 476
Con la semilla: 0.5290375352776632
El la ejecucion n° 70

 - Ejecucion n° 75, 75%
 - Ejecucion finalizada!
```

En los archivos de metadata y solución sólo quedarán
los datos del mínimo en total de todas las ejecuciones.

## Reproducción con una Semilla

<br>
Para ejecutar el algoritmo con una semilla, se llama
al programa con un float (ej, 0.06414813076250481), de la forma:

```bash
$ python3 modelosTP2_entrega.py 0.06414813076250481
```

Esto será similar al uso simple, pero para un resultado
que se espera reproducir:

```
Nuevo minimo encontrado! => 439
Con la semilla: 0.06414813076250481
El la ejecucion n° 1

El mejor tiempo fue 439; con la semilla: 0.06414813076250481
 - Ejecucion finalizada!
```