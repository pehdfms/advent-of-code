""" Advent of code solution """
import utils as ut
import cProfile
from collections import defaultdict

def parse(data):
    """ Parses input data into a friendlier format """
    template, _ = data[0], data[1]
    transformations = {}
    for line in data[2:]:
        rule, result = line.split(" -> ")
        transformations[rule] = result
    return [template, transformations]

def step(counts, transform):
    newcounts = defaultdict(int)
    for k, v in counts.items():
        if k not in transform:
            continue
        newc = transform[k]
        newcounts[k[0] + newc] += v
        newcounts[newc + k[1]] += v
    return newcounts

def get_counts(template):
    counts = defaultdict(int)
    for i in range(len(template)-1):
        counts[template[i] + template[i+1]] += 1
    return counts

def get_result(counts):
    result = defaultdict(int)
    for k, v in counts.items():
        result[k[0]] += v
        result[k[1]] += v
    for k, v in result.items():
        result[k] = result[k] // 2 if result[k] % 2 == 0 else (result[k] + 1) // 2

    return max(result.values()) - min(result.values())

def part1(data):
    """ Solves part 1 """
    template, transform = data
    counts = get_counts(template)
    for _ in range(10):
        counts = step(counts, transform)
    return get_result(counts)

def part2(data):
    """ Solves part 2 """
    template, transform = data
    counts = get_counts(template)
    for _ in range(40):
        counts = step(counts, transform)

    return get_result(counts)

def solve(data):
    """ Solves advent of code day """
    res = [
        part1(data),
        part2(data)
    ]

    return res


if __name__ == '__main__':
    DATA = parse(ut.get_data(14))
    with cProfile.Profile() as pf:
        RESULT = solve(DATA)
        print(RESULT)
    pf.print_stats()
