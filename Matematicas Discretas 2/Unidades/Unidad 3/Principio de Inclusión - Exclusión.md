# Principio de Inclusión - Exclusión

A continuación, se estudiará una herramienta para contar uniones de eventos, se utilizará el cardinal de un conjunto representado por |X|, el cual da el número de elementos del conjunto X. Note que si los conjuntos X y Y son disjuntos, entonces |X+Y| = |X| + |Y|

Si se quiere aplicar el principio de inclusión-exclusión para dos conjuntos que no son disjuntos se da que

|A∪B| = |A| + |B| + |A∩B|

Estos son el número de elementos que hay en ambos conjuntos, restando los elementos comunes, para no contarlos varias veces.

A continuación, se presentará una serie de ejemplos de manera secuencial

_Navegue por el siguiente acordeón haciendo clic en cada ejemplo para desplegar la información_

## Ejemplo 1
 
 **Ejemplo** : De cuarenta personas, 28 nadan y 16 corren. También se sabe que hay 10 que corren y nadan. ¿Cuántas personas de las 40 no corren ni nadan?

Por el principio de inclusión-exclusión, si A son los nadadores y B los que corren, entonces se tiene que |A| = 28, |B| = 16 y |A∩B| = 10, por tanto, todos los que practican alguna disciplina son |A∪B| = 28 + 16 − 10 = 34. Como lo que se busca son los que no practiquen ningún deporte de los dos, se calcula así 40 − 34 = 6.

## Ejemplo 2

**Ejemplo** : ¿Cuántos enteros entre 1 y 1000, inclusive, no comparten un factor común con 1000?

Recuerde que 1000 = 2<sup>3</sup> 5<sup>3</sup>, entonces los números que se buscan no deben
tener ningún factor común con 2 ni con 5. Si A es el conjunto de todos los
números entre 1 y 1000 que son múltiplos de 2 y B el conjunto de todos los
números que son múltiplos de 5, por tanto, | A | = 1000 / 2 = 500,
| B | = 1000 / 5 = 200 y | A ∩ B | = 1000 / 10 = 100. Así, todos los que tienen un
factor en común con mil son : | A ∪ B | = 500 + 200 - 100 = 600 y los que no
tienen un factor común son 1000 - 600 = 400.

Según el contenido visto hasta ahora, se puede verificar esto simplemente
calculando ϕ(1000).

Si se quiere hacer con tres conjuntos: A, B y C, el principio de inclusión exclusión se da de la siguiente forma:
	| A ∪ B ∪ C | = | A | + | B | + | C | - | A ∩ B | + |A ∩ C| + | B ∩ C | + | A ∩ B ∩ C |
Que es la suma de los cardinales de los tres conjuntos, restando los que se
repiten en pares de conjuntos, pero note que se sacan los que están en los tres,
por eso ge deben volver a añadir.

## Ejemplo 3

**Ejemplo** : En un grupo de 30 personas, 8 hablan inglés, 12 francés y 10 italiano; también se sabe que 5 hablan inglés y francés, 5 francés e italiano y 7 inglés e italiano. EI número de personas que hablan los tres idiomas es 3. ¿Cuántas personas no hablan ningún idioma?

Sea A el conjunto de personas que hablan inglés, B el conjunto de personas que hablan francés y C el conjunto de personas que hablan italiano, entonces 10 que se tiene es 10 siguiente:
	| A | = 8
	| B | = 12
	| C | = 10
	| A ∩ B | = 5
	| A ∩ C |= 5
	| B ∩ C | = 7
	| A ∩ B ∩ C | = 3
y así | A ∪ B ∪ C | = 8 + 12 +10 - 5 - 5 - 7 + 3 = 16 y, por tanto, los que no hablan ningún idioma son 30 - 16 = 14

## Ejemplo 4 en Archivo