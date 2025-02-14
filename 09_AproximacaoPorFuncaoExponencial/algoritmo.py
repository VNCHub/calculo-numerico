import numpy as np
import matplotlib.pyplot as plt

def ajuste_exponencial(x, y):
    """
    Ajusta uma função exponencial da forma y = A * e^(Bx) usando mínimos quadrados.
    
    Parâmetros:
    x -- Lista de valores de x
    y -- Lista de valores de y
    
    Retorna:
    A -- Coeficiente A da função exponencial
    B -- Coeficiente B da função exponencial
    """
    # Aplicar logaritmo natural nos valores de y
    Y_log = np.log(y)
    
    # Ajuste linear Y' = A' + Bx (usando mínimos quadrados)
    n = len(x)
    soma_x = np.sum(x)
    soma_Ylog = np.sum(Y_log)
    soma_x2 = np.sum(x**2)
    soma_xYlog = np.sum(x * Y_log)

    # Resolvendo o sistema para A' e B
    B = (n * soma_xYlog - soma_x * soma_Ylog) / (n * soma_x2 - soma_x**2)
    A_log = (soma_Ylog - B * soma_x) / n
    A = np.exp(A_log)  # Convertendo de ln(A) para A

    return A, B

# Exemplo de dados experimentais (crescimento exponencial)
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.7, 7.4, 20.1, 54.6, 148.4])  # Valores que seguem um padrão exponencial

# Ajustando a função exponencial
A, B = ajuste_exponencial(x, y)

# Criando pontos para a curva ajustada
x_ajuste = np.linspace(min(x), max(x), 100)
y_ajuste = A * np.exp(B * x_ajuste)

# Plotando os dados e a curva ajustada
plt.scatter(x, y, color='red', label='Pontos experimentais')
plt.plot(x_ajuste, y_ajuste, color='blue', label=f'Ajuste: y = {A:.2f} e^({B:.2f}x)')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Aproximação por Função Exponencial")
plt.show()
