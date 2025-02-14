# Método de Newton para Sistemas Não Lineares

O método de Newton para sistemas não lineares é uma generalização do método de Newton para uma única equação, aplicado a um sistema de equações não lineares.

Dado um sistema de \( n \) equações com \( n \) incógnitas:
\[ 
F(x) = \begin{bmatrix}
f_1(x_1, x_2, \ldots, x_n) \\
f_2(x_1, x_2, \ldots, x_n) \\
\vdots \\
f_n(x_1, x_2, \ldots, x_n)
\end{bmatrix} = \begin{bmatrix}
0 \\
0 \\
\vdots \\
0
\end{bmatrix}
\]

onde \( F(x) \) representa um vetor de funções não lineares, queremos encontrar uma solução \( x^* \) tal que \( F(x^*) = 0 \).

## Ideia do Método

O método de Newton parte de uma aproximação inicial \( x^{(0)} \) e melhora iterativamente essa solução usando a fórmula:
\[ 
x^{(k+1)} = x^{(k)} - JF(x^{(k)})^{-1} F(x^{(k)})
\]

onde:

\( JF(x) \) é a matriz Jacobiana de \( F(x) \), ou seja:
\[ 
JF(x) = \begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \cdots & \frac{\partial f_1}{\partial x_n} \\
\frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \cdots & \frac{\partial f_2}{\partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial f_n}{\partial x_1} & \frac{\partial f_n}{\partial x_2} & \cdots & \frac{\partial f_n}{\partial x_n}
\end{bmatrix}
\]

\( JF(x)^{-1} \) é a matriz inversa de \( JF(x) \) (se existir).

A cada iteração, resolvemos o sistema linear:
\[ 
JF(x^{(k)}) \cdot \Delta x = -F(x^{(k)})
\]

e atualizamos:
\[ 
x^{(k+1)} = x^{(k)} + \Delta x
\]

O processo se repete até que a norma de \( \Delta x \) seja menor que um limiar de tolerância \( \epsilon \).
