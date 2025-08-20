# Introducción

En la sección anterior se trabajó con el algoritmo de la división en esta sección se continua aplicando, pero en este caso se asume que r=0r=0 y se define:

![Definicion] Dados dos numeros a y b, con b ≠ 0, decimos que b divide a a y se escribe b | a si existe un c ∈ Z tal que bc = a.

Cuando b | a, también se puede decir que a es múltiplo de b o que b es un divisor de a.  
Si b no divide a a, se escribe b∤a. Esto significa que no existe tal c∈Z que permite escribir a a como producto de enteros.  
En los siguientes ejemplos, se pretende determinar la divisibilidad o no divisibilidad de un número por otro.

**Ejemplo**
	Determine si el numero a = 72 es divisible por b = 18

La respuesta es que sí, ya que existe q=4∈Z, tal que 72=18⋅4. Por lo tanto, 18∣72.  

**Ejemplo**
	Determine si el numero a = 43 es divisible por b = 13

La respuesta es que nono, ya que no existe q∈Z, tal que 43=13⋅q. Por lo tanto, 13∤43.

**Ejemplo**
	Determine si el numero a = -78 es divisible por b = 14

La respuesta es que nono, ya que no existe q∈Z, tal que −78=14⋅q. Por lo tanto, 14∤(−78).

**Ejemplo**
	Determine si el numero a = -48 es divisible por b = -12

La respuesta es que sí, ya que existe q=4∈Z, tal que −48=(−12)⋅4. Por lo tanto, (−12)∣−48.

# Propiedades de la división

Las siguientes son propiedades de divisibilidad

![Teorema] Sean a, b y c números enteros que satisfacen lo siguiente: 
1. a | 0 
2. 1 | a 
3. a | a (Reflexividad) 
4. Si a | b y b | a, entonces a = ± b (Antisimetría) 
5. Si a | b y b | c, entonces (Transitividad) 
6. Si a | b, entonces | a | ≤ | b |
7. Si a | b y a | b±c, entonces a | c 
8. Si a | b y a | c, entonces a | bx + cy para x, y ∈ Z

Se invita al lector a hacer la prueba de las propiedades 1, 2, 3, 4.

Para la propiedad 5, suponga que a | b y b | c son ciertas, por lo tanto, existen k, l ∈ Z  tal que b = a ⋅ k  y c = b ⋅ l respectivamente. Ahora si se reemplaza la primera de estas suposiciones en la segunda se obtiene que c = (a ⋅ k) ⋅ l, que es lo mismo que c = a (kl), lo que implica que a | c

Para la prueba de 6, considere que | k | ≥ 1, por tanto | b | = | a || k | ≥ | a |, lo que prueba la propiedad.

Para el 7, por definición de divisibilidad, se tiene que b = ak y b+c=al con k, l ∈ Z y al reemplazar la primera en la segunda se obtiene ak+c=al y despejar c se llega a que

c = al − ak = a(l − k)

lo que significa que a | c.

Para la prueba de la propiedad 8, se invita al lector a verificarla de forma autónoma.

Muchas de las propiedades, son usadas para mostrar otras propiedades o probar cuando algunas expresiones son divisibles por algún entero.

**Ejemplo**
	Encuentre todos los enteros positivos n para los cuales
		( n + 1) | ( n^2 + 1 )

Para este ejemplo, se puede empezar a revisar cada uno de los números desde n=1, pueden haber algunos valores que cumplan y otros que no, pero como encontrar todos los que de verdad cumplen y asegurar que solo esos cumplen la propiedad.

Para eso se debe hacer una prueba que dé todos los valores que satisfacen aplicando propiedades algebraicas, entonces

n^2 + 1 = (n^2 − 1) + 2 = (n + 1)(n − 1) + 2 

Note que n + 1 divide a (n + 1)(n − 1), pero como se necesita que divida a todos los términos, entonces n + 1 debe dividir a dos y esto solo sucede para n = 1. Siendo el único valor que cumple.

Los siguientes retos se hacen de forma similar aplicando propiedades algebraicas, se le dejan al lector.

![Reto] Resuelve los siguientes ejercicios usando divisibilidad:
1. Si 7 | 3x + 2, probar que 7 | 15x^2 - 11x - 14
2. 3 | a y 3 | b si y solo si 3 | a^2 + b^2

##### Recomendación

Para el primer reto, se debe factorizar el polinomio 15x^2−11x−14 y se llega a la conclusión.

Para el segundo reto, se debe aplicar la propiedad 8.

## Ejercicios

Los siguientes ejercicios son para practicar se le dejan al lector
Archivo Descargado.

## Referencias bibliográficas

- Andrica, D., y Andreescu, T. (2009). Number theory: structures, examples, and pro‐ blems. Birkhäuser Boston.
- Burton, D. (2010). Elementary Number Theory. Ebook. McGraw Hill. ‐Grigorieva, E.(2018). Methods of Solving Number Theory Problems. Springer International Publishing.
- Rosen, K. H. (1999). Discrete mathematics & applications. McGraw‐Hill.
- Stevens, J. (s. f.). Olympiad Number Theory Through Challenging Problems. [https://s3.amazonaws.com/cdn.artofproblemsolving.com/resources/articles/olympiad](https://s3.amazonaws.com/cdn.artofproblemsolving.com/resources/articles/olympiad)‐number‐theory.pdf

