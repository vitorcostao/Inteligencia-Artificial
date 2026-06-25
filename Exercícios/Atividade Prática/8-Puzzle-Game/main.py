"""
8-Puzzle Solver — Interface Interativa

Ponto de entrada do programa. Oferece um menu interativo para o usuário
inserir estados iniciais, selecionar algoritmos e heurísticas, e
visualizar a solução passo a passo.

Disciplina: Inteligência Artificial — PUC Minas
"""

import os
import sys

from puzzle_state import PuzzleState, GOAL_STATE, ACTION_ARROWS
from algorithms import ALGORITHMS, bfs, dfs, uniform_cost, greedy, a_star
from heuristics import HEURISTICS
from utils import (
    is_solvable,
    reconstruct_path,
    format_step,
    format_results,
    generate_solvable_state,
    validate_board_input,
    PREDEFINED_STATES,
)


# -----------------------------------------------------------------
# Constantes de exibição
# -----------------------------------------------------------------

HEADER = """
╔══════════════════════════════════════════╗
║           8-Puzzle Solver                ║
║                                          ║
║     Inteligência Artificial — PUC Minas  ║
╚══════════════════════════════════════════╝
"""

SEPARATOR = "─" * 44
GOAL_DISPLAY = PuzzleState(GOAL_STATE)


# -----------------------------------------------------------------
# Funções de interface
# -----------------------------------------------------------------

def clear_screen():
    """Limpa a tela do terminal."""
    os.system("cls" if os.name == "nt" else "clear")


def press_enter():
    """Pausa e espera o usuário pressionar Enter."""
    input("\n  Pressione Enter para continuar...")


def print_header():
    """Exibe o cabeçalho do programa."""
    print(HEADER)


def print_goal_state():
    """Exibe o estado objetivo."""
    print("Estado Objetivo:")
    print(GOAL_DISPLAY)
    print()


def get_board_manual():
    """
    Solicita ao usuário a entrada manual do tabuleiro.

    Returns:
        list[int] | None: Lista de 9 inteiros ou None se cancelado.
    """
    print("Insira o tabuleiro linha por linha (use 0 para o espaço vazio).")
    print("Exemplo: para o estado abaixo, digite '2 8 3' na primeira linha.")
    print("┌───┬───┬───┐")
    print("│ 2 │ 8 │ 3 │")
    print("├───┼───┼───┤")
    print("│ 1 │ 6 │ 4 │")
    print("├───┼───┼───┤")
    print("│ 7 │   │ 5 │")
    print("└───┴───┴───┘")
    print("(Digite 'v' para voltar ao menu)\n")

    board = []
    for row in range(3):
        while True:
            try:
                line = input(f"  Linha {row + 1}: ").strip()
                if line.lower() == "v":
                    return None
                values = list(map(int, line.split()))
                if len(values) != 3:
                    print("  Aviso: Insira exatamente 3 números separados por espaço.")
                    continue
                board.extend(values)
                break
            except ValueError:
                print("  Erro: Entrada inválida. Use apenas números inteiros.")

    return board


def select_initial_state():
    """
    Menu de seleção do estado inicial.

    Returns:
        PuzzleState | None: Estado inicial escolhido ou None para sair.
    """
    while True:
        print(SEPARATOR)
        print("Como deseja definir o estado inicial?\n")
        print("  [1] Inserir manualmente")
        print("  [2] Gerar estado aleatório (solucionável)")
        print("  [3] Escolher estado pré-definido")
        print("  [0] Sair")
        print()

        choice = input("  Escolha: ").strip()

        if choice == "0":
            return None

        elif choice == "1":
            print()
            board = get_board_manual()
            if board is None:
                continue

            valid, msg = validate_board_input(board)
            if not valid:
                print(f"\n  Erro: {msg}")
                press_enter()
                continue

            state = PuzzleState(board)
            print(f"\n  Estado inserido:")
            print(state)

            if not is_solvable(board):
                print("\n  Aviso: Este estado não é solucionável.")
                print("  O número de inversões é ímpar — impossível chegar ao objetivo.")
                press_enter()
                continue

            print("\n  Estado solucionável.")
            return state

        elif choice == "2":
            state = generate_solvable_state(num_moves=50)
            print(f"\n  Estado aleatório gerado:")
            print(state)
            print("\n  Garantidamente solucionável.")
            return state

        elif choice == "3":
            print()
            print("  Estados pré-definidos:\n")
            for i, preset in enumerate(PREDEFINED_STATES, 1):
                solvable_str = "(Solucionável)" if is_solvable(preset["board"]) else "(Insolucionável)"
                print(f"  [{i}] {preset['name']}  {solvable_str}")
                print(f"      {preset['description']}")
            print(f"\n  [0] Voltar")
            print()

            sub_choice = input("  Escolha: ").strip()
            if sub_choice == "0":
                continue

            try:
                idx = int(sub_choice) - 1
                if 0 <= idx < len(PREDEFINED_STATES):
                    preset = PREDEFINED_STATES[idx]
                    state = PuzzleState(preset["board"])
                    print(f"\n  {preset['name']}:")
                    print(state)

                    if not is_solvable(preset["board"]):
                        print("\n  Aviso: Este estado não é solucionável.")
                        print("  O programa detectará isso automaticamente.")

                    return state
                else:
                    print("  Erro: Opção inválida.")
            except ValueError:
                print("  Erro: Entrada inválida.")

        else:
            print("  Erro: Opção inválida.")


