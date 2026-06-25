"""
Módulo de heurísticas para o 8-Puzzle.

Implementa três heurísticas admissíveis para uso com os algoritmos
A* e Busca Gulosa:
    h1 — Peças fora do lugar (Hamming Distance)
    h2 — Distância de Manhattan
    h3 — Manhattan + Conflitos Lineares (Linear Conflict)
"""

from puzzle_state import GOAL_STATE, GOAL_POSITIONS


# -----------------------------------------------------------------
# Tabelas pré-computadas para desempenho
# -----------------------------------------------------------------

# Distância Manhattan de cada peça em cada posição para a posição objetivo
# _MANHATTAN_TABLE[peça][posição_atual] = distância
_MANHATTAN_TABLE = {}
for piece in range(1, 9):  # Peças 1-8
    goal_idx = GOAL_POSITIONS[piece]
    goal_row, goal_col = divmod(goal_idx, 3)
    _MANHATTAN_TABLE[piece] = {}
    for pos in range(9):
        cur_row, cur_col = divmod(pos, 3)
        _MANHATTAN_TABLE[piece][pos] = abs(cur_row - goal_row) + abs(cur_col - goal_col)


# -----------------------------------------------------------------
# Heurística 1: Peças fora do lugar (Hamming Distance)
# -----------------------------------------------------------------

def hamming(state):
    """
    Conta o número de peças que não estão na posição correta.
    O espaço vazio (0) não é contado.

    Admissível: Sim. Cada peça fora do lugar precisa de no mínimo 1 movimento,
    portanto h1(n) ≤ h*(n).

    Args:
        state (PuzzleState): Estado atual do puzzle.

    Returns:
        int: Número de peças fora do lugar.
    """
    count = 0
    board = state.board
    for i in range(9):
        if board[i] != 0 and board[i] != GOAL_STATE[i]:
            count += 1
    return count


# -----------------------------------------------------------------
# Heurística 2: Distância de Manhattan
# -----------------------------------------------------------------

def manhattan(state):
    """
    Soma das distâncias Manhattan (|Δlinha| + |Δcoluna|) de cada peça
    até sua posição objetivo.

    Admissível: Sim. A distância Manhattan de cada peça é o número mínimo
    de movimentos necessários para levá-la à posição correta, ignorando
    todas as outras peças. Portanto h2(n) ≤ h*(n).

    Args:
        state (PuzzleState): Estado atual do puzzle.

    Returns:
        int: Soma total das distâncias Manhattan.
    """
    total = 0
    board = state.board
    for pos in range(9):
        piece = board[pos]
        if piece != 0:
            total += _MANHATTAN_TABLE[piece][pos]
    return total


# -----------------------------------------------------------------
# Heurística 3: Manhattan + Conflitos Lineares
# -----------------------------------------------------------------

def _count_linear_conflicts(board):
    """
    Conta o número de conflitos lineares no tabuleiro.

    Um conflito linear ocorre quando duas peças estão na mesma linha (ou coluna)
    que suas posições objetivo, mas em ordem invertida. Cada conflito requer
    pelo menos 2 movimentos adicionais para ser resolvido.

    Args:
        board (tuple): Tabuleiro representado como tupla de 9 inteiros.

    Returns:
        int: Número total de conflitos lineares.
    """
    conflicts = 0

    # Verificar conflitos em cada linha
    for row in range(3):
        # Coletar peças nesta linha que pertencem a esta mesma linha no objetivo
        pieces_in_row = []
        for col in range(3):
            pos = row * 3 + col
            piece = board[pos]
            if piece != 0:
                goal_row = GOAL_POSITIONS[piece] // 3
                if goal_row == row:
                    pieces_in_row.append((col, GOAL_POSITIONS[piece] % 3, piece))

        # Verificar pares de peças para conflitos
        for i in range(len(pieces_in_row)):
            for j in range(i + 1, len(pieces_in_row)):
                cur_col_i, goal_col_i, _ = pieces_in_row[i]
                cur_col_j, goal_col_j, _ = pieces_in_row[j]
                # Conflito: a peça i está à direita de j, mas deveria estar à esquerda
                if (cur_col_i > cur_col_j and goal_col_i < goal_col_j) or \
                   (cur_col_i < cur_col_j and goal_col_i > goal_col_j):
                    conflicts += 1

    # Verificar conflitos em cada coluna
    for col in range(3):
        pieces_in_col = []
        for row in range(3):
            pos = row * 3 + col
            piece = board[pos]
            if piece != 0:
                goal_col = GOAL_POSITIONS[piece] % 3
                if goal_col == col:
                    pieces_in_col.append((row, GOAL_POSITIONS[piece] // 3, piece))

        for i in range(len(pieces_in_col)):
            for j in range(i + 1, len(pieces_in_col)):
                cur_row_i, goal_row_i, _ = pieces_in_col[i]
                cur_row_j, goal_row_j, _ = pieces_in_col[j]
                if (cur_row_i > cur_row_j and goal_row_i < goal_row_j) or \
                   (cur_row_i < cur_row_j and goal_row_i > goal_row_j):
                    conflicts += 1

    return conflicts


def manhattan_linear_conflict(state):
    """
    Manhattan + Conflitos Lineares.

    Igual à distância de Manhattan mais 2 vezes o número de conflitos
    lineares. Esta heurística domina Manhattan (h3 ≥ h2 para todos os
    estados), mantendo a admissibilidade.

    Admissível: Sim. Cada conflito linear requer pelo menos 2 movimentos
    extras além do mínimo estimado por Manhattan, pois uma das peças em
    conflito deve sair da linha/coluna e voltar.

    Args:
        state (PuzzleState): Estado atual do puzzle.

    Returns:
        int: Manhattan + 2 × conflitos lineares.
    """
    return manhattan(state) + 2 * _count_linear_conflicts(state.board)


# -----------------------------------------------------------------
# Dicionário de heurísticas disponíveis
# -----------------------------------------------------------------

HEURISTICS = {
    "hamming": {
        "func": hamming,
        "name": "Peças fora do lugar (Hamming)",
        "short": "Hamming",
    },
    "manhattan": {
        "func": manhattan,
        "name": "Distância de Manhattan",
        "short": "Manhattan",
    },
    "manhattan_lc": {
        "func": manhattan_linear_conflict,
        "name": "Manhattan + Conflitos Lineares",
        "short": "Manhattan+LC",
    },
}
