"""
Módulo de funções utilitárias para o 8-Puzzle.

Inclui verificação de solucionabilidade, reconstrução de caminho,
formatação do tabuleiro e geração de estados aleatórios.
"""

import random

from puzzle_state import PuzzleState, GOAL_STATE, ACTION_ARROWS


def is_solvable(board):
    """
    Verifica se um estado do 8-Puzzle é solucionável em relação ao
    estado objetivo (1,2,3,8,0,4,7,6,5).

    A solucionabilidade depende da paridade das inversões. Como o
    estado objetivo não segue a ordem linear padrão (1..8), contamos
    inversões relativas à ordem das peças no objetivo.

    Método: atribuímos a cada peça um "rank" baseado na posição em que
    ela aparece no estado objetivo. Depois contamos inversões desses
    ranks na configuração atual (ignorando o vazio).

    Se o número de inversões do estado atual tem a mesma paridade que
    o número de inversões do estado objetivo (que é 0, paridade par),
    então é solucionável.

    Args:
        board (tuple|list): Tabuleiro como sequência de 9 inteiros (0 = vazio).

    Returns:
        bool: True se o estado é solucionável, False caso contrário.
    """
    # O estado objetivo linearizado: (1,2,3,8,0,4,7,6,5)
    # Posições no objetivo: pos 0->1, pos 1->2, pos 2->3, pos 3->8,
    #                       pos 4->0, pos 5->4, pos 6->7, pos 7->6, pos 8->5
    # Rank de cada peça = posição no GOAL_STATE (excluindo o vazio)
    # Peças no goal em ordem de posição: 1(0), 2(1), 3(2), 8(3), 4(5), 7(6), 6(7), 5(8)
    # Ranks: peça -> índice na sequência do goal (sem o vazio)
    goal_order = [val for val in GOAL_STATE if val != 0]  # [1,2,3,8,4,7,6,5]
    rank = {}
    for idx, val in enumerate(goal_order):
        rank[val] = idx

    # Extrair ranks das peças na configuração atual (sem o vazio)
    current_ranks = [rank[p] for p in board if p != 0]

    # Contar inversões nos ranks
    inversions = 0
    for i in range(len(current_ranks)):
        for j in range(i + 1, len(current_ranks)):
            if current_ranks[i] > current_ranks[j]:
                inversions += 1

    return inversions % 2 == 0


def reconstruct_path(state):
    """
    Reconstrói o caminho do estado inicial até o estado dado.

    Args:
        state (PuzzleState): Estado final (objetivo).

    Returns:
        list[PuzzleState]: Lista ordenada de estados do inicial ao final.
    """
    path = []
    current = state
    while current is not None:
        path.append(current)
        current = current.parent
    path.reverse()
    return path


def format_step(step_num, state, total_steps=None):
    """
    Formata um passo da solução para exibição.

    Args:
        step_num (int): Número do passo (0 = inicial).
        state (PuzzleState): Estado neste passo.
        total_steps (int, optional): Total de passos na solução.

    Returns:
        str: Representação formatada do passo.
    """
    lines = []

    if step_num == 0:
        header = "Passo 0 (Estado Inicial)"
    else:
        action_str = ACTION_ARROWS.get(state.action, state.action)
        header = f"Passo {step_num} ({action_str})"

    if total_steps is not None:
        header += f"  [{step_num}/{total_steps}]"

    lines.append(header)
    lines.append(str(state))

    return "\n".join(lines)


def format_results(result):
    """
    Formata os resultados de uma execução de algoritmo.

    Args:
        result (SearchResult): Resultado retornado pelo algoritmo.

    Returns:
        str: String formatada com as métricas.
    """
    lines = []
    lines.append("━" * 44)

    if result.found:
        lines.append("Solução encontrada.")
    else:
        lines.append("Solução não encontrada.")

    lines.append("━" * 44)
    lines.append(f"  Algoritmo:       {result.algorithm_name}")

    if result.heuristic_name:
        lines.append(f"  Heurística:      {result.heuristic_name}")

    lines.append(f"  Movimentos:      {result.depth}")
    lines.append(f"  Nós visitados:   {result.nodes_visited}")
    lines.append(f"  Nós gerados:     {result.nodes_generated}")
    lines.append(f"  Profundidade:    {result.depth}")
    lines.append(f"  Tempo:           {result.execution_time:.6f}s")
    lines.append("━" * 44)

    return "\n".join(lines)


def generate_solvable_state(num_moves=30):
    """
    Gera um estado aleatório solucionável fazendo movimentos
    aleatórios a partir do estado objetivo.

    Args:
        num_moves (int): Número de movimentos aleatórios a fazer.

    Returns:
        PuzzleState: Estado aleatório garantidamente solucionável.
    """
    state = PuzzleState(GOAL_STATE)
    visited = {state.board}

    for _ in range(num_moves):
        successors = state.get_successors()
        # Preferir estados não visitados para gerar mais variação
        unvisited = [s for s in successors if s.board not in visited]
        if unvisited:
            state = random.choice(unvisited)
        else:
            state = random.choice(successors)
        visited.add(state.board)

    # Retornar como estado limpo (sem pai/ação/custo)
    return PuzzleState(state.board)


def validate_board_input(board):
    """
    Valida se a entrada do tabuleiro é válida.

    Args:
        board (list): Lista de inteiros representando o tabuleiro.

    Returns:
        tuple: (válido: bool, mensagem: str)
    """
    if len(board) != 9:
        return False, "O tabuleiro deve ter exatamente 9 valores."

    expected = set(range(9))
    actual = set(board)

    if actual != expected:
        missing = expected - actual
        extra = actual - expected
        msg_parts = []
        if missing:
            msg_parts.append(f"Valores faltando: {sorted(missing)}")
        if extra:
            msg_parts.append(f"Valores inválidos: {sorted(extra)}")
        return False, " | ".join(msg_parts)

    return True, "Tabuleiro válido."


# -----------------------------------------------------------------
# Estados pré-definidos para teste
# -----------------------------------------------------------------

PREDEFINED_STATES = [
    {
        "name": "Fácil (5 movimentos)",
        "board": (2, 0, 3, 1, 6, 4, 8, 7, 5),
        "description": "Requer apenas 5 movimentos para resolver.",
    },
    {
        "name": "Médio (15 movimentos)",
        "board": (7, 0, 1, 6, 8, 3, 2, 4, 5),
        "description": "Dificuldade intermediária — 15 movimentos.",
    },
    {
        "name": "Difícil (22 movimentos)",
        "board": (3, 6, 8, 7, 0, 2, 4, 1, 5),
        "description": "Requer 22 movimentos para resolver.",
    },
    {
        "name": "Muito Difícil (26 movimentos)",
        "board": (5, 7, 6, 4, 0, 3, 2, 1, 8),
        "description": "Um dos estados mais difíceis — 26 movimentos.",
    },
    {
        "name": "Insolucionável",
        "board": (1, 2, 3, 8, 0, 4, 7, 5, 6),
        "description": "Estado sem solução (inversões ímpares).",
    },
]
