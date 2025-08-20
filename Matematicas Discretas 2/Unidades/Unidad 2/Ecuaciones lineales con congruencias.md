# Introducción

Continuando con lo hablado en la clase anterior, se quiere simplificar un poco el cálculo de las potencias tomando el exponente en base 2.

Por ejemplo, el último cálculo que se hizo en la clase anterior fue encontrar el residuo al dividir 167<sup>54</sup>  por 29. El exponente es 54, que escrito en base 2 es 110110. Esto significa que 54 se puede escribir como una vez el 32, más una vez el 16, más cero veces el 8 y una vez el 4 y una vez el 2. Recuerde que en el ejercicio anterior se tenía que 167<sup>54</sup> ≡ 22<sup>54</sup> mod 29. El paso a seguir es el siguiente:

22 ≡ 22 mod 29 
22<sup>2</sup> ≡ 20 mod 29
22<sup>4</sup> ≡ 23 mod 29
22<sup>8</sup> ≡ 7 mod 29 
22<sup>16</sup>≡ 20 mod 29 
22<sup>32</sup> ≡ 23 mod 29 

Por tanto,

22<sup>54</sup> = 22 <sup>32</sup> 22<sup>16</sup> 22<sup>4</sup> 22<sup>2</sup> ≡ 23 ∗ 20 ∗ 23 ∗ 20 ≡ 211600 ≡ 16 mod 29

Como se ve, es mucho más fácil hacer los cálculos pero eso depende de que tan grande es el exponente. Se deja al estudiante los siguientes ejercicios

**Ejercicios** : Encuentre los residuos de los siguiente números, según el modulo.
	43<sup>18</sup> mod 13
	18<sup>33</sup> mod 42
	13<sup>76</sup> mod 65
También en archivo...

# Teorema y corolarios

Otra propiedad que es importante dentro de las congruencias, es la propiedad de cancelación, que ayuda a simplificar las congruencias:

![Teorema] Si ca ≡ cb mod n, entonces a ≡ b mod (n / d), donde d = mcd(c, n)

Note que si 33 ≡ 15 mod 9, que también se puede escribir 3 ∗ 11 ≡ 3 ∗ 5 mod 9, pero mcd(3, 9) = 3, por tanto, 11 ≡ 5 mod 3.

Como resultados complementarios a estos, estan los siguientes dos colorarios que son consecuencias inmediatas del teorema.

![Corolario] Si ca ≡ cb mod n y mcd(c, n) = 1 entonces a ≡ b mod n.

Otro resultado consecuencia del teorema es:

![Corolario] Si ca ≡ cb mod p y p ∤ c, donde p es un numero primo, entonces a ≡ b mod p.

# Ecuaciones con congruencias

Ahora se quiere resolver ecuaciones con congruencias, es decir dada la ecuación:
	ax = b mod n
Se debe determinar si se puede, o no, encontrar una solución y, si se puede, determinar como buscarla.

Note primero que por la definición de congruencia, si se tiene ax = b mod n, es lo mismo que tener n | (ax - b). Y por la definición de divisibilidad, existe y en los enteros, tal que ny = ax - b, al despejar b se obtiene que ax - ny =b, que es una ecuación diofántica. Es decir, la ecuación ax ≡ b mod n si mcd(a, n) | b, tiene la misma condición que tienen las ecuaciones diofánticas.

Con la condición anterior ya se sabe cuando una ecuación de la forma ax ≡ b mod n tiene solución. Ahora se necesita saber si tiene una única solución o muchas.

El hecho que d | b donde d = mcd(a, n), da algo importante y es que la ecuación tiene d soluciones incongruentes módulo n. Esto se da por las soluciones de las ecuaciones diofánticas. Recuerde que cuando se encuentra una solución x<sub>0</sub> , las demás soluciones están dadas por la ecuación x = x<sub>0</sub> + (n / d) * t. Así que todas las soluciones se dan de la siguiente manera:
	x<sub>0</sub>, x<sub>0</sub> + (n / d), x<sub>0</sub> + (2n) / d, x<sub>0</sub> + (3n) / d,..., x<sub>0</sub> + [ (d - 1) n ] / d

Se sabe que son todas soluciones dadas por las ecuaciones diofánticas, resta probar que sean incongruentes y esto se consigue si se toman dos de estas soluciones y se suponen congruentes, se llega a una contradicción, así: sean x<sub>0</sub> + sn / d y x<sub>0</sub> + rn / d dos soluciones de las de arriba mencionadas, es decir, s y r son dos enteros tales que están entre 0 y d- 1, con s ≠ r.

