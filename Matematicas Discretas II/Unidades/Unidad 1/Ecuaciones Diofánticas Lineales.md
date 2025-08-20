# Introducción

El algoritmo de Euclides, visto en la lección anterior, además de servir para hallar el máximo común múltiplo entre dos números enteros también puede ser usado para encontrar las soluciones de ecuaciones que solo tienen solución en los números enteros.

Una ecuación Diofántica o Diofantina lineal es una ecuación de la forma ax + by = c donde a, b, c ∈ Z y las soluciones x y y deben ser soluciones en los enteros también.

En esta lección se llegará a identificar cuando una ecuación diofántica tiene solución, luego cómo usar el algoritmo de Euclides para hallar la primera solución; después se hablará de cómo encontrar más soluciones y, por último, cómo encontrar las soluciones dentro de un intervalo dado.

El primer reto se enfoca en mostrar que las ecuaciones diofánticas pueden tener una solución simple por tanteo.

![Retos] Encuentre el x, y ∈ Z tal que solucione la ecuación
	4x + 18y = 38

Por inspección el lector puede llegar a encontrar que x = 5 y y = 1, son una solución a la ecuación, pero note que x = − 4 y y = 3, también son una solución. Si el lector quiere puede encontrar más simplemente tanteando.

Pero, ¿se podrá encontrar soluciones siempre por tanteo?, ¿todas las ecuaciones diofánticas siempre tienen solución? El siguiente reto ayudará a responder estas inquietudes.

![Reto] Encuentre el x, y ∈ Z tal que solucione la ecuación
	5x + 10y = 27

Note que si se quieren buscar múltiplos de 5 y 10 que den 27, no se puede encontrar solución. ya que la suma de alguna combinación lineal de estos dos enteros solo puede terminar en 5 o en 0.

Esto permite que se tenga una primera e importante propiedad para resolver las ecuaciones diofánticas y es la siguiente:

![Lema] Si mcd(a, b) = d divide a c, entonces la ecuación Diofántica ax + by = c tiene solución.

## Prueba

Recuerde que las propiedades del máximo común divisor se pueden escribir como combinación lineal de a y b, es decir,

d = ax<sub>0</sub> +by<sub>0</sub> 

pero como d | c, entonces c = dk para algún k ∈ Z. Por lo tanto, si se multiplica la ecuación por k a ambos lados de la igualdad se tiene que

dk = a(kx<sub>0</sub>) + b(ky<sub>0</sub>)  

y como dk = c, entonces

c = a(kx<sub>0</sub>) + b(ky<sub>0</sub>)

y se tiene que las soluciones de la ecuación son (kx<sub>0</sub>) y (ky<sub>0</sub>).

En los retos anteriores, note que en el primero de ellos mcd(4, 18) = 2 y 2 | 38, por lo tanto, para la ecuación se puede encontrar solución.

Para el segundo, 5x + 10y = 25 se tiene que mcd(5, 10) = 5, pero 5 ∤ 27. Así a la ecuación no se le puede hallar ninguna solución.

Ya que se sabe cómo averiguar si una ecuación diofántica tiene solución o no.

La pregunta ahora es: ¿si existe un procedimiento para encontrar las soluciones a una ecuación diofántica?

![imagen de un señor con sombrero amarillo](U1_MF5__img 5.png)

La respuesta es sí y la solución se puede obtener de la misma forma en la que se encuentra el máximo común divisor, es decir, aplicando el algoritmo de Euclides. Como se vio en la lección anterior: encontrar una solución para el máximo común divisor y luego multiplicar por un entero.

Para el primer reto se tenía la ecuación 4x + 18y = 38, como ya se vio el mcd(4, 18) = 2, pero por el algoritmo de Euclides para encontrar el valor se hace:

18 = 44 + 2 

Note que de esta ecuación numérica se puede llegar a que

18 ⋅ (1) + 4 ⋅ (−4) = 2 

Así al multiplicar la ecuación por 19 se llega a que 18(19) + 4(−76) = 38. Así x = 19 y y = − 76. Así, es una solución para la ecuación.

Al comprobar se tiene que 18(19) + 4(−76) = 342 − 304 = 38, lo cual afirma la solución.

Pero esta prueba se dio de forma inmediata el resultado. Ahora, lo que se busca es mostrar cómo funciona el método en ecuaciones diferentes. Para ello, se presentan los siguientes dos ejemplos.

## Ejemplo 1

**Ejemplo** : Resuelve la ecuación Diofántica 13x + 49y = 187

Lo primero que se debe hacer es verificar si la ecuación tiene solución. Para ello se tiene que mcd(13, 49) = 1, por tanto 1 | 189, lo que significa que sí tiene solución al aplicar el algoritmo de Euclides.

49 = 13 * 3 + 10           (1)  

13 = 10 * 1 + 3           (2)  

10 = 3 * 3 + 1            (3)

Ya se sabe que el mcd(13, 49) = 1, por eso no se hace la última ecuación. Ahora se necesita escribir a 1 en términos de 13 y 49. Esto se hace como sigue.

Se toma la ecuación (3) y se despeja el 1. Esto queda

10 ∗ (1) + 3 ∗ (−3) = 1           (4)  

pero acá está el 1 escrito en términos de 10 y 3. Ahora, se toma la ecuación (2) y se despeja el 3, obteniendo

13 ∗ (1) + 10 ∗ (−1) = 3           (5)

al reemplazar (5) en (4) se llega a

10 ∗ (1) + (13 ∗ (1) + 10 ∗ (−1) ) ∗ (−3) = 10 ∗ (1) + 13 ∗ (−3) + 10 ∗ (3) = 10 ∗ (4) + 13 ∗ (−3) = 1           (6)

