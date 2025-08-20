# Criterios de divisibilidad

Observa la siguiente presentación para conocer sobre los Criterios de Divisibilidad

- Un número es divisible por 2 cuando este termina en par, es decir, en 0,2,4,6,8, o es divisible por 5 cuando termina en 0 o en 5, estos son ejemplos de a lo que se refieren los criterios de divisibilidad.
- Pues bien, estas son consecuencias de las congruencias. Si se toma a N, un número positivo mayor que 2, este se puede escribir en la base 10 de la forma:
		N= a<sub>n</sub>10<sup>n</sup> + a<sub>n-1</sub>10<sup>n-1</sup> + · · · + a<sub>2</sub>10<sup>2</sup> + a<sub>1</sub>10 + a<sub>0</sub> 
	Donde a<sub>0</sub>, a<sub>1</sub>,..., a<sub>n</sub> son enteros positivos que están entre 0 y 9, incluidos.
- En esta sección se ven algunos de los criterios. Y es cierto que existe un criterio universal, el cual permite determinar la divisibilidad por cualquier primo, pero el costo computacional es el mismo que si se hiciera la división, por eso no es muy utilizado. Este funciona más o menos de la siguiente forma: se considera
	N' = a<sub>n</sub>10<sup>n-1</sup> + a<sub>n-1</sub>10<sup>n-2</sup> + · · · + a<sub>2</sub>10+ a<sub>1</sub> = (N - a<sub>0</sub>)/10
- El criterio entonces dice que si mcd(p, 10) = 1 y existe un b ∈ Z, tal que 10b = 1 mod p, entonces N ≡ 0 mod p si y solo si N' + ba<sub>0</sub>  0 mod p.
	Así, si se quiere saber si un número es divisible por 13, se debe buscar un b tal que 10b ≡ 1 mod 13, esto pasa cuando b ≡ 4 mod 13. Así que si un número N es divisible por 13, entonces 13 debe dividir a N' + 4a<sub>0</sub>. Sea N = 1001, si 13 divide a N, entonces 13
- debe dividir a 100 + 4 * 1 = 104, si esto aún no se puede determinar vuelve y se aplica, es decir, si 104 es divisible por 13, es por que 13 divide a 10 + 4 * 4 = 10 + 16 = 26 y esto es cierto, por tanto 13 divide a 1001.
- Ahora, si se toma p = 29 y N = 2436 para verificar si 29 divide a N, se debe conseguir un b ∈ Z tal que 10b ≡ 1 mod 29 y esto sucede cuando b ≡ 3 mod 29. Por lo tanto, 29 | 2436 si 29 | (243 + 6 * 3) que es igual a 29 | 261, si todavía no se puede determinar, se hace de nuevo el proceso y entonces 29 | 261, si 29 | (26 + 3 * 1) que es lo mismo que 29 | 29, у esto es cierto. Por lo tanto, 29 | 2436.
- **Ejercicios** : Encuentre un b pertinente para cada primo p y verifique si p divide a N dado que
	1. p = 31 y N = 6512
	2. p = 31 y N = 10354
	3. p = 71 N = 237603133
	4. p = 23 y N = 22498963358899
	5. p = 127y N = 1242887506373051
	Como se menciono antes, este criterio es bueno y bonito, pero en costo computacional no es mas eficiente que hacer la división.