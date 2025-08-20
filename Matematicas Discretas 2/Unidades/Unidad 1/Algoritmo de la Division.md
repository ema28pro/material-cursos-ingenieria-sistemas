# Introducción

El siguiente resultado es la base del primer capítulo de este curso y será aplicado para definir conceptos y propiedades de los números enteros.

![Teorema] Dados $a$ y $b$ numeros enteros positivos, existe un unico par $(q, r)$ de enteros no negativos tales que $b = aq + r$ tal que $0 ≤ r > a$. Decimos que q es el cociente y re es el residuo, cuando dividimos b por a.

Para probar este teorema se debe considerar el principio del buen orden, el cual dice que un conjunto está bien ordenado si todos y cada uno de los subconjuntos no vacíos tienen un elemento más pequeño o mínimo. Que es: todo subconjunto no vacío de los enteros positivos tiene un elemento mínimo.

Usando el principio del buen orden. Se considera el conjunto

$S=\{a−bk:k∈Z,a≥bk\}$

Note que S es un conjunto no vacio de enteros positivos (es no vacío, ya que $a−b⋅0∈S$). Por lo tanto, por el principio del buen orden SS tiene un menor elemento, suponga r. Ahora, debe haber un $q∈Z$ tal que $r=a−bq$. Como $r∈S$, entonces $0≤r$, así que resta probar que $r<b$.

Por reducción al absurdo, suponga que $r≥b$. entonces

$r>r−b=a−bq−b=a−b(q+1)≥0$  

Considerando que $r−b≥0$ y que $a−(q+1)b∈S$ como $a−(q+1)b<r$ se llega a un absurdo. Por lo tanto, $r<b$.

Lo siguiente es probar la unicidad

Suponga por reducción al absurdo que $q$ y $r$ no son únicos, es decir, que $a=bq_{1}+r_{1}$ con $0≤r_{1}<b$ y que $a=bq_{2}+r_{2}$ con $0≤r_{2}<b$. Así,
$$bq_{1}+r_{1}=bq_{2}+r_{2}$$
y al simplificar se obtiene $r_{1}−r_{2}=b(q_{2}−q_{1})$ lo que implica que $b | (r_{1}−r_{2})$, pero $r_{2}−r_{1}<b$, por tanto, $r_{2}−r_{1}=0$, así $r_{2}=r_{1}$.

Los siguientes son ejemplos de cómo funciona el algoritmo de la división:

**Ejemplo**
1. Dado que $a = 4$ y $b = 7$, entonces los valores $q$ y $r$ son, respectivamente, $0$ y $4$, asi se puede escribir
$$4 = 7 · 0 + 4$$
2. Dado que $a = 76$ y $b = 23$, entonces los respectivos valores de $q$ y $r$ son, respectivamente, $3$ y $7$, asi se puede escribir
$$76 = 23 · 3 + 7$$
Note que en el algoritmo de la división solo se consideraron números enteros positivos: Como una consecuencia inmediata del teorema, se muestra el siguiente corolario:

![Corolario] Dados $a$ y $b$ numeros enteros, con $b ≠ 0$, exiten enteros unicos $q$ y $r$ tales que
$$a = bq + r, 0 ≤ |b|$$

Es importante resaltar en este punto, la importancia que el residuo tiene en el teorema. Se debe notar que este siempre es positivo y menor que el valor absoluto del divisor.

A continuación se muestra cómo usar el algoritmo de la división con valores negativos.

**Ejemplo**
1. Dado $a = -8$ y $b = 3$, entonces
$$-8 = 3 · (-3) + 1$$
2. Dado $a = 8$ y $b = -3$, entonces
$$8 = (-3) · (3) +1$$
3. Dado $a = -8$ y $b = -3$, entonces
$$-8 = (-3) · (3) + 1$$

En el ejemplo anterior, usamos los mismos números, pero con signos diferentes y se puede ver que el residuo siempre es el mismo y el cociente diferente.
### Retos

Los siguientes retos son para que el estudiante refuerce los conceptos y una vez responda a cada uno obtendrá una retroalimentación.

1. El residuo de dividir a $a=−17$, por $b=13$ es:
	- [ ] $4$
	- [ ] $-9$
	- [x] $9$
	- [ ] $-4$
	**_Comentario_** :  
		¡Tu respuesta es correcta!
		Como el residuo debe ser positivo, entonces cuando se divide $−17$ por $13$, el cociente es igual a $2$ y el residuo igual $9$.

