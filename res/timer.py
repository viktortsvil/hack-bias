import math
from PIL import Image, ImageTk

class MyTimer:
    def __init__(self, args):
        self.bg_canvas = args[0]
        self.time_one = args[1]
        self.time_two = args[2]
        self.time_three = args[3]
        self.time_four = args[4]
        self.WIDTH = args[5]
        self.HEIGHT = args[6]
        self.if_out = args[7]
        self.window = args[8]
        self.gamelevel = args[9]

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.if_out(self.window, False, self.gamelevel)
        else:
            self.remaining = self.remaining - 1
            self.bg_canvas.after(1000, self.countdown)
            self.time_to_img(self.remaining)

    def time_to_img(self, time_in_sec):
        self.numbers = dict()
        self.minutes = list(str(math.floor(time_in_sec / 60)))
        self.seconds = list(str(time_in_sec - 60 * math.floor(time_in_sec / 60)))
        self.minutes = self.add_zero(self.minutes)
        self.seconds = self.add_zero(self.seconds)
        self.image_path = "img/time/%s_Red.png" % self.seconds[1]
        self.get_images()
        self.bg_canvas.itemconfig(self.time_one.tag, image=self.numbers[self.minutes[0]])
        self.bg_canvas.itemconfig(self.time_two.tag, image=self.numbers[self.minutes[1]])
        self.bg_canvas.itemconfig(self.time_three.tag, image=self.numbers[self.seconds[0]])
        self.bg_canvas.itemconfig(self.time_four.tag, image=self.numbers[self.seconds[1]])

    def get_images(self):
        for i in range(10):
            self.numbers[str(i)] = ImageTk.PhotoImage(Image.open("img/time/%s_Red.png" % i).resize((int(0.046 * self.WIDTH),
                                                                                                    int(
                                                                                                        0.049 * self.HEIGHT))))

    def add_zero(self, string_list):
        if len(string_list) < 2:
            string_list.insert(0, "0")
        return string_list
