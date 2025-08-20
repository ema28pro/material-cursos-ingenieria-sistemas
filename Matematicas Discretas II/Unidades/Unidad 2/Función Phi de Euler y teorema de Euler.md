# Función Phi(ϕ) de Euler

Observa la siguiente presentación:

Se comenzará con una pregunta que conducirá a la definición de la función de Euler: ¿Cuántos números enteros positivos menores que 12 son primos relativos con 12? Es bastante fácil, simplemente se listan todos los números del 1 al 11 y escogiendo los que son primos relativos con 12 se llega a que son 4. Es decir, si se tiene la lista:
	1 2 3 4 5 6 7 8 9 10 11

Se deben seleccionar los que son primos relativos con el 12 y estos son los números que no son pares y tampoco múltiplos de 3.
	==1== 2 3 4 ==5== 6 ==7== 8 9 10 ==11==
Así que son 4 los números que satisfacen la propiedad.

Si se toma a 15 y se hace la misma pregunta se llega a que son 8, si de nuevo se hace la lista:
	1 2 3 4 5 6 7 8 9 10 11 12 13 14
De nuevo se toman todos los que no son múltiplos ni de 3, ni de 5 y se obtiene que
	==1 2== 3 ==4== 5 6 ==7 8== 9 10 ==11== 12 ==13 14==
De donde se obtienen los 8 elementos que se dijeron que eran primos relativos con 15.


![Definición] La función ϕ : N --> N que envía a cada n ∈ N en el número de enteros positivos menores que n que son primos relativos con n.

Note que esta función representa los números que se dieron arriba como ejemplos, por tanto, ϕ(12) = 4 y ϕ(15) = 8. Pero encontrar esto para números suficientemente grandes no es tan fácil si se hace una lista y después se escogen los que son primos relativos con n.

Para ello se construirá una fórmula que ayudará a calcular este número de una forma más sencilla. Se advierte que esta fórmula depende de la factorización de n y como este problema es tan complicado entonces trabajar con números muy grandes sigue siendo complejo.

Se comenzará mirando que pasa con los números primos:
	$\phi(2) = 1$
	$\phi(3) = 2$
	$\phi(5) = 4$
	$\phi(7) = 6$
	$\phi(11) = 10$
	$\phi(13) = 12$
	$\phi(17) = 16$

Con esto es suficiente para notar que $\phi(p) = p - 1$ para pun número primo. Es claro que si un número es primo, ningún número positivo menor que el lo divide, excepto el 1, pero este es primo relativo con él.

Ahora, qué pasa con una potencia de un número primo p.
Se comienza con $p ^ 2$
	$\phi(4) = 2 = 4 - 2$
	$\phi(9) = 6 = 9 - 3$
	$\phi(25) = 20 = 25 - 5$
	$\phi(49) = 42 = 49 - 7$
	$\phi(121) = 110 = 121 - 11$
	$\phi(169) = 156 = 169 - 13$
	$\phi(289) = 172 = 189 - 17$

Se nota que entonces $\phi(p ^ 2) = p ^ 2 - p$

En general, el estudiante puede comprobar que $\phi(p ^ n) = p ^ n - p ^ (n - 1)$.

Pero note que sólo se trabajó con potencias de números primos, pero ¿Qué sucede cuando es multiplicación de dos primos?

Si el estudiante comprueba con números que sean de la forma $pq$ con $p$ y $q$ números primos, debe llegar a que $\phi(pq) = (p - 1)(q - 1)$ Si se quiere saber qué pasa con $p²q$, entonces debe llegar a que $\phi(p ^ 2 * q) = (p ^ 2 - p)(q - 1)$ y, en general, a que ϕ(p<sup>n</sup> q) = (p<sup>n</sup> p<sup>n-1</sup>)(q-1).

Si se sigue con este proceso puede notar que ϕ(p<sup>n</sup> * q<sup>m</sup>) = (p<sup>n</sup> - p<sup>n - 1</sup>)(q<sup>m</sup> - q<sup>m - 1</sup>)

Una generalización del problema da la siguiente fórmula si n = p<sub>1</sub><sup>n<sub>1</sub></sup> p<sub>2</sub><sup>n<sub>2</sub></sup> p<sub>3</sub><sup>n<sub>3</sub></sup> p<sub>4</sub><sup>n<sub>4</sub></sup> p<sub>k</sub><sup>n<sub>k</sub></sup> , entonces:
	ϕ(n) = (p<sub>1</sub><sup>n<sub>1</sub></sup> - p<sub>1</sub><sup>n<sub>1</sub>-1</sup>) (p<sub>2</sub><sup>n<sub>2</sub></sup> - p<sub>2</sub><sup>n<sub>2</sub>-1</sup>) (p<sub>3</sub><sup>n<sub>3</sub></sup> - p<sub>3</sub><sup>n<sub>3</sub>-1</sup>) . . . (p<sub>k</sub><sup>n<sub>k</sub></sup> - p<sub>k</sub><sup>n<sub>k</sub>-1</sup>)

