# Introducción

La relación de los números varias veces ayudan a encontrar propiedades de los números enteros y otras clases de conjuntos numéricos como lo son los números racionales. Además, este concepto puede ser aplicado a la criptografía, las ternas pitagóricas, las fracciones continuadas, entre otros.

![Definicion] Sean a y b numeros enteros, no ambos cero, se define como el entero positivo d tal que:
1. d | a y d | b.
2. Si existe un numero a ∈ Z tal que c | a y c | b, entonces c ≤ d o c | d.

Se denota mcd(a,b) = d y se dice que d es el máximo común divisor entre a y b. En palabras, el máximo común divisor significa, que entre todos los divisores de a y b, se toman los que dividen a ambos y entre ellos el mayor.

**Ejemplo** : Halle el maximo comun divisor, entre los siguientes valores dados:
1. El mcd(18, 4) = 2
2. El mcd(21, 4) = 1
3. El mcd(8, 40) = 8

Para el primer ejemplo, los divisores de ambos números son:  

|                 |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- |
| Divisores de 4  | 1   | 2   | 4   |     |     |     |
| Divisores de 18 | 1   | 2   | 3   | 6   | 9   | 18  |

En la siguiente figura se muestran los divisores comunes:

|                 |       |       |     |     |     |     |
| --------------- | ----- | ----- | --- | --- | --- | --- |
| Divisores de 4  | **1** | **2** | 4   |     |     |     |
| Divisores de 18 | **1** | **2** | 3   | 6   | 9   | 18  |

Y como se nota el máximo de los comunes es 2

|                 |       |     |     |     |     |     |
| --------------- | ----- | --- | --- | --- | --- | --- |
| Divisores de 4  | **1** | *2* | 4   |     |     |     |
| Divisores de 18 | **1** | *2* | 3   | 6   | 9   | 18  |

En el segundo ejemplo, los dos números tienen divisores:

|                 |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
| Divisores de 4  | 1   | 2   | 4   |     |     |
| Divisores de 21 | 1   | 2   | 3   | 7   | 21  |

Note que en este caso el único divisor en común es el 1

|                 |       |     |     |     |     |
| --------------- | ----- | --- | --- | --- | --- |
| Divisores de 4  | **1** | 2   | 4   |     |     |
| Divisores de 21 | **1** | 2   | 3   | 7   | 21  |

Por lo tanto, el máximo común divisor entre 4 y 21 es igual 1.
Para el tercer ejemplo, los divisores comunes son:

|                 |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Divisores de 8  | 1   | 2   | 4   | 8   |     |     |     |     |
| Divisores de 40 | 1   | 2   | 4   | 5   | 8   | 10  | 20  | 40  |

Los divisores comunes son:

|                 |       |       |       |       |       |     |     |     |
| --------------- | ----- | ----- | ----- | ----- | ----- | --- | --- | --- |
| Divisores de 8  | **1** | **2** | **4** | **8** |       |     |     |     |
| Divisores de 40 | **1** | **2** | **4** | 5     | **8** | 10  | 20  | 40  |

Al tomar el máximo de los comunes es 88

|                 |       |       |       |     |     |     |     |     |
| --------------- | ----- | ----- | ----- | --- | --- | --- | --- | --- |
| Divisores de 8  | **1** | **2** | **4** | _8_ |     |     |     |     |
| Divisores de 40 | **1** | **2** | **4** | 5   | _8_ | 10  | 20  | 40  |

En el ejemplo dos se vio que el máximo común divisor es igual a 11, cuando esto pasa se define como:

![Definicion] Cuando mcd(a, b) = 1 se dice que a y b son primos relativos o coprimos.

Esto significa, que a∤b y b∤a, pero también significa que el único divisor común entre a y b es 1. Por otro lado, los números a y b no necesariamente deben ser primos para ser primos relativos.

El método usado para buscar el máximo común divisor en los ejemplos anteriores no es lo suficientemente efectivo debido a que para números demasiado grandes su factorización puede ser difícil de hacer, por tanto, encontrar todos los posibles divisores de a y b, es un ejercicio muy complicado.

En sí, el problema de buscar el máximo común divisor entre dos números se complica, debido a los pocos algoritmos que existen para factorizar números naturales. Existen varios métodos para encontrar y algunas propiedades que ayudan a simplificar el cálculo pero estos computacionalmente.