2. El residuo de dividir a $a=65$, por $b=−21$ es:
	- [ ] $2$
	- [ ]  $-2$
	- [x] $19$
	- [ ] $23$
	**_Comentario_** :  
		¡Tu respuesta es correcta!
		Como el residuo debe ser positivo, entonces cuando se divide $65$ por $−21$, el cociente es igual a $−4$ y el residuo igual $19$.
3. El residuo de dividir a $a=-43$, por $b=-65$
	- [ ] $21$
	- [x] $22$
	- [ ] $-22$
	- [ ] $-21$
	**_Comentario_** : 
		¡Tu respuesta es correcta!
		Como el residuo debe ser positivo, entonces cuando se divide $−43$ por $−65$, el cociente es igual a $1$ y el residuo igual $22$.
## Otros ejemplos del uso del algoritmo de división

Los siguientes son otros ejemplos donde se usa el algoritmo de la división para poder ser resueltos:

**Ejemplo**
	¿Cuantos multiplos de $7$ hay entre $345$ y $563$ inclusive?

Para resolver este ejemplo, se debe dividir los números por $7$. Cuando se divide el $345$ por $7$, se obtiene
$$345 = 7 ⋅ 49 + 2$$
Esto quiere decir que el primer múltiplo de $7$ que es mayor que $345$ es el $350$. Por otro lado, al dividir a $563$ por $7$, se obtiene por el algoritmo de la división $563 = 7 ⋅ 80 + 3$, es decir, que el valor más cercano $563$, que es múltiplo de $7$ es el número $560$. Así, el número de múltiplos de $7$ que hay entre $350$ y $560$ inclusive es $( 560 − 350 ) / 7 + 1 = 210 / 7 + 1 = 30 + 1 = 31$ .

Con base en lo anterior, responde la siguiente pregunta:

¿Cuántos múltiplos de $8$ hay entre $246$ y $423$ inclusive?
- [ ] $21$
- [ ] $23$
- [x] $22$
- [ ] $24$
**_Comentario_** :  
	¡Tu respuesta es correcta!
	Si se hace un procedimiento parecido al del ejemplo anterior se llega a que la respuesta es el número de valores es **$22$.**

## Otros ejemplos del uso del algoritmo de división

**Ejemplo**
	Argumente por que el numero $8729133616398$ no es un cuadrado perfecto si al sacar la raíz cuadrada del numero

Cuando se eleva al cuadrado un número, se debe multiplicar el número dos veces, esto hace que la última cifra del número se multiplique por ella misma y este deja un cociente y un residuo cuando se divide por $10$.

En otras palabras, si $n=10q+r$, donde $0≤r<10$, se eleva al cuadrado se obtiene
$$n^{2} = 10^{2}q^{2}+10qr+r^{2}=10(10q^{2}+qr+r^{2})$$
Pero r es un número positivo menor que 10, es decir, que r es un dígito que lo elevamos al cuadrado y su último dígito determina si es un posible cuadrado o no. En la siguiente tabla determinamos ese hecho.

| Dígito | Cuadrado | Último dígito |
| ------ | -------- | ------------- |
| 0      | 0        | 0             |
| 1      | 1        | 1             |
| 2      | 4        | 4             |
| 3      | 9        | 9             |
| 4      | 16       | 6             |
| 5      | 25       | 5             |
| 6      | 36       | 6             |
| 7      | 49       | 9             |
| 8      | 64       | 4             |
| 9      | 81       | 1             |

**Nota:** como se nota en la columna número 3, no aparece el 8 como último dígito, lo que significa que el número dado no puede ser un cuadrado perfecto.

Con base en lo anterior, responde la siguiente pregunta:

¿Todo número que termine en un dígito del conjunto $\{0,1,4,5,6,9\}$ es cuadrado perfecto?

- [ ] Verdadero
- [x] Falso
**_Comentario_** :  
	¡Tu respuesta es correcta!
	La respuesta es **falso**. Ya que la prueba del ejemplo anterior solo ayuda a determinar si el número no es un posible cuadrado perfecto. Pero no determina que el número sea un cuadrado perfecto.
	En conclusión, pueden haber números que terminen en los dígitos del conjunto pero no ser cuadrados perfectos. Por ejemplo el número $6$

## Notación en las matemáticas

Muchas veces en matemáticas se requiere de una buena notación y es importante que esta simplifique la manera de llegar al resultado esperado. El siguiente ejemplo es uno de los casos donde la notación simplifica un poco la forma de abordar el problema.

