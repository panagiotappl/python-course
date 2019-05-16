import tkinter as tk

from display import Display


class TKinterDisplay(Display):

    def __init__(self):
        master = tk.Tk()
        canvas = tk.Canvas(master, width=600, height=400, bg='black')
        canvas.pack()
        self._canvas = canvas
        self._particles = []
        self._fps = 60

    @property
    def bounding_box(self):
        return 0, self._canvas.winfo_width(), 0, self._canvas.winfo_height()

    def draw(self):
        p = self._particles
        for particle in p:
            r, x, y, canvas = particle.r, particle.x, particle.y, self._canvas
            canvas.create_oval(x-r, y+r, x+r, y-r, outline=f'#{particle.colour.as_rgb_f()}')

    def update(self, dt):
        particles, canvas = self._particles, self._canvas

        canvas.delete(tk.ALL)

        self.draw()
        for particle in particles:
            particle.move(dt)
            particle.bounce(self.bounding_box)

        canvas.update()
        canvas.after(17, self.update, 1 / self._fps)

    def go(self):
        self.update(0)
        tk.mainloop()
