def newton(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    
    for _ in range(max_iter):
        f_x = f(x)
        df_x = df(x)
        
        if abs(df_x) < 1e-12:
            raise ValueError("Derivada muito próxima de zero. Escolha outro chute inicial.")

        x_new = x - f_x / df_x

        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    return x

def func(x):
    return x**3 + 2*x**2 + 10*x - 20

def deriv_func(x):
    return 3*x**2 + 4*x + 10

x0 = 1.5

raiz = newton(func, deriv_func, x0)

print(f"A raiz encontrada pelo método de Newton é aproximadamente: {raiz:.6f}")
