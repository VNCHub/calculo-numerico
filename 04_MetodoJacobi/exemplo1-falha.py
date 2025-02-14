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

# Método de Jacobi
def jacobi_method(A, b, tol=1e-6, max_iter=10000):
    n = len(b)
    x = np.zeros(n)
    x_new = np.zeros(n)
    
    for iteration in range(max_iter):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, iteration + 1
        
        x = x_new.copy()
    
    return x, max_iter

# Execução e resultados
solucao_jacobi, iteracoes_jacobi = jacobi_method(A, b)
print("Solução pelo método de Jacobi:", solucao_jacobi)
print("Iterações (Jacobi):", iteracoes_jacobi)
print("A matriz é diagonalmente dominante?", is_diagonally_dominant(A))
