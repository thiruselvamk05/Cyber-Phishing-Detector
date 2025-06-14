import tkinter as tk
import random

class MatrixBackground(tk.Canvas):
    def __init__(self, master, font_size=14, **kwargs):
        super().__init__(master, bg="black", highlightthickness=0, **kwargs)
        self.master = master
        self.font_size = font_size
        self.text_color = "#00FF00"
        self.font = ("Consolas", font_size)
        self.columns = 0
        self.drops = []

        self.bind("<Configure>", self.resize)
        self.after(100, self.animate)

    def resize(self, event=None):
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.columns = self.width // self.font_size
        self.drops = [random.randint(0, self.height // self.font_size) for _ in range(self.columns)]

    def animate(self):
        self.delete("all")
        for i in range(self.columns):
            char = random.choice(["0", "1"])
            x = i * self.font_size
            y = self.drops[i] * self.font_size
            self.create_text(x, y, text=char, fill=self.text_color, font=self.font, anchor="nw")

            if y > self.height or random.random() > 0.985:
                self.drops[i] = 0
            else:
                self.drops[i] += 1

        self.after(80, self.animate)  # slower frame rate
