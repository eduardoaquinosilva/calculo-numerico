import csv

def polinomio_lagrange(X:list[float], Y:list[float], x:float):
    coeficientes=[]
    n = len(X)

    for indice in range(n):
        L=1

        for j in range(n):
            if indice !=j:
                L=L*(x-X[j])/(X[indice]-X[j])
        
        coeficientes.append(L)
    
    pn = 0
    for i in range(len(coeficientes)):
        pn=pn+Y[i]*coeficientes[i]

    return pn


def main() -> None:
    X,Y=[],[]

    with open('Lagrange.csv') as csv_f:
        reader = csv.DictReader(csv_f)

        for line in reader:
            X.append(float(line["X"]))
            Y.append(float(line["Y"]))

    x=float(input("Valor a ser interpolado: "))
    
    pn = polinomio_lagrange(X, Y, x)
    print("pn =", pn)


if __name__ == '__main__':
    main()
