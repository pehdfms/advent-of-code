""" Advent of code solution """
import utils as ut
import cProfile

def parse(data):
    """ Parses input data into a friendlier format """
    return "".join(ut.lmap(binary, data[0]))

def binary(c):
    return bin(int(c, 16)).replace("0b", "").zfill(4)

def get_literal_packet(data, start):
    finish = False
    packet = ""
    length = len(data)
    while start < length:
        finish = data[start] == '0'

        for _ in range(4):
            start += 1
            packet += data[start]
        start += 1

        if finish:
            break

    return packet, start

def p1_parse_packets(data, start):
    version = int(data[start:start+3], 2)
    dtype = int(data[start+3: start+6], 2)

    current = start+6
    if dtype == 4:
        packet, current = get_literal_packet(data, current)
        return version, current
    else:
        lentype = int(data[current])
        current += 1

        if lentype == 0:
            op_len = int(data[current:current+15], 2)
            current += 15
            end_point = op_len + current
            while current < end_point:
                packet_version, current = p1_parse_packets(data, current)
                version += packet_version
        else:
            op_len = int(data[current:current+11], 2)
            current += 11
            for _ in range(op_len):
                packet_version, current = p1_parse_packets(data, current)
                version += packet_version

    return version, current

def p2_parse_packets(data, start):
    version = int(data[start:start+3], 2)
    dtype = int(data[start+3: start+6], 2)

    current = start+6
    if dtype == 4:
        packet, current = get_literal_packet(data, current)
        return int(packet, 2), version, current
    else:
        lentype = int(data[current])
        current += 1

        packet_values = []
        if lentype == 0:
            op_len = int(data[current:current+15], 2)
            current += 15
            end_point = op_len + current
            while current < end_point:
                value, packet_version, current = p2_parse_packets(data, current)
                packet_values.append(value)
                version += packet_version
        else:
            op_len = int(data[current:current+11], 2)
            current += 11
            for _ in range(op_len):
                value, packet_version, current = p2_parse_packets(data, current)
                packet_values.append(value)
                version += packet_version

        table = {
            0: "sum",
            1: "prod",
            2: "min",
            3: "max",
            5: "greater",
            6: "lesser",
            7: "equals",
        }

        if dtype == 0:
            res = sum(packet_values), version, current
        if dtype == 1:
            res = ut.product(packet_values), version, current
        if dtype == 2:
            res = min(packet_values), version, current
        if dtype == 3:
            res = max(packet_values), version, current
        if dtype == 5:
            res = int(packet_values[0] > packet_values[1]), version, current
        if dtype == 6:
            res = int(packet_values[0] < packet_values[1]), version, current
        if dtype == 7:
            res = int(packet_values[0] == packet_values[1]), version, current

        print(table[dtype], packet_values, res[0])


    return value, version, current

def part1(data):
    """ Solves part 1 """
    return p1_parse_packets(data, 0)[0]

def part2(data):
    """ Solves part 2 """
    return p2_parse_packets(data, 0)[0]
    pass

def solve(data):
    """ Solves advent of code day """
    res = [
        part1(data),
        part2(data)
    ]

    return res


if __name__ == '__main__':
    with cProfile.Profile() as pf:
        DATA = parse(ut.get_data(16))
        RESULT = solve(DATA)
        print(RESULT)
    pf.print_stats()
