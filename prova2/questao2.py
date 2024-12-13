from numpy import linalg


def regressive_substitution(coefficient_matrix: list[list[float]], constant_vector: list[float]) -> list[float]:
    n = len(coefficient_matrix)
    x = [0] * n

    for i in range(n - 1, -1, -1):
        summation = 0
        for j in range(i + 1, n):
            summation += coefficient_matrix[i][j] * x[j]
        
        x[i] = (constant_vector[i] - summation) / coefficient_matrix[i][i]

    return x


def main() -> None:
    A = [[2, 3, 1, 4], [0, 0, 2, 6], [0, 0, 7, 1], [0, 0, 0, 8]]
    B = [27, 40, 25, 32]

    try:
        if not linalg.det(A):
            raise ValueError

        x = regressive_substitution(A, B)
        
        for a in range(1, len(x) + 1):
            print(f'x{a} = {x[a - 1]}')
    except ValueError:
        print('O sistema linear não pode ser resolvido, pois a matriz A é singular.')


if __name__ == '__main__':
    main()
