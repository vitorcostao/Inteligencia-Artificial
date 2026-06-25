"""
Módulo de representação do estado do 8-Puzzle.

Define a classe PuzzleState que encapsula o tabuleiro 3x3,
a geração de estados sucessores e a verificação do objetivo.
"""


# Estado objetivo:
# 1 2 3
# 8 _ 4
# 7 6 5
GOAL_STATE = (1, 2, 3, 8, 0, 4, 7, 6, 5)

# Mapeamento de posição objetivo para cada peça (peça -> índice no GOAL_STATE)
GOAL_POSITIONS = {}
for _i, _val in enumerate(GOAL_STATE):
    GOAL_POSITIONS[_val] = _i

# Movimentos possíveis: nome, delta na posição linear
# Para um tabuleiro 3x3 linearizado:
#   0 1 2
#   3 4 5
#   6 7 8
# Cima = -3, Baixo = +3, Esquerda = -1, Direita = +1
MOVES = {
    "cima":     -3,
    "baixo":    +3,
    "esquerda": -1,
    "direita":  +1,
}

# Movimentos válidos para cada posição do espaço vazio
# Pré-computados para evitar verificações repetidas de bordas
VALID_MOVES = {
    0: ["baixo", "direita"],
    1: ["baixo", "esquerda", "direita"],
    2: ["baixo", "esquerda"],
    3: ["cima", "baixo", "direita"],
    4: ["cima", "baixo", "esquerda", "direita"],
    5: ["cima", "baixo", "esquerda"],
    6: ["cima", "direita"],
    7: ["cima", "esquerda", "direita"],
    8: ["cima", "esquerda"],
}

# Nomes legíveis para exibição das ações
ACTION_ARROWS = {
    "cima":     "↑ Cima",
    "baixo":    "↓ Baixo",
    "esquerda": "← Esquerda",
    "direita":  "→ Direita",
}


class PuzzleState:
    """
    Representa um estado do 8-Puzzle.

    Atributos:
        board (tuple): Tupla de 9 inteiros representando o tabuleiro.
                       0 representa o espaço vazio.
        parent (PuzzleState | None): Estado pai na árvore de busca.
        action (str | None): Ação que gerou este estado a partir do pai.
        depth (int): Profundidade na árvore de busca.
        cost (int): Custo acumulado g(n) do caminho até este estado.
    """

    __slots__ = ("board", "parent", "action", "depth", "cost", "_blank_pos", "_hash")

    def __init__(self, board, parent=None, action=None, depth=0, cost=0):
        self.board = tuple(board) if not isinstance(board, tuple) else board
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = cost
        self._blank_pos = self.board.index(0)
        self._hash = hash(self.board)

    @property
    def blank_pos(self):
        """Retorna a posição (índice linear) do espaço vazio."""
        return self._blank_pos

    def is_goal(self):
        """Verifica se este estado é o estado objetivo."""
        return self.board == GOAL_STATE

    def get_successors(self):
        """
        Gera todos os estados sucessores válidos.

        Retorna:
            list[PuzzleState]: Lista de estados alcançáveis a partir deste.
        """
        successors = []
        blank = self._blank_pos

        for move_name in VALID_MOVES[blank]:
            new_blank = blank + MOVES[move_name]

            # Cria novo tabuleiro trocando o vazio com a peça adjacente
            new_board = list(self.board)
            new_board[blank], new_board[new_blank] = new_board[new_blank], new_board[blank]

            successor = PuzzleState(
                board=tuple(new_board),
                parent=self,
                action=move_name,
                depth=self.depth + 1,
                cost=self.cost + 1,
            )
            successors.append(successor)

        return successors

    def __eq__(self, other):
        if not isinstance(other, PuzzleState):
            return NotImplemented
        return self.board == other.board

    def __hash__(self):
        return self._hash

    def __lt__(self, other):
        """Comparação para desempate em filas de prioridade."""
        return self.cost < other.cost

    def __str__(self):
        """Representação visual do tabuleiro 3x3."""
        lines = []
        lines.append("┌───┬───┬───┐")
        for row in range(3):
            cells = []
            for col in range(3):
                val = self.board[row * 3 + col]
                if val == 0:
                    cells.append("   ")
                else:
                    cells.append(f" {val} ")
            lines.append("│" + "│".join(cells) + "│")
            if row < 2:
                lines.append("├───┼───┼───┤")
        lines.append("└───┴───┴───┘")
        return "\n".join(lines)

    def __repr__(self):
        return f"PuzzleState({self.board})"
