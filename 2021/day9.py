""" Advent of code solution """
import utils as ut
import cProfile

def parse(data):
    """ Parses input data into a friendlier format """
    return [[int(height) for height in line] for line in data]

def valid(x, y, grid):
    return x >= 0 and y >= 0 \
        and y < len(grid) and x < len(grid[0])

def part1(data):
    """ Solves part 1 """
    total = 0
    for y, line in enumerate(data):
        for x, height in enumerate(line):
            for offx, offy in (-1, 0), (1, 0), (0, -1), (0, 1):
                newx, newy = x + offx, y + offy
                if not valid(newx, newy, data):
                    continue
                if data[newy][newx] <= height:
                    break
            else:
                total += height + 1
    return total

def find_basin(x, y, data, travelled=set()):
    cur = data[y][x]
    if (x, y) in travelled or cur == 9:
        return 0
    travelled.add((x, y))

    return 1 + sum(find_basin(x+offx, y+offy, data)
                   for offx, offy in ((-1, 0), (1, 0), (0, -1), (0, 1))
                   if valid(x+offx, y+offy, data))

def part2(data):
    """ Solves part 2 """
    basins = []
    for y, line in enumerate(data):
        for x, height in enumerate(line):
            for offx, offy in (-1, 0), (1, 0), (0, -1), (0, 1):
                newx, newy = x + offx, y + offy
                if not valid(newx, newy, data):
                    continue
                if data[newy][newx] <= height:
                    break
            else:
                basins.append(find_basin(x, y, data))
    total = 1
    for basin in sorted(basins)[:-4:-1]:
        total *= basin
    return total

def solve(data):
    """ Solves advent of code day """
    res = [
        part1(data),
        part2(data)
    ]

    return res


if __name__ == '__main__':
    with cProfile.Profile() as pf:
        DATA = parse(ut.get_data(9))
        RESULT = solve(DATA)
        print(RESULT)
    pf.print_stats()
