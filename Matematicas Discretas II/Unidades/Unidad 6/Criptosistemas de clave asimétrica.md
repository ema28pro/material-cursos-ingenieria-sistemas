## Definición

Un criptosistema asimétrico, también conocido como criptografía de clave pública, es un tipo de sistema de cifrado que utiliza dos claves: una pública y una privada. La clave pública se puede distribuir libremente entre quienes quieran enviar un mensaje al propietario esta; mientras que la clave privada se mantiene en secreto y solo la conoce el propietario de ambas claves.

El criptosistema asimétrico más popular es el algoritmo RSA, inventado por Ron Rivest, Adi Shamir y Leonard Adleman del MIT. Este se basa en el problema matemático de factorizar números enteros grandes, asunto considerado difícil de resolver usando computadoras clásicas.

En el algoritmo RSA un usuario genera un par de claves: una pública y una privada. La pública es un número grande producto de dos números primos; mientras que la privada es el par de factores primos utilizados para generar la clave pública. El usuario publica la clave pública a cualquiera que quiera enviarle un mensaje encriptado, manteniendo en secreto la privada.

Para cifrar un mensaje mediante RSA el remitente utiliza la clave pública del destinatario para transformar el mensaje en un texto cifrado. Para descifrar el mensaje, el destinatario usa su clave privada para revertir la transformación y recuperar el mensaje original.

Otros criptosistemas asimétricos populares incluyen el intercambio de claves Diffie-Hellman, utilizadas para establecer una clave secreta compartida entre dos partes, y la criptografía de curva elíptica (ECC), que es un algoritmo más nuevo que se considera más seguro que RSA para la misma clave.

Los criptosistemas asimétricos, a menudo, se usan en combinación con los simétricos para lograr un equilibrio entre seguridad y rendimiento. El criptosistema asimétrico se utiliza para intercambiar, de forma segura, una clave simétrica, que luego se utiliza para cifrar y descifrar el mensaje real. Este enfoque permite el cifrado y descifrado rápido de mensajes, al mismo tiempo que proporciona una forma segura de intercambiar claves.

## Intercambio de claves Diffie-Hellman

En criptografía las claves se utiliza para cifrar y descifrar mensajes de manera que puedan transmitirse de forma segura entre dos partes. El proceso de intercambio de claves de forma segura es crucial para garantizar que la comunicación permanezca confidencial y no pueda ser interceptada por un tercero.

Un algoritmo popular para el intercambio de claves es el intercambio de claves Diffie-Hellman, que permite a dos partes establecer una clave secreta compartida a través de un canal de comunicación inseguro. Los pasos del intercambio de claves Diffie-Hellman son los que se mencionan a continuación.

Se consideran dos personajes para el intercambio, Alice que es el emisor y Bob que es el receptor:

1. Alice y Bob acuerdan un número primo grande, p, y un valor base, g. Ese valor g se pide que sea primo relativo con $p$.
2. Alice elige un número secreto, a, y calcula A ≡ g<sup>a</sup> mod p.
3. Bob elige un número secreto, b, y calcula B ≡ g<sup>b</sup> mod p.
4. Alice y Bob intercambian A y B por el canal de comunicación inseguro.
5. Alice calcula la clave secreta compartida, K ≡ B<sup>a</sup> mod p.
6. Bob calcula la clave secreta compartida, K ≡ A<sup>b</sup> mod p.

Ahora, Alice y Bob han establecido una clave secreta compartida que pueden usar para cifrar y descifrar los mensajes que se envían entre ellos. Este intercambio de claves es seguro porque un intruso que intercepta A y B no puede calcular fácilmente la clave secreta compartida sin conocer a o b.

#### Ejemplo
Sea p=13 y g=3, si Alice escoge a a=5 y Bob escoge b=7, encontrar la clave generada por Alice y Bob

Alice debe calcular:
	A ≡ 3<sup>5</sup> mod 13
Que es igual A ≡ 9 mod 13, y Bob debe calcular:
	B ≡ 3<sup>7</sup> mod 13

