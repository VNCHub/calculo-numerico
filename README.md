# Métodos Numéricos

Este repositório contém implementações de diversos métodos numéricos organizados em subpastas, cada uma contendo a respectiva implementação.

## Métodos Implementados

### 1. Método da Bisseção
Localiza raízes de uma função dividindo sucessivamente um intervalo.  
📂 [Código](./01_MetodoBissecao)

### 2. Método de Newton (Newton-Raphson)
Aproxima raízes de funções utilizando derivadas.  
📂 [Código](./02_MetodoNewtonRaphson/)

### 3. Método da Secante
Semelhante ao método de Newton, mas sem necessidade da derivada.  
📂 [Código](./03_MetodoSecante/)

### 4. Método de Jacobi
Resolve sistemas lineares de forma iterativa.  
📂 [Código](./04_MetodoJacobi/)

### 5. Método de Gauss-Seidel
Uma versão otimizada do método de Jacobi, utilizando valores atualizados.  
📂 [Código](./05_MetodoGausSeidel/)

### 6. Método de Newton para Sistemas Não Lineares
Expande o método de Newton para múltiplas equações simultâneas.  
📂 [Código](./06_NewtonSistemasNaoLineares/)

### 7. Interpolação Polinomial
Ajusta um polinômio a um conjunto de pontos dados.  
📂 [Código](./07_InterpolacaoPolinomial/)

### 8. Método dos Quadrados Mínimos
Ajusta funções a dados experimentais minimizando o erro quadrático.  
📂 [Código](./08_MetodoQuadradosMinimos/)

### 9. Aproximação por Função Exponencial
Ajusta modelos exponenciais do tipo \( y = A e^{Bx} \) a dados.  
📂 [Código](./09_AproximacaoPorFuncaoExponencial/)

## Como Usar
Cada pasta contém um script Python implementando o método e, em alguns casos, exemplos de uso. Para rodar qualquer um dos métodos, basta acessar a subpasta correspondente e executar o código.

```bash
cd 01_MetodoBissecao
python3 algoritmo.py
```

## Contribuições
Sinta-se à vontade para contribuir com melhorias ou novas abordagens. Abra um pull request ou entre em contato!
Licença

Este projeto está sob a licença MIT