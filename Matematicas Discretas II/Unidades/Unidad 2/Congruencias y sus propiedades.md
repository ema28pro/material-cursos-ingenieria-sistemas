# Introducción

La aritmética modular es un sistema de aritmética para números enteros, que considera el residuo. En la aritmética modular, los números “vuelven” a llegar a una cantidad fija dada (esta cantidad dada se conoce como módulo) para dejar un resto. La aritmética modular a menudo está vinculada a los números primos, por ejemplo, en el teorema de Wilson, el teorema de Lucas y el lema de Hensel; y generalmente aparece en campos como la criptografía, la informática y el álgebra informática.

Un uso intuitivo de la aritmética modular es con un reloj de 12 horas. Si ahora son las 10:00, en 5 horas el reloj marcará las 3:00 en lugar de las 15:00. 3 es el resto de 15 con un módulo de 12.

Observa la siguiente definición:

![Definicion] Sea n un entero positivo fijo. Dos enteros, a y b, se dice que son congruentes modulo n, lo cual se simboliza por:
	a ≡ b mod n            si n | a - b

Según definición, si se fija un entero cualquiera, por ejemplo, el número n = 13, entonces 28 ≡ 2 mod 13, ya que 13 | (28−2). Por otro lado, −23 ≡ 3 mod 13, ya que 13 | (−23−3), pero no es el único número que es congruente con el número −23, ya que −23 ≡ −10 mod 13, débido a que 13 | (−23−(−10) ).

Si a y b son tales que n ∤ (a−b) se dice que a y b son incongruentes módulo n y esto se escribe así:

a ≢ b mod n 

Con el mismo número n = 13, se puede notar que 18 ≢ 2, puesto que 13 ∤ (18−6)

Para reforzar un poco el concepto presentado en la sección de la introducción, se expondrán a continuación algunos retos para los estudiantes:

1. Si n = 23, determine cuál de los siguientes números no es congruente con 4 módulo n:
	- [ ] -19
	- [x] -27
	- [ ] 4
	- [ ] 27
	**_Comentario_** :  
		¡Tu respuesta es correcta!
		Lo único quede se debe de hacer es restar 4, con cualquiera de las opciones y la que no de un múltiplo de 23 es la opción a elegir
2. ¿Cual es el mayor numero entero negativo que es congruente con 17 modulo 21?
	- [x] -4
	- [ ] -17
	- [ ] -46
	- [ ] -25
	**_Comentario_** :  
	¡Tu respuesta es correcta!  
	
	Se debe hacer la resta entre el 17 y cada una de las opciones, esa resta debe ser divisible por 21 y luego se debe escoger el que tenga el valor absoluto más pequeño. Así que la respuesta es 4.
	
	La notación de congruencia se basa en el algoritmo de la división, ya que si a es un número entero y sean q y r enteros tales que a = nq + r con 0 ≤ r < n, despejando nq se obtiene a − r = nq y por definición de divisibilidad n | (a−r), pero ahora aplicando la definición de congruencia a ≡ rmod n, por tanto, existen n enteros que son congruentes con exactamente uno de los valores 0,1,2,…,n−1 módulo n.
	
	De esto se deduce que existen infinitos números que son congruentes con algún r, tal que 0 ≤ r < n y también se puede decir que el conjunto 0,1,2,…,n es el menor conjunto completo de residuos, ya que estos son todos los posibles residuos que dejan los enteros cuando se dividen por n.
	
	Ahora la pregunta es ¿por qué el menor?, ¿existen más? Por supuesto que sí y estos pueden tener hasta elementos negativos, por ejemplo, el conjunto:
	
	4,5,6,7,8,9,10,11
	
	también es un conjunto completo de residuos módulo 88, debido a que pasa lo siguiente:
	
	4 ≡ 4 mod 8
	5 ≡ 5 mod 8
	6 ≡ 6 mod 8  
	7 ≡ 7 mod 8  
	8 ≡ 0 mod 8  
	9 ≡ 1 mod 8  
	10 ≡ 2 mod 8  
	11 ≡ 3 mod 8
	
	Es decir, cada uno de los números del conjunto es congruente con uno y solo uno de los elementos del menor conjunto completo de residuos.
	
	Note que el siguiente conjunto:
	
	−5, −24, 7, 21, 37, 50, −12, 30
	
	también es un conjunto completo de residuos, ya que:
	
	−5 ≡ 3 mod 8−24 ≡ 0 mod 8  
	7 ≡ 7 mod 8
	21 ≡ 5 mod 8   
	37 ≡ 1 mod 8
	50 ≡ 2 mod 8  
	−12 ≡ 4 mod 8  
	30 ≡ 6 mod 8
	
	De nuevo cada uno de los elementos del conjunto son congruentes con uno y solo uno de los elementos del menor conjunto completo de residuos módulo 8.
	
	De estos dos ejemplos, se puede decir que un conjunto a<sub>1</sub>, a<sub>2</sub> ,a<sub>3</sub> ,…, a<sub>n</sub> es un conjunto completo de residuos si cada uno de los elementos de él es congruente con uno y solo uno de los elementos del conjunto 0, 1, 2,…, n del menor conjunto completo de residuos esto módulo n.

# Teoremas en Archivo
# Videoclase

Con el propósito de ampliar y profundizar el tema de las congruencias, observa la siguiente video clase antes de adelantar los ejercicios de esta lección:

![Videoclase: Congruencias](https://youtu.be/FBC6Dq6B0Xs)

# Ejercicios

Los ejercicios a continuación son para la práctica de los estudiantes:
En archivo...