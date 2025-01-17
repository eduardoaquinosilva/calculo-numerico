from questao7 import load_lagrange, polinomio_lagrange

def main() -> None:
    X, Y = load_lagrange('Lagrange_Q8.csv')

    x = 3.1
    pn = polinomio_lagrange(X, Y, x)
    
    print(f"e^{x} ≈", pn)


if __name__ == '__main__':
    main()
