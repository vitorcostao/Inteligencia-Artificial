"""
Módulo de algoritmos de busca para o 8-Puzzle.

Implementa 5 algoritmos:
    1. BFS  — Busca em Largura
    2. DFS  — Busca em Profundidade (com limite)
    3. UCS  — Busca de Custo Uniforme
    4. Greedy — Busca Gulosa
    5. A*   — Busca A*

Todos os algoritmos retornam um objeto SearchResult com métricas
de desempenho (nós visitados, gerados, tempo, etc.).
"""

import time
from collections import deque
import heapq

from puzzle_state import PuzzleState
from utils import reconstruct_path


class SearchResult:
    """
    Resultado de uma busca, contendo a solução e métricas de desempenho.

    Atributos:
        found (bool): Se a solução foi encontrada.
        path (list[PuzzleState]): Caminho do estado inicial ao objetivo.
        nodes_visited (int): Número de nós expandidos (retirados da fronteira).
        nodes_generated (int): Número de nós gerados (adicionados à fronteira).
        depth (int): Profundidade da solução (número de movimentos).
        execution_time (float): Tempo de execução em segundos.
        algorithm_name (str): Nome do algoritmo utilizado.
        heuristic_name (str | None): Nome da heurística (se aplicável).
    """

    def __init__(self):
        self.found = False
        self.path = []
        self.nodes_visited = 0
        self.nodes_generated = 0
        self.depth = 0
        self.execution_time = 0.0
        self.algorithm_name = ""
        self.heuristic_name = None

    def __repr__(self):
        return (
            f"SearchResult(found={self.found}, depth={self.depth}, "
            f"visited={self.nodes_visited}, generated={self.nodes_generated}, "
            f"time={self.execution_time:.4f}s)"
        )


# =====================================================================
# 1. BFS — Busca em Largura
# =====================================================================

def bfs(initial_state):
    """
    Busca em Largura (Breadth-First Search).

    Explora todos os nós de uma profundidade antes de avançar para a próxima.
    Usa uma fila (FIFO) como estrutura de dados para a fronteira.

    Propriedades:
        - Completo: Sim (para espaço de estados finito).
        - Ótimo: Sim (quando o custo por passo é uniforme, como neste caso).
        - Complexidade de Tempo: O(b^d), onde b = fator de ramificação, d = profundidade.
        - Complexidade de Espaço: O(b^d).

    Args:
        initial_state (PuzzleState): Estado inicial do puzzle.

    Returns:
        SearchResult: Resultado da busca com métricas.
    """
    result = SearchResult()
    result.algorithm_name = "BFS (Busca em Largura)"

    start_time = time.perf_counter()

    # Verificar se o estado inicial já é o objetivo
    if initial_state.is_goal():
        result.found = True
        result.path = [initial_state]
        result.depth = 0
        result.nodes_visited = 1
        result.nodes_generated = 0
        result.execution_time = time.perf_counter() - start_time
        return result

    frontier = deque([initial_state])
    explored = {initial_state.board}
    nodes_generated = 0

    while frontier:
        current = frontier.popleft()
        result.nodes_visited += 1

        for successor in current.get_successors():
            nodes_generated += 1

            if successor.board not in explored:
                if successor.is_goal():
                    result.found = True
                    result.path = reconstruct_path(successor)
                    result.depth = successor.depth
                    result.nodes_generated = nodes_generated
                    result.execution_time = time.perf_counter() - start_time
                    return result

                explored.add(successor.board)
                frontier.append(successor)

    result.nodes_generated = nodes_generated
    result.execution_time = time.perf_counter() - start_time
    return result


# =====================================================================
# 2. DFS — Busca em Profundidade
# =====================================================================

