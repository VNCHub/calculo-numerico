import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=100):
    """
    Método de Gauss-Seidel para resolver sistemas lineares Ax = b.

    Parâmetros:
    A        -- Matriz dos coeficientes (n x n).
    b        -- Vetor dos termos independentes (n).
    x0       -- Chute inicial (opcional, padrão é um vetor de zeros).
    tol      -- Tolerância para o critério de parada.
    max_iter -- Número máximo de iterações.

    Retorna:
    Um vetor x aproximado para a solução do sistema.
    """
    n = len(A)
    x = np.zeros(n) if x0 is None else np.array(x0, dtype=float)

    for _ in range(max_iter):
        x_old = x.copy()

        for i in range(n):
            soma1 = sum(A[i][j] * x[j] for j in range(i))   # Usa os valores já atualizados
            soma2 = sum(A[i][j] * x_old[j] for j in range(i+1, n))  # Usa os valores antigos

            x[i] = (b[i] - soma1 - soma2) / A[i][i]

        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x

    return x  # Retorna a última aproximação se o critério não for atingido


# Exemplo de uso:
if __name__ == "__main__":
    A = np.array([[10, -1, 2, 0],
                  [-1, 11, -1, 3],
                  [2, -1, 10, -1],
                  [0, 3, -1, 8]], dtype=float)

    b = np.array([6, 25, -11, 15], dtype=float)

    x0 = [0, 0, 0, 0]  # Chute inicial

    solucao = gauss_seidel(A, b, x0)

    print(f"Solução aproximada: {solucao}")
