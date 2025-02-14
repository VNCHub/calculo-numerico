def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Método de Newton-Raphson para encontrar raízes de uma função.

    Parâmetros:
    f        -- Função cuja raiz queremos encontrar.
    df       -- Derivada da função f(x).
    x0       -- Chute inicial para a raiz.
    tol      -- Tolerância para o critério de parada.
    max_iter -- Número máximo de iterações permitidas.

    Retorna:
    Uma aproximação da raiz da função.
    """
    x = x0  # Inicializa x com o chute inicial
    
    for _ in range(max_iter):
        f_x = f(x)
        df_x = df(x)
        
        if abs(df_x) < 1e-12:  # Evita divisão por zero ou valores muito pequenos
            raise ValueError("Derivada muito próxima de zero. Escolha outro chute inicial.")

        x_new = x - f_x / df_x  # Fórmula do método de Newton

        if abs(x_new - x) < tol:  # Critério de parada baseado na tolerância
            return x_new

        x = x_new  # Atualiza x para a próxima iteração

    return x  # Retorna a última aproximação se o critério não for atingido


# Exemplo de uso:
if __name__ == "__main__":
    # Definição de uma função exemplo f(x) = x^2 - 4
    def func(x):
        return x**2 - 4

    # Derivada da função f'(x) = 2x
    def deriv_func(x):
        return 2*x

    # Chute inicial
    x0 = 3

    # Encontrar a raiz usando o método de Newton-Raphson
    raiz = newton_raphson(func, deriv_func, x0)

    print(f"A raiz encontrada pelo método de Newton-Raphson é aproximadamente: {raiz:.6f}")