def dfs(initial_state, max_depth=50):
    """
    Busca em Profundidade (Depth-First Search) com limite de profundidade.

    Explora o caminho mais profundo primeiro, usando uma pilha (LIFO).
    O limite de profundidade evita loops infinitos (o 8-puzzle tem solução
    com no máximo 31 movimentos).

    Propriedades:
        - Completo: Não (sem limite). Com limite, pode não encontrar soluções
          mais profundas que o limite.
        - Ótimo: Não (pode encontrar uma solução subótima).
        - Complexidade de Tempo: O(b^m), onde m = profundidade máxima.
        - Complexidade de Espaço: O(b*m) — muito menor que BFS.

    Args:
        initial_state (PuzzleState): Estado inicial do puzzle.
        max_depth (int): Profundidade máxima permitida (padrão: 50).

    Returns:
        SearchResult: Resultado da busca com métricas.
    """
    result = SearchResult()
    result.algorithm_name = f"DFS (Busca em Profundidade, limite={max_depth})"

    start_time = time.perf_counter()

    if initial_state.is_goal():
        result.found = True
        result.path = [initial_state]
        result.depth = 0
        result.nodes_visited = 1
        result.nodes_generated = 0
        result.execution_time = time.perf_counter() - start_time
        return result

    frontier = [initial_state]
    explored = set()
    nodes_generated = 0

    while frontier:
        current = frontier.pop()

        if current.board in explored:
            continue

        explored.add(current.board)
        result.nodes_visited += 1

        if current.is_goal():
            result.found = True
            result.path = reconstruct_path(current)
            result.depth = current.depth
            result.nodes_generated = nodes_generated
            result.execution_time = time.perf_counter() - start_time
            return result

        # Não expandir além do limite de profundidade
        if current.depth >= max_depth:
            continue

        for successor in current.get_successors():
            nodes_generated += 1
            if successor.board not in explored:
                frontier.append(successor)

    result.nodes_generated = nodes_generated
    result.execution_time = time.perf_counter() - start_time
    return result


# =====================================================================
# 3. UCS — Busca de Custo Uniforme
# =====================================================================

def uniform_cost(initial_state):
    """
    Busca de Custo Uniforme (Uniform Cost Search).

    Expande sempre o nó com menor custo acumulado g(n).
    Usa uma fila de prioridade (min-heap) ordenada por g(n).

    Para o 8-puzzle, onde cada movimento tem custo 1, o UCS se comporta
    de forma idêntica ao BFS. Porém, a implementação é generalizada.

    Propriedades:
        - Completo: Sim (para custos positivos).
        - Ótimo: Sim.
        - Complexidade de Tempo: O(b^(1+⌊C*/ε⌋)), onde C* = custo ótimo.
        - Complexidade de Espaço: O(b^(1+⌊C*/ε⌋)).

    Args:
        initial_state (PuzzleState): Estado inicial do puzzle.

    Returns:
        SearchResult: Resultado da busca com métricas.
    """
    result = SearchResult()
    result.algorithm_name = "Busca de Custo Uniforme"

    start_time = time.perf_counter()

    # Contador para desempate na fila de prioridade (FIFO order)
    counter = 0
    # Fila: (custo, contador, estado)
    frontier = [(initial_state.cost, counter, initial_state)]
    explored = set()
    # Mapa de melhor custo conhecido para cada estado na fronteira
    frontier_costs = {initial_state.board: initial_state.cost}
    nodes_generated = 0

    while frontier:
        cost, _, current = heapq.heappop(frontier)

        # Se já exploramos este estado com custo menor ou igual, pular
        if current.board in explored:
            continue

        explored.add(current.board)
        result.nodes_visited += 1

        if current.is_goal():
            result.found = True
            result.path = reconstruct_path(current)
            result.depth = current.depth
            result.nodes_generated = nodes_generated
            result.execution_time = time.perf_counter() - start_time
            return result

        for successor in current.get_successors():
            nodes_generated += 1

            if successor.board not in explored:
                old_cost = frontier_costs.get(successor.board, float("inf"))
                if successor.cost < old_cost:
                    counter += 1
                    heapq.heappush(frontier, (successor.cost, counter, successor))
                    frontier_costs[successor.board] = successor.cost

    result.nodes_generated = nodes_generated
    result.execution_time = time.perf_counter() - start_time
    return result


# =====================================================================
# 4. Greedy — Busca Gulosa
# =====================================================================

