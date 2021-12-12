""" Advent of code solution """
import utils as ut
import cProfile

def parse(data):
    """ Parses input data into a friendlier format """
    parser = ut.identity
    return list(map(parser, data))

def part1(data):
    """ Solves part 1 """
    print(data)
    pass

def part2(data):
    """ Solves part 2 """
    pass

def solve(data):
    """ Solves advent of code day """
    res = [
        part1(data),
        part2(data)
    ]

    return res


if __name__ == '__main__':
    with cProfile.Profile() as pf:
        DATA = parse(ut.get_data(1))
        RESULT = solve(DATA)
        print(RESULT)
    pf.print_stats()
