"""
    O objetivo desse algoritmo é realizar o cálculo do tempo de execução de algoritmos para uma análise de complexidade computacional usando integração.

    A ideia é usar a integração para estimar o tempo total de execução de um algoritmo que varia de acordo com o tamanho da entrada.
    
    Supondo que o tempo de um algoritmo é dado por T(n) e que deseja-se calcular o tempo total de execução acumulado para entradas que variem de n = 1 até n = N, podemos utilizar o seguinte algoritmo.

    T(n) = n * logn + n^2/2 + sin(n)
"""

from math import log, sin
from questao2 import integral_simpson_3_8


def T(n: float) -> float:
    return n * log(n, 10) + n**2 / 2 + sin(n)


def main() -> None:
    N = 1000

    print(f"Tempo total de execução acumulado de 1 até {N}: {integral_simpson_3_8(1, N, 1000, T):.2f}s")


if __name__ == "__main__":
    main()
