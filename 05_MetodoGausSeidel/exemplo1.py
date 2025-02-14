import numpy as np

# Matriz de coeficientes A e vetor b de demandas
A = np.array([[5, 1, 0, 0, 0],
              [0, 2, 1, 0, 0],
              [2, 0, 1, 1, 0],
              [0, 1, 0, 1, 1],
              [4, 0, 0, 0, 1]])
b = np.array([15, 25, 30, 35, 40])

# Função para verificar se a matriz é diagonalmente dominante
def is_diagonally_dominant(A):
    for i in range(len(A)):
        row_sum = sum(abs(A[i][j]) for j in range(len(A)) if j != i)
        if abs(A[i][i]) < row_sum:
            return False
    return True

# Método de Gauss-Seidel
def gauss_seidel_method(A, b, tol=1e-6, max_iter=10000):
    n = len(b)
    x = np.zeros(n)
    
    for iteration in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, iteration + 1
        
        x = x_new
    
    return x, max_iter

# Execução e resultados
solucao_gauss_seidel, iteracoes_gauss_seidel = gauss_seidel_method(A, b)
print("Solução pelo método de Gauss-Seidel:", solucao_gauss_seidel)
print("Iterações (Gauss-Seidel):", iteracoes_gauss_seidel)
