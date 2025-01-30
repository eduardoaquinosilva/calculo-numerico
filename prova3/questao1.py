from questao2 import integral_simpson_3_8

X     = [0,  80,  160,  240,  320,  400,  480,  560,  640,  720,  800,  880,  960, 1040, 1120, 1200]
Y_pos = [0,   0,    0,    0,    0,  480,  480,  480,  255,  230,  220,  190,  190,  230,  190,    0]
Y_neg = [0, -85, -160, -315, -325, -250, -250, -330, -480, -620, -640, -650, -415, -370, -245, -240]


def f_pos(x: float) -> float | None:
    try:
        return Y_pos[X.index(x)]
    except ValueError:
        return None
     

def f_neg(x: float) -> float | None:
    try:
        return Y_neg[X.index(x)]
    except ValueError:
        return None


def integral_ponto_central(limite_inf: float, limite_sup: float, n: int, f: callable, values: list[float] | None = None) -> float:
    n_base = n if values is None else len(values) - 1
    deltax = (limite_sup - limite_inf) / n_base

    soma = 0
    values_iterable = [limite_inf + deltax * (i + 1/2) for i in range(n)] if values is None else values

    for x in values_iterable:
        soma += f(x) * deltax

    return soma


def main() -> None:
    a = integral_ponto_central(X[0], X[-1], len(X) - 1, f_pos, X) - integral_ponto_central(X[0], X[-1], len(X) - 1, f_neg, X)
    b = integral_simpson_3_8(X[0], X[-1], len(X) - 1, f_pos, X) - integral_simpson_3_8(X[0], X[-1], len(X) - 1, f_neg, X)
    
    print("Método ponto central: ", a)
    print("Método de Simpson 3/8:", b)


if __name__ == '__main__':
    main()
