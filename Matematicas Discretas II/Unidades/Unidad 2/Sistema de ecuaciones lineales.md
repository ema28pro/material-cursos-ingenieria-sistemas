# Introducción

En esta sección se trabaja sobre sistemas lineales de congruencias y se quiere encontrar una solución simultanea para cada una de las ecuaciones.

El problema fue propuesto y resuelto por el matemático Chino Sun-Tsu, quien se planteó lo siguiente: existe un número que es desconocido, se sabe que cuando este se divide por 3 el residuo es 2, cuando se divide por 5, el residuo es 3 y cuando se divide por 7, el residuo es 2, ¿cuál es el número que satisface estas condiciones?

Este juego se puede escribir de la siguiente forma:

x ≡ 2 mod 3 
x ≡ 3 mod 5 
x ≡ 2 mod 7 

Este acertijo fue resuelto por Sun-Tsu y en esta sección se mostrarán dos formas en las que se puede solucionar.

La primera se trata de la manera natural de resolverlo. Se le llama natural porque, de acuerdo a lo aprendido en un curso básico de matemáticas, para resolver un sistema de ecuaciones se despeja una de las variables y simplemente se reemplaza hasta que se obtiene la solución de alguna de ellas y, así, se hace el proceso de ir sustituyendo.

Se debe resaltar que al reemplazar se encontrará una solución módulo del producto de todos los módulos.

Vea el siguiente caso:

Para hallar una solución se toma la primera congruencia lineal  x ≡ 2 mod 3, como se conoce, entonces x − 2 = 3k<sub>1</sub> para k<sub>1</sub> ∈ Z, se despeja de ésta x y se obtiene lo siguiente:

x = 3k<sub>1</sub> + 2

Reemplazando la x de la segunda ecuación, se obtiene que 3k<sub>1</sub> + 2 ≡ 3 mod 5, y restando a ambos lados 2, se llega a que 3k<sub>1</sub> ≡ 1 mod 5, que es una congruencia que se puede resolver por los métodos aprendidos en la clase anterior. Sin embargo, note que el k<sub>1</sub> que es el inverso de 3 módulo 5 es el número 2, por tanto se obtiene k<sub>1</sub> ≡ 2 mod 5. De nuevo al aplicar la definición de congruencia se llega a que existe k<sub>2</sub>, tal que 5k<sub>2</sub> = k<sub>1</sub> − 2 y al despejar k<sub>1</sub> y al reemplazarlo en (1) queda:

x = 3 (5k<sub>2</sub> + 2) + 2 = 15k<sub>2</sub> + 8

Al reemplazar esta en la ecuación tres, dada por el sistema de congruencias, se obtiene que 15k<sub>2</sub> + 8 ≡ 2 mod 7, al restarle 8 a ambos lados de la congruencia, se obtiene 15k<sub>2</sub> ≡ −6 ≡ 1 mod 7, pero 15 ≡ 1 mod 7, por tanto, se obtiene que k<sub>2</sub> ≡ 1 mod 7 y por definición de la congruencia que existe un k<sub>3</sub> tal que 7k<sub>3</sub> = k<sub>2</sub> − 1 y así k<sub>2</sub> = 7k<sub>3</sub> + 1, que al reemplazarlo en (2) se obtiene que:

x = 15 (7k<sub>3</sub> + 1) + 8 = 105k<sub>3</sub> + 15 + 8 = 105k<sub>3</sub> + 23

De aquí se llega a que x ≡ 23 mod 105 y, por tanto, el 23 era el número buscado por Sun-Tsu.

# Teorema Chino de los residuos

Los mismos chinos generaron un algoritmo que hace más simples estos cálculos. Note que si el sistema tiene muchas ecuaciones este método se vuelve muy complejo o largo. Vea el siguiente teorema:

![Teorema] Sean m<sub>1</sub>, m<sub>2</sub>,...,m<sub>n</sub> enteros positivos mayores que 1 primos relativos dos a dos y sean a<sub>1</sub>, a<sub>2</sub>,...,a<sub>n</sub> enteros arbitrarios, Entonces el sistema
	x ≡ a<sub>1</sub> mod m<sub>1</sub>
	x = a<sub>2</sub> mod m<sub>2</sub>
	 ·
	 ·
	 ·
	 x = a<sub>n</sub> mod m<sub>n</sub>
tiene solución única modulo M = m<sub>1</sub> m<sub>2</sub> m<sub>3</sub> · · · m<sub>n</sub> y todas las soluciones son congruentes con este modulo M.

Para probar el teorema se debe tener en cuentea la forma en la que se llega a la solución; es decir, lo primero que se debe considerar son los valores a<sub>i</sub> con i = 1,...,n.
Luego se debe encontrar unos valores que se llamaran M<sub>k</sub>, los cuales se calcula de la siguiente manera:
	M<sub>k</sub> = M / m<sub>k</sub> 

Para k = 1,2,...,n note que mcd(M<sub>k</sub>, m<sub>k</sub>) = 1 y así se puede hallar la solución de cada una de las congruencias lineales de la forma:
	M<sub>k</sub>y<sub>k</sub> ≡ 1 mod m<sub>k</sub>
Para k = 1, 2 ,...,n valores y<sub>k</sub> dan el tercer valor a encontrar para escribir la solución, la cual viene dada por:
	_X_ = a<sub>1</sub> M<sub>1</sub> y<sub>1</sub> + a<sub>2</sub> M<sub>2</sub> y<sub>2</sub> + · · · + a<sub>n</sub> M<sub>n</sub> y<sub>n</sub> mod M

