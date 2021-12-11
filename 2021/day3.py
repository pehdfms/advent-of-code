""" Advent of code solution """
import utils as ut
import cProfile

def parse(data):
    """ Parses input data into a friendlier format """
    parser = ut.identity
    return ut.lmap(parser, data)

def sint(obj):
    """ Shitty hack to get 0's and 1's out of booleans """
    return str(int(obj))

def bin(n):
    """ Returns number read from string in binary """
    return int(n, 2)

def get_bit_count(data, bit):
    lst = [0, 0]
    for line in data:
        lst[int(line[bit])] += 1
    return lst

def get_bit_counts(data):
    # Yeah I could have just reused get_bit_count
    # but then I would have to read the entire array multiple times out of order
    # it would still be the same O(nm) runtime but with a fuckton of cache misses
    lst = [[0, 0] for _ in range(len(data[0]))]
    for line in data:
        for idx, val in enumerate(line):
            lst[idx][int(val)] += 1
    return lst

def rec_get_rating(data, cond_op, bit_pos):
    if (len(data) == 1):
        return bin(data[0])
    lst = get_bit_count(data, bit_pos)
    cond = cond_op(lst[0], lst[1])
    data = ut.lfilter(lambda s: s[bit_pos] == sint(cond), data)
    return rec_get_rating(data, cond_op, bit_pos + 1)

def get_rating(data, cond_op):
    return rec_get_rating(data, cond_op, 0)

def part1(data):
    """ Solves part 1 """
    def negate(s):
        return (sint(x == '0') for x in s)

    lst = get_bit_counts(data)
    gamma = "".join(sint(val[0] > val[1]) for val in lst)
    epsilon = "".join(negate(gamma))

    return bin(gamma) * bin(epsilon)

def part2(data):
    """ Solves part 2 """
    oxg = get_rating(data, lambda a, b: a <= b)
    co2 = get_rating(data, lambda a, b: a > b)

    return oxg * co2

def solve(data):
    """ Solves advent of code day """
    res = [
        part1(data),
        part2(data)
    ]

    return res


if __name__ == '__main__':
    with cProfile.Profile() as pf:
        DATA = parse(ut.get_data(3))
        RESULT = solve(DATA)
        print(RESULT)
    pf.print_stats()