Que se puede reescribir como:
	ϕ(n) = p<sub>1</sub><sup>n<sub>1</sub></sup> p<sub>2</sub><sup>n<sub>2</sub></sup> p<sub>3</sub><sup>n<sub>3</sub></sup> p<sub>4</sub><sup>n<sub>4</sub></sup> . . . p<sub>k</sub><sup>n<sub>k</sub></sup> (1 - 1 / p<sub>1</sub>) (1 - 1 / p<sub>2</sub>) . . . (1 - 1 / p<sub>k</sub>)

Que es lo mismo que tener:
	$\phi(n)= n(1 - 1/p_{1})(1 - 1/p_{2}) ...(1- 1 p k )$

Así, por ejemplo, si se quiere calcular:
	$\phi(12) = phi(2 ^ 2 * 3) = 12(1 - 1/2)(1 - 1/3) = 12(1/2)(2/3) = 2 * 1 * 2 = 4$

Con un número más grande, si se quiere calcular:
	$\phi(1000) = phi(2 ^ 3 * 5 ^ 3) = 1000(1 - 1/2)(1 - 1/5) = 1000(1/2)(4/5) = 100 * 1 * 4 = 400$
Por lo tanto, hay 400 enteros positivos que son menores que 1000 y primos relativos con 1000.

# Teorema de Euler

Ya que se sabe como calcular el número de primos relativos con n, que son menores que n. Ahora se mostrará su aplicación, para ello se enuncia el siguiente teorema.

![Teorema] Sea n ∈ Z, con n ≥ 2 y sea a un entero tal que mcd(a, n) = 1, entonces a<sup>ϕ(n)</sup> ≡ 1 mod n

El anterior es el teorema de Euler y ayuda a simplificar el cálculo de residuos que involucren potencias. Además, note que de este teorema se desprende el de Fermat, pues si se toma n = p, donde p es un número primo, como ϕ(p) = p − 1, entonces a<sup>p−1</sup> ≡ 1 mod p, siempre y cuando mcd(a, p) = 1.

**Ejemplo** : Encuentre los dos últimos dígitos de 17<sup>2015</sup>.

Cuando se pregunta por los dos últimos dígitos de una potencia se debe dividir por 100m ya que con esto se asegura que el residuo va a tener máximo dos dígitos.

Ahora, se tiene que mcd(17, 100) = 1, por lo tanto, aplica el teorema de Euler y como ϕ(100) = 40 (verifique), entonces 17<sup>40</sup> ≡ 1 mod 100. Al elevar por 50 se llega a que:
	(17<sup>40</sup>)<sup>50</sup> = 17<sup>2000</sup> ≡ 1 mod 100

Y así sólo resta encontrar cuánto es 17<sup>15</sup> mod 100.

Volviendo a las técnicas de antes, esto se calculará pasando 15 a la base 2, para lo cual queda 1111 y así:
	17 ≡ 17 mod 100 
	17<sup>2</sup> ≡ 89 mod 100
	17<sup>4</sup> ≡ 21 mod 100
	17<sup>8</sup> ≡ 41 mod 100

Lo cual lleva a que:
	17<sup>15</sup> = 17<sup>8</sup> 17<sup>4</sup> 17<sup>2</sup> 17<sup>1</sup> ≡ 17 ∗ 89 ∗ 21 ∗ 42 = 1334466 ≡ 66 mod 100

Y por lo tanto:
	17<sup>2015</sup> = 17<sup>2000</sup> 17<sup>15</sup> ≡ 1 ∗ 66 = 66 mod 100.

**Ejemplo** :  Calcule el residuo que deja 43<sup>57853</sup> cuando se divide por 51.

Note que mcd(43, 51) = 1 y como 51 es compuesto, se puede aplicar el teorema de Euler. Como ϕ(51) = 32 (verifique), entonces
	43<sup>32</sup> ≡ 1 mod 51

Ahora al elevar este a la 1807, se llega a que 43<sup>57824</sup> ≡ 1 mod 51. Resta encontrar a que es igual 43<sup>29</sup> módulo 51. Para ello se escribe 29 en base 22 y es igual 11101 y así:
	43 ≡ 43 ≡ 51 
	43<sup>2</sup> ≡ 13 ≡ 51 
	43<sup>4</sup> ≡ 16 ≡ 51
	43<sup>8</sup> ≡ 1 ≡ 51
	43<sup>16</sup> ≡ 13 ≡ 51

Y por tanto:
	43<sup>29</sup> = 43<sup>16</sup> 43<sup>8</sup> 43<sup>4</sup> 43 ≡ 1 ∗ 1 ∗ 16 ∗ 13 = 208 = 4 mod 51

Y por tanto:
	43<sup>57853</sup> = 43<sup>57824</sup> 43<sup>29</sup> ≡ 1 ∗ 4 = 4 mod 51

# Ejercicios
Los siguientes ejercicios son para la practica.
En archivo...