def greedy(initial_state, heuristic_func, heuristic_name=""):
    """
    Busca Gulosa (Greedy Best-First Search).

    Expande sempre o nó com menor valor heurístico h(n), ignorando o
    custo acumulado g(n). Tende a ser rápida, mas não garante otimalidade.

    Propriedades:
        - Completo: Não (pode entrar em loops sem detecção de estados visitados;
          esta implementação usa conjunto de explorados, então é completo para
          espaços finitos).
        - Ótimo: Não.
        - Complexidade de Tempo: O(b^m) no pior caso, mas geralmente melhor.
        - Complexidade de Espaço: O(b^m).

    Args:
        initial_state (PuzzleState): Estado inicial do puzzle.
        heuristic_func (callable): Função heurística h(state) -> int.
        heuristic_name (str): Nome da heurística para exibição.

    Returns:
        SearchResult: Resultado da busca com métricas.
    """
    result = SearchResult()
    result.algorithm_name = "Busca Gulosa"
    result.heuristic_name = heuristic_name

    start_time = time.perf_counter()

    counter = 0
    h_initial = heuristic_func(initial_state)
    frontier = [(h_initial, counter, initial_state)]
    explored = set()
    nodes_generated = 0

    while frontier:
        _, _, current = heapq.heappop(frontier)

        if current.board in explored:
            continue

        explored.add(current.board)
        result.nodes_visited += 1

        if current.is_goal():
            result.found = True
            result.path = reconstruct_path(current)
            result.depth = current.depth
            result.nodes_generated = nodes_generated
            result.execution_time = time.perf_counter() - start_time
            return result

        for successor in current.get_successors():
            nodes_generated += 1
            if successor.board not in explored:
                counter += 1
                h = heuristic_func(successor)
                heapq.heappush(frontier, (h, counter, successor))

    result.nodes_generated = nodes_generated
    result.execution_time = time.perf_counter() - start_time
    return result


# =====================================================================
# 5. A* — Busca A*
# =====================================================================

def a_star(initial_state, heuristic_func, heuristic_name=""):
    """
    Busca A* (A-Star Search).

    Combina o custo acumulado g(n) com a estimativa heurística h(n) para
    expandir o nó com menor f(n) = g(n) + h(n).

    Propriedades:
        - Completo: Sim.
        - Ótimo: Sim (quando h é admissível, ou seja, nunca superestima).
        - Complexidade de Tempo: O(b^d) no pior caso, mas geralmente
          muito menor com boa heurística.
        - Complexidade de Espaço: O(b^d) — mantém todos os nós na memória.

    Args:
        initial_state (PuzzleState): Estado inicial do puzzle.
        heuristic_func (callable): Função heurística h(state) -> int.
        heuristic_name (str): Nome da heurística para exibição.

    Returns:
        SearchResult: Resultado da busca com métricas.
    """
    result = SearchResult()
    result.algorithm_name = "A*"
    result.heuristic_name = heuristic_name

    start_time = time.perf_counter()

    counter = 0
    h_initial = heuristic_func(initial_state)
    f_initial = initial_state.cost + h_initial
    frontier = [(f_initial, counter, initial_state)]
    explored = set()
    # Melhor g(n) conhecido para estados na fronteira
    best_g = {initial_state.board: initial_state.cost}
    nodes_generated = 0

    while frontier:
        f, _, current = heapq.heappop(frontier)

        if current.board in explored:
            continue

        explored.add(current.board)
        result.nodes_visited += 1

        if current.is_goal():
            result.found = True
            result.path = reconstruct_path(current)
            result.depth = current.depth
            result.nodes_generated = nodes_generated
            result.execution_time = time.perf_counter() - start_time
            return result

        for successor in current.get_successors():
            nodes_generated += 1

            if successor.board not in explored:
                old_g = best_g.get(successor.board, float("inf"))
                if successor.cost < old_g:
                    best_g[successor.board] = successor.cost
                    counter += 1
                    h = heuristic_func(successor)
                    f_val = successor.cost + h
                    heapq.heappush(frontier, (f_val, counter, successor))

    result.nodes_generated = nodes_generated
    result.execution_time = time.perf_counter() - start_time
    return result


# =====================================================================
# Dicionário de algoritmos disponíveis
# =====================================================================

ALGORITHMS = {
    "bfs": {
        "func": bfs,
        "name": "BFS (Busca em Largura)",
        "uses_heuristic": False,
    },
    "dfs": {
        "func": dfs,
        "name": "DFS (Busca em Profundidade)",
        "uses_heuristic": False,
    },
    "ucs": {
        "func": uniform_cost,
        "name": "Busca de Custo Uniforme",
        "uses_heuristic": False,
    },
    "greedy": {
        "func": greedy,
        "name": "Busca Gulosa",
        "uses_heuristic": True,
    },
    "astar": {
        "func": a_star,
        "name": "A*",
        "uses_heuristic": True,
    },
}
