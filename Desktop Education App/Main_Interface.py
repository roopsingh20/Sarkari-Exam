from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os


def stf():
    fep = Toplevel(ep)
    fep.title('Educational Point-Shortcut Tricks & Formulas')
    fep.geometry('900x620')
    fep.resizable(0, 0)

    mainTitle = Label(fep, text="Educational Point", font=("Trebuchet ms", 50, "bold"))
    mainTitle.place(x=70, y=30)
    stitle = Label(fep, text="Study Application", font=("Trebuchet ms", 30, "bold italic"))
    stitle.place(x=190, y=120)

    photo = PhotoImage(file="app logo.png")
    img = Label(fep, image=photo, bd=0)
    img.place(x=640, y=5)

    star = Label(fep, text="*", font=("Tw Cen MT", 30, "bold"), fg="red")
    star.place(x=200, y=195)

    sel = Label(fep, text="Select a Category", font=("Tw Cen MT", 50, "bold"), fg="red")
    sel.place(x=220, y=190)

    cap1 = Button(fep, text="Arithmetic Aptitude", width=22, height=2, bg='#6b4796', font=('Trebuchet Ms', 16, "bold"), bd=5)
    cap1.place(x=100, y=300)

    cap2 = Button(fep, text="Logical Reasoning", width=22, height=2, bg='#6b4796', font=('Trebuchet Ms', 16, "bold"),bd=5)
    cap2.place(x=500, y=300)

    cap3 = Button(fep, text="Verbal Reasoning", width=22, height=2, bg='#6b4796', font=('Trebuchet Ms', 16, "bold"), bd=5)
    cap3.place(x=100, y=400)

    cap4 = Button(fep, text="Non Verbal Reasoning", width=22, height=2, bg='#6b4796', font=('Trebuchet Ms', 16, "bold"), bd=5)
    cap4.place(x=500, y=400)

    cap5 = Button(fep, text="Quit", width=22, height=2, bg='#2ba813', font=('Trebuchet Ms', 16, "bold"), bd=5, command=lambda: fep.destroy())
    cap5.place(x=310, y=510)

    fep.mainloop()


def ques():
    que = Toplevel(ep)
    que.title('Educational Point-Questions Section')
    que.geometry('900x720')
    que.resizable(0, 0)

    mainTitle = Label(que, text="Educational Point", font=("Trebuchet ms", 50, "bold"))
    mainTitle.place(x=70, y=30)
    stitle = Label(que, text="Study Application", font=("Trebuchet ms", 30, "bold italic"))
    stitle.place(x=190, y=120)

    photo = PhotoImage(file="app logo.png")
    img = Label(que, image=photo, bd=0)
    img.place(x=640, y=5)

    star = Label(que, text="*", font=("Tw Cen MT", 30, "bold"), fg="red")
    star.place(x=200, y=195)

    sel = Label(que, text="Select a Category", font=("Tw Cen MT", 50, "bold"), fg="red")
    sel.place(x=220, y=190)

    cap1 = Button(que, text="Arithmetic Aptitude", width=22, height=2, bg='#6b4796', font=('Trebuchet Ms', 16, "bold"), bd=5)
    cap1.place(x=100, y=300)

    cap2 = Button(que, text="Logical Reasoning", width=22, height=2, bg='#6b4796', font=('Trebuchet Ms', 16, "bold"),bd=5)
    cap2.place(x=500, y=300)

    cap3 = Button(que, text="Verbal Reasoning", width=22, height=2, bg='#6b4796', font=('Trebuchet Ms', 16, "bold"), bd=5)
    cap3.place(x=100, y=400)

    cap4 = Button(que, text="Non Verbal Reasoning", width=22, height=2, bg='#6b4796', font=('Trebuchet Ms', 16, "bold"), bd=5)
    cap4.place(x=500, y=400)

    cap5 = Button(que, text="Verbal Ability", width=22, height=2, bg='#6b4796', font=('Trebuchet Ms', 16, "bold"),bd=5)
    cap5.place(x=100, y=500)

    cap6 = Button(que, text="Data Interpretation", width=22, height=2, bg='#6b4796', font=('Trebuchet Ms', 16, "bold"),bd=5)
    cap6.place(x=500, y=500)

    cap7 = Button(que, text="Quit", width=22, height=2, bg='#2ba813', font=('Trebuchet Ms', 16, "bold"), bd=5, command=lambda: que.destroy())
    cap7.place(x=310, y=610)

    que.mainloop()