Esta se escribió en términos de 10 y 13, pero todavía falta, eso se hace con la ecuación (1) que al despejar se obtiene

49 ∗ (1) + 13(−3) = 10           (7)

y reemplazando (7) en (6) se llega a que

(49 ∗ (1) + 13(−3) ) ∗ (4) + 13 ∗ (−3) = 49 ∗ (4) + 13 ∗ (−12) + 13 ∗ (−3) = 49 ∗ (4) + 13 ∗ (−15) = 1           (8)

Se escribe el máximo común divisor como combinación lineal de 13 y 49; pero esta no es la solución de la ecuación. Para llegar a esta se debe multiplicar por 187 y se obtiene

13 ∗ (−2805) + 49 ∗ (748) = 187            (9)  
y así se obtiene la solución

## Ejemplo 2

**Ejemplo** : Encuentre la solución a la ecuación Diofántica 34x +20y = 440

Recuerde que lo primero que se debe verificar es que la ecuación tiene solución, para ello se calcula el mcd(34, 20) = 2 y 2 | 440.

Para encontrar la solución se debe aplicar el algoritmo de Euclides.

34 = 20 * 1 + 14           (10)  

20 = 14 * 1 + 6           (11)  

14 = 6 * 2 + 2           (12)

Como en el ejemplo anterior se obvia la última ecuación debido a que ya se sabía que el máximo común divisor es 2.

Tomando la ecuación (12) y despejando 2, se obtiene

14 ∗ (1) + 6 ∗ (−2) = 2           (13)

y ahora se toma la ecuación (11) y si se despeja el 6 se llega a que

20 ∗ (1) + 14 ∗ (−1) = 6           (14)

al reemplazar (14) en (13)

14 ∗ (1) + (20 ∗ (1) + 14 ∗ (−1) ) ∗ (−2) = 14 ∗ (1) + 20 ∗ (−2) + 14 ∗ (2) = 14 ∗ (3) + 20 ∗ (−2) = 2           (15)

De la ecuación (10) se despeja 14 y se obtiene

34 ∗ (1) + 20 ∗ (−1) = 14           (16)  

Al reemplazar (16) en (15), se llega a que

( 34 ∗ (1) + 20 ∗ (−1) ) ∗ (3) + 20 ∗ (−2) = 34 ∗ (3) + 20 ∗ (−3) + 20 ∗ (−2) = 34 ∗ (3) + 20 ∗ (−5) = 2           (17)  

Es decir, que se escribe a 2 en términos de 34 y 20, pero para encontrar la solución a la ecuación se debe multiplicar toda la ecuación por 220, y por lo tanto

34 ∗ (660) + 20 ∗ (−1100) = 440

da las soluciones x = 660 y y = −1100

# Teorema

Una preocupación que todavía falta resolver es cómo encontrar las demás soluciones, ya que se sabe que si la ecuación tiene solución, esta tiene infinitas soluciones. El siguiente teorema aclara la forma de encontrar las demás soluciones.

![Teorema] Si la ecuacion ax + by = c tiene solicion x<sub>0</sub> y y<sub>0</sub>, las demas soluciones estan dadas por las ecuaciones
	x = x<sub>0</sub> + (b/d)t
	y = y<sub>0</sub> - (a/d)t            (18)
	donde d = mcd(a, b) y t ∈ Z

Al reemplazar t por cualquier entero en las ecuaciones de (18), se encuentran todas las soluciones.

Se quieren encontrar todas las soluciones positivas, es decir, cuando tanto x y y son positivas y satisfagan la ecuación. Lo primero que se debe hacer es escribir todas las posibles soluciones y estas son:

x = −2805 + 49t

y = 748 − 13t           (19)  
  

Y se debe analizar cuando estas son positivas, esto pasa cuando x > 0 y y > 0. Si x > 0, se tiene que −2805 + 49t > 0 al despejar t, se tiene

t > 2805/49 ≈ 57.2448977

por tanto t ≥ 58

Si y > 0, se tiene que 748 − 13t > 0 al despejar t, se llega a

t < 748/13 ≈ 57.538461

por tanto t ≤ 57.

Como no hay intersecciones no podemos encontrar ninguna solución positiva.

Ahora para el ejemplo 4 todas las soluciones son

x = 660 + 10t

y = −1100 − 17t           (20)  

De nuevo se debe analizar si x > 0 y y = 0.

Si x > 0, se tiene 660 + 10t > 0, al despejar t, se obtiene que

t > −660/10 = −66

Por lo tanto t ≥ −65  

Si y > 0, se tiene que −1100 − 17t > 0; al despejar $t$ se obtiene que

t < −1100/17 ≈ 64.70588  

por tanto t ≤ −65

Así que solo hay un valor que satisface y es cuando t = −65. Al reemplazar en las dos ecuaciones de (22) se llega a que x = 10 y y = 5, que al reemplazarlas en la ecuación diofántica se llega a que 34 ∗ (10) + 20 ∗ (5) = 440, lo que comprueba que es solución.

## Ejercicios

Se invita al estudiante a practicar lo visto en la lección.
Archivo descargado...

## Referencias bibliográficas

- Andrica, D., y Andreescu, T. (2009). Number theory: structures, examples, and pro‐ blems. Birkhäuser Boston.
- Burton, D. (2010). Elementary Number Theory. Ebook. McGraw Hill. ‐Grigorieva, E. (2018). Methods of Solving Number Theory Problems. Springer International Publishing.
- Rosen, K. H. (1999). Discrete mathematics & applications. McGraw‐Hill.
- Stevens, J. (s. f.). Olympiad Number Theory Through Challenging Problems. [https://s3.amazonaws.com/](https://s3.amazonaws.com/) cdn.artofproblemsolving.com/resources/articles/olympiad‐number‐theory.pdf

