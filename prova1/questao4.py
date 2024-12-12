from time import perf_counter
import questao3 as q3

epsilon = 0.00001
iterations = 0

def s(x):
    # return (x-4)**4
    return x**3 - 9*x + 2
    # return x**3 + 2*x**2
    # return x**2 - 1


def find_root_false_position(a, b, f, k):
    global iterations

    if (f(a) == 0): return a
    if (f(b) == 0): return b

    limits = [a, b]

    while iterations <= k:
        new_limits = []
        for i, limit in enumerate(limits[:-1]):
            new_limits.append(limit)
            new_limits.append((limits[i] * f(limits[i + 1]) - limits[i + 1] * f(limits[i])) / (f(limits[i + 1]) - f(limits[i])))
        new_limits.append(limits[-1])

        limits = new_limits.copy()
        iterations += 1

        for i, limit in enumerate(limits[:-1]):
            if (abs(f(limit)) <= epsilon): return limit
            if f(limit) * f(limits[i + 1]) < 0:
                if (limits[i + 1] - limit) > epsilon: return find_root_false_position(limit, limits[i + 1], f, k)
                else: return limit

    return None


def main():
    a = 2
    b = 3
    k = 23
    
    try:
        print('MÉTODO DA FALSA POSIÇÃO:')
        start = perf_counter()
        print(f"A raiz aproximada é: {find_root_false_position(a, b, s, k):.5f}")
        ending = perf_counter()
        print(f'Tempo de execução: {ending - start}')
        print(f'Quantidade de iterações: {iterations}')

        print('\nMÉTODO DA BISSECÇÃO:')
        start = perf_counter()
        print(f'A raiz aproximada é: {q3.find_root_bissection(a, b, s):.5f}')
        ending = perf_counter()
        print(f'Tempo de execução: {ending - start}')
        print(f'Quantidade de iterações: {q3.iterations}')
    except TypeError:
        print("Raiz não encontrada, desculpe :(")


if __name__ == '__main__':
    main()
