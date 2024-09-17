import game_of_life as gol
import tkinter as tk
import time

# rows, cols = 0, 0
side_length = 20


def load_board_state(path):
    global rows, cols
    with open(path, 'r') as file:
        lines = file.readlines()
        state = [list(line.strip()) for line in lines]
    state = [[int(element) for element in row] for row in state]
    rows = len(state)
    cols = len(state[0])
    return state


def draw_grid(canvas, rows, cols, width):

    for col in range(cols + 1):
        x = col * width
        canvas.create_line(x, 0, x, (rows * width), fill='grey')

    for row in range(rows + 1):
        y = row * width
        canvas.create_line(0, y, (cols * width), y, fill='grey')


def draw_state(canvas, state, rows, cols, width):
    canvas.delete('all')
    draw_grid(canvas, rows, cols, width)
    for i in range(len(state[0])):
        x = i * width
        for j in range(len(state)):
            y = j * width
            if state[j][i] == 1:
                canvas.create_rectangle(
                    x, y, x + width, y + width, fill='black')
    canvas.pack()


# if __name__ == '__main__':
#     path = 'shapes/biblockpuffer.txt'
#     # state = load_board_state('shapes/gosper_glider_gun.txt')
#
#     window = tk.Tk()
#
#     game = gol.game(file=path)
#     rows = len(game.state)
#     cols = len(game.state[0])
#
#     canvas_width = cols * side_length
#     canvas_height = rows * side_length
#
#     canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
#     canvas.pack()
#
#     while (True):
#         # print_state(game.state)
#         draw_state(canvas, game.state)
#         window.update_idletasks()
#         window.update()
#         game.get_next_state()
#         time.sleep(0.01)
