from math import e as EULER
from time import perf_counter
import questao7 as q7

def f(x):
    return ((EULER ** (39.0744 * x)) * (1 + 39.0744 * x) - (EULER ** 19.5372))


def main():
    a = 15

    print("MÉTODO DE NEWTON:")
    start = perf_counter()
    print(f"A raiz aproximada é: {q7.newtons_method(f, a):.5f}")
    ending = perf_counter()
    print(f'Tempo de execução: {ending - start}')
    print(f'Quantidade de iterações: {q7.counter_n}')


if __name__ == '__main__': 
    main()
