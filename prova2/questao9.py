

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
    last_month_inflation = image[x-1] if x-1 >= 0 else image[x+1]
    inflation_prediction = lagrange_polynomial(domain, image, x)

    absolute_error = abs(last_month_inflation - inflation_prediction)

    return absolute_error

def c(domain:list[float], image:list[float]) -> float:
    inflation_prediction = lagrange_polynomial(domain, image, 2)
    semi_annual_inflation = sum(image) + inflation_prediction

    return semi_annual_inflation

domain = [0, 1, 3] # fevereiro, março, maio
image = [0.64, 0.24, 2.94]
x = 2 # abril

inflation_prediction = a(domain, image, x)
absolute_error = b(domain, image, x)
semi_annual_inflation = c(domain, image)

x = 5 # julho
july_prediction = a(domain, image, x)

print("Resposta da a): Previsão da inflação de abril\n %.6f \n" % inflation_prediction)
print("Resposta da b): Erro da previsão sobre março\n %.6f \n" % absolute_error)
print("Resposta da c): Inflação semestral\n %.6f \n" % semi_annual_inflation)
print("Resposta da d): Previsão da inflação de julho\n %.6f \n" % july_prediction)