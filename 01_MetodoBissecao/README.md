# Método da Bisseção

O método da bisseção é um método numérico usado para encontrar raízes de funções contínuas. Ele se baseia no Teorema do Valor Intermediário, que diz que se uma função \( f(x) \) é contínua em um intervalo \([a,b]\) e \( f(a) \) e \( f(b) \) têm sinais opostos, então existe pelo menos um valor \( c \) no intervalo \([a,b]\) tal que \( f(c) = 0 \).

## Passos do Método da Bisseção

1. Escolher um intervalo \([a,b]\) onde \( f(a) \) e \( f(b) \) tenham sinais opostos.
2. Calcular o ponto médio \( c = \frac{a+b}{2} \).
3. Verificar o valor de \( f(c) \):
    - Se \( f(c) \) for muito próximo de zero (dentro de uma tolerância aceita), então \( c \) é a raiz.
    - Se \( f(c) \) tiver o mesmo sinal de \( f(a) \), então substituímos \( a \) por \( c \), restringindo o intervalo para \([c,b]\).
    - Se \( f(c) \) tiver o mesmo sinal de \( f(b) \), então substituímos \( b \) por \( c \), restringindo o intervalo para \([a,c]\).
4. Repetimos os passos acima até que a raiz seja encontrada com a precisão desejada.