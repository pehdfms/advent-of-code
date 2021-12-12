""" Advent of code solution """
import utils as ut
import cProfile
from collections import defaultdict

class Node:
    def __init__(self, name, adjacents):
        this.name = name
        this.adjacents = adjacents

def parse(data):
    """ Parses input data into a friendlier format """
    paths = defaultdict(list)
    for line in data:
        k, v = line.split("-")
        paths[k] = paths[k] + [v]
        paths[v] = paths[v] + [k]
    return paths

def traverse_p1(data, root, visited):
    if root in visited or root not in data:
        return 0
    if root == "end":
        return 1
    if root.islower():
        visited.add(root)
    return sum(traverse_p1(data, path, set(visited)) for path in data[root])

def traverse_p2(data, root, visited, visitedTwice):
    if root not in data:
        return 0
    if visited[root] == 1 and (visitedTwice or root == "start") or visited[root] > 1:
        return 0
    if root == "end":
        return 1
    if root.islower():
        visited[root] += 1
        visitedTwice |= visited[root] >= 2
    if visitedTwice:
        return sum(traverse_p1(data, path, set(key for key in visited.keys() if visited[key] != 0)) for path in data[root])
    return sum(traverse_p2(data, path, visited.copy(), visitedTwice) for path in data[root])

def part1(data):
    """ Solves part 1 """
    return traverse_p1(data, "start", set())

def part2(data):
    """ Solves part 2 """
    return traverse_p2(data, "start", defaultdict(int), False)

def solve(data):
    """ Solves advent of code day """
    res = [
        part1(data),
        part2(data)
    ]

    return res


if __name__ == '__main__':
    with cProfile.Profile() as pf:
        DATA = parse(ut.get_data(12))
        RESULT = solve(DATA)
        print(RESULT)
    pf.print_stats()
