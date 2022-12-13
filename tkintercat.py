from tkinter import *

import requests
from io import BytesIO
from PIL import Image, ImageTk

window = Tk()
window.geometry('600x600')
window.title("Добро пожаловать в приложение Котиков ;)")
res = requests.get("https://aws.random.cat/meow")
response = res.json()
response_n = requests.get(response['file'])


def new_meow():
    res_n = requests.get("https://aws.random.cat/meow")
    response_nn = res_n.json()
    response_nnn = requests.get(response_nn['file'])
    imgn = ImageTk.PhotoImage(Image.open(BytesIO(response_nnn.content)).resize((600, 600)))
    lbl_bg.config(image=imgn)
    lbl_bg.image = imgn



c = Canvas(window, width=100, height=10)
img = ImageTk.PhotoImage(Image.open(BytesIO(response_n.content)).resize((600, 600)))
c.pack()

lbl_bg = Label(window, image=img)
lbl_bg.place(relx=0, rely=0)
btn = Button(window, text="Click", font=('Arrial', 20), command=new_meow)
btn.place(relx=0.45, rely=0.9)
window.mainloop()
