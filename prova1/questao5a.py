from math import sin

EPSILON = 0.1

def f(x: float) -> float:
    if (x == 0):
        return 0
    else:
        return x**4 * sin(1/x)


def main():
    x0 = float(input('Informe o valor do ponto a ser analisado: '))
    right_value = f(x0 + 1 / (10 + 10000**2))
    left_value = f(x0 - 1 / (10 + 10000**2))

    print(f'O valor do limite pela direita é: {right_value}')
    print(f'O valor do limite pela esquerda é: {left_value}')

    if (abs(right_value - left_value) < EPSILON):
        print(f'O limite bilateral é: {max(right_value, left_value)}')
    else:
        print('Não existe limite bilateral para essa função.')


if __name__ == '__main__':
    main()
