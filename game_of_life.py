import os
import random


class game_of_life:
    def __init__(self, width=None, height=None, file=None):
        if width is not None and height is not None:
            self.width = width
            self.height = height
        elif file is not None:
            self.file = file
            self.load_board_state()

    def dead_state(self):
        return [[0 for _ in range(self.width)]
                for _ in range(self.height)]

    def random_state(self):
        return [[random.randint(0, 1) for _ in range(self.width)]
                for _ in range(self.height)]

    def set_state(self, state):
        self.state = state

    def load_board_state(self):
        with open(self.file, 'r') as file:
            lines = file.readlines()
            self.state = [list(line.strip()) for line in lines]
        self.state = [[int(element) for element in row] for row in self.state]
        self.width = len(self.state[0])
        self.height = len(self.state)

    def get_next_state(self):
        next_state = self.dead_state()
        neighbors = self.dead_state()
        for x in range(self.height):
            for y in range(self.width):
                count = self.count_neighbors(x, y)
                neighbors[x][y] = count
                next_state[x][y] = self.evolve_cell(self.state[x][y], count)
        self.state = next_state

    def print_state(self):
        os.system('cls')
        print('-'*(len(self.state[0]) + 2))
        for row in self.state:
            print('|', end='')
            for element in row:
                print('#', end='') if element == 1 else print(' ', end='')
            print('|')
        print('-'*(len(self.state[0]) + 2))

    def render(self):
        os.system('cls')
        for row in self.state:
            print(''.join('#' if cell == 1 else ' ' for cell in row))

    def count_neighbors(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                nr = x + i
                nc = y + j
                if 0 <= nr < len(self.state) and 0 <= nc < len(self.state[0]):
                    count = count + self.state[nr][nc]
        return count

    def evolve_cell(self, cell, neighbors):
        result = 0
        if cell == 1:
            if neighbors == 0 or neighbors == 1:
                result = 0
            if neighbors == 2 or neighbors == 3:
                result = 1
            if neighbors > 3:
                result = 0
        elif cell == 0:
            if neighbors == 3:
                result = 1
        return result
