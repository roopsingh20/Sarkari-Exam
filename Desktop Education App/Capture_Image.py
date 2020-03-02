import cv2
from tkinter import *
import os
import random
import time
from PIL import Image, ImageTk

cap = cv2.VideoCapture(0)


def img_cap():
    ret, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    padding = 40
    faces = face_cascade.detectMultiScale(cv2image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(cv2image, (x - padding, y - padding), (x + w + padding, y + h + padding), (0, 0, 255), 2)

    img = Image.fromarray(cv2image)
    # img = Image.fromarray(frame)
    img_tk = ImageTk.PhotoImage(image=img)
    win.img_tk = img_tk
    # win.img = img
    win.config(image=img_tk)
    win.after(10, img_cap)


def capt():
    ret, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    padding = 40
    faces = face_cascade.detectMultiScale(cv2image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(cv2image, (x - padding, y - padding), (x + w + padding, y + h + padding), (0, 0, 255), 2)

        path = "C:/Users/krast.DESKTOP-UQL8ILS"
        # img_name = "img_cap{}.jpg".format(random.randint(1, 1000000))
        # timestr = time.strftime("%d%m%Y-%H%M%S")
        img_name = "img_cap_{}.jpg".format(time.strftime("%d%m%Y-%H%M%S"))
        cv2.imwrite(os.path.join(path, img_name), frame[y:y + h, x:x + w])
        print("{} written!".format(img_name))


def kill():
    cp.quit()
    cap.release()


cp = Tk()
cp.title("Image Capture")
cp.geometry('610x600')
cp.resizable(0, 0)

btn1 = Button(cp, text='Capture Image', width=16, height=1, bd=8
,font="trebuchet 18 italic bold", bg='azure3', command=capt).place(x=20, y=515)

btn2 = Button(cp, text='Quit', width=16, height=1, bd=8
,font="trebuchet 18 italic bold", bg='azure3', command=kill).place(x=300, y=515)

frames = Frame(cp, width=600, height=500)
frames.place(y=10)

win = Label(frames)
win.place(x=10, y=10)
img_cap()
cp.mainloop()
