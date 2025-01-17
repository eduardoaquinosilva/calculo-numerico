import numpy as np
from questao4 import is_diagonally_dominant, determinant, are_b_values_equal, has_zero_in_diagonal, is_solution_valid


def is_sassenfeld_valid(A: np.ndarray) -> bool:
    beta = [1] * len(A)
    
    for a in range(len(A)):
        beta[a] = sum([abs(b) * abs(c) for i, (b, c) in enumerate(zip(A[a], beta)) if i != a]) / abs(A[a][a])
    
    return max(beta) < 1


# Função que implementa o método de Gauss-Seidel
def gauss_seidel(A: np.ndarray, b: np.ndarray, tol=1e-6, max_iter=1000) -> tuple[np.ndarray, int]:
    n = len(A)
    x = np.zeros(n)
    iter_count = 0  # Contador de iterações
    
    # Iteração de Gauss-Seidel
    for k in range(max_iter):
        iter_count += 1
        for i in range(n):
            sum_ = 0
            for j in range(n):
                if i != j:
                    try:
                        sum_ += A[i][j] * x[j]
                    except RuntimeWarning:
                        print("Houve um tempo de execução excedido devido à uma multiplicação com overflow")
            
            # Atualiza x[i] com o valor mais recente durante a iteração
            x[i] = (b[i] - sum_) / A[i][i]
        
        # Checar a convergência
        if np.linalg.norm(np.dot(A, x) - b, ord=np.inf) < tol:
            return x, iter_count
    
    return x, iter_count


# Função principal para todas as verificações e solução
def solve_system(A: np.ndarray, b: np.ndarray) -> tuple[np.ndarray, int]:
    # Verificar se há zero na diagonal principal
    if has_zero_in_diagonal(A):
        raise ValueError("A matriz contém zero na diagonal principal")
    
    # Verificar o determinante da matriz
    if determinant(A) == 0:
        raise ValueError("A matriz têm de ter determinante igual a 0.")
    
    # Verificar se a matriz é diagonal dominante
    if not is_diagonally_dominant(A):
        print("A matriz não é diagonal dominante. O resultado pode não convergir.\n")

        # Verificar se a matriz está de acordo com o critério de Sassenfeld.
        if not is_sassenfeld_valid(A):
            print("A matriz não está de acordo com o critério de Sassenfeld. O resultado pode não convergir.\n")

    # Verificar se todos os valores de b são iguais
    if are_b_values_equal(b):
        print("Os valores de b são todos iguais. O resultado pode não convergir.\n")
    
    # Resolver o sistema usando o método de Gauss-Seidel
    x, iter_count = gauss_seidel(A, b)

    return x, iter_count


def main() -> None:
    A = np.array([[9, -2, 3, 2], [2, 8, -2, 3], [-3, 2, 11, -4], [-2, 3, 2, 10]])
    b = np.array([54.5, -14, 12.5, -21])
    # Resultado esperado x = [5, -2, 2.5, -1]

    # A = np.array([[5, 1, 1], [3, 4, 1], [3, 3, 6]])
    # b = np.array([5, 6, 0])
    # Resultado esperado x = [1.0075, 0.9912, -0.9993]

    # A = np.array([[1, 1], [1, -3]])
    # b = np.array([3, -3])
    # Resultado esperado x = [1.5, 1.5]

    # A = np.array([[1, -3], [1, 1]])
    # b = np.array([-3, 3])
    # Resultado esperado x = [1.5, 1.5]

    # A = np.array([[1, 0.5, -0.1, 0.1], [0.2, 1, -0.2, -0.1], [-0.1, -0.2, 1, 0.2], [0.1, 0.3, 0.2, 1]])
    # b = np.array([0.2, -2.6, 1, -2.5])

    # A = np.array([[2, 1, 3], [0, -1, 1], [1, 0, 3]])
    # b = np.array([9, 1, 3])

    # A = np.array([[1, 0, 3], [0, -1, 1], [2, 1, 3]])
    # b = np.array([3, 1, 9])

    # A = np.array([[3, 0, 1], [1, -1, 0], [3, 1, 2]])
    # b = np.array([3, 1, 9])

    # A = np.array([[5, 2, 2], [1, 3, 1], [0, 6, 8]])
    # b = np.array([3, -2, -6])

    # A = array([[4, -1, 0, 0], [-1, 4, -1, 0], [0, -1, 4, -1], [0, 0, -1, 3]])
    # b = array([15, 10, 10, 10])

    try:
        solution, iterations = solve_system(A, b)

        print('Solução encontrada:')
        for a in range(len(solution)):
            print(f'x{a + 1}: {solution[a]}')
        
        # Verificar se a solução é válida
        print("\nA solução é válida!" if is_solution_valid(A, b, solution) else "\nA solução não é válida!")

        print("\nNúmero de iterações:", iterations)
    except ValueError as e:
        print("Erro:", e)


if __name__ == '__main__':
    main()
