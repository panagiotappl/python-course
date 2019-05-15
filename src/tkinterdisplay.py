import tkinter as tk

from particle import Particle


class TKinterDisplay:

    def __init__(self):
        master = tk.Tk()
        canvas = tk.Canvas(master, width=600, height=400, bg='black')
        canvas.pack()
        self._canvas = canvas
        self._p = Particle(30, (canvas.winfo_height() / 2, canvas.winfo_width() / 2), (80.0, 150.0))
        self._fps = 60

    @property
    def bounding_box(self):
        return 0, self._canvas.winfo_width(), 0, self._canvas.winfo_height()

    def draw(self):
        r, x, y, canvas = self._p.r, self._p.x, self._p.y, self._canvas
        canvas.create_oval(x-r, y+r, x+r, y-r, outline="yellow")

    def update(self, dt):
        p, canvas = self._p, self._canvas

        canvas.delete(tk.ALL)
        p.move(dt)
        p.bounce(self.bounding_box)
        self.draw()

        canvas.update()
        canvas.after(17, self.update, 1 / self._fps)

    def go(self):
        self.update(0)
        tk.mainloop()
