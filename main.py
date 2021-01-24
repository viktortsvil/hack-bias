import tkinter as tk
from res.stages import Menu


root = tk.Tk()
#WIDTH = root.winfo_screenwidth()
#HEIGHT = root.winfo_screenheight()

WIDTH = 1920
HEIGHT = 1080

root.geometry(f"{WIDTH}x{HEIGHT}+0+0")

#root.attributes("-fullscreen", 1)
root.resizable(width=False, height=False)
LEVEL=1
mainStage = Menu(root)

root.mainloop()
