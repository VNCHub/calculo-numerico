import numpy as np
import matplotlib.pyplot as plt

def ajuste_quadrados_minimos(x, y):
    """
    Ajusta uma reta y = ax + b pelo método dos quadrados mínimos.
    
    Parâmetros:
    x -- Lista de valores de x
    y -- Lista de valores de y
    
    Retorna:
    a -- Coeficiente angular
    b -- Coeficiente linear
    """
    n = len(x)
    
    # Calculando as somas necessárias
    soma_x = sum(x)
    soma_y = sum(y)
    soma_x2 = sum(xi**2 for xi in x)
    soma_xy = sum(x[i] * y[i] for i in range(n))

    # Resolvendo o sistema de equações normais
    a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x**2)
    b = (soma_y - a * soma_x) / n

    return a, b

# Exemplo de dados experimentais
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 2.8, 3.6, 4.5, 5.1])

# Calculando os coeficientes da reta de ajuste
a, b = ajuste_quadrados_minimos(x, y)

# Criando pontos para a reta ajustada
x_ajuste = np.linspace(min(x), max(x), 100)
y_ajuste = a * x_ajuste + b

# Plotando os dados e a reta ajustada
plt.scatter(x, y, color='red', label='Pontos experimentais')
plt.plot(x_ajuste, y_ajuste, color='blue', label=f'Reta ajustada: y = {a:.2f}x + {b:.2f}')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Ajuste por Quadrados Mínimos")
plt.show()
