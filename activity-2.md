## Questão 1 

    1 --	T(n)= 5T(n/2) + n^3
        T(n/2) = 5T(n/4) + (n^3/2^3)

    2 -- 	T(n) = 5(5T(n/4) +  (n^3/2^3)) + n^3   /// substituindo pelo valor de T(n/2).
        T(n) = 5^2T(n/4) + 5(n^3/2^3) + n^3
        T(n/4) = 5T(n/8) + (n^3/4^3)

    3 --	T(n) = 5^2(5T(n/8) + (n^3/4^3)) + 5(n^3/2^3) + n^3  /// substituindo pelo valor de T(n/4)
        T(n) = 5^3T(n/8) + (5^2(n^3/4^3)) + 5(n^3/2^3) + n^3
        T(n/8) = 5T(n/16) + (n^3/8^3)

    4 -- 	T(n) = 5^3(5T(n/16) + (n^3/8^3)) + (5^2/4^3)n^3 + (5/2^3)n^3 + n^3
        T(n) = 5^4T(n/16) + (5^3/8^3)n^3 + (5^2/4^3)n^3	 + (5/2^3)n^3 + n^3

para o todo, temos que:

	T(n) = (5^p)T(n/2^p) + SUM(p, i=1, (((5/8)^i)n^3 + n^3))

sendo p pertencentes aos inteiros e SUM() o somátorio dos termos.
sabendo que T(1) = 1, então n/2^p = 1. chegamos a n = 2p. portanto p = log(n), temos:

	T(n) = 5^(log(n))T(n/2^(log(n)) + SUM(log(n), i=1, (((5/8)^i)n^3 + n^3))
	T(n) = 5^(log(n)) + (n^3)(SUM(log(n), i = 1, (5/8)^i)n^3 + n^7))
	T(n) = 5^(log(n)) + (n^3)( 1 + SUM(log(n), i = 1, (5/8)^i))

Retirando todas as constantes e descartando funções com crescimento inferior, temos que ao todo
	
	 O(n^3)