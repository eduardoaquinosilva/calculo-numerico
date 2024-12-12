from math import log
from time import perf_counter

epsilon = 0.00001
iterations = 0

def s(x):
    return (x-4)**4


def find_root_bissection(a, b, f, k=None):
    global iterations
    if (f(a) == 0): return a
    if (f(b) == 0): return b

    limits = [a, b]

    # Calcular k
    if k is None: 
        k = (log(b - a, 10) - log(epsilon, 10)) / log(2, 10)

    while iterations <= k:
        new_limits = []
        for i, limit in enumerate(limits[:-1]):
            new_limits.append(limit)
            new_limits.append((limits[i] + limits[i + 1]) / 2)
        new_limits.append(limits[-1])

        limits = new_limits.copy()
        iterations += 1

        for i, limit in enumerate(limits[:-1]):
            if (abs(f(limit)) <= epsilon): return limit
            if f(limit) * f(limits[i + 1]) < 0:
                if (limits[i + 1] - limit) > epsilon: return find_root_bissection(limit, limits[i + 1], f, k)
                else: return limit

    return None


def main():
    a = 0
    b = 5

    try:
        start = perf_counter()
        print(f"A raiz aproximada é: {find_root_bissection(a, b, s):.5f}")
        ending = perf_counter()
        print(f'Tempo de execução: {ending - start}')
        print(f'Quantidade de iterações: {iterations}')
    except TypeError:
        print("Raiz não encontrada, desculpe :(")


if __name__ == '__main__':
    main()
