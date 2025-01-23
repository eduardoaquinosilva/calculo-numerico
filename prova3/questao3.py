from math import sqrt

def f(x:float) -> float:
    return sqrt(1 - x**2)


def integral_boole(limite_inf:float, limite_sup:float, n:int, f:callable, values:list[float] | None = None) -> float:
    deltax = (limite_sup - limite_inf) / n

    soma1, soma2, soma3, soma4 = 0, 0, 0, 0

    values = [limite_inf + i * deltax for i in range(n)] if values is None else values

    for i, x in enumerate(values):
        if (i == 0 or i == n):
            soma1 += 7*f(x)
        elif (i % 4 == 1 or i % 4 == 3):
            soma2 += 32*f(x)
        elif (i % 4 == 2):
            soma3 += 12*f(x)
        else:
            soma4 += 14*f(x)
            
    soma = (soma1 + soma2 + soma3 + soma4) * (2 * deltax / 45)    

    return soma


def main() -> None:
    a = integral_boole(-1, 1, 8, f)
    
    print("Regra de Boole:", a)


if __name__ == '__main__':
    main()
