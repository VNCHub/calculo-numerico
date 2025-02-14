# Métodos Numéricos

Este repositório contém implementações de diversos métodos numéricos organizados em subpastas, cada uma contendo a respectiva implementação.

## Métodos Implementados

### 1. Método da Bisseção
Localiza raízes de uma função dividindo sucessivamente um intervalo.  
📂 [Código](./metodo_bissecao/)

### 2. Método de Newton (Newton-Raphson)
Aproxima raízes de funções utilizando derivadas.  
📂 [Código](./metodo_newton/)

### 3. Método da Secante
Semelhante ao método de Newton, mas sem necessidade da derivada.  
📂 [Código](./metodo_secante/)

### 4. Método de Jacobi
Resolve sistemas lineares de forma iterativa.  
📂 [Código](./metodo_jacobi/)

### 5. Método de Gauss-Seidel
Uma versão otimizada do método de Jacobi, utilizando valores atualizados.  
📂 [Código](./metodo_gauss_seidel/)

### 6. Método de Newton para Sistemas Não Lineares
Expande o método de Newton para múltiplas equações simultâneas.  
📂 [Código](./metodo_newton_sistemas/)

### 7. Interpolação Polinomial
Ajusta um polinômio a um conjunto de pontos dados.  
📂 [Código](./interpolacao_polinomial/)

### 8. Método dos Quadrados Mínimos
Ajusta funções a dados experimentais minimizando o erro quadrático.  
📂 [Código](./quadrados_minimos/)

### 9. Aproximação por Função Exponencial
Ajusta modelos exponenciais do tipo \( y = A e^{Bx} \) a dados.  
📂 [Código](./aproximacao_exponencial/)

## Como Usar
Cada pasta contém um script Python implementando o método e, em alguns casos, exemplos de uso. Para rodar qualquer um dos métodos, basta acessar a subpasta correspondente e executar o código.

```bash
cd metodo_bissecao
python metodo_bissecao.py
```

## Contribuições
Sinta-se à vontade para contribuir com melhorias ou novas abordagens. Abra um pull request ou entre em contato!
Licença

Este projeto está sob a licença MIT