El cual es igual a B ≡ 3 mod 13, entonces Alice recibe B y Bob recibe A.

Alice toma a B y calcula K ≡ 3<sup>5</sup> mod 13, obtiene K ≡ 9 mod 13 y Bob toma a A A y calcula K ≡ 9<sup>7</sup> mod 13 y obtiene K ≡ 9 mod13, así que la clave con la que van a cifrar es K=9.

En este ejemplo se puede notar que el algoritmo funciona, pero se debe de tener claro que el número p debe de ser grande para poder garantizar la privacidad del intercambio de las claves.

Dado p=127 y g=43, entonces la clave que comparten Bob y Alice, si se sabe que a=23 y b=51, es:
- [ ] 49
- [ ] 100 
- [ ] 18
- [x] 80
**_Comentario_** :  
	La respuesta es 80, ya que 43<sup>23</sup> ≡ 23 mod 127 y 43<sup>51</sup> ≡ 89 mod 127, si Alice calcula 89<sup>23</sup> ≡ 80 mod127 y si Bob calcula 23<sup>51</sup> ≡ 80 mod 127.

## Criptosistema RSA

RSA es un criptosistema ampliamente utilizado para la comunicación segura. Se basa en las propiedades matemáticas de los números primos y la aritmética modular.

El criptosistema RSA funciona de la siguiente manera:

**Generación de claves**: primero se genera un par de claves:una pública y una privada. La clave pública se distribuye a cualquier persona que desee enviar un mensaje cifrado, mientras que el propietario mantiene en secreto la privada.

**Cifrado**: para cifrar un mensaje, el remitente utiliza la clave pública del destinatario para transformar el mensaje de texto plano en texto cifrado. Esto se hace elevando cada caracter del mensaje a la potencia del módulo de clave pública (un producto de dos números primos grandes). El texto cifrado resultante solo se puede descifrar utilizando la clave privada del destinatario.

**Descifrado**: para descifrar el texto cifrado el destinatario usa su clave privada para transformarlo nuevamente en texto plano. Esto se hace elevando cada caracter del texto cifrado a la potencia del módulo de clave privada. El texto plano resultante es el mensaje original.

La seguridad del criptosistema RSA se basa en la dificultad de factorizar números grandes en sus factores primos. Cuanto mayor sea el tamaño de la clave más seguro será el cifrado. RSA se usa ampliamente en transacciones en línea, encriptación de correo electrónico y otras aplicaciones donde la comunicación segura es esencial. Sin embargo, es importante tener en cuenta que RSA es vulnerable a los ataques de las computadoras cuánticas y, por lo tanto, se están desarrollando alternativas resistentes a dicha computación.

Para encriptar con el RSA, se deben seguir los siguientes pasos:

1. Generar claves: en este proceso se generan tanto la claves pública como la privada, y los pasos que se deben de seguir son los siguientes:  
    - Seleccionar dos números primos grandes y distintos, $p$ y $q$. Al principio se trabajaba con números de 128 bits, hoy en día se esta trabajando con números de 2048 bits.
    - Calcular el módulo $n = p × q$.
    - Calcular la función $ϕ(n) = (p − 1) ⋅ (q − 1)$.
    - Elegir un número $e$ que sea primo relativo con $ϕ(n)$ y menor que $ϕ(n)$ como clave pública.
    - Calcular el inverso multiplicativo $d$ de $e$, módulo $ϕ(n)$, como clave privada.
2. Cifrado: para cifrar el emisor, tome la clave pública y ejecute lo siguiente:
	- Convertir el mensaje en un número entero mm que sea menor que $n$.
	- Calcular el valor cifrado $c ≡ m$<sup> e</sup>$\mod n$.
3. Descifrado: para descifrar el receptor reciba el mensaje cifrado y descifre con la clave privada $d$, siguiendo los siguientes pasos:
	- Calcular el valor descifrado $m ≡ c$<sup>d</sup> $\mod n$.
	- Convertir mm en el mensaje original.

En los ejemplos a continuación se usan números primos pequeños, pero la idea es que se comprenda que los números usados son grandes y que el éxito del criptosistema se basa en la imposibilidad de poder factorizar $n$.

