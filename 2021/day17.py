""" Advent of code solution """
import utils as ut
import cProfile

def parse(data):
    """ Parses input data into a friendlier format """
    parsed = data[0].replace("target area: ", "").replace("y=", "").replace("x=", "")
    x, y = parsed.split(", ")

    xmin, xmax = ut.lmap(int, x.split(".."))
    ymin, ymax = ut.lmap(int, y.split(".."))

    return ((xmin, xmax), (ymin, ymax))

class Probe:
    def __init__(self, velx, vely, boundaries):
        self.velx = velx
        self.vely = vely
        self.boundaries = boundaries

        self.maxy = float("-inf")
        self.x = 0
        self.y = 0

    def step(self):
        self.x += self.velx
        self.y += self.vely

        self.maxy = max(self.maxy, self.y)

        self.velx -= 1 if self.velx > 0 else -1 if self.velx < 0 else 0
        self.vely -= 1

    def check_within_bounds(self):
        xbound, ybound = self.boundaries

        xmin, xmax = xbound
        ymin, ymax = ybound

        return xmin <= self.x <= xmax and \
               ymin <= self.y <= ymax

    def possible(self):
        xbound, ybound = self.boundaries

        xmin, xmax = xbound
        ymin, ymax = ybound

        return not (\
               self.y < ymin or \
               (self.x < 0 and xmin > self.x) or \
               (self.x > 0 and xmax < self.x) or \
               self.check_within_bounds())

def part1(data):
    """ Solves part 1 """
    maxy = float("-inf")
    (xmin, xmax), (ymin, ymax) = data
    for y in range(ymin - 1, -ymin):
        for x in range(-100, xmax+2):
            test = Probe(x, y, data)
            while test.possible():
                test.step()
            if test.check_within_bounds():
                maxy = max(maxy, test.maxy)
    return maxy

def part2(data):
    """ Solves part 2 """
    count = 0
    (xmin, xmax), (ymin, ymax) = data
    for y in range(ymin - 1, -ymin):
        for x in range(xmax+2):
            test = Probe(x, y, data)
            while test.possible():
                test.step()
            if test.check_within_bounds():
                count += 1
    return count

def solve(data):
    """ Solves advent of code day """
    res = [
        part1(data),
        part2(data)
    ]

    return res


if __name__ == '__main__':
    with cProfile.Profile() as pf:
        DATA = parse(ut.get_data(17))
        RESULT = solve(DATA)
        print(RESULT)
    pf.print_stats()
