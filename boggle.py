from typing import List, Dict, Tuple, Set
import sys

BOARD_SIZE = 4

Position = Tuple[int, int]
Board = Dict[Position, str]

def build_board(board_str: str) -> Board:
    return {(i // BOARD_SIZE, i % BOARD_SIZE): board_str[i] for i in range(BOARD_SIZE * BOARD_SIZE)}

def neighbours(position: Position) -> List[Position]:
    row, col = position
    return [
        (row + rd, col + cd)
        for rd in (-1, 0, 1)
        for cd in (-1, 0, 1)
        if not (rd == 0 and cd == 0)
        if 0 <= row + rd < BOARD_SIZE and 0 <= col + cd < BOARD_SIZE
    ]

def board_has_word(board: Board, word: str) -> bool:
    def dfs(position: Position, suffix: str, visited: Set[Position]) -> bool:
        if not suffix:
            return True

        for next_position in neighbours(position):
            if not next_position in visited and board.get(next_position) == suffix[0]:
                if dfs(next_position, suffix[1:], visited | {next_position}):
                    return True

        return False

    for start_position, char in board.items():
        if char == word[0]:
            if dfs(start_position, word[1:], {start_position}):
                return True

    return False

def solve(board_str: str, dictionary: List[str]) -> List[str]:
    board = build_board(board_str)
    letters = board.values()
    candidates = [w for w in dictionary if w[0] in letters]
    return [w for w in candidates if board_has_word(board, w)]

def main():
    if len(sys.argv) != 3:
        return print("Usage: python3 boggle.py <board> <dictionary>")

    board_str = sys.argv[1].strip().lower()
    if len(board_str) != BOARD_SIZE * BOARD_SIZE:
        return print(f"Error: board string must contain {BOARD_SIZE * BOARD_SIZE} characters")

    dictionary_path = sys.argv[2].strip()
    with open(dictionary_path, 'r') as f:
        dictionary = [w.strip().lower() for w in f if len(w.strip()) > 2 and w.strip().isalpha() and w.strip().islower()]

    results = solve(board_str, dictionary)
    print(", ".join(results))


if __name__ == "__main__":
    main()