Dados lo primos $p = 43$ y $q = 71$ y que $e = 17$, hallar la clave privada $d$

Recuerde que $n = 3053$. Se quiere hallar $ϕ(3053)=(43−1)(71−1)=42⋅70=2940$, y como $e=17$, se debe encontrar el inverso de $17$ módulo $2940$, el cual se obtiene de calcular $17d ≡ 1 \mod 2940$, lo que implica que $d ≡ 173 \mod 2940$. Por lo tanto, la clave privada es $d=173$.

Ahora con un poco más de dificultad:
#### Ejemplo 2

Dado que $n=296986533663941440404829$ y que $e=5723$, hallar la clave privada $d$

La dificultad se da por la necesidad de factorizar el número. La cantidad de primos que tiene cada primo en el producto $n$ es de $12$. Así que es más complicado al hacerlo a mano, pero con un software de cálculo se consigue que $n=497253498331⋅597253784359$. Así $ϕ(n)=296986533662846933122140$, y si se quiere verificar que $mcd(e, ϕ(n))=1$, puede hacerse, y al encontrar su inverso da que $d=61545697872468366710267$. La cual se toma como la clave privada.

Ahora se muestran ejemplos de como encriptar usando la misma codificación de los métodos anteriores. Para esto se puede usar cada letra para encriptar, pero también se puede hacer por bloques

#### Ejemplo 3
Encriptar la palabra ``discretas``, si se sabe que $n=4183$ y $e=57$

Note que para encriptar solo se necesita esta información, por lo tanto, como ``discretas`` en código es ``03 08 18 02 17 04 19 00 18``, cada uno se debe elevar a la $57$ módulo $4183$.

Esto es:

3<sup>57</sup> ≡ $2871 \mod 4183$
8<sup>57</sup> ≡ $3891 \mod 4183$
18<sup>57</sup> ≡ $1137 \mod 4183$
2<sup>57</sup> ≡ $2941 \mod 4183$
17<sup>57</sup> ≡ $53 \mod 4183$
4<sup>57</sup> ≡ $3220 \mod 4183$
19<sup>57</sup> ≡ $29 \mod 4183$
0<sup>57</sup> ≡ $0 \mod 4183$
18<sup>57</sup> ≡ $1137 \mod 4183$

De este modo, por RSA queda cifrado la palabra ``discretas`` como ``2871 3891 1137 2941 53 3220 29 0 1137``.

Note que al cifrar no se escribe en palabras lo que se cifra, ya que es complicado cifrar todas las números con el vocabulario limitado que se tiene.

Recuerde que el único que conoce la clave privada es el receptor, por eso es que con la clave pública se puede cifrar, pero si no se sabe la factorización de $n$, es imposible saber cual es la frase de descifrado.

Para el ejemplo anterior, si Bob quiere descifrar el mensaje debe saber cual es la factorización, que en este caso es: $n = 4183 = 47 ⋅ 89$ así $ϕ(n) = 4048$. Y para encontrar la clave privada se debe calcular el inverso de $57$ módulo $4048$, para eso se debe comprobar que $57$ es primo relativo con $4048$ y resolver la ecuación modular lineal $57d ≡ 1 \mod 4048$, al resolver se encuentra que $d ≡ 3977 mod 4048$.

Ahora, para descifrar, Bob toma su clave privada y calcula:

2871<sup>3977</sup> ≡ $3 \mod 4183$
3891<sup>3977</sup> ≡ $8 \mod 4183$
1137<sup>3977</sup> ≡ $18 \mod 4183$
2941<sup>3977</sup> ≡ $2 \mod 4183$
53<sup>3977</sup> ≡ $17 \mod 4183$
3220<sup>3977</sup> ≡ $4 \mod 4183$
29<sup>3977</sup> ≡ $19 \mod 4183$
0<sup>3977</sup> ≡ $0 \mod 4183$
1137<sup>3977</sup> ≡ $18 \mod 4183$

Lo que hace que se regrese a los códigos de las letras para descifrar el mensaje oculto o texto plano.

