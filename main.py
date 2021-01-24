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


class MainStage:
    def __init__(self, window):
        self.window = window

        self.background_image = Image.open("img/background.jpg").resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(window, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.drop_menu_btn = tk.Button(window, text="Menu", bg='red', command=None)
        self.drop_menu_btn.place(relx=0.01, rely=0.01, width=rtoa(hdtor(50)), height=rtoa(hdtor(50, False), False))

        self.suspect_frame = tk.Frame(window, bg='blue')
        self.suspect_frame.place(relx=0.2, rely=0.05, width=rtoa(0.6), height=rtoa(0.3))

        self.judge_canvas = tk.Canvas(window)
        self.judge_canvas.place(relx=0.35, rely=0.65, relwidth=0.3, relheight=0.35)
        self.judge_image = ImageTk.PhotoImage(Image.open("img/judge.png").resize((int(0.3*WIDTH), int(0.35*HEIGHT)), Image.ANTIALIAS))
        self.judge_canvas.create_image(int(0.3*WIDTH / 2), int(0.35*HEIGHT / 2), image=self.judge_image)

        self.evidence_image = ImageTk.PhotoImage(Image.open("img/folder.png").resize((int(0.109*WIDTH), int(0.257*HEIGHT)), Image.ANTIALIAS))
        self.evidence_btn = tk.Button(window, image=self.evidence_image, bg='white', command=None)
        self.evidence_btn.place(relx=0.172, rely=0.667, relwidth=0.109, relheight=0.257)

        self.decide_image = ImageTk.PhotoImage(Image.open("img/gavel.png").resize((int(0.163*WIDTH), int(0.244*HEIGHT)), Image.ANTIALIAS))
        self.decide_btn = tk.Button(window, image=self.decide_image, bg='white', command=None)
        self.decide_btn.place(relx=0.706, rely=0.671, relwidth=0.163, relheight=0.244)

        self.suspect_buttons = []
        for i in range(5):
            self.suspect_buttons.append(tk.Button(self.suspect_frame, text=f"Suspect{i+1}", fg='green', command=None,
                                                  borderwidth=2))
            self.suspect_buttons[-1].place(relx=0.2*i, rely=0.2, relwidth=0.2, relheight=0.8)




root = tk.Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")

WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

root.attributes("-fullscreen", 1)
root.resizable(width=False, height=False)
try:
    root.attributes('-transparentcolor', 'red')
except:
    pass

mainStage = MainStage(root)

root.mainloop()
