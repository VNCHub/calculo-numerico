def secante(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Método da Secante para encontrar raízes de uma função.

    Parâmetros:
    f        -- Função cuja raiz queremos encontrar.
    x0, x1   -- Dois chutes iniciais para a raiz.
    tol      -- Tolerância para o critério de parada.
    max_iter -- Número máximo de iterações permitidas.

    Retorna:
    Uma aproximação da raiz da função.
    """
    for _ in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        if abs(f_x1 - f_x0) < 1e-12:  # Evita divisão por zero
            raise ValueError("Divisão por zero detectada. Escolha outro par de chutes iniciais.")

        # Fórmula do método da secante
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if abs(x2 - x1) < tol:  # Critério de parada
            return x2

        x0, x1 = x1, x2  # Atualiza os valores para a próxima iteração

    return x1  # Retorna a última aproximação se o critério não for atingido


# Exemplo de uso:
if __name__ == "__main__":
    # Definição de uma função exemplo f(x) = x^2 - 4
    def func(x):
        return x**2 - 4

    # Chutes iniciais
    x0, x1 = 3, 2.5

    # Encontrar a raiz usando o método da secante
    raiz = secante(func, x0, x1)

    print(f"A raiz encontrada pelo método da secante é aproximadamente: {raiz:.6f}")
