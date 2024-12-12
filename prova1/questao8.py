from math import pi as PI, sqrt
from time import perf_counter
import questao6 as q6

epsilon = 0.00001

def f(x: float) -> float:
    return PI * x * sqrt(x ** 2 + 400) - 1200


def phi(x: float) -> float:
    return 1200 / (PI * sqrt(x ** 2 + 400))


def main():
    a = 17

    print("MÉTODO DO PONTO FIXO:")
    start = perf_counter()
    print(f'A raiz aproximada é: {q6.ponto_fixo(f, phi, a, 5):.5f}')
    ending = perf_counter()
    print(f'Tempo de execução: {ending - start}')
    print(f'Quantidade de iterações: {q6.iterations}')


if __name__ == '__main__': 
    main()
