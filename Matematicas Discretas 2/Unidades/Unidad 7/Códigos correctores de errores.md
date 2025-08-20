# Códigos correctores de errores

Un código corrector de errores es un algoritmo o sistema diseñado para detectar y corregir errores que pueden ocurrir durante la transmisión o almacenamiento de datos digitales. Estos errores pueden surgir debido a:

- Interferencias en la señal
- Ruido
- Fallas en los dispositivos de comunicación
- O cualquier otro factor que pueda alterar los datos

El objetivo principal de un código corrector de errores es garantizar la integridad y confiabilidad de los datos, asegurándose de que se transmitan o almacenen de manera precisa, sin errores. Estos códigos se utilizan en una amplia gama de aplicaciones, incluyendo telecomunicaciones, redes de computadoras, almacenamiento de datos, sistemas de control, transmisión de video y audio, entre otros.

Un código corrector de errores, generalmente, se basa en la adición de bits adicionales a los datos originales, también se llama **código redundante**, de modo que la información contenida en esos bits redundantes permita detectar y, en algunos casos, corregir errores.

Al recibir los datos, el receptor utiliza el código corrector de errores para verificar si los hays. Si se detectan errores, el código puede determinar la ubicación y la magnitud de ellos, y en algunos casos, corregirlos mediante algoritmos específicos.

Como se vio en los códigos de paridad, son códigos correctores de errores muy simples que se utilizan, principalmente, para detectar errores en la transmisión de datos. Aunque no pueden corregir errores, pueden identificar cuándo se ha producido uno en la transmisión.

Suponga que tiene una palabra de datos de 4 bits: 1011, y quiere agregar un bit de paridad para detectar errores en la transmisión.

Se cuenta el número de unos en la palabra de datos. En este caso, como se puede notar, hay 3. Entonces se agraga un bit de paridad al final de la palabra de datos. El valor de este bit se establecerá para que la suma total de unos (incluido el bit de paridad) sea par o impar. En este caso, como hay 3 unos (un número impar), se establece que el bit de paridad es 1.

La palabra de datos original con el bit de paridad agregado sería: 10111.

Ahora, se supone que durante la transmisión se produce un error y se cambia el tercer bit. La palabra de datos recibida sería: 10011.

Para verificar si hay un error, se cuenta nuevamente el número de unos en la palabra de datos recibida. En este caso, hay 2 unos.

A continuación, se compara el bit de paridad recibido con el número de unos. Si son diferentes, eso significa que se ha producido un error.

En este caso, el bit de paridad recibido es 1, pero el número de unos en la palabra de datos es 2, lo que indica que ha ocurrido un error.

Mediante el código de paridad, se pudó detectar que se ha producido un error, pero no se puede determinar qué bit específico es incorrecto ni corregirlo. Para la corrección de errores, se necesitarían códigos más avanzados. En este caso, se debe solicitar la retransmisión.

Algo que se debe tener en cuenta es que un código de paridad se puede determinar un solo error.

En un código de 5 dígitos, determine si en $111010$ existe un error o no. Note que el número de paridad es cero, es decir, que exite un número par de unos, lo cual es verdad, por lo tanto el código no tiene errores.

Para el código Hamming, visto en la sección anterior, recuerde que la matriz generadora es $G = (I_{k}|−A^{T})$, pero la matriz de verificación de paridad es $H = (A | I_{n−k})$. Se debe notar que para verificar si estas dos matrices están bien construidas se debe tener que $HG^{T} = 0$, donde el $0$ determina la matriz de ceros.

Para el código $H(7,4)$, el código de verificación de paridad es:

$$
H = \begin{bmatrix}
1&1&0&1&1&0&0\\
1&0&1&1&0&1&0\\
0&1&1&1&0&0&1
\end{bmatrix}
$$

Para determinar si existe un error, se debe tomar el vector recibido y multiplicarse por la transpuesta de la matriz de verificación de paridad, si se obtiene el vector nulo, no existe ningún error en el código recibido. Es decir, si $s = xH^{T}$. Si $s=0$ como vector, no se tienen errores.

En el ejemplo de la sección anterior se recibió como mensaje codificado:
$$
\begin{bmatrix}
1&0&1&1&0&1&0
\end{bmatrix}
$$
Si se multiplica:
$$
\begin{bmatrix}
1 & 0 & 1 & 1 & 0 & 1 & 0
\end{bmatrix}
\begin{bmatrix}
1 & 1 & 0 \\
1 & 0 & 1 \\
0 & 1 & 1 \\
1 & 1 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix} =
\begin{bmatrix}
0 & 0 & 0
\end{bmatrix}
$$
Por lo tanto no hay errores.

Note que, si por el contrario, se cambia el tercer dígito del vector recibido, el vector queda:
$$\begin{bmatrix}
1 & 0 & 0 & 1 & 0 & 1 & 0
\end{bmatrix}$$
Al multiplicar se obtiene:
$$
\begin{bmatrix}
1 & 0 & 0 & 1 & 0 & 1 & 0
\end{bmatrix}
\begin{bmatrix}
1 & 1 & 0 \\
1 & 0 & 1 \\
0 & 1 & 1 \\
1 & 1 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix} =
\begin{bmatrix}
0 & 1 & 1
\end{bmatrix}
$$
Por lo tanto, existe un error, ya que no se obtuvo el vector nulo, pero ¿Cómo corregirlo? Pues en este sentido es fácil, se obtiene debido a que el vector resultante queda en la posición 33 de la matriz HH. Por lo que el dígito a cambiar es el dígito en la posición 33.

Otro ejemplo es cambiar el dígito 6 del vector de entrada, es decir:
$$
\begin{bmatrix}
1 & 0 & 1 & 1 & 0 & 0 & 0
\end{bmatrix}
\begin{bmatrix}
1 & 1 & 0 \\
1 & 0 & 1 \\
0 & 1 & 1 \\
1 & 1 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix} =
\begin{bmatrix}
0 & 1 & 0
\end{bmatrix}
$$
Por lo tanto, el código detector de errores determina que existe un error en la posición 66, ya que el vector en la posición $6$ de la matriz $H$ es $\begin{bmatrix} 0 & 1 & 0 \end{bmatrix}$.
# Ejercicios

Los siguientes ejercicios son para la práctica de los estudiantes.
En archivo...