def select_algorithm():
    """
    Menu de seleção do algoritmo de busca.

    Returns:
        tuple | None: (chave_algoritmo, info_algoritmo) ou None para voltar.
    """
    print()
    print(SEPARATOR)
    print("Selecione o algoritmo de busca:\n")

    algo_list = list(ALGORITHMS.items())
    for i, (key, info) in enumerate(algo_list, 1):
        print(f"  [{i}] {info['name']}")

    print(f"\n  [0] Voltar")
    print()

    choice = input("  Escolha: ").strip()

    if choice == "0":
        return None

    try:
        idx = int(choice) - 1
        if 0 <= idx < len(algo_list):
            return algo_list[idx]
        else:
            print("  Erro: Opção inválida.")
            return None
    except ValueError:
        print("  Erro: Entrada inválida.")
        return None


def select_heuristic():
    """
    Menu de seleção da heurística.

    Returns:
        tuple | None: (chave_heurística, info_heurística) ou None para voltar.
    """
    print()
    print(SEPARATOR)
    print("Selecione a heurística:\n")

    heur_list = list(HEURISTICS.items())
    for i, (key, info) in enumerate(heur_list, 1):
        print(f"  [{i}] {info['name']}")

    print(f"\n  [0] Voltar")
    print()

    choice = input("  Escolha: ").strip()

    if choice == "0":
        return None

    try:
        idx = int(choice) - 1
        if 0 <= idx < len(heur_list):
            return heur_list[idx]
        else:
            print("  Erro: Opção inválida.")
            return None
    except ValueError:
        print("  Erro: Entrada inválida.")
        return None


def display_solution(result):
    """
    Exibe os resultados e, opcionalmente, o caminho passo a passo.

    Args:
        result (SearchResult): Resultado da busca.
    """
    print()
    print(format_results(result))

    if not result.found:
        print("\n  O algoritmo não encontrou uma solução.")
        if result.algorithm_name.startswith("DFS"):
            print("  Dica: O DFS pode não encontrar soluções além do limite de profundidade.")
        return

    print()
    show_path = input("  Exibir caminho passo a passo? (s/n): ").strip().lower()

    if show_path in ("s", "sim", "y", "yes"):
        print()
        total = len(result.path) - 1

        for i, state in enumerate(result.path):
            print(format_step(i, state, total))
            print()

            # Pausar a cada 5 passos para não sobrecarregar o terminal
            if i > 0 and i < len(result.path) - 1 and i % 5 == 0:
                cont = input("  ... continuar? (Enter/n): ").strip().lower()
                if cont == "n":
                    print(f"\n  (Pulando para o final — passo {total})")
                    print()
                    print(format_step(total, result.path[-1], total))
                    print()
                    break

        print("  Fim do caminho.")


