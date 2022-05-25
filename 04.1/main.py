import os

def list_cleaner(bingo_list: list[str]) -> list:
    drawn_numbers = bingo_list[0].rstrip("\n")
    drawn_numbers = drawn_numbers.split(",")
    drawn_numbers = [int(x) for x in drawn_numbers]


    boards = bingo_list[2:]
    splitted_boards = []

    board = []
    for line in boards:
        if line != "\n":
            line = line.rstrip("\n")
            line = line.split(" ")
            line = [int(x) for x in line if x]
            board.append(line)
        else:
            splitted_boards.append(board)
            board = []
    
    return drawn_numbers, splitted_boards

def transpose_board(board: list):
    transposed = [x[:] for x in board]

    for i, line in enumerate(board):
        for n, number in enumerate(line):
            transposed[n][i] = number
    
    return transposed


def check_winner(board):
    for line in board:
        bool_line = [True if x == "x" else False for x in line]
        if all(bool_line):
            return True
    
    transposed = transpose_board(board)
    for line in transposed:
        bool_line = [True if x == "x" else False for x in line]
        if all(bool_line):
            return True
    
    return False



def bingo(drawn_numbers, boards):
    for d in drawn_numbers:
        for i, board in enumerate(boards):
            for j, line in enumerate(board):
                for k, number in enumerate(line):
                    if d == number:
                        boards[i][j][k] = "x"
                        wins = check_winner(boards[i])
                        if wins:
                            print(boards[i])
                            board_score = 0
                            for line in boards[i]:
                                for number in line:
                                    try:
                                        board_score += number
                                    except Exception:
                                        continue
                            print(f"Board score: {board_score}")
                            final_score = board_score * d
                            return final_score
                                

if __name__ == "__main__":

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, "input"), "r") as f:
        lines = f.readlines()

    drawn_numbers, boards = list_cleaner(lines)
    final_score = bingo(drawn_numbers, boards)
    print(f"Final score: {final_score}")