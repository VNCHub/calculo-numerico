# Método de Newton

O método de Newton, também chamado de método de Newton-Raphson, é um método numérico usado para encontrar aproximações de raízes de funções. Ele é muito eficiente e geralmente converge mais rápido do que o método da bisseção, especialmente quando a função é bem comportada e a estimativa inicial está próxima da raiz.

## Como funciona o Método de Newton?

O método se baseia na aproximação da função \( f(x) \) por sua tangente em um ponto próximo da raiz. A equação da tangente em um ponto \( x_n \) é usada para encontrar uma melhor aproximação \( x_{n+1} \), iterativamente.

A fórmula do método de Newton é:

\[ x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \]

onde:

- \( x_n \) é a aproximação atual da raiz,
- \( f(x) \) é a função cujo zero queremos encontrar,
- \( f'(x) \) é a derivada de \( f(x) \),
- \( x_{n+1} \) é a nova aproximação da raiz.

Esse processo é repetido até que a diferença entre \( x_n \) e \( x_{n+1} \) seja menor que uma tolerância desejada.