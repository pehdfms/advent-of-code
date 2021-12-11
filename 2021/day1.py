""" Advent of code solution """
import utils as ut
import cProfile

def parse(data):
    """ Parses input data into a friendlier format """
    parser = int
    return ut.lmap(parser, data)

def sliding(data, size):
    prev = sum(data[:size])
    count = 0
    for i in range(1, len(data) - size + 1):
        current = prev - data[i - 1] + data[i + size - 1]
        if (current > prev):
            count += 1
        prev = current
    return count

def part1(data):
    """ Solves part 1 """
    return sliding(data, 1)

def part2(data):
    """ Solves part 2 """
    return sliding(data, 3)

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
