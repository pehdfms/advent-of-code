""" Advent of code solution """
import utils as ut
import cProfile

def parse(data):
    """ Parses input data into a friendlier format """
    parsed = [[]]
    folds = []

    folding = False
    for line in data:
        if line == "":
            folding = True
            continue
        if folding:
            line = line.replace("fold along ", "")
            k, v = line.split("=")
            folds.append((k != "x", int(v)))
        else:
            coord = ut.lmap(int, line.split(","))
            parsed[0].append(coord)
    parsed.append(folds)
    return parsed

def part1(data):
    """ Solves part 1 """
    points, folds = data
    coord, pos = folds[0]
    for point in points:
        if point[coord] >= pos:
            point[coord] = 2*pos - point[coord]
    return len(set(tuple(point) for point in points))

def part2(data):
    """ Solves part 2 """
    points, folds = data
    for fold in folds:
        coord, pos = fold
        for point in points:
            if point[coord] >= pos:
                point[coord] = 2*pos - point[coord]
    maxx = max(x[0] for x in points)
    maxy = max(y[1] for y in points)
    grid = [[" " for _ in range(maxx+1)] for _ in range(maxy+1)]
    for point in points:
        grid[point[1]][point[0]] = "#"
    for line in grid:
        print("".join(line))

def solve(data):
    """ Solves advent of code day """
    res = [
        part1(data),
        part2(data)
    ]

    return res


if __name__ == '__main__':
    with cProfile.Profile() as pf:
        DATA = parse(ut.get_data(13))
        RESULT = solve(DATA)
        print(RESULT)
    pf.print_stats()
