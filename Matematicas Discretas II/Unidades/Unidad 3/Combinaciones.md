# Combinaciones

Se tienen n objetos y se quieren escoger k de ellos con 0 ≤ k ≤ n. El símbolo (n k), el cual se lee "n tomados de a k", se define por:

(n k) = n! / [ k! (n − k)! ]

Y significa que el número de formas de escoger $k$ objetos de un grupo de n, es (n k).

Note que si se escoge un grupo de k objetos de un grupo de n objetos, es como si se estuvieran sacando los que no se necesitan. Es decir, (n−k), del grupo de los n objetos, por lo tanto:

(n k) = (n n−k)

A continuación, se presentará una serie de ejemplos que de manera secuencial expondrán diversas combinaciones:

_Navegue por el siguiente acordeón haciendo clic en cada ejemplo para desplegar la información_

## Ejemplo 1

**Ejemplo** : Si de un grupo de 7 personas se quiere escoger 5, ¿de cuántas formas se puede hacer esto?

Esto se puede hacer de (7 5), que es lo mismo:
	7! / [ 5! (2!) ] = ( 6 ∗ 7 ) / 2 =21

Que es lo mismo que si se fueran a sacar los dos que no se van a seleccionar, esto se hace así: (7 2)= 21. También así:
	(7 5) = (7 2).

## Ejemplo 2

**Ejemplo** : Encuentre el número de parejas que se pueden hacer con los elementos del conjunto {A, B, C, D}

Como se tienen que escoger de a dos, esto está dado por (4 2) = 6 y las posibilidades son:
	AB, AC, AD, BC, BD, CD.

## Ejemplo 3

**Ejemplo** : Encuentre el número de ternas que se pueden hacer con los elementos del conjunto {A, B, C, D}

El número de ternas que se pueden sacar está dado por (4 3) = 4, y las posibilidades son:
	ABC, ABD , ACD, BCD

## Ejemplo 4

**Ejemplo** : En un grupo de dos perros, tres gatos y diez canarios, ¿en cuántas formas se puede escoger un grupo de seis animales si:
1. no existen restricciones?
2. dos perros deben estar incluidos?
3. debe haber solo dos gatos?
4. debe haber al menos 3 canarios?
5. debe haber máximo 2 canarios?

- **Respuesta 1** : No importa la clase de animales que hay en el grupo de $6$, por ende, de los 2+3+10=15 posibles animales se van a escoger 6, esto es:
	(15 6) = 5005
- **Respuesta 2** : Como los dos perros deben estar incluidos, entonces del grupo de perros se escogen los dos, esto se puede hacer de (2 2) = 1 formas. De los demás animales se escogen los otros cuatro, pero como los demás son 13, esto esta dado por:
	(13 4) = 715.
- **Respuesta 3** : Si solo debe haber dos gatos, entonces de los tres se escogen 2 y esto es (3 2) = 3. Después de los animales restantes, perros y canarios, se escogen los otros cuatro, pero estos son 12 y así hay (12 4) = 495, por tanto, en total hay 3 × 495= 1485 formas.
- **Respuesta 4** : Cuando se dice que, al menos, 3 canarios se asume que hay tres o más, por eso hay que considerar cuando haya 3, 4, 5 y 6 canarios y en cada caso de los demás animales se escogen los que hagan falta. Así el conteo es:
	(10 3) (5 3) + (10 4) (5 2) + (10 5) (5 1) + (10 6) (5 0) = 1200 + 2100 + 1260 + 210 = 4770
- **Respuesta 5** : Si debe haber máximo 2 canarios, se asume que hay, como máximo, 2 canarios que pueden ser 0 o 1, pero no pueden ser 0, pues no se podrían conseguir los 6, así que son 1 o 2 y así esto es:
	(10 1) (5 5) + (10 2) (5 4) = 10 + 225 = 235

## Ejemplo 5

**Ejemplo** : En un salón hay 12 mujeres y 8 hombres, responda las siguientes preguntas:
1. ¿De cuántas formas se puede formar un grupo de diez personas?
2. ¿De cuántas maneras se puede formar el grupo si deben estar todos los hombres?
3. ¿De cuántas maneras se puede formar eI grupo si deben haber exactamente 8 mujeres?
4. ¿De cuántas maneras si, máximo, debe haber dos hombres?
5. ¿De cuántas maneras si, por 10 menos, debe haber 8 mujeres?

- **Respuesta 1** : Para escoger un grupo de 10 de las 20 personas, el número de formas es:
	(20 10) = 184756
- **Respuesta 2** : Si todos los hombres deben estar, significa que de las 12 mujeres se deben escoger 2 y hay
	(12 2) = 66 formas de escogerlas.
- **Respuesta 3** : Si debe haber 8 mujeres exactamente se tienen que escoger del grupo de las 12, y del de los hombres solo 2. Es decir, hay:
	(12 8) (8 2) = 13860 formas.
- **Respuesta 4** : Si deben haber a lo más 2 hombres quiere decir cuando haya 0 hombres, 1 hombre o 2 hombres, así van haber
	(8 0) (12 10) + (8 1) (12 9) + (8 2) (12 8) = 66 + 1760 + 13860 =15686
