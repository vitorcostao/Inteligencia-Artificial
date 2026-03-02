# Inteligência Artificial - Aula 05 - Parte 01

## Algoritmo ID3

O algoritmo ID3 constrói uma árvore de decisão usando entropia e ganho de informação. Trata-se de um algoritmo recursivo baseado em busca gulosa.
O ponto central do algoritmo é procurar o melhor conjunto de atributos que dividem as melhores amostras em subárvores.

<img width="1216" height="763" alt="image" src="https://github.com/user-attachments/assets/af5456a1-01d7-4e5b-aa9a-8f1b19b13ea0" />

### Limitações

1) Não lida com valores contínuos (Que devem ser discretizados).
2) Não lida com valores desconhecidos, ou seja, todos
os exemplos do conjunto de treinamento deve ter
valores conhecidos para todos os seus atributos.
3) O algoritmo também não lida com nenhum
mecanismo de poda, o que poderia amenizar árvores
mais complexas

---

## Algoritmo C4.5

Surge como alternativa para os problemas apontados no algoritmo ID3 tendo as seguintes melhorias:

- Lida com valores contínuos e discretos.
- Lida com valor limiar e divide dados em dois grupos a partir de ponto de referência.

   - Ordena os pontos de referência.
   - Testa valores adjacentes como candidato limiar.
   - Acha o ganho de informação.
   - De todos os possíveis pontos de referência, aqueles que maximizam o ganho de informação separam dois exemplos de classes diferentes
 
- Poda da árvore pós criação (Remove ramificações que são inúteis).
    
### Funcionamento

O algoritmo C4.5 Implementa a Razão de Ganho (gain ratio) no lugar do ganho de informação tradicional, pois o ID3 favorecia atributos com 
muitos valores diferentes (como um CPF ou ID), o que gerava árvores inúteis, visto que não é possível prever resultados por atributos únicos.

A Razão de Ganho foi introduzida para corrigir o viés do Ganho de Informação, pois ela normaliza o ganho de informação ao considerar
o número de valores distintos de um atributo.

### Razão de Ganho (Gain Ratio)

<img width="734" height="391" alt="image" src="https://github.com/user-attachments/assets/d6c4d209-1a75-4af4-92f9-db19676e2d26" />


Aqui todo subconjunto (de um elemento) contém exemplos de uma mesma classe, ou seja, o ganho de informação 
do atributo será máximo (entropia de cada subconjunto é 0). O C4.5 resolve isso normalizando o ganho. Ele divide o
ganho de informação por uma métrica chamada SplitInfo (Informação de Divisão).

$$\text{GainRatio}(atributo) = \frac{\text{Ganho}(atributo)}{\text{SplitInfo}(atributo)}$$

$$\text{SplitInfo}(atributo) =- \sum_{i} \frac{|S_i|}{|S|}\log_{2}\left(\frac{|S_i|}{|S|}\right)$$


$$  \text{S: Conjunto total de dados antes da divisão.}$$
$$  \text{Si: Subconjuntos gerados após divisão.}$$

>OBS: O SplitInfo mede o quanto o atributo fragmentou os dados, um split alto mantém muitos subconjuntos pequenos, um split baixo
>mantém poucos subconjuntos grandes.

---

<img width="507" height="175" alt="image" src="https://github.com/user-attachments/assets/2b88622f-a5c0-409f-84b1-6b4dde7cee44" />

---

## Algoritmo CART

O CART (Classification and Regression Trees) é um método amplamente utilizado em tarefas de classificação e regressão. 
Ele constrói árvores binárias, onde cada nó interno possui exatamente dois filhos, e determina as divisões nos nós com base em critérios como o índice de Gini,
no caso de classificação, ou o erro quadrático médio, em problemas de regressão.

### Índice de Gini

Mede a impureza de um nó, ou seja, quanto maior o Gini, mais misturadas estão as classes.:

- Nó puro → Gini = 0  
- Nó misturado → Gini alto  

$$Gini(S) = 1 - \sum_{i=1}^{c} p_i^2$$

$$Gini_{pond} = \sum_{i=1}^{v} \frac{|S_i|}{|S|} Gini(S_i)$$

$$Ganho = Gini(S) - Gini_{pond}$$


---

## Referências Bibliográficas

RUSSEL, Stuart J.; NORVIG, James. Artificial Intelligence: a
modern approach. (Cap. 18 – 3ª ed. ou Cap. 19 – 4ª ed.)

HSSINA, Badr et al. A comparative study of decision tree ID3 and
C4. 5. IJACSA, v. 4, n. 2, p. 13-19, 2014.

SINGH, Sonia; GUPTA, Priyanka. Comparative study ID3, cart and
C4.5 decision tree algorithm: a survey. IJAIST, v. 27, n. 27, p.
97-103, 2014.

