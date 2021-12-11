""" Advent of code solution """
import utils as ut
import cProfile
from collections import defaultdict

def parse(data):
    """ Parses input data into a friendlier format """
    res = []
    for diagnosis in data:
        tests, results = diagnosis.split(" | ")
        res.append(([s for s in tests.split(" ") if len(s) not in (2, 7)], results.split(" ")))
    return res

def part1(data):
    """ Solves part 1 """
    return sum(1 for _, results in data for result in results if len(result) in (2, 4, 3, 7))

def done(d):
    for value in d.values():
        if len(value) not in (1, 2):
            return False
    return True

def clean(d):
    confirmed = set()
    dubs = {
    }

    while not done(d):
        for key in d:
            val = d[key]
            if len(val) == 1:
                confirmed.add(list(val)[0])
            elif len(val) == 2:
                s = "".join(sorted(val))
                if s not in dubs:
                    dubs[s] = 1
                else:
                    dubs[s] = 2
                    confirmed = confirmed.union(set(s))
            else:
                d[key] = d[key].difference(confirmed)

def part2(data):
    """ Solves part 2 """
    possible_translations = {
        2: ["cf"],
        3: ["acf"],
        4: ["bcdf"],
        5: ["acdeg", "acdfg", "abdfg"],
        6: ["abcefg", "abdefg", "abcdfg"],
        7: ["abcdefg"],
    }

    translation_table = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9
    }

    total_sum = 0
    for tests, results in data:
        bits = ""
        for result in results:
            if len(result) not in (2, 3, 4, 7):
                break
            bits += str(translation_table[possible_translations[len(result)][0]])
        else:
            total_sum += int(bits)
            continue

        segment_translations = {segment:set(possible_translations[7][0]) for segment in possible_translations[7][0]}
        for datum in tests:
            length = len(datum)
            for segment in datum:
                possible_translation = set("".join(s for s in possible_translations[length]))
                segment_translations[segment] = segment_translations[segment].intersection(possible_translation)
        clean(segment_translations)

        dubs = []
        for key, val in segment_translations.items():
            if len(val) != 2:
                continue
            for dub in dubs:
                if len(dub) == 2 and val == dub[1]:
                    dub[0] += str(key)
                    break
            else:
                dubs.append([key, val])
        for datum in tests:
            for dub in dubs:
                if len(set(datum).intersection(dub[0])) in (0, 2):
                    continue
                found, notfound = dub[0] if datum.find(dub[0][0]) != -1 else dub[0][::-1]
                possible = set("".join(c for c in s if c in dub[1]) for s in possible_translations[len(datum)])
                possible = set(s for s in possible if len(s) == 1)
                if len(possible) == 1:
                    other = list(dub[1].difference(possible))[0]
                    result = list(possible)[0]
                    segment_translations[found] = result
                    segment_translations[notfound] = other
        segment_translations = {k:list(v)[0] for k, v in segment_translations.items()}
        bits = ""
        for result in results:
            s = "".join((sorted("".join(segment_translations[c] for c in result))))
            bits += str(translation_table[s])
        total_sum += int(bits)
    return total_sum

def solve(data):
    """ Solves advent of code day """
    res = [
        part1(data),
        part2(data)
    ]

    return res


if __name__ == '__main__':
    with cProfile.Profile() as pf:
        DATA = parse(ut.get_data(8))
        RESULT = solve(DATA)
        print(RESULT)
    pf.print_stats()
