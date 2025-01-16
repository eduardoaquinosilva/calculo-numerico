from questao7 import load_lagrange, polinomio_lagrange

def main():

    X, Y = load_lagrange('Lagrange_Q8.csv')

    x = 3.1
    pn = polinomio_lagrange(X, Y, x)

    Y_erro = [Y[3], Y[4], pn]
    M = max([abs(y) for y in Y_erro])

    # Limitante para o erro usando o Corolário 1
    limitante_erro_c1 = abs((3.1 - 3.0)*(3.1 - 3.2)) * M / 2
    
    # Limitante para o erro usando o Corolário 2
    h = 0.2
    n = 2 - 1
    limitante_erro_c2 = (h**(n + 1) * M) / (4 * (n + 1))

    print(f"Limitante erro (Corolário 1): {limitante_erro_c1:.5f}")
    print(f"Limitante erro (Corolário 2): {limitante_erro_c2:.5f}")


if __name__ == '__main__':
    main()
