""" Advent of code solution """
import utils as ut
import cProfile
import numpy as np

def parse(data):
    """ Parses input data into a friendlier format """
    lst = [0 for _ in range(9)]
    for fish in ut.lmap(int, data[0].split(",")):
        lst[fish] += 1
    return lst

def matsimulate(data, days):
    transformation = np.matrix([[0, 1, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 1, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 1, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 1, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 1, 0, 0],
                               [1, 0, 0, 0, 0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 1],
                               [1, 0, 0, 0, 0, 0, 0, 0, 0],
                               ], dtype=np.double) ** days
    return int(np.sum(transformation * np.matrix(data, dtype=np.double).T))

def simulate(data, days):
    prev = data.copy()
    for day in range(days):
        current = [0 for _ in range(9)]
        buffer = 0
        for idx, fish_count in enumerate(prev):
            if idx == 0:
                buffer = fish_count
            else:
                current[idx-1] = fish_count
        current[6] += buffer
        current[8] += buffer
        prev = current
    return sum(prev)

def part1(data):
    """ Solves part 1 """
    return simulate(data, 80)

def part2(data):
    """ Solves part 2 """
    return simulate(data, 256)

def solve(data):
    """ Solves advent of code day """
    res = [
        part1(data),
        part2(data)
    ]

    return res


if __name__ == '__main__':
    with cProfile.Profile() as pf:
        DATA = parse(ut.get_data(6))
        RESULT = solve(DATA)
        print(RESULT)
    pf.print_stats()
