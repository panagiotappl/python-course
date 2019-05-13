import tkinter as tk

master = tk.Tk()

w = tk.Canvas(master, width=600, height=400, bg='black')
w.pack()

x, y = w.winfo_height() / 2, w.winfo_width() / 2
vx, vy = 80.0, 150.0

diameter = 60
particle = w.create_oval(x, y, diameter, diameter, outline='yellow')
min_x, min_y = 0, 0


def update(dt):
    global x, y, vx, vy
    old_x, old_y = x, y
    x += vx*dt
    y += vy*dt

    if x + diameter > w.winfo_width():
        x = w.winfo_width() - diameter
        vx = - vx

    if x < min_x:
        x = min_x
        vx = - vx

    if y + diameter > w.winfo_height():
        y = w.winfo_height() - diameter
        vy = - vy

    if y < min_y:
        y = min_y
        vy = - vy

    w.move(particle, x-old_x, y-old_y)
    w.update()
    w.after(17, update, 1/diameter)


update(0)

tk.mainloop()
