# Método de Gauss-Seidel

O método de Gauss-Seidel é um método iterativo para resolver sistemas de equações lineares da forma:

\[ Ax = b \]

onde:

- \( A \) é uma matriz quadrada \( n \times n \),
- \( x \) é o vetor de incógnitas,
- \( b \) é o vetor dos termos independentes.

## Diferença entre Gauss-Seidel e Jacobi

O método de Gauss-Seidel é uma variação do método de Jacobi, mas com uma diferença importante:

- **Jacobi**: Usa apenas os valores da iteração anterior para calcular novos valores.
- **Gauss-Seidel**: Usa imediatamente os valores recém-calculados na mesma iteração, tornando a convergência geralmente mais rápida.

## Fórmula do Método de Gauss-Seidel

Para cada variável \( x_i \), a fórmula de atualização é:

\[ x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j<i} a_{ij} x_j^{(k+1)} - \sum_{j>i} a_{ij} x_j^{(k)} \right) \]

onde:

- \( x_i^{(k+1)} \) é a nova aproximação da variável \( x_i \),
- \( x_j^{(k+1)} \) já foi atualizado dentro da mesma iteração,
- \( x_j^{(k)} \) são os valores antigos da iteração anterior.

## Condições de Convergência

O método de Gauss-Seidel nem sempre converge, mas há garantia de convergência se a matriz \( A \) for:

- Diagonalmente dominante, ou seja:

\[ |a_{ii}| > \sum_{j \neq i} |a_{ij}| \]

para todas as linhas \( i \).

- Simétrica e definida positiva, isto é, se \( A^T = A \) e todos os autovalores de \( A \) forem positivos.