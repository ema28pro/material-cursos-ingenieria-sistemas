# Principio del palomar

Este principio también se conoce como el principio de las casillas o el principio a de Dirichlet y se trata de lo siguiente:

Si se tienen n+1 palomas y n palomares, se puede asegurar que existe al menos un palomar con dos palomas. Este simple hecho ayuda a demostrar problemas tanto de combinatoria, como de geometría, álgebra o teoría de números.

![Teorema] Si se tienen n + I objetos y se ponen en n cajas, entonces existe, al menos, una caja que contiene más de un objeto.

Hay ejemplos simples que ayudan a entender un poco más fácil el problema, si hay 13 personas en un salón se puede asegurar que, al menos, dos de ellos cumplen años el mismo mes y si hay 8 personas, como mínimo, se puede asegurar que al menos dos de ellos cumplen años el mismo día de la semana. Cuando se dice día no es por fecha en el calendario es por que cumple años un lunes, un martes, un miércoles, etc. Estos son algunos otros ejemplos que ayudan a entender el problema:

**Ejemplo** : Suponga que se sacan de un mazo de cartas, consecutivamente, de a una carta, el mazo tiene 52 cartas, ¿Cuántas cartas se deben sacar del mazo para asegurarse que existe, al menos, un par?

Se debe determinar cuales son los palomares y cuales son las palomas, los palomares los va a dar siempre una propiedad matemática o una propiedad que tengan los objetos con los que se trabaja o un conocimiento previo del problema. En este problema se sabe que cada pinta o dibujo tiene el mismo número de cartas, es decir, $13$, por lo tanto, los palomares van a ser las 13 posibles cartas.

Para asegurarse que se tiene un par, se deben sacar, como mínimo, 14 cartas y estas son las palomas, ya que en el caso más malo o en el caso que menor suerte se tenga, va a salir cada una de las cartas de los palomares que se tienen, es decir, 13 cartas con diferente número y al sacar la 14 esta va a encajar en cualquiera de las cajas que ya tienen un ocupante.

En el principio del palomar siempre se debe pensar en el caso más malo o el caso en el que se tenga la posibilidad de fracasar, ya que la propiedad que se está pidiendo puede cumplirse inmediatamente, pero se trata es de probar hasta que extremo se puede llevar sin que se cumpla.

**Ejemplo** : Dados 8 enteros, prueba que se pueden escoger 2 de tal forma que su diferencia sea divisible entre 7.

Note que cuando se divide un número entre 7, los posibles residuos son 0,1,2,3,4,5,6. Se toman estos 7 residuos como las casillas o palomares. Ahora se tienen 8 números, si cada uno de estos tiene un residuo diferente, hay uno que debe sobrar.

Además, note que si se tiene residuos diferentes, entonces cuando se haga la diferencia se obtiene lo siguiente: si a = 7k +r<sub>1</sub> y b = 7l+r<sub>2</sub> entonces:
	a − b = 7k + r<sub>1</sub> − 7l − r<sub>2</sub> = 7(k − l) + (r<sub>1</sub> − r<sub>2</sub>)
Pero como r<sub>1</sub> ≠ r<sub>2</sub> entonces a − b = 7t + r donde r = r<sub>1</sub> − r<sub>2</sub> ≠ 0. Así todos los que tengan diferentes residuos van en palomares diferentes. El último debe tener residuo igual a uno de los que ya esta en una de las palomeras y si tiene residuo igual, cuando se haga la resta debe dar 0 y, por tanto, la diferencia es múltiplo de 7.

Una generalización del teorema es la siguiente:

![Teorema] Si se tienen más de mk objetos y se ponen en k cajas, entonces en, al menos una de las cajas debe haber m + 1 objetos.

Los siguientes son algunos ejemplos en los que se aplica la generalización del principio del palomar.

**Ejemplo** : 25 cajas de manzanas son compradas en una tienda. Las manzanas son de tres tipos distintos y todas las manzanas de cada caja son del mismo tipo. Pruebe que de entre las cajas hay al menos 9 que contienen el tipo de manzanas.

Note que los palomares son 3 (los tres tipos de manzanas), en el caso más malo se tienen 8 cajas de cada uno en cada palomar, reste una que debe ir en alguna de las tres, por lo tanto, mínimo, hay 9 que contienen el mismo tipo de manzanas.
# Ejercicios

Los siguientes ejercicios son para la práctica
En archivo...

# Video Clase
![Videoclase: Principio del palomar](https://youtu.be/2JNDLgI2SPs)