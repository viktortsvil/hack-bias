import tkinter as tk
import tkinter.font
from PIL import Image, ImageTk


class CanvasObject:
    def __init__(self, canvas, path, x, y, width, height, tag):  # x,y -> center of the image
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.tag = tag
        self.image = ImageTk.PhotoImage(Image.open(path).resize((self.width, self.height), Image.ANTIALIAS))
        self.object = canvas.create_image(self.x, self.y, image=self.image, tag=tag)
        # print(self.object)

    def overlap(self, x, y):
        if self.x - self.width / 2 <= x <= self.x + self.width / 2 and self.y - self.height / 2 <= y <= self.y + self.height / 2:
            return True
        return False


class Suspect:
    def __init__(self, name, age, sex, race, lineup_path, card_path, biography, evidence):
        self.name = name
        self.age = age
        self.sex = sex
        self.race = race
        self.lineup_path = lineup_path
        self.card_path = card_path
        self.biography = biography
        self.evidence = evidence





class CanvasText:
    font = 'FreeMono'

    def __init__(self, canvas, size, text, x, y, tag):
        print(tkinter.font.families())
        self.x = int(x)
        self.y = int(y)
        self.tag = tag
        self.text = text
        self.object = canvas.create_text(x, y, font=CanvasText.font + " " + str(size), tag=tag, text=text)


class MetaStage:
    def __init__(self, window):
        self.window = window
        self.bg_canvas = tk.Canvas(window)
        self.background = CanvasObject(self.bg_canvas, "img/background.jpg", WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT,
                                       'bcg')


class Popup:
    def __init__(self, canvas, path):
        scalefactor = 0.7  # scale to take up part of the screen

        self.object = CanvasObject(canvas, path, WIDTH / 2, HEIGHT / 2, WIDTH * scalefactor,
                                   HEIGHT * scalefactor, 'popup')


class MainStage(MetaStage):
    character_names = ["alien.png", 'blue_coat_guy.png', 'football_shirt.png', 'lady.png', 'tall_man.png']

    def __init__(self, window):
        super().__init__(window)
        self.judge = CanvasObject(self.bg_canvas, "img/judge.png", WIDTH / 2, 0.825 * HEIGHT, 0.3 * WIDTH,
                                  0.35 * HEIGHT, "judge")
        self.evidence = CanvasObject(self.bg_canvas, "img/folder.png", 0.226 * WIDTH, 0.718 * HEIGHT, 0.109 * WIDTH,
                                     0.257 * HEIGHT, 'evidence')
        self.decide = CanvasObject(self.bg_canvas, "img/gavel.png", 0.786 * WIDTH, 0.733 * HEIGHT, 0.163 * WIDTH,
                                   0.244 * HEIGHT, 'decide')
        self.lineup = CanvasObject(self.bg_canvas, "img/lineup.png", 0.5 * WIDTH, 0.375 * HEIGHT, 0.6 * WIDTH,
                                   0.35 * HEIGHT, 'lineup')

        self.blur = None

        self.overlay = None

        self.characters = []
        for i in range(len(self.character_names)):
            self.characters.append(CanvasObject(self.bg_canvas, "img/characters/" + self.character_names[i],
                                                self.lineup.x + (0.2 * i - 0.4) * self.lineup.width,
                                                self.lineup.y,
                                                self.lineup.width / 5, self.lineup.height, 'char' + str(i)))
            self.bg_canvas.tag_bind(self.characters[-1].tag, '<ButtonPress-1>', self.func)

        self.bg_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

    def func(self, event):
        for char in self.characters:
            if char.overlap(event.x, event.y):
                self.blur = CanvasObject(self.bg_canvas, "img/background_faded.png",
                                         self.background.x, self.background.y, WIDTH, HEIGHT, 'blur')
                scalefactor = 0.7
                self.overlay = Popup(self.bg_canvas, "img/characters/John_Lincoln.png")# not sure why this doesn't work
                #self.overlay = CanvasObject(self.bg_canvas, "img/characters/John_Lincoln.png", WIDTH / 2, HEIGHT / 2,
                 #                           WIDTH * scalefactor, HEIGHT * scalefactor, 'popup')

                self.text = CanvasText(self.bg_canvas, 25, "hello hello\nbreak line", 0.49 * WIDTH, 0.37 * HEIGHT, "text")


root = tk.Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

root.geometry(f"{WIDTH}x{HEIGHT}+0+0")

root.attributes("-fullscreen", 1)
root.resizable(width=False, height=False)

mainStage = MainStage(root)

root.mainloop()
