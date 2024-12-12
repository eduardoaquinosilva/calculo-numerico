def decimal_to_any_base(number: int, base: int) -> str:
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if base == 1:
        return 0
    elif number < base:
        return characters[number]
    else:
        answer = ''
        while number > 0:
            answer += characters[number % base]
            number //= base
        return answer[::-1]


def main():
    number = int(input('Informe um número na base 10: '))
    base = int(input('Informe a base desejada (de 1 a 36): '))

    if 1 <= base <= 36:
        print(f"O número {number} na base {base} é: {decimal_to_any_base(number, base)}")
    else:
        print('A base deve estar entre 1 e 36.')


if __name__ == '__main__':
    main()
    