Use la misma clave pública para identificar cuál de los siguientes códigos cifrados es ``hola``
 - [x] ``412 2805 1214 0``
 - [ ] ``959 2147 133 0``
 - [ ] ``1916 1818 274 0``
 - [ ] ``1547 342 1258 0``
_Comentario_:  
	La respuesta es **"412 2805 1214 0"**, ya que cuando se calcula:
		$7^{57} \equiv 412 \mod 4183$
		$14^{57}\equiv 2805 \mod 4183$
		$11^{57}\equiv 1214 \mod 418$
		$0^{57} \equiv 0 \mod 4183$
	Se invita al estudiante a investigar cómo hacer el cifrado por bloques.

## Criptosistema ElGammal

Es un tipo de algoritmo de cifrado de clave pública propuesto por primera vez por Taher ElGamal en 1985. Se basa en el problema del logaritmo discreto, que se cree que es computacionalmente difícil de resolver.

Como es un cifrado de clave pública, involucra la clave pública y una clave privada. La clave pública consta de número primo $p$ grande y se debe tomar un generador gg del grupo multiplicativo módulo $p$. Se suponde que todos los números del 11 hasta $p−1$, son primos relativos con $p$, pero no todos ellos cuando se elevan a una potencia negativa $n$ tienen orden $n$, que es $g^{p−1} ≡ 1 \mod p$. En sí, pueden tener orden menor. A continuación se presenta un ejemplo con un número $p$ pequeño.

Sea $p=7$, entonces el orden de cada elemento, en un grupo multiplicativo, se define como el menor entero $n$ tal que $g^{n} ≡ 1 mod p$. Como los elementos de este grupo son $\{1,2,3,4,5,6\}$, sus órdenes son:
	$1^{1} ≡ 1 \mod 7$
	$2^{3} ≡ 1 \mod 7$
	$3^{6} ≡ 1 \mod 7$
	$4^{3} ≡ 1 \mod 7$
	$5^{6} ≡ 1 \mod 7$
	$6^{2} ≡ 1 \mod 7$
Entonces como posibles generadores solo sirven el $3$ y el $5$, ya que son los que generan todos los números del conjunto.

Si $p=11$ los generadores son $2,6,7,8$ y la cantidad de posibles generadores va creciendo de acuerdo al primo. Por ejemplo, $p=127$ tiene $36$ generadores y $1237$ tiene $408$, y el primer primo mayor que un millón, que es $1000003$, tiene $333332$ generadores. La importancia de estos es que al tomar alguno, permite tomar la clave privada que consiste en un número entero secreto $x$ elegido al azar, tal que $1≤x≤p−1$.

Se sabe que $y ≡ g^{x} mod p$, así la clave privada es xx y la clave pública es $(p,g,y)$.

El emisor quiere enviar un mensaje $M$, el cual debe ser un número entre $0≤M≤p−1$, entonces escoge un valor $k$, tal que $0≤k≤p−1$ y calcula $K ≡ y^{k} \mod p$.

Posteriormente, cifra el mensaje $M$ por el par $(C1,C2)$, donde $C_{1} ≡ g^{k} \mod p$ y $C_{2} ≡ KM \mod p$.

Para descifrar se recibe $(C1,C2)$ se calcula $K$, calculando $K ≡ (C_{1})^{x} \mod p$, y se obtiene el texto plano calculando $M ≡ C_{2}K^{−1} \mod p$.

Como ejemplo se toma a $p=19$, el cual tiene como raíces primitivas:
	$\{2,3,10,13,14,15\}$
Se toma como $g=13$ y $x=5$, así $y ≡ 13^{5} \mod 19$, lo cual da que $y ≡ 14 \mod 19$. Por tanto, la clave pública es $(19,13,14)$.

Si se quiere enviar un mensaje con valor $M=12$, entonces se toma un $k=3$ y se calcula $K ≡ 14_{3} mod 19$, lo cual da $K ≡ 8 \mod 19$, así $C_{1} ≡ 13^{3} \mod 19$ lleva a que $C_{1} ≡ 12 \mod 19$ y $C_{2} ≡ 8 × 12 \mod 19$, lo cual es igual a $C_{2} ≡ 1 \mod 19$, así el mensaje encriptado es $(12,1)$.