- **Respuesta 5** : Si por lo menos debe haber 8 mujeres, y si se usa el mismo conteo del ejercicio anterior, es cuando hay 10, 9 y 8. Así hay en total 15686 formas.

# Combinaciones con repetición

En esta sección se estudiará la forma de escoger k objetos de n donde hay objetos repetidos.

![Teorema] Sea n un entero positivo, en numero de soluciones enteras de la ecuación:
	x<sub>1</sub> + x<sub>2</sub> + x<sub>3</sub> + · · · + x<sub>k</sub> = n
es:
	(n-1 k-1)

A continuación, se presentará una serie de ejemplos de manera secuencial

_Navegue por el siguiente acordeón haciendo clic en cada ejemplo para desplegar la información_

## Ejemplo 1

**Ejemplo** : ¿De cuántas formas se puede escribir el número 9 como suma de tres sumandos enteros positivos? Cabe resaltar que , por ejemplo, 2 + 3 + 4 es una forma diferente a 2 + 4 + 3.

Lo que se quiere es resolver la ecuación:
	a + b + c = 9

Con a, b, c > 1 el numero de soluciones a esto es:
	(9-1 3-1) = 28

y las formas son:

|   |   |   |   |
|---|---|---|---|
|7+1+1|6+2+1|6+1+2|5+3+1|
|5+1+3|5+2+2|4+4+1|4+1+4|
|4+3+2|4+2+3|3+5+1|3+1+5|
|3+4+2|3+2+4|3+3+3|2+6+1|
|2+1+6|2+2+5|2+5+2|2+4+3|
|2+3+4|1+7+1|1+1+7|1+6+2|
|1+2+6|1+5+3|1+3+5|1+4+4|
## Ejemplo 2

**Ejemplo** : ¿De cuántas formas se puede escribir eI 100 como suma de cuatro enteros positivos?

Ahora lo que se quiere es resolver la ecuación:
	a + b + c + d = 100

Donde a, b, c, d > 0. El número de soluciones es:
	(99 3) = 156849

Otra forma de mirar el teorema es si se tiene un número $n$ de enteros positivos. El número de soluciones enteras no negativas de la ecuación:
	y<sub>1</sub> + y<sub>2</sub> + y<sub>3</sub> + ⋯ + y<sub>k</sub> = n
es
	(n+r−1 r−1)

Esta no es más que una consecuencia del teorema anterior, ya que si se toma a $x_{i}-1=y_{i}$ , entonces la ecuación queda:
	x<sub>1</sub> - 1 + x<sub>2</sub> - 1 + x<sub>3</sub> - 1 + ⋯ + x<sub>k</sub> = n
Es equivalente a tener:
	x<sub>1</sub> + x<sub>2</sub> + x<sub>3</sub> + ⋯ + x<sub>k</sub> = n + k
lo cual por el teorema es:
	(n+k−1 k−1)

## Ejemplo 3

**Ejemplo** : Encuentre el número de cuatruplas (a, b, c, d) de enteros que satisfacen:
	a + b + c + d = 100 con a ≥ 30, b ≥ 21, c ≥ 1, d > 0

Si se considera a a = a′+ 29, b = b′+21, el número de soluciones enteras a la ecuación
	a′ + 29 + b′ + 21 + c + d = 100
O lo que es lo mismo:
	a′ + b′ + c + d = 50
Y el número de soluciones es:
	(49 3) = 18424

## Ejemplo 4

**Ejemplo** : Hay cinco personas en un ascensor de un edificio que tiene ocho pisos. ¿De cuántas maneras pueden elegir su piso para salir del ascensor?

Sea x<sub>i</sub> el número de personas que se bajan en el piso i, lo que se quiere solucionar es la ecuación:
	x<sub>1</sub> + x<sub>2</sub> + x<sub>3</sub> + ⋯ + x<sub>8</sub> = 5

Si se considera a y<sub>i</sub> = x<sub>i</sub> + 1, entonces:
	x<sub>1</sub> + x<sub>2</sub> + x<sub>3</sub> + ⋯ + x<sub>8</sub> = 5 ⟹ (y<sub>1</sub> − 1) + (y<sub>2</sub> − 1) + ⋯ + (y<sub>8</sub> − 1) = 5
					⟹ y<sub>1</sub> + y<sub>2</sub> + y<sub>3</sub> + ⋯ + y<sub>8</sub> = 13
Y el número de soluciones es (12 7) = 792.

Esto también se puede ver sin ecuaciones: se tienen 5 personas que se quieren distribuir, de alguna forma, en 8 espacios. Estos espacios son separados por líneas verticales y el menor número de líneas verticales que se usan para encontrar los 8 espacios es 7. Entonces se tienen 12 objetos entre personas y líneas verticales, así que el conteo sería de los doce objetos separarlos por 7, lo que da
	(12 7) = 792.

## Ejemplo 5

**Ejemplo** : Se quiere comprar una docena y se puede escoger entre donas de chocolate, glaciadas y de chantilly.

Si se quiere hacer por las ecuaciones se tiene que la ecuación es:
	a + b + c = 12

Con a, b, c ≥ 0, o también, si se tienen que escoger doce donas más, los dos separadores serían 14, de los cuales se deben escoger 2, por tanto, se pueden escoger de
	(14 2) = 91

# Ejercicios en Archivo