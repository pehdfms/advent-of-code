""" Advent of code solution """
import utils as ut
import cProfile

def parse(data):
    """ Parses input data into a friendlier format """
    return [[int(n) for n in line] for line in data]

def flash(x, y, data, visited):
    data[y][x] = 0
    visited.add((x, y))

    length = len(data)

    adjacents = (x-1, y), (x-1, y-1), (x-1, y+1), (x, y-1), \
                (x, y+1), (x+1, y-1), (x+1, y+1), (x+1, y)

    for adjacent in adjacents:
        newx, newy = adjacent
        if (newx, newy) in visited:
            continue

        if newx < 0 or newx >= length or \
           newy < 0 or newy >= length:
               continue

        if data[newy][newx] >= 9:
            flash(newx, newy, data, visited)
            continue
        data[newy][newx] += 1

def part1(data):
    """ Solves part 1 """
    ylen, xlen = 10, 10
    zeros = 0
    for iteration in range(100):
        visited = set()
        for y in range(ylen):
            for x in range(xlen):
                val = data[y][x]
                if (x, y) in visited:
                    continue
                if val >= 9:
                    flash(x, y, data, visited)
                    continue
                data[y][x] += 1
        zeros += sum([1 for line in data for n in line if n == 0])
    return zeros

def part2(data):
    """ Solves part 2 """
    ylen, xlen = 10, 10
    zeros = 0
    for iteration in range(1000):
        visited = set()
        for y in range(ylen):
            for x in range(xlen):
                val = data[y][x]
                if (x, y) in visited:
                    continue
                if val >= 9:
                    flash(x, y, data, visited)
                    continue
                data[y][x] += 1
        if all(n == 0 for line in data for n in line):
            return iteration + 101

def solve(data):
    """ Solves advent of code day """
    res = [
        part1(data),
        part2(data)
    ]

    return res


if __name__ == '__main__':
    with cProfile.Profile() as pf:
        DATA = parse(ut.get_data(11))
        RESULT = solve(DATA)
        print(RESULT)
    pf.print_stats()
