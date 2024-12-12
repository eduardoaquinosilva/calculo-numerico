from time import perf_counter

epsilon = 10 ** (-7)
counter_n = 0
counter_s = 0
max_iterations = 10 ** 5

def f(x):
    return 2**x - x**2


def derivative_of(f, x):
    return (f(x+epsilon) - f(x)) / epsilon


def newtons_method(f, x_0):
    global counter_n
    x = x_0

    while (abs(f(x)) > epsilon):
        try:
            x = x - f(x) / derivative_of(f, x)
        except ZeroDivisionError:
            exit(f"A raiz não pode ser encontrada porque a derivada da função no ponto {x} é zero.")
            
        counter_n += 1
        if (counter_n > max_iterations): return None

    return x


def raiz_secante(f, x_0, x_1):
    global counter_s

    while (abs(f(x_1)) > epsilon):
        x_old = x_1

        try:
            x_1 = x_1 - f(x_1) * (x_1 - x_0) / (f(x_1) - f(x_0))
        except ZeroDivisionError:
            exit("Divisão por zero na iteração. Método falhou.")
        
        x_0 = x_old
            
        counter_s += 1
        if (counter_s > max_iterations): return None

    return x_1


def main():
    try:
        print("MÉTODO DE NEWTON:")
        start = perf_counter()
        print(f"A raiz aproximada é: {newtons_method(f, 10):.5f}")
        ending = perf_counter()
        print(f'Tempo de execução: {ending - start}')
        print(f'Quantidade de iterações: {counter_n}')

        print("\nMÉTODO DA SECANTE:")
        start = perf_counter()
        print(f"A raiz aproximada é: {raiz_secante(f, 6, 10):.5f}")
        ending = perf_counter()
        print(f'Tempo de execução: {ending - start}')
        print(f'Quantidade de iterações: {counter_s}')
    except TypeError:
        print("Raiz não encontrada, desculpe :(")


if __name__ == '__main__':
    main()
