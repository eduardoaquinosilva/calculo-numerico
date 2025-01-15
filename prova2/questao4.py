import numpy as np


# Função para verificar se a matriz é diagonal dominante
def is_diagonally_dominant(A: np.ndarray) -> bool:
    for i in range(len(A)):
        sum_off_diagonal = sum(abs(A[i][j]) for j in range(len(A)) if j != i)
        if sum_off_diagonal / abs(A[i][i]) >= 1:
            return False
    return True


# Função para verificar se há zero na diagonal principal
def has_zero_in_diagonal(A: np.ndarray) -> bool:
    for i in range(len(A)):
        if A[i][i] == 0:
            return True
    return False


# Função para calcular o determinante
def determinant(A: np.ndarray) -> float:
    return np.linalg.det(A)


# Função para verificar se todos os valores de b são iguais
def are_b_values_equal(b: np.ndarray) -> bool:
    return len(set(b)) == 1


# Função que implementa o método de Gauss-Jacobi
def gauss_jacobi(A: np.ndarray, b: np.ndarray, tol=1e-6, max_iter=1000) -> tuple[np.ndarray, int]:
    n = len(A)
    x = np.zeros(n)
    x_new = np.zeros(n)
    iter_count = 0  # Contador de iterações
    
    # Iteração de Gauss-Jacobi
    for k in range(max_iter):
        iter_count += 1
        for i in range(n):
            sum_ = 0
            for j in range(n):
                if i != j:
                    sum_ += A[i][j] * x[j]
            x_new[i] = (b[i] - sum_) / A[i][i]
        
        # Checar a convergência
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, iter_count
        
        x = np.copy(x_new)
    
    return x_new, iter_count


# Função para verificar se a solução é válida (Ax = b)
def is_solution_valid(A: np.ndarray, b: np.ndarray, x: np.ndarray) -> bool:
    return np.allclose(np.dot(A, x), b)


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
        print("A matriz não é diagonal dominante. O resultado pode não convergir.")
    
    # Verificar se todos os valores de b são iguais
    if are_b_values_equal(b):
        print("Os valores de b são todos iguais. O resultado pode não convergir.")
    
    # Resolver o sistema usando o método de Gauss-Jacobi
    x, iter_count = gauss_jacobi(A, b)

    return x, iter_count


def main() -> None:
    A = np.array([[9, -2, 3, 2], [2, 8, -2, 3], [-3, 2, 11, -4], [-2, 3, 2, 10]])
    b = np.array([54.5, -14, 12.5, -21])
    # Resultado esperado x = [5, -2, 2.5, -1]

    # A = np.array([[10, 2, 1], [1, 5, 1], [2, 3, 10]])
    # b = np.array([7, -8, 6])
    # Resultado esperado x = [0.9994, -1.9888, 0.9984]

    # A = np.array([[1, 1], [1, -3]])
    # b = np.array([3, -3])
    # Resultado esperado x = [1.5, 1.5]

    # A = np.array([[1, 3, 1], [5, 2, 2], [0, 6, 8]])
    # b = np.array([-2, 3, -6])

    # A = np.array([[5, 2, 2], [1, 3, 1], [0, 6, 8]])
    # b = np.array([3, -2, -6])

    # A = array([[4, -1, 0, 0], [-1, 4, -1, 0], [0, -1, 4, -1], [0, 0, -1, 3]])
    # b = array([15, 10, 10, 10])

    try:
        solution, iterations = solve_system(A, b)
        
        print('Solução encontrada:')
        for a in range(len(solution)):
            print(f'x{a + 1}: {solution[a]:.4f}')
        
        # Verificar se a solução é válida
        if not is_solution_valid(A, b, solution):
            print("\nA solução não é válida!")

        print("\nNúmero de iterações:", iterations)
    except ValueError as e:
        print("Erro:", e)


if __name__ == '__main__':
    main()
