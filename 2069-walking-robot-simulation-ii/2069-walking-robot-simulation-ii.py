class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.perimeter = 2 * (width - 1) + 2 * (height - 1)
        self.pos = 0
        self.moved = False

    def step(self, num: int) -> None:
        self.pos = (self.pos + num) % self.perimeter
        self.moved = True

    def getPos(self) -> list[int]:
        if self.pos <= self.w - 1:
            return [self.pos, 0]
        elif self.pos <= self.w + self.h - 2:
            return [self.w - 1, self.pos - (self.w - 1)]
        elif self.pos <= 2 * self.w + self.h - 3:
            return [(self.w - 1) - (self.pos - (self.w + self.h - 2)), self.h - 1]
        else:
            return [0, (self.h - 1) - (self.pos - (2 * self.w + self.h - 3))]

    def getDir(self) -> str:
        if self.pos == 0:
            return "South" if self.moved else "East"
        elif self.pos <= self.w - 1:
            return "East"
        elif self.pos <= self.w + self.h - 2:
            return "North"
        elif self.pos <= 2 * self.w + self.h - 3:
            return "West"
        else:
            return "South"










            # elif self.pos < 2 * self.w + self.h - 3:  # Fails when pos hits the exact corner