Si ellas son congruentes módulo n, entonces se tiene que:
	x<sub>0</sub> + sn / d ≡ x<sub>0</sub> + rn / d
Note que se pueden cancelar las x<sub>0</sub> simplemente restando a ambos lados x<sub>0</sub> así la congruencia queda:
	sn / d ≡ rn / d mod n

Ahora note que mcd(n, n / d) = n / d, así por el último teorema de la clase anterior se llega a que s ≡ r mod n / (n / d) eso quiere decir que s ≡ r mod d, como r y s son menores que d, se tiene que la única forma que sean congruentes es que sean iguales, por tanto, ellas son incongruentes y así las dos soluciones tomadas.
De lo anterior se tiene que si mcd(a, n) = d y d | b, entonces la ecuación tiene d soluciones incongruentes.

## Ejemplos

Visualiza los siguientes ejemplos haciendo clic en cada uno de ellos para ampliar la información:

**Ejemplo 1** : Encontrar todas las soluciones de la ecuacion 15 x ≡ 6 mod 9

Note que el mcd(15, 9) = 3 y 3 | 6, por tanto, la ecuación debe tener 3 soluciones incongruentes. Hay una solución trivial a la ecuación y esta se da cuando x = 1, como las otras soluciones se dan por la ecuación
	x = 1 + 3 t

con t = 1, 2, entonces las demás soluciones son x = 4 y x = 7.

En verdad, cualquier ecuación de la forma $ax\equiv b \mod n$ tiene más que las soluciones mencionadas anteriormente, lo que pasa es que las otras son congruentes módulo $n$, por tanto, se consideran la misma. Con este hecho, en el ejemplo anterior si se reemplaza en $t=3$, se llega a que $x=10$, pero $10≡1mod9$. O si se toma $t=7$, entonces $x=22$, pero $22 ≡ 4\mod9$. Por lo tanto, las tres respuestas que se dieron arriba son las soluciones de la ecuación $15x≡6\mod9$.
## Resto de Ejemplos en Archivo

# Cálculo del modo inverso

El último método es relativamente nuevo, fue descubierto por Christina Doran, Shen Lu y Barry R. Smith en su artículo ``A new algorthm for computing inverses in modular arithmetic``. Consiste en calcular el inverso mediante el algoritmo de Euclides del mcd(n2,an+1), el mayor residuo en el cálculo del algoritmo que sea menor que nn, es el inverso.

Se debe calcular para el ejercicio el mcd(169,66), cuando se llegue al mayor residuo menor que 13, se dice que ese es el inverso.
	169 = 66 ∗ 2 + 37
	66 = 37 ∗ 1 + 29
	37 = 29 ∗ 1 + 8 

Por lo tanto el inverso es 8 y el ejercicio se termina como en el primer método.

El último método parece el más eficiente, pero se deja al estudiante que él elija la forma de encontrar el inverso.

**Ejemplo** Encuentre al menos una solución de la ecuación 127x ≡ 37 mod 211

Note que mcd(127, 211) = 1 y 1 | 37, por tanto tiene solución. Usando el último método se encuentra el inverso de 127 módulo 211. Se debe calcular por medio del algoritmo de Euclides $mcd(211^2,211∗127+1)=mcd(44521,26798)$, Al desarrollarlo se obtiene que:
	$44521 = 26798 ∗ 1 + 17723$ 
	$26798 = 17723 ∗ 1 + 9075$ 
	$17723 = 9075 ∗ 1 + 8648$ 
	$9075 = 8648 ∗ 1 + 427$
	$8648 = 427 ∗ 20 + 108$

Por tanto, 108 es el inverso de 127, módulo 211, eso significa que 127 ∗ 108 ≡ 1 mod 211. Para resolver la ecuación se debe multiplicar 108 a ambos lados y se obtiene 127 ∗ 108 x ≡ 37 ∗ 108 mod211 y al reducirlo se obtiene x ≡ 198 mod 211. Así el valor que satisface la ecuación es x = 198.

# Video Clase
Con el propósito de ampliar y profundizar el tema de esta lección, observa la siguiente video clase antes de adelantar los ejercicios:
![Videoclase: Ecuaciones lineales con congruencia](https://youtu.be/jqgjwx6hX_A)

# Ejercicios

Los siguientes ejercicios son para la practica, el estudiarlos ayudará mucho en su desempeño en el examen.
En archivo...