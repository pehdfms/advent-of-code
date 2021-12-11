""" Advent of code solution """
import utils as ut
import cProfile
import math

def parse(data):
    """ Parses input data into a friendlier format """
    parser = int
    return sorted(list(map(parser, data[0].split(","))))

def median(lst):
    # Assumes sorted list
    length = len(lst)
    if length == 0:
        return 0
    if length % 2 == 0:
        return (lst[length // 2] + lst[length // 2 + 1]) // 2
    return lst[length // 2]

def mean(lst):
    return math.ceil(sum(lst) / len(lst))

def fuel_function(cost, anchor):
    def dist(origin):
        return cost(abs(origin - anchor))
    return dist

def part1(data):
    """ Solves part 1 """
    min_fuel = float("inf")
    for anchor in range(data[0], median(data) + 1):
        find_fuel = fuel_function(ut.identity, anchor)
        fuel_required = sum(map(find_fuel, data))
        min_fuel = min(fuel_required, min_fuel)

    return min_fuel

def part2(data):
    """ Solves part 2 """
    min_fuel = float("inf")
    for anchor in range(data[0], mean(data) + 1):
        cost = lambda dist: int(dist / 2 * (1 + dist))
        find_fuel = fuel_function(cost, anchor)
        fuel_required = sum(map(find_fuel, data))
        min_fuel = min(fuel_required, min_fuel)

    return min_fuel

def solve(data):
    """ Solves advent of code day """
    res = [
        part1(data),
        part2(data)
    ]

    return res


if __name__ == '__main__':
    with cProfile.Profile() as pf:
        DATA = parse(ut.get_data(7))
        RESULT = solve(DATA)
        print(RESULT)
    pf.print_stats()
