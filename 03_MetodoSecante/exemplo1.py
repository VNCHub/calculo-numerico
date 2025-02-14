def secante(f, x0, x1, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if abs(f_x1 - f_x0) < 1e-12:
            raise ValueError("Divisão por zero detectada. Escolha outro par de chutes iniciais.")

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if abs(x2 - x1) < tol:
            return x2

        x0, x1 = x1, x2

    return x1

def func(x):
    return x**3 + 2*x**2 + 10*x - 20

x0, x1 = 1, 1.5
raiz = secante(func, x0, x1)

print(f"A raiz encontrada pelo método da secante é aproximadamente: {raiz:.6f}")
