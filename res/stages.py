import tkinter as tk
from PIL import ImageTk, Image
from .timer import MyTimer
from .entities import Suspect

WIDTH = None
HEIGHT = None

class CanvasObject:
    def __init__(self, canvas, path, x, y, width, height, tag):  # x,y -> center of the image
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.tag = tag
        self.image = ImageTk.PhotoImage(Image.open(path).resize((self.width, self.height), Image.ANTIALIAS))
        self.object = canvas.create_image(self.x, self.y, image=self.image, tag=tag)

    def overlap(self, x, y):
        if self.x - self.width / 2 <= x <= self.x + self.width / 2 and self.y - self.height / 2 <= y <= self.y + self.height / 2:
            return True
        return False

class CanvasText:
    font = 'FreeMono'

    def __init__(self, canvas, size, text, x, y, tag):
        self.x = int(x)
        self.y = int(y)
        self.tag = tag
        self.text = text
        self.object = canvas.create_text(x, y, font=CanvasText.font + " " + str(size), tag=tag, text=text, width=0.5*WIDTH)


class MetaStage:
    def __init__(self, window):
        global WIDTH, HEIGHT
        WIDTH = window.winfo_screenwidth()
        HEIGHT = window.winfo_screenheight()
        self.window = window
        self.bg_canvas = tk.Canvas(window)
        self.background = CanvasObject(self.bg_canvas, "img/background.jpg", WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT,
                                       'bcg')


class MainStage(MetaStage):
    character_names = ["alien.png", 'blue_coat_guy.png', 'football_shirt.png', 'lady.png', 'tall_man.png']


    def __init__(self, window, level=1):
        super().__init__(window)
        self.suspects = []
        for i in range(5):
            self.suspects.append(Suspect(level, i + 1))

        self.judge = CanvasObject(self.bg_canvas, "img/judge.png", WIDTH / 2, 0.825 * HEIGHT, 0.3 * WIDTH,
                                  0.35 * HEIGHT, "judge")
        self.evidence = CanvasObject(self.bg_canvas, "img/folder.png", 0.226 * WIDTH, 0.718 * HEIGHT, 0.109 * WIDTH,
                                     0.257 * HEIGHT, 'evidence')
        self.decide = CanvasObject(self.bg_canvas, "img/gavel.png", 0.786 * WIDTH, 0.733 * HEIGHT, 0.163 * WIDTH,
                                   0.244 * HEIGHT, 'decide')
        self.lineup = CanvasObject(self.bg_canvas, "img/lineup.png", 0.5 * WIDTH, 0.375 * HEIGHT, 0.6 * WIDTH,
                                   0.35 * HEIGHT, 'lineup')
        self.time_one = CanvasObject(self.bg_canvas, "img/time/0_Red.png", 0.811 * WIDTH, 0.1 * HEIGHT, 0.046 * WIDTH,
                                     0.052 * HEIGHT, 'time_one')
        self.time_two = CanvasObject(self.bg_canvas, "img/time/0_Red.png", 0.846 * WIDTH, 0.1 * HEIGHT, 0.051 * WIDTH,
                                     0.06 * HEIGHT, 'time_two')
        self.time_column = CanvasObject(self.bg_canvas, "img/time/two_dots_Red.png", 0.871 * WIDTH, 0.1 * HEIGHT,
                                        0.02 * WIDTH,
                                        0.06 * HEIGHT, 'time_column')
        self.time_three = CanvasObject(self.bg_canvas, "img/time/0_Red.png", 0.892 * WIDTH, 0.1 * HEIGHT, 0.051 * WIDTH,
                                       0.06 * HEIGHT, 'time_three')
        self.time_four = CanvasObject(self.bg_canvas, "img/time/0_Red.png", 0.931 * WIDTH, 0.1 * HEIGHT, 0.051 * WIDTH,
                                      0.06 * HEIGHT, 'time_four')
        self.clock = CanvasObject(self.bg_canvas, "img/Clock.png", 0.971 * WIDTH, 0.093 * HEIGHT, 0.04 * WIDTH,
                                  0.075 * HEIGHT, 'clock')

        self.blur = None
        self.blur = None
        self.overlay = None
        self.backbutton = None
        self.text = None

        for i in range(5):
            self.suspects[i].lineup_image = CanvasObject(self.bg_canvas, self.suspects[i].lineup_path,
                                                self.lineup.x + (0.2 * i - 0.4) * self.lineup.width,
                                                self.lineup.y,
                                                self.lineup.width / 5, self.lineup.height, 'char' + str(i))
            self.bg_canvas.tag_bind(self.suspects[i].lineup_image.tag, '<ButtonPress-1>', self.func)

        self.bg_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        my_args = [self.bg_canvas, self.time_one, self.time_two, self.time_three, self.time_four, WIDTH, HEIGHT]
        new_timer = MyTimer(my_args)

        new_timer.countdown(80)

    def func(self, event):
        for char in self.suspects:
            if char.lineup_image.overlap(event.x, event.y):
                self.overlay = Popup(self.bg_canvas, char)

