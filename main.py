import random
import tkinter
import os
import win32com.client
from PIL import Image, ImageTk
from os import system
try:
    system("python3 --version")
except FileNotFoundError:
    print('go to hel')
system("sudo zypper install python3-pip python3-setuptools python3-wheel")
system("pip install tk")
system("pip3 install pillow")
clik = 0


class WindowsMain:
    def __init__(self):
        self.root = tkinter.Tk()
        self.label = tkinter.Label(self.root)
        self.image_paths = [
                    'image/holo.jpg',
                    'image/lehrf.jpg',
                    'image/rbhgbx.jpg'
                    ]
        self.img_path = random.choice(self.image_paths)
        self.img = Image.open(self.img_path)
        self.img = self.img.resize((400, 300), Image.LANCZOS)
        self.img_tkinter = ImageTk.PhotoImage(self.img)

    def star_windows(self):
        self.root.title('Hi in class')
        self.root.resizable(True, True)
        self.root.protocol("WM_DELETE_WINDOW")
        WindowsMain.button()
        self.root.mainloop()

    @staticmethod
    def button():
        button = tkinter.Button(text='test', command=click_button)
        button.pack()

    def get_condition_windows(self):
        pass

    def update_windows(self):
        pass

    def image(self):
        self.label.config(image=self.img_tkinter)
        self.label.image = self.img_tkinter
        self.label.pack()


def click_button():
    global clik

    class_Windows.image()
    clik += 1
    print(clik)


def create_shortcut(target, shortcut_name, description=""):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    shortcut_path = os.path.join(desktop, f"{shortcut_name}.lnk")

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)

    shortcut.TargetPath = target
    shortcut.Description = description
    shortcut.IconLocation = "image/icon.jpg"
    shortcut.save()

if __name__ == "__main__":
    target_path = r"C:/"
    shortcut_name = "TKINER SCRIPT"
    create_shortcut(target_path, shortcut_name, "It's better to have an emo RPG project written in x86 assembly "
                                                "language, so bend your knees")

    class_Windows = WindowsMain()
    class_Windows.star_windows()