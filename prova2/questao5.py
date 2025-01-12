import numpy as np

# Função para verificar se a matriz é diagonal dominante
def is_diagonally_dominant(A):
    for i in range(len(A)):
        sum_off_diagonal = sum(abs(A[i][j]) for j in range(len(A)) if j != i)
        if abs(A[i][i]) <= sum_off_diagonal:
            return False
    return True

# Função para verificar se há zero na diagonal principal
def has_zero_in_diagonal(A):
    for i in range(len(A)):
        if A[i][i] == 0:
            return True
    return False

# Função para calcular o determinante
def determinant(A):
    return np.linalg.det(A)

# Função para verificar se todos os valores de b são iguais
def are_b_values_equal(b):
    return len(set(b)) == 1

# Função que implementa o método de Gauss-Seidel
def gauss_seidel(A, b, tol=1e-6, max_iter=1000):
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
                    sum_ += A[i][j] * x[j]
            # Atualiza x[i] com o valor mais recente durante a iteração
            x[i] = (b[i] - sum_) / A[i][i]
        
        # Checar a convergência
        if np.linalg.norm(np.dot(A, x) - b, ord=np.inf) < tol:
            return x, iter_count
    
    return x, iter_count

# Função para verificar se a solução é válida (Ax = b)
def is_solution_valid(A, b, x):
    return np.allclose(np.dot(A, x), b)

# Função principal para todas as verificações e solução
def solve_system(A, b):
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
        raise ValueError("A matriz têm de ter determinante igual a 0.")
    
    # Resolver o sistema usando o método de Gauss-Seidel
    x, iter_count = gauss_seidel(A, b)
    
    # Verificar se a solução é válida
    if is_solution_valid(A, b, x):
        return x, iter_count
    else:
        raise ValueError("A solução não é válida!")

# Exemplo de uso
A = np.array([[4, -1, 0, 0],
              [-1, 4, -1, 0],
              [0, -1, 4, -1],
              [0, 0, -1, 3]])

b = np.array([15, 10, 10, 10])

try:
    solution, iterations = solve_system(A, b)
    print("Solução encontrada:", solution)
    print("Número de iterações:", iterations)
except ValueError as e:
    print("Erro:", e)
