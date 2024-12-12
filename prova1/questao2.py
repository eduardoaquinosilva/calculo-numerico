def f(x):
    return (x**3)


def erro_percentual(y_true, y_pred):
    try: return f"{(abs(y_true - y_pred) * 100 / y_true):.10f}%"
    except ZeroDivisionError: return "undefined"


def main():
    h = float(input("Digite o valor do acréscimo: "))
    x = float(input("Digite o ponto para o cálculo da derivada: "))

    derivada1_ordem1 = (f(x+h)-f(x))/h
    derivada2_ordem1 = (f(x)-f(x-h))/h
    derivada3_ordem1 = (f(x+h)-f(x-h))/(2*h)
    derivada4_ordem1 = (f(x-2*h)+8*f(x+h)-8*f(x-h)-f(x+2*h))/(12*h)

    derivada1_ordem2 = (f(x+h)-2*f(x)+f(x-h))/(h**2)
    derivada2_ordem2 = (f(x+2*h)-2*f(x+h)+f(x))/(h**2)
    derivada3_ordem2 = (f(x)-2*f(x-h)+f(x-2*h))/(h**2)
    derivada4_ordem2 = -(f(x+2*h)-16*f(x+h)+30*f(x)-16*f(x-h)+f(x-2*h))/(12*(h**2))

    derivada1_ordem3 = (f(x+2*h)-2*f(x+h)+2*f(x-h)-f(x-2*h))/(2*(h**3))
    derivada2_ordem3 = (3*f(x-4*h)-3*f(x-3*h)+f(x-2*h)-f(x-5*h))/(h**3)
    derivada3_ordem3 = (f(x+h)-3*f(x)+3*f(x-h)-f(x-2*h))/(h**3)
    derivada4_ordem3 = (f(x-h)-f(x-4*h)+3*f(x-3*h)-3*f(x-2*h))/(h**3)

    derivadas_ordem1 = [derivada1_ordem1, derivada2_ordem1, derivada3_ordem1, derivada4_ordem1]
    derivadas_ordem2 = [derivada1_ordem2, derivada2_ordem2, derivada3_ordem2, derivada4_ordem2]
    derivadas_ordem3 = [derivada1_ordem3, derivada2_ordem3, derivada3_ordem3, derivada4_ordem3]

    # Printar as derivadas
    msgs = ["primeira", "segunda", "terceira"]
    for (i, derivadas) in enumerate([derivadas_ordem1, derivadas_ordem2, derivadas_ordem3]):
        print(f"Derivada de {msgs[i]} ordem:")
        for derivada in derivadas: print("A derivada função no ponto desejado é:", derivada)
        print()

    # Printar os erros
    for (i, derivadas) in enumerate([derivadas_ordem1, derivadas_ordem2, derivadas_ordem3], 1):
        derivada_certa = float(input(f"Digite o valor correto da derivada de ordem {i} para o cálculo do erro: "))
        for derivada in derivadas: print(f"Erro percentual fórmula 1:", erro_percentual(derivada_certa, derivada))
        print()


if __name__ == '__main__':
    main()
