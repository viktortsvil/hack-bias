import tkinter as tk
from PIL import Image, ImageTk


def hdtor(val, w=True):
    if w:
        return val / 1920
    return val / 1080


def rtoa(val, w=True):  # relative coordinate to absolute
    if w is True:
        return val * WIDTH
    return val * HEIGHT


class Timer:
    def __init__(self, init_mins, init_secs):
        pass


class CanvasObject:
    def __init__(self, canvas, path, x, y, width, height):  # x,y -> center of the image
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.image = ImageTk.PhotoImage(Image.open(path).resize((self.width, self.height), Image.ANTIALIAS))
        self.object = canvas.create_image(self.x, self.y, image=self.image)


class MainStage:
    character_names = ["alien.png", 'blue_coat_guy.png', 'football_shirt.png', 'lady.png', 'tall_man.png']

    def __init__(self, window):
        self.window = window

        self.bg_canvas = tk.Canvas(window)

        self.background = CanvasObject(self.bg_canvas, "img/background.jpg", WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
        self.judge = CanvasObject(self.bg_canvas, "img/judge.png", WIDTH / 2, 0.825 * HEIGHT, 0.3 * WIDTH,
                                  0.35 * HEIGHT)
        self.evidence = CanvasObject(self.bg_canvas, "img/folder.png", 0.226 * WIDTH, 0.718 * HEIGHT, 0.109 * WIDTH,
                                     0.257 * HEIGHT)
        self.decide = CanvasObject(self.bg_canvas, "img/gavel.png", 0.786 * WIDTH, 0.733 * HEIGHT, 0.163 * WIDTH,
                                   0.244 * HEIGHT)
        self.lineup = CanvasObject(self.bg_canvas, "img/lineup.png", 0.5 * WIDTH, 0.375 * HEIGHT, 0.6 * WIDTH,
                                   0.35 * HEIGHT)

        self.characters = []
        for i in range(len(self.character_names)):
            self.characters.append(CanvasObject(self.bg_canvas, "img/characters/" + self.character_names[i],
                                                self.lineup.x + (0.3 + 0.2 * i) * self.lineup.width,0, self.lineup.width / 5, self.lineup.height))

        self.bg_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)


root = tk.Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")

WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

root.attributes("-fullscreen", 1)
root.resizable(width=False, height=False)

mainStage = MainStage(root)

root.mainloop()
