""" Advent of code solution """
import utils as ut
import cProfile

from collections import defaultdict

def parse(data):
    """ Parses input data into a friendlier format """
    parser = lambda l: tuple(map(int, l))
    return [parser(line.replace(" -> ", ",").split(",")) for line in data]

def minmax(a, b):
    return (a, b) if a < b else (b, a)

def mark_line(pipe, grid):
    x1, y1, x2, y2 = pipe
    if x1 == x2 or y1 == y2:
        minx, maxx = minmax(x1, x2)
        miny, maxy = minmax(y1, y2)
        for x in range(minx, maxx + 1):
            for y in range(miny, maxy + 1):
                grid[(x, y)] += 1

def part1(data):
    """ Solves part 1 """
    grid = defaultdict(int)
    for pipe in data:
        mark_line(pipe, grid)

    return sum(1 for count in grid.values() if count > 1)

def part2(data):
    """ Solves part 2 """
    grid = defaultdict(int)
    for pipe in data:
        mark_line(pipe, grid)
        x1, y1, x2, y2 = pipe
        if x1 != x2 and y1 != y2:
            xoff = 1 if x1 <= x2 else - 1
            yoff = 1 if y1 <= y2 else - 1
            y = y1
            for x in range(x1, x2+xoff, xoff):
                grid[(x, y)] += 1
                y += yoff
    return sum(1 for count in grid.values() if count > 1)

def solve(data):
    """ Solves advent of code day """
    res = [
        part1(data),
        part2(data)
    ]

    return res


if __name__ == '__main__':
    with cProfile.Profile() as pf:
        DATA = parse(ut.get_data(5))
        RESULT = solve(DATA)
        print(RESULT)
    pf.print_stats()
