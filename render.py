import tkinter as tk

rows, cols = 0, 0
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


def draw_grid(canvas):

    for col in range(cols + 1):
        x = col * side_length
        canvas.create_line(x, 0, x, (rows * side_length), fill='black')

    for row in range(rows + 1):
        y = row * side_length
        canvas.create_line(0, y, (cols * side_length), y, fill='black')


def draw_state(canvas, state):
    for i in range(len(state[0])):
        x = i * side_length
        for j in range(len(state)):
            y = j * side_length
            if state[j][i] == 1:
                canvas.create_rectangle(
                    x, y, x + side_length, y + side_length, fill='black')
    canvas.pack()


def print_state(state):
    # os.system('cls')
    print('-'*(len(state[0]) + 2))
    for row in state:
        print('|', end='')
        for element in row:
            print('#', end='') if element == 1 else print(' ', end='')
        print('|')
    print('-'*(len(state[0]) + 2))


if __name__ == '__main__':
    state = load_board_state('shapes/gosper_glider_gun.txt')
    print(f'rows={rows}, cols={cols}')
    print_state(state)
    window = tk.Tk()

    canvas_width = cols * side_length
    canvas_height = rows * side_length

    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
    canvas.pack()

    draw_grid(canvas)
    draw_state(canvas, state)

    window.mainloop()
