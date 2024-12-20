from numpy import linalg
from questao2 import regressive_substitution


def lu_decomposition(coefficient_matrix: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
    n = len(coefficient_matrix)
    L = [[0 for _ in range(n)] for _ in range(n)]
    U = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n): 
        U[j][j] = 1
        
        for i in range(j, n):
            L[i][j] = coefficient_matrix[i][j] - sum(L[i][k] * U[k][j] for k in range(j))
        
        for i in range(j + 1, n):
            U[j][i] = (coefficient_matrix[j][i] - sum(L[j][k] * U[k][i] for k in range(j))) / L[j][j]

    return L, U


def progressive_substitution(coefficient_matrix: list[list[float]], constant_vector: list[float]) -> list[float]:
    n = len(coefficient_matrix)
    y = [0] * n
    
    for i in range(n):
        y[i] = (constant_vector[i] - sum(coefficient_matrix[i][j] * y[j] for j in range(i))) / coefficient_matrix[i][i]

    return y


def solve_linear_system(coefficient_matrix: list[list[float]], constant_vector: list[float]) -> list[float]:
    L, U = lu_decomposition(coefficient_matrix)

    y = progressive_substitution(L, constant_vector)
    x = regressive_substitution(U, y)
    
    return x


def main() -> None:
    A = [[4, -2, -3, 6], [-6, 7, 6.5, -6], [1, 7.5, 6.25, 5.5], [-12, 22, 15.5, -1]]
    B = [12, -6.5, 16, 17]

    try:
        if not linalg.det(A):
            raise ValueError
        
        x = solve_linear_system(A, B)

        for a in range(1, len(x) + 1):
            print(f'x{a} = {x[a - 1]:.4f}')
    except ValueError:
        print('O sistema linear não pode ser resolvido, pois a matriz A é singular.')


if __name__ == '__main__':
    main()
