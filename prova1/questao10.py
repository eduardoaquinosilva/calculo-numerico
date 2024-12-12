from math import pi as PI, cos
from time import perf_counter
import questao7 as q7

L = 3
E = 70e9
I = 52.9e-6
W0 = 15e3
Y = 0.009

def f(x):
    return (((W0*L) / (3*PI**4*E*I))) * (48*L**3*cos((PI*x) / (2*L)) - 48*L**3 + 3*PI**3*L*x**2 - PI**3*x**3) - Y


def main():
    a = 1.5

    print("MÉTODO DE NEWTON:")
    start = perf_counter()
    print(f"A raiz aproximada é: {q7.newtons_method(f, a):.5f}")
    ending = perf_counter()
    print(f'Tempo de execução: {ending - start}')
    print(f'Quantidade de iterações: {q7.counter_n}')

    print("\nMÉTODO DA SECANTE:")
    start = perf_counter()
    print(f"A raiz aproximada é: {q7.raiz_secante(f, 0, a):.5f}")
    ending = perf_counter()
    print(f'Tempo de execução: {ending - start}')
    print(f'Quantidade de iterações: {q7.counter_s}')


if __name__ == '__main__':
    main()
