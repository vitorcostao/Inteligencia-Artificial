# Inteligência Artificial - Aula 19


## 1. Redes Neurais Convolucionais (CNNs) e os Desafios da Visão Computacional

Para um computador, reconhecer um gato é mais difícil do que resolver equações diferenciais. Isso ocorre porque o reconhecimento de imagens envolve a extração de conhecimento visual, uma tarefa que o cérebro humano realiza de forma intuitiva. A **Visão Computacional** é a área da IA que permite aos computadores "enxergar" e extrair conhecimento de imagens.

### Redes Neurais Multicamadas (MLP) e seus Problemas

Redes Neurais (RNAs) aprendem padrões complexos através da combinação de pesos e ativações. Uma **Multilayer Perceptron (MLP)** é uma rede neural com múltiplas camadas (entrada, intermediárias/ocultas, saída). Embora eficazes para certos problemas, MLPs enfrentam desafios significativos na classificação de imagens:

*   **Alta Dimensionalidade:** Uma imagem de 224x224 pixels RGB (3 valores por pixel) possui mais de 150 mil valores de entrada. Conectar isso a 1.000 neurônios na primeira camada oculta resultaria em 150 milhões de pesos para aprender, tornando o processo computacionalmente muito caro.
*   **Perda de Estrutura Espacial:** MLPs tratam cada pixel como uma entrada independente, não considerando a relação espacial entre eles. Um pixel do olho de um gato é tratado da mesma forma que um pixel da pata, ignorando a estrutura da imagem.

## 2. Histórico e Inspiração das CNNs

A intuição das Redes Convolucionais (CNNs) é imitar a forma como o cérebro humano processa imagens: não olhando todos os pixels ao mesmo tempo, mas varrendo a imagem em pedaços locais e acumulando evidências. As bases das CNNs remontam aos anos 1970, com um artigo seminal de LeCun, Bengio e Haffner em 1998. No entanto, a tecnologia "dormiu" por cerca de 14 anos devido à falta de poder computacional e dados.

O ressurgimento ocorreu em **2012 com a AlexNet**, que venceu o desafio ImageNet com uma taxa de erro significativamente menor, impulsionando a revolução do Deep Learning (DL) e o uso de GPUs. Desde então, as CNNs foram amplamente adotadas por grandes empresas de tecnologia para diversas aplicações, como busca de imagens, recomendação de produtos e marcação de usuários em fotos.

**Deep Learning** é um termo que descreve redes neurais com muitas camadas de transformações não lineares, capazes de consumir dados de entrada brutos e aprender representações complexas.

## 3. Redes Convolucionais: Inspiração e Definições

As CNNs são inspiradas biologicamente no reconhecimento de objetos pelo cérebro, que parte de primitivas básicas e constrói conceitos abstratos iterativamente, utilizando **orientação seletiva** e **campo receptivo local**. Uma CNN é um algoritmo de Deep Learning que:

1.  Capta uma imagem de entrada.
2.  Atribui importância (pesos e vieses aprendíveis) a vários aspectos/objetos da imagem.
3.  É capaz de diferenciar um objeto do outro.

O processo de uma CNN geralmente envolve quatro etapas principais:

### 3.1. Etapa 1: Convolução

Esta é a etapa de **extração de características (features)**. Pequenos filtros matemáticos (kernels) são passados por toda a imagem. Cada filtro procura um padrão específico (ex: linhas, bordas, formas geométricas). A imagem e o kernel são matrizes, e a operação de convolução gera um **mapa de características (feature map)**. Este mapa é uma representação menor da imagem original, preservando suas características principais e facilitando o processamento. Após a convolução, uma função de ativação (como ReLU) é aplicada ao feature map.

### 3.2. Etapa 2: Pooling

O Pooling é a etapa de **redução de dimensionalidade**, que seleciona as características mais relevantes do feature map. Técnicas comuns incluem **Max Pooling** (seleciona o valor máximo em uma região) ou Average Pooling (calcula a média). O objetivo é reduzir o tamanho da representação, mantendo as informações essenciais, sem precisar da localização exata de um padrão.

As etapas de Convolução e Pooling geralmente se repetem várias vezes na arquitetura de uma CNN, permitindo a extração de padrões cada vez mais complexos e abstratos.

### 3.3. Etapa 3: Flattening

Esta etapa prepara os dados para a rede neural densa. As matrizes resultantes das camadas convolucionais e de pooling são transformadas em um **vetor unidimensional (1D)**. Isso é necessário porque as redes neurais tradicionais (redes densas) aceitam dados em formato linear, não em matrizes.

### 3.4. Etapa 4: Rede Neural Densa

Esta é a etapa de **classificação**. Geralmente, é uma rede MLP (fully connected) que recebe o vetor de características extraídas e resumidas pelas etapas anteriores. A rede densa aprende a combinar essas características para tomar a decisão final, atribuindo probabilidades a diferentes classes (ex: "95% de chance de ser um Gato e 5% de chance de ser um Cachorro").

## Referências

- RUSSELL, Stuart J.; NORVIG, Peter. *Artificial intelligence: a modern approach*. 4ª ed. Pearson, 2021. (Capítulo 21)
- Material da Profa. Cristiane Nobre
- [Uma breve história das redes neurais artificiais](https://www.deeplearningbook.com.br/uma-breve-historia-das-redes-neurais-artificiais/)
- [Reconhecimento de imagens com redes neurais convolucionais em Python](https://www.deeplearningbook.com.br/reconhecimento-de-imagens-com-redes-neurais-convolucionais-em-python-parte-4/)
- [Simulador de rede neural](https://adamharley.com/nn_vis/cnn/2d.html)
