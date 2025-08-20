# Permutaciones

Antes de comenzar, ten en cuenta que al hacer clic en cada ejemplo podrás ver su resolución
## Ejemplo 1

Sean x<sub>1</sub>, x<sub>2</sub> ,x<sub>3</sub> ,…, x<sub>n</sub> objetos. Una permutación es un reordenamiento de estos elementos.

Si se tienen n objetos como los listados arriba, se dice que hay n! permutaciones.

**Ejemplo** : ¿Cuántas permutaciones hay de las letras en la palabra MATE?

Por lo dicho anteriormente como todas las letras son diferentes debe haber 4! = 24 permutaciones. Todas las permutaciones se listan a continuación:

|   |   |   |   |   |   |
|---|---|---|---|---|---|
|MATE|MAET|MTAE|MTEA|META|MEAT|
|AMTE|AMET|ATME|ATEM|AETM|AEMT|
|TMAE|TMEA|TAME|TAEM|TEMA|TEAM|
|EMAT|EMTA|EATM|EAMT|ETAM|ETMA|
## Ejemplo 2

**Ejemplo** : Dado el conjunto {1, 2, 3}, ¿Cuántos posibles conjuntos iguales a A existen?

Debe haber 5 conjuntos, ya que eI número de permutaciones que hay con tres elementos es 3! = 6, y como lo que se busca es eI número de conjuntos que son iguales a A, si se descarta A, quedan 5.

## Ejemplo 3

**Ejemplo** : Un estante para libros tiene 5 libros de algebra, 7 libros de algoritmos y 8 libros de programación y todos ellos son diferentes.
1. ¿De cuántas formas se pueden ordenar los libros en eI estante?
2. ¿De cuántas formas se pueden ordenar en el estante si los libros de cada clase deben ir juntos?
3. ¿De cuántas formas se pueden ordenar en el estante si los libros de programación deben ir juntos?
4. ¿De cuántas formas se pueden ordenar en el estante si los libros de programación no pueden estar juntos?

- **Respuesta 1** : Se deben permutar 5 + 7 + 8 = 20 objetos, los cuales se pueden permutar en 20! = 2432902008176640000 formas.
- **Respuesta 2** : Pegue todos los libros de cada clase, pero eso se puede hacer de 5! formas para los libros de álgebra, de 7! formas para los libros de algoritmos y de 8! formas para los libros de programación. También se debe contar el orden en el que van los paquetes de libros en el estante, que como son tres paquetes sería 3!. Por tanto por la regla del producto, existen:
	3! (5!) (7!) (8!) formas.
- **Respuesta 3** : Del numeral anterior, se sabe que el número de formas de ordenar los libros de programación es 8!. Ahora, este forma un libro grande que se llamará el libron de programación y el problema se concentra ahora en ordenar los 5 libros de álgebra, los 7 de algoritmos y el libron, por la regla de la suma 1 + 5 + 7 =13 y al permutarlos da 13! formas y esto multiplicado por los 8! formas de re-arreglar los de programación se obtiene que se pueden organizar en el estante de 8! (13!) formas.
- **Respuesta 4** : Se tienen 12! formas de ordenar los libros de álgebra y algoritmos, ahora se quieren meter los libros de programación entre estos, pero ellos no pueden estar juntos, por lo tanto, se deben abrir espacios entre los de álgebra y algoritmos, si se hace esto quedan 13 espacios entre los libros. Si se quiere poner el primero de programación hay 13 formas de ponerlo, al segundo en 12 formas, al tercero en 11 formas, el cuarto en 10 formas, al quinto en 9 formas, al sexto en 8 formas, al séptimo en 7 formas y al octavo en 6 formas. Así en total para ponerlo en el estante hay:
	(13) (12) (11) (10) (9) (8) (7) (6) 12!

## Ejemplo 4

**Ejemplo** : Una junta directiva está conformada por 8 personas. ¿De cuántas formas se pueden sentar si el presidente y el secretario siempre deben estar juntos?

De nuevo, si el presidente y el secretario deben ir juntos, pues estos se pueden sentar en la mesa de 2! = 2 formas y quedan seis personas restantes por sentar, pero también queda una posición extra que es la que forman el presidente y el secretario, por tanto se tienen 7! formas de sentarlos en la mesa y esto multiplicado por el número de permutaciones en las que se organizan presidente y secretario. En total son 2 7!.

# Permutaciones de n de k

Muchas veces se tienen n objetos pero de ellos solo se quieren permutar k, esto esta dado por la fórmula:
	n (n - 1) (n - 2) (n - 3) · · · (n - k + 2) (n - k + 1)
