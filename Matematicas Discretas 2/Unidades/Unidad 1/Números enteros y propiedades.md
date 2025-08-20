# Introducción

La teoría de números es el área de las matemáticas que se encarga de estudiar las propiedades de los números enteros. En computación, por ejemplo en Python y en casi todos los lenguajes de programación, los números enteros se toman como un tipo de dato primitivo y se pueden usar para expresar valores cuantitativos a las variables.  
  
A diferencia de los números con punto flotante, los enteros siempre se almacenan de forma exacta y no de forma aproximada. Sabemos que en la mayoría de los lenguajes de programación estos últimos se almacenan en una cantidad de espacio fija. A saber, 3232 bits, lo que limita su valor máximo a 231−1231−1 para enteros con signo. En Python se puede tener un tamaño arbitrario para los números enteros, solo lo limita la memoria de cada computadora.  
  
El estudio de la teoría de los números comienza con el conjunto de los números naturales, los cuales se denotarán por NN y son el conjunto  

N={1,2,3,4,5,…}N={1,2,3,4,5,…}

Para este conjunto se definen dos operaciones básicas: la adición y la multiplicación. En general, la sustracción no esta definida para el conjunto de los números naturales, ya que u,v∈Nu,v∈N, u−vu−v no siempre estan en el conjunto. Por lo tanto, se hace necesaria la inclusión de un nuevo símbolo, para representar los números negativos. Además, se debe agregar otro número que representa el neutro, el cual se denota por 00.  
  
La inclusión del cero y de los números negativos generan el conjunto de los números enteros, el cual se denota por ZZ y es

Z={…,−4,−3,−2,−1,0,1,2,3,4,…}Z={…,−4,−3,−2,−1,0,1,2,3,4,…}  

que también se puede ver como  

Z=N−∪{0}∪N+Z=N−∪{0}∪N+

La notación de ZZ al conjunto de los números enteros se debe a la palabra alemana Zahlen, la cual significa numbersnumbers.


## Propiedades de los números enteros

Las siguientes son las propiedades de los números enteros:

1. El conjunto de los números enteros es cerrado para la adición. Es decir, para todo a,b∈Za,b∈Z, se cumple que a+b∈Za+b∈Z
2. El conjunto de los números enteros es cerrado para la multiplicación. Es decir, Para todo a,b∈Za,b∈Z, se cumple que a⋅b∈Za⋅b∈Z
3. Si aa y bb son números enteros tales que a⋅b=0a⋅b=0, entonces a=0a=0 ó b=0b=0.

![Nota 1] Los numero enteros son cerrados para la division, es decir si a, b ∈ Z, no siempre se cumple que a ÷ b ∈ Z.
![Ejemplo] si a = 3 y b = 4, pero 3 ÷ 4 = 3 / 4 ∉ Z

![Nota 2] Para los números enteros no se puede garantizar el inverso multiplicativo, ya que no
es posible encontrar siempre el número entero b, tal que a · b = 1. Para que la propie-
dad se cumpla b € Q donde Q es el conjunto de los números racionales.

Debido al algoritmo de la división, el cual se verá en la próxima sección, el conjunto de los números enteros se le puede particionar en dos conjuntos disjuntos que son el conjunto de números impares y el conjunto de pares:  

I={±1,±3,±5,…}I={±1,±3,±5,…}  

P={0,±2,±4,±6,…}P={0,±2,±4,±6,…}  

Los cuales se pueden representar como I={2n+1|n∈Z}I={2n+1|n∈Z} y P{2n|n∈Z}P{2n|n∈Z}, respectivamente.  
  
Con esta partición y las propiedades de los números enteros y la representación de los números pares e impares, el lector debe ser capaz de demostrar las siguientes propiedades.

**Ejercicio 1**
- Par + Par = Par
- Par + Impar = Impar
- Impar + Impar = Par
- Par · Par = Par
- Par · Impar = Par
- Impar · Impar = Impar
Con base en lo anterior, resuelve el siguiente reto:

### Quiz

En las redes sociales se acostumbra poner retos matemáticos que muchas veces son aplicaciones simples de algunas propiedades de los conjuntos numéricos, uno de estos retos es:

![Reto] Dado {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29}, es posible escribir 30 como suma de 3 números del conjunto?
- [x] No
- [ ] Si
**_Comentario_** :  
La respuesta a esta pregunta es que NONO, ya que si se tienen tres número del conjunto, aa, bb y  
cc, podemos representar el problema como que a+b+c=30 a+b+c=30. Pero note que todos los elementos del conjunto son números impares, por lo que la suma es en una forma simple Impar + Impar + Impar = Par. El ejercicio anterior es falso, ya que Impar + Impar = Par, y ese resultado par al sumarlo con un impar es igual a impar. Lo cual hace que sea imposible que la suma de 30.

### Ejercicios
Con todos estos elementos dados en esta sección y un poco de razonamiento, el estudiante debe de ser capaz de hacer los siguientes ejercicios:
En Archivo...

## Referencias bibliográficas

- Andrica, D., y Andreescu, T. (2009). Number theory: structures, examples, and pro‐ blems. Birkhäuser Boston.
- Burton, D. (2010). Elementary Number Theory. Ebook. McGraw Hill. ‐Grigorieva, E. (2018). Methods of Solving Number Theory Problems. Springer International Publishing.
- Rosen, K. H. (1999). Discrete mathematics & applications. McGraw‐Hill.
- Stevens, J. (s. f.). Olympiad Number Theory Through Challenging Problems. [https://s3.amazonaws.com/cdn.artofproblemsolving.com/resources/articles/olympiad](https://s3.amazonaws.com/cdn.artofproblemsolving.com/resources/articles/olympiad)‐number‐theory.pdf