![Teorema] Sean a, b, c ∈ Z, entonces:
1. Cada divisor común de a y b es divisor de mcd(a, b)
2. Si a | bc y el mcd(a, b) = 1, entonces a | b
3. Si mcd(a, b) = 1 y mcd(a, c) = 1, entonces el mcd(a, bc) = 1
4. Si m∈ Z, entonces mcd(a + m · b, b) = mcd(a, b).
5. mcd(a, b) = mcd(| a |, | b |)
6. Si k es un entero, entonces mcd(ka, kb) = | k |mcd(a, b)
7. Si mcd(a, b) = 1, entonces para cualquier entero c, mcd(ac, b) = mcd(c, b)
8. Si mcd(a, b) = d, entonces mcd(a/d, b/d) = 1
9. El mcd(a, b) siempre se puede expresar como combinación lineal de a y b, es decir, que existen enteros x y y tales que mcd(a, b) = ax + by.
10. mcd(a, b), donde a y b no son ambos cero, se puede definir alternativamente y equivalentemente como el menor entero d tal que d = ax + by con x, y ∈ Z

A continuación, se hace la prueba de algunas propiedades, las demás se le dejan al lector para que las ensaye.

Prueba de 2 Suponga que a | bc y mcd(a, b) = 1. Por definición de divisibilidad se tiene que existe un k ∈ Z tal que ak = bc y debido a que el mcd(a, b) = 1, entonces a ∤ b, asi a | c

Prueba 4. Suponga que el mcd(a + mb, b) = d, se debe probar que d = mcd(a ,b). Note que d | a + mb y d | b, por la propiedad 7 de divisibilidad, se concluye que d | a. Ahora se debe probar que sí existe otro valor. Suponga l ∈ Z tal que l | a  y l | b, entonces l | d. Pero como ll divide a los dos valores divide a cualquier combinación lineal de ellos, en particular l | a + mb. Así l | a + mb y l | b, lo que significa que l | d. Ya que d = mcd(a + mb, b).

**Ejemplo** : Los numeros en la sucesion 101, 104, 109, 116, dots son de la forma a<sub>n</sub> = 100 + n^2, donde n = 1, 2, 3,... . halle el maximo valor de mcd(a<sub>n</sub>, a<sub>n+1</sub>) 

Note que:

mcd(a<sub>n</sub>, a<sub>n+1</sub>) = mcd(100+n^2, 100 + (n + 1)^2)
	= mcd(100 + n^2, 100 + (n + 1)^2 − 100 − n^2)            propiedad 4
	= mcd(100 + n^2, 2n + 1)
	= mcd(200 + 2n^2, 2n + 1)            mcd(2, 2n + 1) = 1
	= mcd(200 + 2n^2 − n(2n + 1), 2n + 1)             propiedad 4
	= mcd(200 − n, 2n + 1)
	= mcd(400 − 2n, 2n + 1)            mcd(2, 2n + 1) = 1
	= mcd(401, 2n + 1)            propiedad 4

Por lo tanto, la respuesta es 401 y se obtiene cuando n = 200

![Ejemplo] Probar que la fracción (21n + 4)/(14n +3)

Por la propiedad 9, se puede tomar x = −2 y y = 3 y así se llega a que:

mcd(21n + 4, 14n + 3) = −2(21n + 4) +3(14n+ 3) = −42n − 8 + 42n + 9 = 1

y por la propiedad 10, este es el menor que cumple esto y, por lo tanto, es el máximo común divisor, lo que significa que nunca van a tener factores en común. Así, la fracción es irreducible.

Un algoritmo bueno y que permite encontrar de una manera "sencilla" el máximo común divisor es el que se conoce como el algoritmo de Euclides, que se basa en el algoritmo de la división.

# Algoritmo de Euclides

Dados dos números a y b enteros, se supone sin pérdida de generalidad que a≥b, entonces el algoritmo funciona de la siguiente manera:

Se utiliza el algoritmo de la división al dividir a por b, lo que se obtiene  

a=bq<sub>1</sub> + r<sub>1</sub>

0 ≤ r<sub>1</sub> < b

