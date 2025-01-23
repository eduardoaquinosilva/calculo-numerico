from math import sqrt

def f(x):
    return sqrt(1 - x**2)


def integral_simpson_1_3(limite_inferior: float, limite_superior: float, n: int, f:callable) -> float:
    deltax = (limite_superior-limite_inferior)/n

    soma1, soma2, soma3 = 0, 0, 0

    for i in range(n):
        x=limite_inferior+deltax*i

        if (i==0 or i==n):
            soma1 = (soma1 + f(x))
        elif (i%2==0):
            soma2 = (soma2 + 2*f(x))
        else:
            soma3 = (soma3 + 4*f(x))
            
        soma = (soma1 + soma2 + soma3)*(deltax/3)    

    return soma


def integral_simpson_3_8(limite_inferior: float, limite_superior: float, n: int, f:callable) -> float:
    deltax = (limite_superior-limite_inferior)/n

    soma1, soma2, soma3 = 0, 0, 0

    for i in range(n):
        x=limite_inferior+deltax*i

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
