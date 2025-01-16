from questao7 import load_lagrange, polinomio_lagrange

def main() -> None:

    X, Y = load_lagrange('Lagrange_Q8.csv')

    x = 3.1
    pn = polinomio_lagrange(X, Y, x)

    Y.append(pn)
    M = max([abs(y) for y in Y])

    # Limitante para o erro usando o Corolário 1
    d = 1
    for x in X: d *= (3.1 - x)
    limitante_erro_c1 = abs(d) * M / 6
    
    # Limitante para o erro usando o Corolário 2
    h = 0.2
    n = 3 - 1
    limitante_erro_c2 = (h**(n + 1) * M) / (4 * (n + 1))

    print(f"Limitante erro (Corolário 1): {limitante_erro_c1}")
    print(f"Limitante erro (Corolário 2): {limitante_erro_c2}")


if __name__ == '__main__':
    main()
