from questao2 import integral_simpson_3_8

X =     [0,  80,  160,  240,  320,  400,  480,  560,  640,  720,  800,  880,  960, 1040, 1120, 1200]
Y_pos = [0,   0,    0,    0,    0,  480,  480,  480,  255,  230,  220,  190,  190,  230,  190,    0]
Y_neg = [0, -85, -160, -315, -325, -170, -170, -330, -480, -620, -640, -650, -415, -370, -245, -240]


def f_pos(x:float) -> float | None:
    try:
        return Y_pos[X.index(x)]
    except ValueError:
        return None
     

def f_neg(x:float) -> float | None:
    try:
        return Y_neg[X.index(x)]
    except ValueError:
        return None


def integral_ponto_central(limite_inf:float, limite_sup:float, n:int, f:callable, values:list[float] | None = None) -> float:
    deltax = (limite_sup-limite_inf)/n

    soma1, soma2 = 0, 0

    values = [limite_inf+deltax*i for i in range(n)] if values is None else values

    for i, x in enumerate(values):
        if (i==0 or i==n):
            soma1 = f(limite_sup) + f(limite_inf)
        else:
            soma2 += f(x)
            
    soma = (soma1 + 2 * soma2)*(deltax/2)    

    return soma


def main() -> None:
    a = integral_ponto_central(X[0], X[-1], len(X), f_pos, X) - integral_ponto_central(X[0], X[-1], len(X), f_neg, X)
    b = integral_simpson_3_8(  X[0], X[-1], len(X), f_pos, X) - integral_simpson_3_8(  X[0], X[-1], len(X), f_neg, X)
    
    print("Método ponto central: ", a)
    print("Método de Simpson 3/8:", b)


if __name__ == '__main__':
    main()
