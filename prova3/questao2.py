from math import sqrt

def f(x:float) -> float:
    return sqrt(1 - x**2)


def integral_simpson_1_3(limite_inf:float, limite_sup:float, n:int, f:callable, values:list[float] | None = None) -> float:
    deltax = (limite_sup-limite_inf)/n

    soma1, soma2, soma3 = 0, 0, 0

    values = [limite_inf+deltax*i for i in range(n)] if values is None else values

    for i, x in enumerate(values):
        if (i==0 or i==n):
            soma1 = (soma1 + f(x))
        elif (i%2==0):
            soma2 = (soma2 + 2*f(x))
        else:
            soma3 = (soma3 + 4*f(x))
            
    soma = (soma1 + soma2 + soma3)*(deltax/3)    

    return soma


def integral_simpson_3_8(limite_inf:float, limite_sup:float, n:int, f:callable, values:list[float] | None = None) -> float:
    deltax = (limite_sup-limite_inf)/n

    soma1, soma2, soma3 = 0, 0, 0

    values = [limite_inf+deltax*i for i in range(n)] if values is None else values

    for i, x in enumerate(values):
        if (i==0 or i==n):
            soma1 += f(x)
        elif (i%3==2 or i%3==0):
            soma2 += 3*f(x)
        else:
            soma3 += 2*f(x)

    soma = (soma1 + soma2 + soma3)*(3*deltax/8)

    return soma


def main() -> None:
    a = integral_simpson_1_3(-1, 1, 8, f)
    b = integral_simpson_3_8(-1, 1, 9, f)
    
    print("Método de Simpson 1/3:", a)
    print("Método de Simpson 3/8:", b)


if __name__ == '__main__':
    main()
