import numpy as np

def diferencas_divididas(x, y):
    """
    Calcula a tabela de diferenças divididas para a interpolação de Newton.
    
    Parâmetros:
    x -- Lista de pontos x
    y -- Lista de pontos y
    
    Retorna:
    Lista de coeficientes do polinômio interpolador.
    """
    n = len(x)
    coef = np.array(y, dtype=float)

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])

    return coef

def polinomio_newton(x, coef, x_interp):
    """
    Avalia o polinômio interpolador de Newton em um ponto x_interp.
    
    Parâmetros:
    x -- Lista de pontos x conhecidos
    coef -- Lista de coeficientes obtidos por diferenças divididas
    x_interp -- Ponto onde o polinômio será avaliado
    
    Retorna:
    Valor do polinômio interpolador em x_interp.
    """
    n = len(x)
    resultado = coef[-1]

    for i in range(n - 2, -1, -1):
        resultado = resultado * (x_interp - x[i]) + coef[i]

    return resultado

# Exemplo de uso
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]  # f(x) = x², então estamos interpolando y = x²

# Calcula os coeficientes do polinômio interpolador
coeficientes = diferencas_divididas(x, y)

# Avalia o polinômio em x_interp = 2.5
x_interp = 2.5
resultado = polinomio_newton(x, coeficientes, x_interp)

print(f"O valor interpolado em x = {x_interp} é {resultado}")
