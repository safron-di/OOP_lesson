class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left



if __name__ == '__main__':
    pt1 = Point(1, 2)
    pt2 = Point(10, 20)
    print(pt1.MAX_COORD)
    pt1.set_bound(-100)
    print(pt1.__dict__)
    print(pt2.__dict__)
    print(Point.__dict__)
