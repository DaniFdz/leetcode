import random

class RandomizedSet:
    def __init__(self):
        self.l = list()
        self.m = set()


    def insert(self, val: int) -> bool:
        if val in self.m:
            return False

        self.m.add(val)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.m:
            return False
        self.m.remove(val)

        return True

    def getRandom(self) -> int:
        n = ""
        while not n in self.m:
            n = random.choice(self.l)

        return n


if __name__ == "__main__":
    s = RandomizedSet()
    assert s.insert(1)
    assert not s.insert(1)
    assert s.remove(1)
    assert not s.remove(1)
    assert s.insert(2)
    assert s.getRandom() == 2
