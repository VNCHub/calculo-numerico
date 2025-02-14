# Método dos Quadrados Mínimos

O método dos quadrados mínimos (ou mínimos quadrados) é uma técnica utilizada para ajustar uma função modelo a um conjunto de dados experimentais. Ele busca encontrar a função que minimiza o erro entre os valores observados e os valores previstos pela função.

É amplamente usado em regressão linear, análise estatística e machine learning.

## Ideia do Método

Dado um conjunto de $n$ pontos experimentais:
$(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)$

queremos encontrar uma função $f(x)$ que melhor se ajusta aos dados, minimizando os erros. O erro (ou resíduo) para cada ponto é dado por:
$r_i = y_i - f(x_i)$

O objetivo do método dos quadrados mínimos é minimizar a soma dos quadrados dos resíduos:
$S = \sum_{i=1}^{n} r_i^2 = \sum_{i=1}^{n} (y_i - f(x_i))^2$

## Aplicação na Regressão Linear

O caso mais comum é a regressão linear, onde buscamos ajustar uma reta:
$f(x) = ax + b$

A minimização de $S$ nos leva ao sistema de equações normais:
$a \sum x_i^2 + b \sum x_i = \sum x_i y_i$
$a \sum x_i + nb = \sum y_i$

Resolvendo esse sistema, obtemos os coeficientes $a$ e $b$ da reta de melhor ajuste.
