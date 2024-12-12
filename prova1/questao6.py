from time import perf_counter
import questao3 as q3

epsilon = 0.00001
iterations = 0

def f(x: float) -> float:
    return x**2 + x - 6


def phi(x: float) -> float:
    return 6 / (x + 1)


def ponto_fixo(f, phi, a, max_iteractions=None):
    global iterations
    if max_iteractions is None: max_iteractions = float('inf')

    c = a # Ponto inicial
    phi_c = phi(c)

    iterations += 1

    while abs(f(phi_c)) > epsilon and iterations < max_iteractions:
        c = phi_c
        phi_c = phi(c)
        iterations += 1

    return phi_c


def main():
    a = 0
    b = 5

    try:
        print("MÉTODO DO PONTO FIXO:")
        start = perf_counter()
        print(f'A raiz aproximada é: {ponto_fixo(f, phi, a):.5f}')
        ending = perf_counter()
        print(f'Tempo de execução: {ending - start}')
        print(f'Quantidade de iterações: {iterations}')

        print('\nMÉTODO DA BISSECÇÃO:')
        start = perf_counter()
        print(f'A raiz aproximada é: {q3.find_root_bissection(a, b, f):.5f}')
        ending = perf_counter()
        print(f'Tempo de execução: {ending - start}')
        print(f'Quantidade de iterações: {q3.iterations}')
    except TypeError:
        print("Raiz não encontrada, desculpe :(")


if __name__ == '__main__':
    main()
