# Método de Jacobi

O método de Jacobi é um método iterativo para resolver sistemas de equações lineares da forma:
\[ Ax = b \]

onde:

- \( A \) é uma matriz quadrada \( n \times n \),
- \( x \) é o vetor de incógnitas,
- \( b \) é o vetor dos termos independentes.

## Ideia Principal

O método de Jacobi parte de uma aproximação inicial e refina essa solução iterativamente. A ideia central é isolar cada variável na sua própria equação e usar os valores das outras variáveis da iteração anterior.

Dada a matriz \( A \) e o vetor \( b \), reescrevemos cada equação na forma:

\[ x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \neq i} a_{ij} x_j^{(k)} \right) \]

onde:

- \( x_i^{(k+1)} \) é a nova aproximação da variável \( x_i \),
- \( x_j^{(k)} \) são os valores antigos da iteração anterior,
- \( a_{ii} \) é o elemento diagonal da matriz \( A \) (deve ser dominante).

O processo continua até que a diferença entre as iterações seja menor que uma tolerância \( \epsilon \).

## Condições de Convergência

O método de Jacobi nem sempre converge, mas a convergência é garantida se a matriz \( A \) for diagonalmente dominante, ou seja:

\[ |a_{ii}| > \sum_{j \neq i} |a_{ij}| \]

para todas as linhas \( i \).

Se a matriz não for diagonalmente dominante, o método pode ainda convergir, mas não há garantia.