Si r1=0, entonces se dice que mcd(a, b) = b, sino es decir, si r<sub>1</sub> ≠ 0, entonces se divide a b por r1, lo que lleva a

b = r<sub>1</sub>q<sub>2</sub> + r<sub>2</sub>

0 ≤ r<sub>2</sub> < b

De nuevo, si r<sub>2</sub> = 0, entonces mcd(a, b) = r<sub>1</sub> , si esto no se cumple, se divide a r1 por r2 aplicando el algoritmo de la división,

r<sub>1</sub> = r<sub>2</sub>q<sub>3</sub> + r<sub>3</sub>

0 ≤ r<sub>3</sub> < b

Si  r<sub>3</sub> = 0, entonces mcd(a, b) = r<sub>2</sub>, sino, se continua con el proceso hasta que r<sub>n+1</sub> sea igual a cero. Es decir, el proceso continua y se llega a

r<sub>n-1</sub> = r<sub>n</sub>q<sub>n+1</sub> + r<sub>n+1</sub>

0 ≤ r<sub>n</sub> + 1 < r<sub>n</sub>

y como r<sub>n+1</sub> = 0, entonces r<sub>n</sub> = mcd(a, b)

A continuación, se presentarán algunos ejemplos que ayudan a probar cómo funciona el algoritmo de Euclides.  
Al aplicar el algoritmo de Euclides, se tiene  

84 = 18 ∗ 4 + 12 
18 = 12 ∗ 1 + 6 
12 = 6 ∗ 2 + 0

Por tanto, mcd(18, 84) = 6 

**Ejemplo** : Encuentre el mcd(24, 49) usando el algoritmo de Euclides.

Aplicando el algoritmo de Euclides, se obtiene que:

49 = 24 ∗ 2 + 1 
24 = 1 ∗ 24 + 0 

Así el mcd(24, 48) = 1

**Ejemplo** : Encuentra el mcd(184, 28) usando el algortimo de Euclides.

Aplicando el algoritmo de Euclides, se obtiene que:

184 = 28 ∗ 6 + 16 
28 = 16 ∗ 1 + 12
16 = 12 ∗ 1 + 4 
12 = 4 ∗ 3 + 0 

Por tanto, mcd(184, 28) = 4 

Otro término importante que tiene que ver con la comparación de números enteros es el del mínimo común múltiplo el cual se define a continuación:

![Teorema] Dados dos numeros enteros a y b, no ambos cerom se define el minimo comun multiplo m con las siguientes dos condiciones:
1. a | m y b | m
2. Si existe un c ∈ Z tal que a | c y b | c, entonces m | c.

El mínimo común múltiplo se denota por m = mcm(a, b) y se dice que mm es el mínimo común múltiplo entre a y b.

**Ejemplo** :  Encuentre el mcm(5, 16) = 80

**Ejemplo** : Encuentre el mcm(12, 9) = 36

De nuevo, calcular el mínimo común múltiplo se convierte en un problema de factorización, que como se mencionó anteriormente es muy difícil de hacer para números grandes. El siguiente teorema muestra una forma fácil de encontrar el mínimo común múltiplo:

![Teorema] mcm(a, b)mcd(a, b) = ab para un par de enteros a y b, no ambos cero.

Este teorema, hace la búsqueda del mcm(a, b), sea sólo la búsqueda del mcd(a,b) y así, se puede escribir el  

mcm(a, b) = (ab / mcd(a, b) )

## Ejercicios

A continuación se comparten varios ejercicios para que el estudiante practique.
Archivo descargado...

## Referencias biliográficas

- Andrica, D., y Andreescu, T. (2009). Number theory: structures, examples, and pro‐ blems. Birkhäuser Boston.
- Burton, D. (2010). Elementary Number Theory. Ebook. McGraw Hill. ‐Grigorieva, E. (2018). Methods of Solving Number Theory Problems. Springer International Publishing.
- Rosen, K. H. (1999). Discrete mathematics & applications. McGraw‐Hill.
- Stevens, J. (s. f.). Olympiad Number Theory Through Challenging Problems. [https://s3.amazonaws.com/cdn.artofproblemsolving.com/resources/articles/olympiad](https://s3.amazonaws.com/cdn.artofproblemsolving.com/resources/articles/olympiad)‐number‐theory.pdf

