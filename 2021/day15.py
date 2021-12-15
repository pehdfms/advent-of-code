""" Advent of code solution """
import utils as ut
import cProfile
import heapq
import copy

def parse(data):
    """ Parses input data into a friendlier format """
    return [[int(n) for n in line] for line in data]

def neighbors(grid, current, lengthx, lengthy):
    x, y = current
    return (adjacent for adjacent in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)) \
           if adjacent[0] >= 0 and adjacent[0] < lengthx and
              adjacent[1] >= 0 and adjacent[1] < lengthy
           )

def dijkstra(grid):
    dist = {}
    prev = {}

    queue = []
    entry_finder = {}
    REMOVED = '<r>'
    counter = 0

    def add_coord(coord, priority):
        if coord in entry_finder:
            remove_coord(coord)
        entry = [priority, counter, coord]
        entry_finder[coord] = entry
        heapq.heappush(queue, entry)

    def remove_coord(coord):
        entry = entry_finder.pop(coord)
        entry[-1] = REMOVED

    def pop_coord():
        while queue:
            priority, count, coord = heapq.heappop(queue)
            if coord is not REMOVED:
                del entry_finder[coord]
                return coord

    dist[(0, 0)] = 0
    lengthy, lengthx = len(grid), len(grid[0])
    for y in range(lengthy):
        for x in range(lengthx):
            if (x, y) != (0, 0):
                dist[(x, y)] = 10**10
                prev[(x, y)] = None
            add_coord((x, y), dist[(x, y)])
            counter += 1

    while queue:
        current = pop_coord()
        if current == (lengthx-1, lengthy-1):
            return dist[current]
        for neighbor in neighbors(grid, current, lengthx, lengthy):
            alt = dist[current] + grid[neighbor[1]][neighbor[0]]
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = current
                add_coord(neighbor, alt)
                counter += 1

def part1(data):
    """ Solves part 1 """
    result = dijkstra(data)
    return result

def part2(data):
    """ Solves part 2 """
    realgrid = copy.deepcopy(data)
    def inc(x, y):
        def increment(n):
            res = n+x+y
            if res > 9:
                return res % 9
            return res
        return increment

    for y in range(4):
        curinc = inc(0, y+1)
        current_list = [ut.lmap(curinc, line) for line in data]
        for x in range(4):
            curinc = inc(x+1, y+1)
            x_list = [ut.lmap(curinc, line) for line in data]
            for idx, line in enumerate(current_list):
                line.extend(x_list[idx])
        realgrid.extend(current_list)

    for x in range(4):
        curinc = inc(x+1, 0)
        x_list = [ut.lmap(curinc, line) for line in data]
        for idx in range(len(data)):
            realgrid[idx].extend(x_list[idx])
    return dijkstra(realgrid)

def solve(data):
    """ Solves advent of code day """
    res = [
        part1(data),
        part2(data)
    ]

    return res


if __name__ == '__main__':
    DATA = parse(ut.get_data(15))
    with cProfile.Profile() as pf:
        RESULT = solve(DATA)
        print(RESULT)
    pf.print_stats()
