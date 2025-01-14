import numpy as np


# Função para verificar se a matriz é diagonal dominante
def is_diagonally_dominant(A: np.ndarray) -> bool:
    for i in range(len(A)):
        sum_off_diagonal = sum(abs(A[i][j]) for j in range(len(A)) if j != i)
        if abs(A[i][i]) <= sum_off_diagonal:
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
    # Verificar se a matriz é diagonal dominante
    if not is_diagonally_dominant(A):
        raise ValueError("A matriz não é diagonal dominante")
    
    # Verificar se há zero na diagonal principal
    if has_zero_in_diagonal(A):
        raise ValueError("A matriz contém zero na diagonal principal")
    
    # Verificar se todos os valores de b são iguais
    if are_b_values_equal(b):
        raise ValueError("Os valores de b são todos iguais")
    
    # Verificar o determinante da matriz
    if determinant(A) == 0:
        raise ValueError("A matriz têm de ter determinante iguak 0.")
    
    # Resolver o sistema usando o método de Gauss-Jacobi
    x, iter_count = gauss_jacobi(A, b)
    
    # Verificar se a solução é válida
    if is_solution_valid(A, b, x):
        return x, iter_count
    else:
        raise ValueError("A solução não é válida!")


def main() -> None:
    A = np.array([[9, -2, 3, 2], [2, 8, -2, 3], [-3, 2, 11, -4], [-2, 3, 2, 10]])
    b = np.array([54.5, -14, 12.5, -21])
    # Resultado esperado x = [5, -2, 2.5, -1]

    # A = array([[4, -1, 0, 0], [-1, 4, -1, 0], [0, -1, 4, -1], [0, 0, -1, 3]])
    # b = array([15, 10, 10, 10])

    try:
        solution, iterations = solve_system(A, b)
        
        print('Solução encontrada:')
        for a in range(len(solution)):
            print(f'x{a + 1}: {solution[a]:.4f}')

        print("\nNúmero de iterações:", iterations)
    except ValueError as e:
        print("Erro:", e)


if __name__ == '__main__':
    main()
