import tkinter as tk
from window.view import WindowMaker

# Build tkinter
root = tk.Tk()

window = WindowMaker(root)
window.initialize()

# Tkinter loop
root.mainloop()
