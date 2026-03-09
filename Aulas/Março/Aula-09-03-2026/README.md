# Inteligência Artificial - Aula 07

## Aprendizado em conjunto (Ensemble)

### O que é Ensemble?

Trata-se de uma classe de algoritmos a qual um grupo de modelos individuais são combinados para tomar uma determinada
decisão. Nesse contexto, entende-se na literatura que o desempenho de muitos classificadores fracos é melhor do que um
único classificador para uma mesma quantia de dados de treinamento.

### Condições para o Ensemble

- A Diversidade: Os classificadores base devem ser independentes e cometer erros para instâncias diferentes.
- A acurácia: O desemepenho de cada classificador deve ser no mínimo melhor que um palpite aleatório.

De modo simples, pensando em três classificadores com 60% de acurácia, se caso cometam os mesmos erros, a acurácia do
Ensemble é igual. No entanto, se forem independentes, o Ensemble do errará se ao mínimo dois dos três errarem.

Para combinar os resultados, existem duas abordagens: Na classificação, na regressão. Nesse sentido, na classificação
é realizada uma "votação" entre os modelos para determinar a resposta, enquanto na regressão é feita uma média dos 
resultados para determinar o valor.

### Tipos de Ensemble

1) Bagging (Bootstrap Aggregating)
   
    Tal modelo é baseado na redução da variância, o qual se cria múltiplos subconjuntos de treino (Bootstrap) e, para
  cada um dos conjuntos, é realizado um treino independente e simultâneo entre os indutores, de modo que, ao final,
  tem-se os resultados combinados formando um estimador.

3) Boosting
   
     Neste modelo, é realizado o treinamento de forma sequencial para reduzir o viés. A cada treinamento é avaliado
   o erro para determinada instância. Com base nesse erro, o próximo treinamento será visado para o corrigir até
   que o processo seja encerrado. Apesar de ser bom para indutores de base fracos e possuir uma convergência de
   resultados, tal modelo não serve para conjuntos de dados pequenos (Foca em exemplos difíceis) e com muitos ruídos.

5) Stacking

     No Stacking, vários indutores são combinados de forma ao final se tenha um Meta-indutor. Vale ressaltar que os
   indutores nesse modelo podem ser heterogêneos ou homogêneos.


---

### Ensemble nas árvores de decisão

1) **XGBoost (Árvores geradas pelo CART)**

     O XGBoost, que é baseado no boosting, combina várias árvores de modo sequencial, sendo que ao final do processo
   os resultados serão somados e avaliados para obter uma resposta.

     <img width="695" height="336" alt="image" src="https://github.com/user-attachments/assets/f835a667-467e-45ff-96a1-9ce84445837e" />

2) Random Forest

     É um algoritmo que utiliza várias árvores de decisão em paralelo para prever os valores, o principal problema é que, para
   atributos fortes, a raiz das árvores sempre será a mesma, é por isso que a fonte de aleatoriedade deve vir do Bootstrap e do
   subconjunto aleatório de atributos a cada divisão.

   Para construção da floresta é preciso:

   - Gerar amostra Bootstrap
   - Construir árvore para cada nó
       - Selecionar melhores atributos
       - Escolher os melhores splits
   - Crescer a árvore até critério de parada
  
   Como principais vantagens, tem-se a robustez aos ruídos e o fornecimento da importância das variáveis. No entanto, tal método
   é lento para requisições em tempo real e difícil de explicar as decisões das árvores.

   Como principais hiperparâmetros, tem-se: Número de árvores, tamanho do subconjunto aleatório de atributos, entropia e aleatoriedade.

## Referências Bibliográficas

FACELI, Katti et al. Inteligência artificial: uma abordagem de
aprendizado de máquina. Rio de Janeiro, RJ: LTC, 2011. (Capítulo 8)

Material da Profa. Cristiane Nobre

Breiman, L. Random Forest. Machine Learning (2001) 45: 5.

https://doi.org/10.1023/A:1010933404324

Chen, T & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting
System. In: KDD. pp. 785–794.

https://doi.org/10.1145/2939672.2939785

https://www.stat.berkeley.edu/~breiman/RandomForests/cc_home.htm#workings
