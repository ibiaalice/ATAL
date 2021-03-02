## questão 1

Por linha, temos os custos: 

    2 ---- 1
    3 ---- 1+(n+1)+ n
    4 ---- n + n
    5 ---- 1

Somando os custos das linhas 2, 3, 4 e 5 :

    - 1 + 1 +(n+1) + n + 2n + 1
     - 3 n + 3 + n + 1 

Chegando ao custo de:
    - 4n + 4


<br/>

## questão 2 

<br/>

Com a hipótese que g(n) = Θ(n) , e sabendo que pela regra 0<= C1n <= f(n) <= C2n, temos:
      -  C1n <= 2n+3 <= C2n

Assim, definindo o caso de C1 = 1, C2 = 12, n0 = 1, aplicando na fórmula: 

     - 1.1 <= 2.1 + 3 <= 12.1 
     - 1 <= 5 <= 12          , sendo então 2n+3 pertencente a Θ(n)


<br/>

## questão 3 

<br/>
opções certas :

	- T(n) = Ω(n).
	- T(n) = Θ(n²).
 	- T(n) = O(n³).