def ask():
    ask_qu = Toplevel(ep)
    ask_qu.title('Educational Point-Ask Questions')
    ask_qu.geometry('950x720')
    ask_qu.resizable(0, 0)

    mainTitle = Label(ask_qu, text="Educational Point", font=("Trebuchet ms", 50, "bold"))
    mainTitle.place(x=90, y=30)
    stitle = Label(ask_qu, text="Study Application", font=("Trebuchet ms", 30, "bold italic"))
    stitle.place(x=210, y=120)

    photo = PhotoImage(file="app logo.png")
    img = Label(ask_qu, image=photo, bd=0)
    img.place(x=670, y=8)

    point = "In this Section, You can ask questions to the trainer of the particular category and \n"\
            "you can also ask question about the app and help related to the app that can be \n" \
            "answered through the application owner."
    info = Label(ask_qu, text=point, font=("Trebuchet ms", 18, "italic"), fg="red")
    info.grid(row=0,column=0,pady=210, padx=20)

    quest = Label(ask_qu, text="Question:- ", font=("Trebuchet ms", 18, "italic"))
    quest.place(x=15, y=310)

    text = Text(ask_qu, font=('Trebuchet Ms', 14, 'italic'), width=92, height=11)
    text.place(x=12, y=350)

    cap1 = Button(ask_qu, text="Submit", width=12, height=2, bg='#3260a8', font=('Trebuchet Ms', 16, "bold"),bd=5)
    cap1.place(x=485, y=630)

    cap2 = Button(ask_qu, text="Quit", width=10, height=2, bg='#2ba813', font=('Trebuchet Ms', 16, "bold"), bd=5, command=lambda: ask_qu.destroy())
    cap2.place(x=800, y=630)

    cap3 = Button(ask_qu, text="Clear", width=10, height=2, bg='#6b4796', font=('Trebuchet Ms', 16, "bold"),bd=5)
    cap3.place(x=655, y=630)
    ask_qu.mainloop()


ep = Tk()
ep.title('Educational Point')
ep.geometry('950x650')
ep.resizable(0, 0)

mainTitle = Label(ep, text="Educational Point", font=("Trebuchet ms", 50, "bold"))
mainTitle.place(x=100, y=20)
stitle = Label(ep, text="Study Application", font=("Trebuchet ms", 30, "bold italic"))
stitle.place(x=220, y=110)

photo = PhotoImage(file="app logo.png")
img = Label(ep, image=photo, bd=0)
img.place(x=680, y=5)

btn1 = Button(ep, text="Shortcut Tricks & Formulas", width=22, height=2, bg='#6b4796',font=('Trebuchet Ms', 16,"bold"), bd=5, command=stf)
btn1.place(x=130, y=230)

btn2 = Button(ep, text="Questions Section",width=22,height=2,bg='#6b4796',font=('Trebuchet Ms', 16,"bold"), bd=5, command=ques)
btn2.place(x=530, y=230)

btn3 = Button(ep, text="Download Section",width=22,height=2,bg='#6b4796',font=('Trebuchet Ms', 16,"bold"), bd=5)
btn3.place(x=130, y=330)

btn4 = Button(ep, text="Video Tutorials Links",width=22,height=2,bg='#6b4796',font=('Trebuchet Ms', 16,"bold"), bd=5)
btn4.place(x=530, y=330)

btn5 = Button(ep, text="Ask a Question",width=22,height=2,bg='#6b4796',font=('Trebuchet Ms', 16,"bold"), bd=5, command=ask)
btn5.place(x=130, y=430)

btn6 = Button(ep, text="Delete Account",width=22,height=2,bg='#6b4796',font=('Trebuchet Ms', 16,"bold"), bd=5)
btn6.place(x=530, y=430)

btn7 = Button(ep, text="Quit", width=20,height=2,bg='#2ba813',font=('Trebuchet Ms', 16,"bold"), bd=5, command=lambda: ep.destroy())
btn7.place(x=330, y=540)
ep.mainloop()