Para desencriptar: $K ≡ 12^{5} mod 19$, lo que muestra que $K ≡ 8 \mod 19$. Se calcula su inverso $K^{−1} = 8^{−1} ≡ 12 \mod 19$, así al calcular $M ≡ (1×12) \mod 19$, lo que lleva que $M ≡ 12 \mod 19$.

# Ejercicios

Los siguientes ejercicios son para la práctica de los estudiantes.

1. Suponga que desea utilizar el algoritmo de encriptación RSA para enviar un mensaje a su amigo con una clave pública $(n,e)=(35,11)$. Cifre el mensaje HOLA usando el código ASCII y muéstrele a su amigo cómo descifrar el mensaje con la clave privada.
2. Suponga que está utilizando el algoritmo de cifrado RSA con una clave pública $(n,e)=(187,5)$ y una clave privada $(n,d)=(187,101)$. Recibe un mensaje encriptado "49 118 145 26" de su amigo. Descifre el mensaje y muestre lo que dice.
3. Suponga que desea utilizar el algoritmo de encriptación RSA para enviar un mensaje a su amigo con una clave pública $(n,e)=(91,5)$. Si el mensaje es "ME ENCANTAN LAS MATEMÁTICAS", cífrelo con el código ASCII y muestre el resultado.
4. Suponga que está utilizando el algoritmo de cifrado RSA con una clave pública $(n,e)=(3233,17)$ y una clave privada $(n,d)=(3233,2753)$. Recibe un mensaje encriptado "855 1540 2904 1025 1248 2904" de su amigo. Descifre el mensaje y muestre lo que dice.
5. Se intersecta un mensaje de tu amigo que está encriptado usando RSA con la clave pública $(n,e)=(299,5)$. El mensaje cifrado es "245 69 54 214". Encuentre la clave privada y descifre el mensaje.
6. Seleccione dos números primos grandes $p=23$ y $q=11$ y un número entero aleatorio $g=3$, tal que $1<g<p$. Alice elige un número secreto $x_{A}=7$ y calcula $y_{A} = g^{x_{A}} \mod p$. Ahora, Bob quiere enviarle un mensaje a Alice. Para ello, elija un número aleatorio $k=5$ y calcule $a = g^{k} \mod p$ y $b = m ⋅ y^{k}_{A} \mod p$, donde $m$ es el mensaje que desea enviar$(m=17)$. ¿Cuál es el mensaje cifrado que Bob enviará a Alice?
7. Continuando con el ejercicio anterior, Alice recibe el mensaje cifrado $(a,b)$ de Bob. Para descifrar el mensaje, ella utiliza su número secreto $x_{A}$ y calcula $a^{p−1−x_{A}} \mod p$ y, luego, multiplica el resultado obtenido por $b \mod p$. ¿Cuál es el mensaje que Alice recibió?
8. Seleccione dos números primos grandes $p=47$ y $q=23$ y un número entero aleatorio $g=5$, tal que $1<g<p$. Alice elige un número secreto $x_{A} = 11$ y calcula $y_{A} = g^{x_{A}} \mod p$. Ahora, Bob quiere enviarle un mensaje a Alice. Para ello, elige un número aleatorio $k=9$ y calcula $a = g^{k} \mod p$ y $b = m ⋅ y^{k}_{A} \mod p$, donde $m$ es el mensaje que desea enviar $(m=13)$. ¿Cuál es el mensaje cifrado que Bob enviará a Alice?
9. Continuando con el ejercicio anterior, Alice recibe el mensaje cifrado $(a,b)$ de Bob. Para descifrar el mensaje, ella utiliza su número secreto $x_{A}$ y calcula $a^{p−1−x_{A}} \mod p$ y, luego, multiplica el resultado obtenido por $b \mod p$. ¿Cuál es el mensaje que Alice recibió?