Ahora, al revisar el problema de Sun-Tse por este método, ya se tiene que a<sub>1</sub> = 2, a<sub>2</sub> = 3 y a<sub>3</sub> = 2. Además, se tiene que M = 105 y así M<sub>1</sub> = 105/3 = 35, M<sub>2</sub> = 105/5 = 21 y M<sub>3</sub> = 105/7 = 15. Resta encontrar los y para i = 1, 2, 3, esto se hace resolviendo las congruencias lineales:
	35y<sub>1</sub> mod 3
	21y<sub>2</sub> mod 5
	15y<sub>1</sub> mod 7

Las cuales se solucionan por los métodos vistos en la clase anterior, llegando a que y<sub>1</sub> = 2, y<sub>2</sub> = 1 y y<sub>3</sub> = 1.
De los valores anteriores se tiene que: 
	X ≡ 2 * 35 * 2 + 3 * 21 * 1 + 2 * 15 * 1 = 140 + 63 + 30 = 233 ≡ 23 mod 105
La cual es la solución conseguida por el método anterior.

## Ejemplos

Con base en el contenido visto hasta el momento, visualiza los siguientes ejemplos:

**Ejemplo 1:** Resolver el sistema de ecuaciones:
	x ≡ 5 mod 8
	x ≡ 7 mod 9

Aplicando el teorema chino de los residuos, se obtiene que a<sub>1</sub> = 5 y a<sub>2</sub> = 7, además, que M=72, M<sub>1</sub> = 9 y M<sub>2</sub> = 8. Solo resta encontrar los valores de y<sub>1</sub> y y<sub>2</sub>.
Para hallar y<sub>1</sub>:
	9y<sub>1</sub> ≡ 1 mod 8 
	y<sub>1</sub> ≡ 1 mod 8

Ya que el residuo que deja 9 cuando se divide por 8 es 1.
Para hallar y<sub>2</sub>:
	8y<sub>2</sub> ≡ 1 mod 9 
	−1y<sub>2</sub> ≡ 1 mod 9

Ya que 8 ≡ −1 mod 9, por tanto, multiplicando esta última por -1 se llega a que:
	y<sub>2</sub> ≡ 8 mod 9

Así la solución general es:
	X ≡ 5 ⋅ 9 ⋅ 1 + 7 ⋅ 8 ⋅ 8 mod 72

Al calcular esta se llega a que:
	X ≡ 45 + 448 mod 72

Que es lo mismo X ≡ 493 mod 72. Así la solución es:
	X ≡ 61 mod 72

Por lo tanto, el valor que satisface cada una de las congruencias del ejemplo es X = 61.

**Ejemplo 2:** Resolver el sistema de ecuaciones:
	7x ≡ 5 mod 8
	13x ≡ 7 mod 9
	4x ≡ 7 mod 11

Note que es muy parecido al teorema chino de los residuos, pero con coeficientes multiplicando a los valores de x. Así que los a<sub>i</sub> para i = 1, 2, 3 no son los valores que aparecen en cada ecuación. Lo primero que se debe hacer es resolver cada una de las ecuaciones lineales para x, en el ejemplo, al resolver cada una, se llega a que:
	x ≡ 3 mod 8 
	x ≡ 4 mod 9
	x ≡ 10 mod 11

Al encontrar esto, se sigue aplicando el teorema y la solución encontrada resuelve los dos sistemas de ecuaciones.

Ahora, si a<sub>1</sub> = 3, a<sub>2</sub> = 4 y a<sub>3</sub> = 10, además, M = 792 y M<sub>1</sub> = 99, M<sub>2</sub> = 88 y M<sub>3</sub> = 72 y resta encontrar los y<sub>i</sub>, para i = 1, 2, 3. Para esto se tienen que solucionar las siguientes ecuaciones:
	99 y<sub>1</sub> ≡ 1 mod 8 
	88 y<sub>2</sub> ≡ 1 mod 9 
	72y<sub>3</sub> ≡ 1 mod 11

Al reducirlas quedan:
	3 y<sub>1</sub> ≡ 1 mod 8
	7 y<sub>2</sub> ≡ 1 mod 9 
	6 y<sub>3</sub> ≡ 1 mod 11

Y al resolverlas quedan:
	y<sub>1</sub> ≡ 3 mod 8
	y<sub>2</sub> ≡ 4 mod 9 
	y<sub>3</sub> ≡ 2 mod 11

Por lo tanto,
	X = 3 ∗ 99 ∗ 3 + 4 ∗ 88 ∗ 4 + 10 ∗ 72 ∗ 2 = 891 + 1408 + 1440 = 3739 ≡ 571 mod 792

A continuación, responde las siguientes preguntas aplicando los contenidos vistos hasta el momento en este recurso:
![Reto] Cierto o falso: el ejemplo anterior tiene solución única:
- [ ] Cierto
- [x] Falso
**_Comentario_**:  
	Falso, ya que como se esta resolviendo, al final, la ecuación lineal se pueden encontrar más soluciones simplemente poniendo un valor al parámetro t, la ecuación 61 + 72t.

En el ejemplo anterior, una solución en el intervalo [300, 350]
- [ ] Ninguna de las opciones es correcta
- [x] 349
- [ ] No existen soluciones en este intervalo
- [ ] 316
**_Comentario_**:  
	Si se aplica la fórmula del reto anterior con t = 4, se llega a la solución x = 349. Así la respuesta es: 349.
	Note que las ecuaciones del teorema son muy específicas, sin ningún coeficiente multiplicando los valores de x, pero ¿Qué pasa si estos coeficientes existieran? Visualiza con atención el ejemplo 2 de la sección anterior para mayor claridad del ejercicio.

# Ejercicios en Archivo