def run_all_algorithms(initial_state):
    """
    Executa todos os algoritmos e exibe uma tabela comparativa.

    Args:
        initial_state (PuzzleState): Estado inicial do puzzle.
    """
    print()
    print(SEPARATOR)
    print("Executando TODOS os algoritmos...\n")

    if not is_solvable(initial_state.board):
        print("  Aviso: Estado insolucionável — todos os algoritmos irão falhar.\n")

    results = []

    # 1. BFS
    print("  Executando BFS...", end=" ", flush=True)
    r = bfs(initial_state)
    print(f"{'(Concluído)' if r.found else '(Falhou)'} ({r.execution_time:.4f}s)")
    results.append(("BFS", "-", r))

    # 2. DFS
    print("  Executando DFS...", end=" ", flush=True)
    r = dfs(initial_state)
    print(f"{'(Concluído)' if r.found else '(Falhou)'} ({r.execution_time:.4f}s)")
    results.append(("DFS", "-", r))

    # 3. Custo Uniforme
    print("  Executando Custo Uniforme...", end=" ", flush=True)
    r = uniform_cost(initial_state)
    print(f"{'(Concluído)' if r.found else '(Falhou)'} ({r.execution_time:.4f}s)")
    results.append(("Custo Uniforme", "-", r))

    # 4-6. Gulosa com cada heurística
    for hkey, hinfo in HEURISTICS.items():
        label = f"Gulosa ({hinfo['short']})"
        print(f"  Executando {label}...", end=" ", flush=True)
        r = greedy(initial_state, hinfo["func"], hinfo["name"])
        print(f"{'(Concluído)' if r.found else '(Falhou)'} ({r.execution_time:.4f}s)")
        results.append((f"Gulosa", hinfo["short"], r))

    # 7-9. A* com cada heurística
    for hkey, hinfo in HEURISTICS.items():
        label = f"A* ({hinfo['short']})"
        print(f"  Executando {label}...", end=" ", flush=True)
        r = a_star(initial_state, hinfo["func"], hinfo["name"])
        print(f"{'(Concluído)' if r.found else '(Falhou)'} ({r.execution_time:.4f}s)")
        results.append(("A*", hinfo["short"], r))

    # Exibir tabela comparativa
    print()
    print("━" * 90)
    print("TABELA COMPARATIVA DE RESULTADOS")
    print("━" * 90)
    print(
        f"{'Algoritmo':<20} {'Heurística':<15} {'Solução?':<10} "
        f"{'Movim.':<8} {'Visitados':<12} {'Gerados':<12} {'Tempo (s)':<12}"
    )
    print("─" * 90)

    for algo_name, heur_name, r in results:
        found_str = "Sim" if r.found else "Não"
        depth_str = str(r.depth) if r.found else "-"
        print(
            f"{algo_name:<20} {heur_name:<15} {found_str:<10} "
            f"{depth_str:<8} {r.nodes_visited:<12} {r.nodes_generated:<12} "
            f"{r.execution_time:<12.6f}"
        )

    print("━" * 90)

    # Análise rápida
    solved = [(name, heur, r) for name, heur, r in results if r.found]
    if solved:
        fastest = min(solved, key=lambda x: x[2].execution_time)
        fewest_visited = min(solved, key=lambda x: x[2].nodes_visited)
        shortest = min(solved, key=lambda x: x[2].depth)

        print()
        print("Análise Rápida:")
        h_str = f" ({fastest[1]})" if fastest[1] != "-" else ""
        print(f"  Mais rápido:         {fastest[0]}{h_str} — {fastest[2].execution_time:.6f}s")
        h_str = f" ({fewest_visited[1]})" if fewest_visited[1] != "-" else ""
        print(f"  Menos nós visitados: {fewest_visited[0]}{h_str} — {fewest_visited[2].nodes_visited} nós")
        h_str = f" ({shortest[1]})" if shortest[1] != "-" else ""
        print(f"  Menor caminho:       {shortest[0]}{h_str} — {shortest[2].depth} movimentos")


# -----------------------------------------------------------------
# Loop principal
# -----------------------------------------------------------------

def main():
    """Função principal — loop interativo do programa."""
    clear_screen()
    print_header()
    print_goal_state()

    while True:
        # 1. Selecionar estado inicial
        initial_state = select_initial_state()
        if initial_state is None:
            print("\n  Encerrando o programa. Até logo!\n")
            sys.exit(0)

        # Verificar se já é o objetivo
        if initial_state.is_goal():
            print("\n  O estado inserido já é o estado objetivo. Nenhuma busca necessária.")
            press_enter()
            continue

        # 2. Menu de algoritmo
        while True:
            print()
            print(SEPARATOR)
            print("O que deseja fazer com este estado?\n")
            print(f"  [1] Executar um algoritmo específico")
            print(f"  [2] Executar TODOS os algoritmos (tabela comparativa)")
            print(f"  [0] Escolher outro estado inicial")
            print()

            mode = input("  Escolha: ").strip()

            if mode == "0":
                break

            elif mode == "2":
                run_all_algorithms(initial_state)
                press_enter()
                continue

            elif mode == "1":
                algo = select_algorithm()
                if algo is None:
                    continue

                algo_key, algo_info = algo

                # 3. Selecionar heurística (se necessário)
                if algo_info["uses_heuristic"]:
                    heur = select_heuristic()
                    if heur is None:
                        continue
                    heur_key, heur_info = heur
                    heuristic_func = heur_info["func"]
                    heuristic_name = heur_info["name"]
                else:
                    heuristic_func = None
                    heuristic_name = None

                # 4. Executar algoritmo
                print()
                print(f"  Resolvendo com {algo_info['name']}", end="")
                if heuristic_name:
                    print(f" + {heuristic_name}", end="")
                print("...\n")

                if algo_info["uses_heuristic"]:
                    result = algo_info["func"](initial_state, heuristic_func, heuristic_name)
                else:
                    result = algo_info["func"](initial_state)

                # 5. Exibir resultados
                display_solution(result)
                press_enter()

            else:
                print("  Erro: Opção inválida.")


if __name__ == "__main__":
    main()
