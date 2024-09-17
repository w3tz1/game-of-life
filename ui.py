import tkinter as tk
import render

running = True
rows = 30
columns = 60
cell_width = 20


def main():
    window = tk.Tk()
    window.rowconfigure([0, 1], minsize=50, weight=1)
    window.columnconfigure(0, minsize=50, weight=1)
    # window.geometry('800x600')
    frame_canvas = tk.Frame()
    frame_ui = tk.Frame()

    canvas = tk.Canvas(master=frame_canvas,
                       width=columns * cell_width,
                       height=rows*cell_width,
                       background='green')

    btn_run = tk.Button(master=frame_ui, text='Run',
                        width=100)
    btn_run.grid(row=0, column=0, sticky='nsew')

    frame_canvas.pack()
    frame_ui.pack()
    canvas.pack()

    render.draw_grid(canvas, rows, columns, cell_width)

    while running:
        window.update_idletasks()
        window.update()


if __name__ == '__main__':
    main()
