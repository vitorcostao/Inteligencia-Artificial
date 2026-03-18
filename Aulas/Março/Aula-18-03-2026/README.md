# Inteligência Artificial - Aula 10

## Mineração de padrões frequentes e regra de associação

### Regras de associação

As regras de associação possuem relação com as regras de classificação. Desse modo, tem-se a representação
de uma regra de associação:

$$A \to B$$

Em que:

- A: É o conjunto de dados antecedente
- B: É o conjunto de dados consequente
- O número de itens de cada conjunto pode ser maior que um.

Nesse contexto, tendo A = {pão, manteiga} e B = {ovo}, uma associação $A \to B$ é diferente de uma associação
$B \to A$
> A associação é comumente utilizada para recomendações, seja de produtos, filmes e entre outros. Além disso,
o número de regras de associação é bem maior que o número de regras de classificação.

---

### Alguns conceitos básicos

- Dataset: Trata-se do conjunto de dados.
- Transações: Corresponde às instâncias do Dataset.
- Item: São os elementos individuais.
- Itemset: São conjuntos de itens que são combinados com um valor mínimo de suporte.

---

### Qualidade das regras de associação

1) Suporte: Trata-se da frequência de um item em um dataset
   
   $S(x) = \frac{|T_x|}{T}$

2) Confiança: Indica a proporção de vezes que uma transação contendo A também contém B

   $C(A \to B) = \frac{P(A \cup B)}{P(A)}$

3) Lift: É o coeficiente de interesse, ou seja, quanto mais frequente torna-se B quando A ocorre.

   $Lift = \frac{C(A \to B)}{S(B)}$