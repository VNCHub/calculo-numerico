# Método da Secantes

O método da secante é um método numérico para encontrar raízes de uma função sem precisar calcular sua derivada explicitamente. Ele é uma modificação do método de Newton-Raphson, mas substitui a derivada \( f'(x) \) por uma aproximação usando dois pontos distintos da função.

## Fórmula do Método da Secante

Dado dois pontos iniciais \( x_0 \) e \( x_1 \), a próxima aproximação \( x_{n+1} \) é calculada por:

\[ x_{n+1} = x_n - \frac{f(x_n)(x_n - x_{n-1})}{f(x_n) - f(x_{n-1})} \]

onde:

- \( x_n \) e \( x_{n-1} \) são os valores das iterações anteriores,
- \( f(x_n) \) e \( f(x_{n-1}) \) são os valores da função nesses pontos.

O processo é repetido até atingir uma tolerância desejada.