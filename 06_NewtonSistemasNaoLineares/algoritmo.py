import numpy as np

def newton_system(F, J, x0, tol=1e-6, max_iter=50):
    """
    Método de Newton para sistemas não lineares.

    Parâmetros:
    F        -- Função que retorna um vetor de funções não lineares.
    J        -- Função que retorna a matriz Jacobiana de F.
    x0       -- Aproximação inicial (vetor).
    tol      -- Tolerância para o critério de parada.
    max_iter -- Número máximo de iterações.

    Retorna:
    Vetor solução x que satisfaz F(x) ≈ 0.
    """
    x = np.array(x0, dtype=float)

    for _ in range(max_iter):
        Fx = np.array(F(x))  # Calcula F(x)
        Jx = np.array(J(x))  # Calcula J(x)

        # Resolve o sistema linear J(x) * Δx = -F(x)
        delta_x = np.linalg.solve(Jx, -Fx)

        # Atualiza x
        x = x + delta_x

        # Critério de parada
        if np.linalg.norm(delta_x, ord=np.inf) < tol:
            return x

    return x  # Retorna a última aproximação
