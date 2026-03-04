# Inteligência Artificial - Aula 06

## Métodos de amostragem e avaliação de algoritmos

### Como comparar algoritmos?

Existem vários algoritmos para construção das árvores de decisão e regressão. Desse modo, mesmo Machine Learn sendo algo bom,
não existe o melhor algoritmo. Para realizar a comparação de algoritmos é preciso ter em mente os seguintes pontos:

- Saber os prós e contras dos que estão em análise.
- Saber o contexto do problema o qual o algoritmo será submetido.
- Saber a metodologia de comparação.

### Método de amostragem

O mundo real apresenta uma distribuição de exemplos D em um dado domínio, a qual é desconhecida. Ao extrair exemplos do mundo real, forma-se assim um
conjunto de exemplos com distribuição D'. Para estimar a precisão/erro do indutor, treina-se o modelo com amostras de D’ e avalia-se
seu desempenho em exemplos da mesma distribuição.

<img width="1288" height="627" alt="image" src="https://github.com/user-attachments/assets/09f9141e-2634-4764-b134-a322730f18e1" />

Dados um conjunto de exemplos de tamanho finito e um indutor, é importante estimar o desempenho futuro do classificador induzido utilizando o conjunto de exemplos.

---

### Ressubstituição

Trata-se de um método o qual o conjunto de testes é igual ao conjunto de treinamento. Uma das principais características dessa metodologia é que o erro/acerto
são aparentes, visto que o método em questão "decora" todas as intâncias, o que gera um overfitting e torna avaliações futuras imprecisas. Possui um bias (viés)
otimista na previsão, mas o bom desempenho pode não ser observado em conjuntos independentes (desconhecidos) de teste.

<img width="1221" height="666" alt="image" src="https://github.com/user-attachments/assets/703588b8-1994-4351-8eac-8e1c35dee23e" />

> O treinamento consiste em construir a árvore, enquanto o classificador consiste em utilizar a árvore criada.

---

### Holdout

Para resolver o problema de especialização da ressubstituição, o **Holdout** divide os conjuntos de dados em proporções, sendo que para treino será um valor p e 
para teste 1 - p. Além disso, é importante que o conjunto de treino seja maior do que o conjunto de testes.

Por exemplo, se existe uma base de dados com uma certa quantia de valores, é possível dividir essas instâncias em duas partes sendo que uma será de 80% enquanto
a outra será 20%. Obviamente, a soma das porcentagens deve resultar no valor do conjunto completo.

- **Limitações:**
  
  - Taxa de acerto menor para conjuntos de dados pequenos.
  - Depende do particionamento (exemplos fáceis no conjunto de testes).

<img width="1209" height="350" alt="image" src="https://github.com/user-attachments/assets/19258b04-c521-436a-a744-4bef98fbf5ec" />


---


### Amostragem aleatória

Para solucionar o problema do particionamento mencionado acima, a **Amostragem Aleatória** surge como uma metodologia possível. Em termos práticos, 
a ideia é calcular a média de vários resultados de holdout através da construção de várias partições. O erro final é calculado como sendo a média dos erros
de todas as r hipóteses induzidas e calculadas em conjuntos de teste independentes e extraídos aleatoriamente.

Desse modo, a amostragem aleatória pode produzir melhores estimativas de erro que o estimador holdout


<img width="1301" height="484" alt="image" src="https://github.com/user-attachments/assets/bd2d2cb2-92e6-4d22-92ca-76fbfcbb5dfc" />


---


### Validação Cruzada

Nesse método, o conjunto de exemplos é dividido em r subconjuntos (folds) de tamanho aproximadamente igual (r-fold cross validation), 
os objetos de r-1 partições são usados no treinamento, enquanto a partição restante é usada no teste. Este processo é repetido r vezes, 
utilizando em cada ciclo uma partição diferente para teste. Tal procedimento de rotação reduz o viés inerente ao método de holdout.

- **Limitações:**
  - Parte dos dados são compartilhados entre os subconjuntos de treinamento.
  - É computacionalmente cara.

<img width="1206" height="735" alt="image" src="https://github.com/user-attachments/assets/e50d314d-803c-4a53-ba24-0a64154c9fdd" />

> Na validação cruzada estratificada, cada partição procura manter as proporções do conjunto original.


---


### Bootstrap

No método bootstrap, são gerados r subconjuntos de treinamento a partir do conjunto original. A partir disso, os exemplos são amostrados aleatoriamente desse
conjunto com reposição, ou seja, um exemplo pode estar presente em um mesmo subconjunto de treinamento mais de uma vez. Por fim, os exemplos que não apareceram
no conjunto de treino são submetidos ao conjunto de testes. 

<img width="1171" height="677" alt="image" src="https://github.com/user-attachments/assets/ec3ff0e0-ac02-4c83-a382-c4c46543ccdf" />


---

## Ajuste de parâmetros

Em alguns casos, é importante realizar um ajuste de hiperparâmetros de um indutor, ou seja, deseja-se saber quais seriam os melhores valores para estes hiperparâmetros.
Nesses casos, é necessário reservar uma parte dos exemplos para ajustar os parâmetros (conjunto de validação) e outra parte para teste.

<img width="1177" height="665" alt="image" src="https://github.com/user-attachments/assets/44f78861-3b38-4866-8105-93ebaf86fdcd" />

<img width="1294" height="754" alt="image" src="https://github.com/user-attachments/assets/5d384f74-024c-4627-8182-5a4b9084da41" />


---

## Referências Bibliográficas

FACELI, Katti et al. Inteligência artificial: uma abordagem de aprendizado de máquina. Rio de Janeiro, RJ: LTC, 2011. (Capítulo 9)

Material do Prof. José Augusto Baranauskas (USP)






