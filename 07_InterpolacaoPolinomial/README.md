# Interpolação Polinomial

A interpolação polinomial é um método para encontrar um polinômio que passa exatamente por um conjunto de pontos dados. Se tivermos um conjunto de \( n+1 \) pontos:
\[ (x_0, y_0), (x_1, y_1), \ldots, (x_n, y_n) \]

procuramos um polinômio \( P_n(x) \) de grau no máximo \( n \) tal que:
\[ P_n(x_i) = y_i, \text{ para } i = 0, 1, \ldots, n. \]

Ou seja, o polinômio interpola os pontos dados, assumindo que a função que os gerou seja "suave" o suficiente.

## Diferença entre Interpolação e Método de Newton para Sistemas Não Lineares

A interpolação polinomial e o método de Newton para sistemas não lineares são bem diferentes:

| Método | Objetivo | Tipo de Problema |
|--------|----------|------------------|
| Newton para sistemas não lineares | Encontra raízes de sistemas não lineares \( F(x) = 0 \) | Resolve equações não lineares simultâneas |
| Interpolação polinomial | Encontra um polinômio que passa por um conjunto de pontos | Aproxima funções a partir de pontos conhecidos |

Enquanto o método de Newton encontra soluções para sistemas de equações, a interpolação polinomial reconstrói funções a partir de dados discretos.
