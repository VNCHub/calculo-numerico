# Enunciado:
# No ano de 1225, Leonard of Pisa estudou a equação:
# 
#     x³ + 2x² + 10x - 20 = 0
# 
# e obteve a solução aproximada: x = 1.368808107.
# Ninguém sabe qual método Leonard usou, mas a solução é uma boa aproximação.
# 
# Usando o método da bisseção, encontre uma aproximação para a raiz dessa equação.

def bissecao(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("A função deve ter sinais opostos em a e b.")

    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        f_c = f(c)

        if abs(f_c) < tol:
            return c

        if f(a) * f_c < 0:
            b = c
        else:
            a = c

        iter_count += 1

    return (a + b) / 2


# Definição da função f(x) = x³ + 2x² + 10x - 20
def func(x):
    return x**3 + 2*x**2 + 10*x - 20

raiz = bissecao(func, 1, 2)

print(f"A raiz encontrada pelo método da bisseção é aproximadamente: {raiz:.6f}")
