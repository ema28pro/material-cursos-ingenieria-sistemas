# Introducción

Ahora se estudiará uno de los temas más interesantes y complicados de la matemática, el área de la combinatoria.

Desde pequeños se aprende a contar y se cree que se sabe contar, pero en realidad lo que se ha contado solo son elementos que se tocan y que nunca implican problemas más complicados que involucren conjuntos, grafos, retículos, entre muchas cosas más. Por tal motivo, a lo largo de este recurso se podrán conocer algunas técnicas de conteo que involucran formas más sofisticadas.

# Principio de la multiplicación

Suponga que un experimento A puede ser realizado en k etapas: A<sub>1</sub> primero, A<sub>2</sub> segundo, A<sub>3</sub> tercero, ……, A<sub>k</sub> por último. Suponga, además, que A<sub>i</sub> puede ser hecho de n<sub>i</sub> formas diferentes y que ese número de formas para realizar A<sub>i</sub> no es influenciado por los pasos anteriores o siguientes. Entonces, A<sub>1</sub> y A<sub>2</sub> y …… y E<sub>k</sub> pueden ocurrir simultáneamente en n<sub>1</sub> n<sub>2</sub> . . . n<sub>k</sub> formas.

**Ejemplo** : En un grupo de 12 hombres y 15 mujeres se puede escoger un hombre y una mujer en 12 · 15 = 180 formas.

**Ejemplo** : Un dado rojo y un dado azul, ¿de cuantas formas ellos pueden caer?

Note que lo que se esta buscando son los pares ordenados (r, a), donde r y a son los valores en los que puede caer el dado rojo y el dado azul, respectivamente. Así, la regla de la multiplicación da que hay 66 posibles parejas. Estas son:

|       |       |       |       |       |       |
| ----- | ----- | ----- | ----- | ----- | ----- |
| (1,1) | (1,2) | (1,3) | (1,4) | (1,5) | (1,6) |
| (2,1) | (2,2) | (2,3) | (2,4) | (2,5) | (2,6) |
| (3,1) | (3,2) | (3,3) | (3,4) | (3,5) | (3,6) |
| (4,1) | (4,2) | (4,3) | (4,4) | (4,5) | (4,6) |
| (5,1) | (5,2) | (5,3) | (5,4) | (5,5) | (5,6) |
| (6,1) | (6,2) | (6,3) | (6,4) | (6,5) | (6,6) |

Otra forma de mirar esto es tomando dos espacios en blanco:

|     |     |
| --- | --- |

Pero como el dado rojo puede caer de seis formas diferentes, entonces, en el primer cajón, que es el que representa dicho dado, se cuentan las formas en las que puede caer, no uno de los números en los que cae.

| 6   |     |
| --- | --- |

y como el dado azul puede caer también en seis formas diferentes, por tanto, en el segundo cajón se debe poner el número 66.

| 6   | 6   |
| --- | --- |

Y al multiplicar el número de formas debe ser 36.

Aplicando está última técnica se puede hacer el primer ejemplo y los siguientes:

**Ejemplo** : Un examen de selección múltiple tiene 20 preguntas, cada una con cuatro posibles respuestas. ¿De cuentas formas se puede realizar el examen?

Como cada pregunta tiene 4 posibles soluciones, estas se pueden poner en 20 cajones y, así, la respuesta por la regla del producto 4<sub>20</sub> = 1099511627776.
# Principio de la suma

A<sub>1</sub>, A<sub>2</sub>, …, A<sub>k</sub> son eventos mutuamente excluyentes por parejas. Si A<sub>i</sub> puede ocurrir de n<sub>i</sub> formas, entonces A<sub>i</sub> o A<sub>2</sub> o …… o A<sub>k</sub> puede ocurrir en n<sub>1</sub> + n<sub>2</sub> + n<sub>3</sub> + ⋯ + n<sub>k</sub> formas.

**Ejemplo** : En un grupo de 12 hombres y 15 mujeres, ¿de cuantas formas se puede escoger un hombre o una mujer?

Esto se puede hacer de 12 + 15 = 27 formas.

**Ejemplo** : Hay cinco golde retrievers, seis irish setters y ocho poodles para la venta en una veterinaria, de cuantas maneras se puede escoger un perro?

El número de formas para escoger un perro es 5 + 6 + 8 = 19.

**Ejemplo** : En el ejemplo anterior, ¿de cuántas formas se pueden escoger dos perros si ellos no son de la misma raza?

Este problema es un poco más complicado, pero lo que lo complica es que se deben usar las dos reglas, primero la de la múltiplicación y luego la de la suma.

Note que para escoger un golden y un irish hay 5 ⋅ 6 = 30 formas, que para escoger un golden y un poodle hay 5 ⋅ 8 = 40 formas, y que para escoger un irish y un poodle hay 6 ⋅ 8 = 48  formas. En total las formas de escoger dos perros de dos razas diferentes es 30 + 40 + 48 = 118

**Ejemplo** : Para ir de una ciudad A a una ciudad B, se pueden tomar cuatro rutas de bus, cuatro posibles trenes o seis formas de ir en bote. ¿De cuántas formas se puede ir de A hasta B.

Como cada uno de esos eventos son independientes, se tiene que hay 4 + 4 + 6 = 14 formas.

# Ejercicios

Los siguientes problemas son para la practica de los estudiantes.
En archivo...