O que también se puede escribir como
	p(n, k) = p<sub>k</sub><sup>n</sup> = n! / (n - k)!

**Ejemplo** : ¿Cuántas claves de acceso se pueden generar con los géneros 1, 2, 3 si se desea que las claves a formar consten de 2 números? 

Se tienen 3 números para escoger 2, por ende el número de claves de asceso son
	p(3, 2) = 3! / 1! = 6

Estas son:
	12 13 21 23 31 33

Este problema es similar al anterior, lo que cambia es que la cantidad de números a escoger son 10 y el número de dígitos a escoger son 4, por lo tanto, se pueden hacer:
	p(10, 4) = 10! / 6! = (10) (9) (8) (7) = 5040

# Permutaciones con repetición

Si se tienen n objetos y se permite repetirlos, entonces el número de permutaciones es n<sup>n</sup>.

**Ejemplo** : ¿Cuántas posibles cedulas se pueden hacer si estas constan de 10 dígitos?

Como los dígitos son 10 y se quiere contar la cantidad de números de diez cifras que se pueden hacer, no importando que empiecen por cero, entonces el número de cédulas es 10<sup>10</sup>.

Si lo que se quiere es escoger una cantidad k de los $n$ objetos y estos se pueden repetir, entonces esto se puede hacer de n<sup>k</sup> formas.

**Ejemplo** : Si con los dígitos el banco permite repeticiones, entonces cuantas posibles claves hay?

Como se permiten repeticiones y el número de dígitos es 1010, entonces se tienen 10<sup>4</sup> = 10000 posibles claves.

Pero si se tienen k tipos de objetos, n<sub>1</sub> del tipo 1, n<sub>2</sub> del tipo 2, etc. Entonces el número de formas en las que estos n<sub>1</sub> + n<sub>2</sub> + ⋯ + n<sub>k</sub> pueden ser organizados es:
	(n<sub>1</sub> + n<sub>2</sub> + ⋯ + n<sub>k</sub>)! / (n<sub>1</sub>! + n<sub>2</sub>! + ⋯ + n<sub>k</sub>!)

**Ejemplo** : ¿De cuantas formas se pueden arreglar la palabra COCO?

Note que se tienen dos tipos de objetos la CC y OO, estas son indistinguibles en la palabra, por tanto al re-arreglarla se puede escribir de cuatro formas diferentes, pero eso no se podría distinguir. Por eso el número de formas en las que se puede hacer esto es:

4! / (2! 2!) = 6

Esto debido a que CC se repite dos veces y OO también. Estas son:

|   |   |   |   |   |   |
|---|---|---|---|---|---|
|COCO|COOC|CCOO|OOCC|OCCO|OCOC|
**Ejemplo** : ¿De cuantas formas se pueden re-arreglar la palabra OLLA?

Note que en esta palabra solo se repite una letra, por tanto el número de formas es:
	4! / 2! = 12

Estas son:

|   |   |   |   |   |   |
|---|---|---|---|---|---|
|OLLA|OLAL|OALL|ALLO|ALOL|AOLL|
|LALO|LAOL|LOLA|LOAL|LLAO|LLOA|

**Ejemplo** : ¿De cuantas formas se pueden re-arreglar la palabra Matematicas?

Note que en este problema existen más tipos de letras que se repiten, M dos veces, A tres veces, T dos veces y la palabra tiene 11 letras, así que el número de formas en las que se puede hacer esto es:
	11! / (2! 3! 2!) = 1663200.

**Ejemplo** : ¿En cuantas formas se puede escribir el 5 como suma de tres enteros positivos?

Se necesita resolver la ecuación:
	a + b + c = 5

Y encontrar las tripletas (a, b, c) que la satisfacen con 1 ≤ a ≤ b ≤ c ≤ 3, debido a que si uno de ellos es 5, no podría haber tres sumandos positivos y, más o menos, para el cuatro funciona igual. Note que solo hay dos posibles sumas que satisfacen esto, ellas son 1 + 2 + 2 y 3 + 1 + 1, pero como lo que se está buscando son las tripletas (a, b, c), falta contar las permutaciones, entonces para cada tripleta se aplica la siguiente tabla:

| Tripleta  | # de permutaciones |
| --------- | ------------------ |
| (1, 2, 2) | 3! / 2! = 3        |
| (1, 1, 3) | 3! / 2! = 3        |

De la tabla se nota que hay 6 formas diferentes de escribir al 5 como suma de tres enteros positivos.

# Permutaciones circulares en Archivo

# Ejercicios en Archivo