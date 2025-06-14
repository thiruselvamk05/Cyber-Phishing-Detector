import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from url_checker import analyze_url_wrapper
from matrix_background import MatrixBackground
import threading
import time

# ---- Cyberpunk Styled Window ----
app = ttk.Window("Phishing Detector - Cyber Mode", "cyborg")
app.geometry("900x650")
app.minsize(800, 550)

# ---- Matrix Background ----
bg = MatrixBackground(app)
bg.place(x=0, y=0, relwidth=1, relheight=1)

# ---- Central Container ----
container = ttk.Frame(app, padding=25, bootstyle="dark")
container.place(relx=0.5, rely=0.5, anchor="center")

title = ttk.Label(
    container,
    text="PHISHING URL DETECTOR",
    font=("Orbitron", 20, "bold"),
    bootstyle="inverse-primary"
)
title.pack(pady=(10, 20))

url_entry = ttk.Entry(container, font=("Consolas", 14), width=55, bootstyle="info")
url_entry.pack(pady=10)
url_entry.focus()
url_entry.bind("<Return>", lambda e: check_url())

def typewriter_effect(text_widget, message, color):
    def run():
        text_widget.configure(state="normal", foreground=color)
        text_widget.delete("1.0", "end")
        for i in range(len(message) + 1):
            text_widget.delete("1.0", "end")
            text_widget.insert("1.0", message[:i])
            time.sleep(0.015)
        text_widget.configure(state="disabled")
    threading.Thread(target=run).start()

def loading_animation(text_widget):
    def animate():
        dots = ""
        for _ in range(10):
            dots += "."
            text_widget.configure(state="normal")
            text_widget.delete("1.0", "end")
            text_widget.insert("1.0", f"Analyzing URL{dots}")
            text_widget.configure(state="disabled")
            time.sleep(0.15)
    threading.Thread(target=animate).start()

def check_url():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Warning", "Please enter a URL.")
        return

    loading_animation(result_box)

    def analyze():
        time.sleep(1.5)
        result = analyze_url_wrapper(url)
        if result["phishing"]:
            msg = f"🚨 PHISHING ALERT!\n\nReason: {result['reason']}"
            color = "#FF3366"  # bright red
        else:
            msg = f"✅ LEGITIMATE SITE\n\nReason: {result['reason']}"
            color = "#00FF88"  # neon green
        typewriter_effect(result_box, msg, color)
    threading.Thread(target=analyze).start()

check_btn = ttk.Button(
    container, text="🔎 Analyze URL", command=check_url,
    bootstyle="success outline"
)
check_btn.pack(pady=10)

result_box = ScrolledText(
    container,
    height=10,
    width=75,
    font=("Consolas", 12),
    wrap="word",
    background="black",        # match Matrix canvas
    foreground="#00FF00",      # neon green text
    borderwidth=0,
    highlightthickness=0,
    insertbackground="white",  # cursor color
)
result_box.configure(state="disabled")
result_box.pack(pady=15, fill="x")


# ---- Overlay Fix ----
container.lift()
app.mainloop()
