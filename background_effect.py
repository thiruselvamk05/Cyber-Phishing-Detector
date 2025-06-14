import tkinter as tk
import random

class AnimatedBackground(tk.Canvas):
    def __init__(self, master, width=800, height=600, dots=150, **kwargs):
        super().__init__(master, width=width, height=height, bg="#0A0A1E", highlightthickness=0, **kwargs)
        self.width = width
        self.height = height
        self.dots = []
        self.create_dots(dots)
        self.animate()

    def create_dots(self, count):
        for _ in range(count):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            dot = self.create_oval(x, y, x+2, y+2, fill="#00FF00", outline="")
            self.dots.append((dot, random.uniform(0.5, 1.5)))  # dot with speed

    def animate(self):
        for dot, speed in self.dots:
            x1, y1, x2, y2 = self.coords(dot)
            if x1 > self.width:
                new_x = random.randint(-20, -5)
                new_y = random.randint(0, self.height)
                self.coords(dot, new_x, new_y, new_x+2, new_y+2)
            else:
                self.move(dot, speed, 0)
        self.after(50, self.animate)
