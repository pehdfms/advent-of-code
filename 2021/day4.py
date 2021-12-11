""" Advent of code solution """
import utils as ut
import cProfile

class Board:
    marked = set()
    def __init__(self, number_board):
        self.number_board = number_board

    def mark(self, number):
        self.marked.add(number)

    def get_unmarked(self):
        return [number for row in self.number_board for number in row if number not in self.marked]

    def check_solve(self):
        height, width = 5, 5
        horizontal = lambda i, j: self.number_board[i][j]
        vertical   = lambda i, j: self.number_board[j][i]

        def check_line(line):
            for i in range(height):
                for j in range(width):
                    if line(i, j) not in self.marked:
                        break
                else:
                    return True
            return False
        return check_line(horizontal) or check_line(vertical)

def boardify(data):
    boards = []
    current = []
    for line in data:
        if (line == ""):
            boards.append(Board(current))
            current = []
            continue

        current.append([int(num) for num in line.split()])
    boards.append(Board(current))
    return boards

def parse(data):
    """ Parses input data into a friendlier format """
    return [int(number) for number in data[0].split(',')], boardify(data[2:])

def part1(data):
    """ Solves part 1 """
    called_numbers, boards = data
    for number in called_numbers:
        for board in boards:
            board.mark(number)
            for row in board.number_board:
                if (board.check_solve()):
                    return sum(board.get_unmarked()) * number
    return data

def part2(data):
    """ Solves part 2 """
    called_numbers, boards = data
    for number in called_numbers:
        for board in boards:
            board.mark(number)
        for board in boards:
            for row in board.number_board:
                if (board.check_solve()):
                    if len(boards) == 1:
                        return sum(board.get_unmarked()) * number
                    boards.remove(board)
                    break

def solve(data):
    """ Solves advent of code day """
    res = [
        part1(data),
        part2(data)
    ]

    return res


if __name__ == '__main__':
    with cProfile.Profile() as pf:
        DATA = parse(ut.get_data(4))
        RESULT = solve(DATA)
        print(RESULT)
    pf.print_stats()