class Menu(MetaStage):
    def __init__(self, window):
        super().__init__(window)
        self.title = CanvasText(self.bg_canvas, int(WIDTH / 32), "Hack-bias", WIDTH / 2, WIDTH / 16, 'title')
        self.text = CanvasText(self.bg_canvas, int(WIDTH / 60), "Our description goes here", WIDTH / 2, WIDTH / 8, 'text')
        self.button = CanvasObject(self.bg_canvas, "img/gavel.png", WIDTH / 2, HEIGHT - WIDTH / 8, 0.15 * WIDTH, 0.2 * HEIGHT, 'button')
        self.bg_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.bg_canvas.tag_bind(self.button.tag, '<ButtonPress-1>', self.movetostage)
    def movetostage(self, event):
        if self.button.overlap(event.x, event.y):
            global mainStage
            mainStage = MainStage(self.window)


class Popup:
    def __init__(self, canvas, suspect):
        scalefactor = 0.9  # scale to take up part of the screen
        self.canvas = canvas

        self.blur = CanvasObject(self.canvas, "img/background_faded.png", WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT, 'blur')
        self.card = CanvasObject(canvas, suspect.card_path, WIDTH / 2, HEIGHT / 2, WIDTH * scalefactor,
                                   HEIGHT * scalefactor, 'suscard')
        self.name = CanvasText(canvas, 25, suspect.name, 0.62 * WIDTH, 0.35*HEIGHT, "susname")
        self.gender = CanvasText(canvas, 25, suspect.sex, 0.62 * WIDTH, 0.38*HEIGHT, "susgender")
        self.age = CanvasText(canvas, 25, suspect.age, 0.62 * WIDTH, 0.41*HEIGHT, "susage")
        self.record = CanvasText(canvas, 25, suspect.record, 0.62 * WIDTH, 0.44*HEIGHT, "susrecord")
        self.biography_canvas = tk.Canvas(canvas)
        self.biography = CanvasText(self.biography_canvas, 25, suspect.biography, 100, 300, "susbio")
        self.biography_canvas.configure(scrollregion=canvas.bbox("all"))

        self.biography_canvas.place(x=0.2*WIDTH, y=0.57*HEIGHT, width=0.4*WIDTH, height=0.4*HEIGHT)
        self.backbutton = CanvasObject(canvas, "img/back-button.png", WIDTH - 50, 50, 100, 100, 'backbutton')
        canvas.tag_bind(self.backbutton.tag, '<ButtonPress-1>', self.back)

    def back(self, event):
        for attr in dir(self):
            if not attr.startswith("_") and not attr.endswith("canvas"):
                if not callable(self.__getattribute__(attr)):
                    if attr == 'biography':
                        self.biography_canvas.delete(self.__getattribute__(attr).object)
                    else:
                        self.canvas.delete(self.__getattribute__(attr).object)
        self.biography_canvas.destroy()