**Ejemplo**
	Demuestre que el cuadrado de todo numero impar siempre se puede escribir en la forma $8k + 1$ para $k ∈ Z$

Primero se trabajará con una notación no apropiada para mostrar luego que con una buena notación se puede simplificar el cómo llegar al resultado.

Usando el algoritmo de la división, se toma a un número impar de la forma $n=2k+1$ donde $k∈Z$

Al elevar este número al cuadrado se obtiene que
$$ \begin{aligned} n^{2} & = (2k + 1)^{2} \\
	& = 4k^{2} + 4k + 1 \\
	& = 4k (k + 1) + 1 \end {aligned} $$
Pero note que no se llegó directamente a que el cuadrado de un número es de la forma $8k+1$ con $k∈Z$. Si el lector no tiene mucha experiencia en demostrar, el no llegar directamente al resultado puede ser un gran obstáculo.

Para llegar a la conclusión de la demostración el lector debe notar que $k(k+1)$ es un número par. ¿Cómo es esto posible? Note que como k es un entero, entonces $k$ y $k+1$ son enteros consecutivos y esto da que alguno de los dos debe ser un número par. Además, como se está multiplicando y el producto de un número par por un impar siempre es par, entonces $k(k+1)=2K$ con $K∈Z$. Por lo tanto,
$$ \begin{aligned}
n^{2} &= 4k (k + 1) + 1 \\
&= 4 (2K) + 1 \\
&= 8K + 1
\end{aligned}
$$
y así se llega a la solución del ejemplo.

Por otro lado, note que el algoritmo de la división también da la posibilidad de que $n=4k+1$ o $n=4k+3$ sean números impares. Se deben considerar las dos formas, ya que los números enteros impares que se generan con una forma son diferentes a los impares que se generan con la otra forma. Entonces considerando los dos casos se obtiene
	Para $n=4k+1$, al elevar n al cuadrado
$$ \begin{aligned}
n^{2} & = (4k + 1)^{2} \\
& = 16k^{2} + 8k + 1 \\ 
& = 8 (2k^{2} + k) + 1 \end{aligned} $$
Pero $2k^{2}+k$ es un número entero que se denotará por $K$. Así, $n^{2}=8K+1$, y se llega a la solución.

De esta manera, al cambiar la notación se llegó por otro lado a la solución. Use una notación adecuada para demostrar el siguiente reto.

![Reto] Demuestre que el cuadrado de cualquier entero es la forma $3k$ o $3k +1$ 

**Nota:** la forma en la que se ven los números es la forma que muchas veces puede llegar a la conclusión de una demostración; el siguiente ejemplo es una muestra de esta aseveración.

**Ejemplo** 
	Demuestre que todo entero de la forma $6j + 5$ también es de la forma $3k +2$

**Nota:**:se quiere partir del número $6j+5$ que es igual a $3⋅2j+(3+2)$, pero al aplicar la propiedad asociativa se llega a que la expresión a anterior: $(3⋅2j+3)+2$ y sacando el factor común del primer término $3(2j+1)+2$ y tomando a $2j+1=k$, se concluye que $6j+5$ también se puede ver como $3k+2$.

Este reto ayudará a practicar los conceptos aprendidos en la lección.

![Reto] Demuestra las siguientes formas de escribir algunos números enteros:
1. Demuestre que $10j + 7$ se puede escribir de la forma $5k + 2$.
2. Demuestre que $30k + 23$, se puede escribir de la forma $2j + 1$ o de la forma $3j + 2$ o de la forma $10j +3$.

## Ejercicios

Los siguientes ejercicios te servirán para practicar lo visto en esta lección.
En archivo.

## Referencias bibliográficas

- Andrica, D., y Andreescu, T. (2009). Number theory: structures, examples, and pro‐ blems. Birkhäuser Boston.
- Burton, D. (2010). Elementary Number Theory. Ebook. McGraw Hill. ‐Grigorieva, E. (2018). Methods of Solving Number Theory Problems. Springer International Publishing.
- Rosen, K. H. (1999). Discrete mathematics & applications. McGraw‐Hill.
- Stevens, J. (s. f.). Olympiad Number Theory Through Challenging Problems. [https://s3.amazonaws.com/cdn.artofproblemsolving.com/resources/articles/olympiad](https://s3.amazonaws.com/cdn.artofproblemsolving.com/resources/articles/olympiad)‐number‐theory.pdf