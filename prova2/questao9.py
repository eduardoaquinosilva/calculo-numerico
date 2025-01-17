
def diferencas_divididas(f, *args:float) -> float:
    
    if len(args) == 1: 
        return f(args[0])
    else:
        return (diferencas_divididas(f, *args[1:]) - diferencas_divididas(f, *args[:-1])) / (args[-1] - args[0])

M = [1, 2, 3, 5, 6]
I = [0.75, 0.64, 0.24, 2.94, 0.37]

def f(x) -> float | None:
    try:
        return I[M.index(x)]
    except ValueError:
        return None


def lagrange_polynomial(domain:list[float], image:list[float], x:float) -> float:
    coefficients=[]

    for i in range(len(domain)):
        Lx=1

        for j in range(len(domain)):
            if i != j:
                Lx=Lx*(x-domain[j])/(domain[i]-domain[j])
        
        coefficients.append(Lx)
    
    Pn = 0
    for i in range(len(coefficients)):
        Pn=Pn+image[i]*coefficients[i]

    return Pn


def a(domain:list[float], image:list[float], x:float) -> float:
    prediction = lagrange_polynomial(domain, image, x)

    return prediction

def b(domain:list[float], image:list[float], x:float) -> float:
    M_n = max(abs(diferencas_divididas(f, *M[:-1])), abs(diferencas_divididas(f, *M[1:])))
    d = 1
    for x in domain: d *= (2 - x)

    limitante_erro = abs(d) * M_n
    return limitante_erro

def c(domain:list[float], image:list[float]) -> float:
    inflation_prediction = lagrange_polynomial(domain, image, 2)

    inflacoes_mensais = I + [inflation_prediction]

    semi_annual_inflation = 1
    for inflacao_mensal in inflacoes_mensais: semi_annual_inflation *= (1 + inflacao_mensal / 100)
    semi_annual_inflation -= 1

    return semi_annual_inflation * 100

def main() -> None:
    domain = [0, 1, 3] # fevereiro, março, maio
    image = [0.64, 0.24, 2.94]
    x = 2 # abril

    inflation_prediction = a(domain, image, x)
    absolute_error = b(domain, image, x)
    semi_annual_inflation = c(domain, image)

    domain = [0, 1, 4] # fevereiro, março, junho
    image = [0.64, 0.24, 0.37]
    x = 5 # julho
    july_prediction = a(domain, image, x)

    print("Resposta da a): Previsão da inflação de abril\n %.6f \n" % inflation_prediction)
    print("Resposta da b): Erro da previsão sobre março\n %.6f \n" % absolute_error)
    print("Resposta da c): Inflação semestral\n %.6f \n" % semi_annual_inflation)
    print("Resposta da d): Previsão da inflação de julho\n %.6f \n" % july_prediction)


if __name__ == '__main__':
    main()
