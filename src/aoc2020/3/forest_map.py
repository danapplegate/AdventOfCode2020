class ForestMap:
    def __init__(self, input_lines):
        self._map = [[char for char in row.strip()] for row in input_lines]
        self.width = len(self._map[0])
        self.height = len(self._map)

    def __str__(self):
        return "\n".join(["".join(row) for row in self._map])

    def get(self, x, y):
        x = x % self.width
        return self._map[y][x]

    def num_trees(self, right, down):
        num_trees = 0
        x, y = right, down
        while y < self.height:
            char = self.get(x, y)
            print(f"Encountered {char} at {x}, {y}")
            if char == "#":
                num_trees += 1
            x += right
            y += down
        return num_trees
