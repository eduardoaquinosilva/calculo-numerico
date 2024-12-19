from numpy import linalg
from questao2 import regressive_substitution


def gaussian_elimination(coefficient_matrix: list[list[float]], constant_vector: list[float]) -> list[float]:
    n = len(coefficient_matrix)

    for k in range(0, n - 1):
        if not coefficient_matrix[k][k]:
            for a in range(k, n):
                if coefficient_matrix[a][k]:
                    coefficient_matrix[k], coefficient_matrix[a] = coefficient_matrix[a], coefficient_matrix[k]
                    constant_vector[k], constant_vector[a] = constant_vector[a], constant_vector[k]
                    break
            else:
                raise ValueError

        for i in range(k + 1, n):
            m = coefficient_matrix[i][k] / coefficient_matrix[k][k]
            coefficient_matrix[i][k] = 0

            for j in range(k + 1, n):
                coefficient_matrix[i][j] = coefficient_matrix[i][j] - m * coefficient_matrix[k][j]
            
            constant_vector[i] = constant_vector[i] - m * constant_vector[k]
    
    return regressive_substitution(coefficient_matrix, constant_vector)


def main() -> None:
    A = [[4, -2, -3, 6], [-6, 7, 6.5, -6], [1, 7.5, 6.25, 5.5], [-12, 22, 15.5, -1]]
    B = [12, -6.5, 16, 17]
    # Resultado esperado x = [2, 4, -3, 0.5]

    # A = [[9, -4, -2, 0], [-4, 17, -6, -3], [-2, -6, 14, -6], [0, -3, -6, 11]]
    # B = [24, -16, 0, 18]
    # Resultado esperado x = [4.0343, 1.6545, 2.8452, 3.6395]

    # A = [[0.0003, 12.34], [0.4321, 1]]
    # B = [12.343, 5.321]
    # Resultado esperado x = [10, 1]

    # A = [[3, 2, 4], [1, 1, 2], [4, 3, -2]]
    # B = [1, 2, 3]
    # Resultado esperado x = [-3, 5, 0]

    # A = [[0.0002, 2], [2, 2]]
    # B = [5, 6]
    # Resultado esperado x = [0.5, 0.25]

    # A = [[1, -1, 1], [1, 0, 0], [1, 2, 4]]
    # B = [4, 1, -1]
    # Resultado esperado x = [1, -2.3, 0.67]

    # A = [[0, 0.9231, 0, 0, 0, 0, 0, 0], [-1, -0.3846, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0.8575, 0],
    #      [1, 0, -0.7809, 0, 0, 0, 0, 0], [0, -0.3846, -0.7809, 0, -1, 0.3846, 0, 0],
    #      [0, 0.9231, 0.6247, 0, 0, -0.9231, 0, 0], [0, 0, 0.6247, -1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, -0.5145, -1]]
    # B = [1690, 3625, 0, 0, 0, 0, 0, 0]
    # Resultado esperado x = [-4329.1, 1830.8, -5543.8, -3463.2, 2886.2, -1920.9, -3365.9, -1731.5]

    try:
        if not linalg.det(A):
            raise ValueError

        x = gaussian_elimination(A, B)
        
        for a in range(1, len(x) + 1):
            print(f'x{a} = {x[a - 1]:.4f}')
    except ValueError:
        print('O sistema linear não pode ser resolvido, pois a matriz A é singular.')


if __name__ == '__main__':
    main()
