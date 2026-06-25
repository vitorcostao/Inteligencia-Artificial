# 🧩 8-Puzzle Solver

Solver interativo para o jogo 8-Puzzle, implementado em Python como Atividade Prática #2 da disciplina de **Inteligência Artificial** — PUC Minas.

## 📋 Requisitos

- **Python 3.8** ou superior
- Sem dependências externas (usa apenas bibliotecas padrão)

## ▶️ Como Executar

```bash
cd Code
python main.py
```

## 🎯 Estado Objetivo

```
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 8 │   │ 4 │
├───┼───┼───┤
│ 7 │ 6 │ 5 │
└───┴───┴───┘
```

## 🔧 Algoritmos Implementados

| # | Algoritmo | Completo? | Ótimo? | Estrutura de Dados |
|---|-----------|-----------|--------|--------------------|
| 1 | BFS (Busca em Largura) | ✅ | ✅ | Fila (FIFO) |
| 2 | DFS (Busca em Profundidade) | ❌* | ❌ | Pilha (LIFO) |
| 3 | Busca de Custo Uniforme | ✅ | ✅ | Min-Heap |
| 4 | Busca Gulosa | ❌** | ❌ | Min-Heap |
| 5 | A* | ✅ | ✅ | Min-Heap |

\* Com limite de profundidade (padrão: 50).  
\** Completo nesta implementação pois usa conjunto de estados explorados.

## 📐 Heurísticas (para A* e Gulosa)

| Heurística | Descrição | Admissível? |
|------------|-----------|-------------|
| Hamming | Peças fora do lugar | ✅ |
| Manhattan | Soma das distâncias Manhattan | ✅ |
| Manhattan + LC | Manhattan + Conflitos Lineares | ✅ |

## 📂 Estrutura do Projeto

```
Code/
├── main.py           # Interface interativa (ponto de entrada)
├── puzzle_state.py   # Representação do estado do tabuleiro
├── algorithms.py     # 5 algoritmos de busca
├── heuristics.py     # 3 heurísticas admissíveis
├── utils.py          # Utilitários (solucionabilidade, formatação)
└── README.md         # Este arquivo
```

## 🕹️ Funcionalidades

- **Entrada manual** do tabuleiro
- **Geração aleatória** de estados solucionáveis
- **Estados pré-definidos** com dificuldades variadas (incluindo insolucionável)
- **Detecção automática** de estados insolucionáveis (por contagem de inversões)
- **Visualização passo a passo** do caminho da solução
- **Modo comparativo**: executa todos os algoritmos e gera tabela com métricas
- **Métricas por execução**: movimentos, nós visitados, nós gerados, profundidade, tempo

## 📊 Exemplo de Tabela Comparativa

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 TABELA COMPARATIVA DE RESULTADOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Algoritmo            Heurística      Solução?   Movim.  Visitados    Gerados      Tempo (s)
──────────────────────────────────────────────────────────────────────────────────────────
BFS                  -               Sim        5       25           42           0.001234
DFS                  -               Sim        23      35           58           0.000891
A*                   Manhattan       Sim        5       8            14           0.000567
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
