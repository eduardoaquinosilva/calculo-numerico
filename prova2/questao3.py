from numpy import linalg
from questao2 import regressive_substitution


def gaussian_elimination(coefficient_matrix: list[list[float]], constant_vector: list[float]) -> list[float]:
    n = len(coefficient_matrix)

    for k in range(0, n - 1):
        if coefficient_matrix[k][k] == 0:
            raise UserWarning

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

    try:
        if not linalg.det(A):
            raise ValueError

        x = gaussian_elimination(A, B)
        
        for a in range(1, len(x) + 1):
            print(f'x{a} = {x[a - 1]:.4f}')
    except ValueError:
        print('O sistema linear não pode ser resolvido, pois a matriz A é singular.')
    except UserWarning:
        print('O sistema linear não pode ser resolvido, pois a matriz A possui um pivô nulo.\nRecomenda-se a troca de linhas')


if __name__ == '__main__':
    main()
