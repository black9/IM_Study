from tkinter import *
import random

## 변수 선언 부분 ##
btnList = [""] * 9
fnameList = ["froyo.gif", "gingerbread.gif", "honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif", "nougat.gif"]
photoList=[None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

## 메인 코드 부분 ##
window = Tk()
window.geometry("210x210")

for i in range(0, 9) :
    photoList[i] = PhotoImage(file = "image/" + fnameList[i])
random.shuffle(photoList)

for i in range(0, 9) :
      btnList[i] = Button(window, image = photoList[i])


for i in range(0, 3) :
    for k in range(0, 3) :
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()
