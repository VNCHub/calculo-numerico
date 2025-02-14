def bissecao(f, a, b, tol=1e-6, max_iter=100):
    """
    Implementação do método da bisseção para encontrar raízes de uma função contínua.
    
    Parâmetros:
    f        -- Função cuja raiz queremos encontrar.
    a, b     -- Intervalo inicial [a, b], onde f(a) e f(b) têm sinais opostos.
    tol      -- Tolerância para o critério de parada.
    max_iter -- Número máximo de iterações permitidas.

    Retorna:
    A aproximação da raiz da função no intervalo dado.
    """
    # Verifica se f(a) e f(b) têm sinais opostos
    if f(a) * f(b) >= 0:
        raise ValueError("A função deve ter sinais opostos em a e b.")
    
    iter_count = 0  # Contador de iterações
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2  # Calcula o ponto médio
        f_c = f(c)  # Avalia a função em c

        if abs(f_c) < tol:  # Se f(c) estiver dentro da tolerância, encontramos a raiz
            return c

        if f(a) * f_c < 0:  # Se f(a) e f(c) têm sinais opostos, a raiz está em [a, c]
            b = c
        else:  # Se f(b) e f(c) têm sinais opostos, a raiz está em [c, b]
            a = c
        
        iter_count += 1  # Atualiza o contador de iterações

    return (a + b) / 2  # Retorna o valor médio do intervalo final como aproximação da raiz


# Exemplo de uso
if __name__ == "__main__":
    import math

    # Definição da função f(x) = x^3 - x - 2
    def func(x):
        return x**3 - x - 2

    # Intervalo onde sabemos que a raiz está presente
    raiz = bissecao(func, 1, 2)
    
    print(f"A raiz encontrada é aproximadamente: {raiz:.6f}")
