""" Advent of code solution """
import utils as ut
import cProfile

class Submarine:
    forward = 0
    depth = 0
    aim = 0

def parse(data):
    """ Parses input data into a friendlier format """
    parser = lambda l: (l[0], int(l[1]))
    return [parser(val.split()) for val in data]

def part1(data):
    """ Solves part 1 """
    sub = Submarine()
    for op, val in data:
        if (op == "forward"):
            sub.forward += val
        elif (op == "down"):
            sub.depth += val
        else:
            sub.depth -= val
    return sub.depth * sub.forward

def part2(data):
    """ Solves part 2 """
    sub = Submarine()
    for op, val in data:
        if (op == "forward"):
            sub.forward += val
            sub.depth += sub.aim * val
        elif (op == "down"):
            sub.aim += val
        else:
            sub.aim -= val
    return sub.depth * sub.forward

def solve(data):
    """ Solves advent of code day """
    res = [
        part1(data),
        part2(data)
    ]

    return res


if __name__ == '__main__':
    with cProfile.Profile() as pf:
        DATA = parse(ut.get_data(2))
        RESULT = solve(DATA)
        print(RESULT)
    pf.print_stats()
