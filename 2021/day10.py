""" Advent of code solution """
import utils as ut
import cProfile

def parse(data):
    """ Parses input data into a friendlier format """
    parser = ut.identity
    return list(map(parser, data))

class Consumer:
    def __init__(self, s):
        self.pointer = 0
        self.s = s
        self.error_char = ""
        self.expected_closer = []

    def get_closer(self, c):
        closer = {
            "(": ")",
            "[": "]",
            "{": "}",
            "<": ">"
        }

        return closer[c]

    def consume_group(self, pointer=0):
        length = len(self.s)
        while True:
            if pointer >= length:
                return -1

            start = self.s[pointer]
            if start not in "([{<":
                return pointer
            pointer += 1

            expected = self.get_closer(start)
            self.expected_closer.append(expected)

            while True:
                newpointer = self.consume_group(pointer=pointer)
                if newpointer == -1:
                    return -1
                if pointer == newpointer:
                    break
                pointer = newpointer

            got = self.s[pointer]
            if got != expected:
                self.error_char = got
                return -1
            self.expected_closer.pop(-1)
            pointer += 1

    def get_points(self):
        points_table = {
            "" : 0,
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137
        }
        return points_table[self.error_char]

    def get_incomplete_points(self):
        points_table = {
            ")": 1,
            "]": 2,
            "}": 3,
            ">": 4
        }

        score = 0
        while self.expected_closer:
            score *= 5
            score += points_table[self.expected_closer.pop(-1)]
        return score

def part1(data):
    """ Solves part 1 """
    score = 0
    for line in data:
        consumer = Consumer(line)
        consumer.consume_group()
        score += consumer.get_points()
    return score

def part2(data):
    """ Solves part 2 """
    scores = []
    for line in data:
        consumer = Consumer(line)
        consumer.consume_group()
        if (consumer.get_points()):
            continue
        scores.append(consumer.get_incomplete_points())
    return sorted(scores)[len(scores)//2]

def solve(data):
    """ Solves advent of code day """
    res = [
        part1(data),
        part2(data)
    ]

    return res


if __name__ == '__main__':
    with cProfile.Profile() as pf:
        DATA = parse(ut.get_data(10))
        RESULT = solve(DATA)
        print(RESULT)
    pf.print_stats()
