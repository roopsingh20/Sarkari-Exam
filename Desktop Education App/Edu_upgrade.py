from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import cv2
import os
import pymysql
import pymysql.cursors

master = Tk()
master.geometry("900x550")
master.title("Educational Point")
master.config(bg="#14c492")
master.resizable(0, 0)


def login():
    logs = Toplevel(master)
    logs.geometry("850x450")
    logs.title("Application - Login")
    logs.config(bg='#8946b0')
    logs.resizable(0, 0)

    head = Label(logs, text="Login", bg='#8946b0', font=("Trebuchet ms", 80, "bold italic"))
    head.place(x=250, y=5)

    global photo
    photo = PhotoImage(file="G:/Siddhant Project/Desktop Education App/enter.png")
    img = Label(logs, image=photo, bg='#8946b0', bd=0)
    img.place(x=550, y=5)

    l1 = Label(logs, text="Enter Username: ", bg='#8946b0', font=("Trebuchet ms", 18))
    user = StringVar()
    e1 = Entry(logs, width=20, font=('Trebuchet ms', 18, 'bold'), textvariable=user)

    l2 = Label(logs, text="Enter Password: ", bg='#8946b0', font=("Trebuchet ms", 18))
    passd = StringVar()
    e2 = Entry(logs, width=20, show="*", font=('Trebuchet ms', 18, 'bold'), textvariable=passd)
    value = IntVar()

    # show password in the entry field window
    def show_pass():
        if value.get():
            e2.config(show="")
        else:
            e2.config(show="*")

    checkB = Checkbutton(logs, text='Show Password', bg='#8946b0', font=('Trebuchet ms', 16, 'bold')
                         , onvalue=1, offvalue=0, variable=value, command=show_pass)

    def logged():
        id = user.get()
        pwd = passd.get()
        #p = hashlib.sha1((id[:5] + pwd).encode('utf-8')).hexdigest()
        conn = pymysql.connect(host='localhost', db='world', user='root', password='')
        a = conn.cursor()
        a.execute("select * from register where Username='" + id + "' and Password='" + pwd + "'")
        results = a.fetchall()
        count = a.rowcount
        print(results)
        print(count)

        if count > 0:
            messagebox.showinfo('Message', 'Login Successful!')
            reset()
            logs.after(5000, lambda: logs.destroy())
            os.system('Main_Interface.py')

        else:
            messagebox.showinfo('Message', 'Login Unsuccessful!')
            reset()
        conn.commit()

    b1 = Button(logs, text="Login", width=16, height=1, fg="#0d0fa1", bd=5, bg="lavender", font=('Trebuchet ms', 14, 'bold'), command=logged)
    b2 = Button(logs, text="Exit", width=16, height=1, fg="#0d0fa1", bd=5, bg="lavender", font=('Trebuchet ms', 14, 'bold'), command=lambda: logs.destroy())

    l1.place(x=200, y=160)
    e1.place(x=400, y=160)
    l2.place(x=200, y=220)
    e2.place(x=400, y=220)
    b1.place(x=220, y=340)
    b2.place(x=460, y=340)
    checkB.place(x=400, y=270)

    def reset():
        user.set('')
        passd.set('')


def open_converts():
    global data
    width = 140
    height = 160
    filename = filedialog.askopenfilename(filetypes=[("jpeg files", "*.jpg")])
    im = Image.open(filename)
    im = im.resize((width, height), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(im)
    print(filename)
    win.config(image=photo)
    win.photo = photo

    with open(filename, 'rb') as fr:
        data = fr.read()
    print(data, end=" ")


def converted():
    tests = data
    return tests


def captures():
    os.system('Capture_Image.py')


# image removing function
def remove_img():
    win.config(image=None)
    win.photo = None


def register():
    regis = Toplevel(master)
    regis.geometry("880x720")
    regis.title("Application - Registration")
    regis.config(bg="#28e0da")
    regis.resizable(0, 0)

    mainTitle = Label(regis, text="Register Yourself", bg="#28e0da", font=("Tw Cen MT", 35, "bold"))
    mainTitle.place(x=250, y=15)
    frames = Frame(regis, highlightbackground="black", highlightcolor="black", highlightthickness=4, width=160, height=180)
    frames.place(x=255, y=90)
    global win
    win = Label(frames)
    win.place(x=5, y=5)
    caps = Button(regis, text='Capture Image', width=15, height=1, bg='#5a5a5a', fg='white', font=('Trebuchet Ms', 14, "bold"), bd=5, command=captures)
    caps.place(x=430, y=95)
    sels = Button(regis, text='Select From Files', width=15, height=1, bg='#5a5a5a', fg='white', font=('Trebuchet Ms', 14, "bold"), bd=5, command=open_converts)
    sels.place(x=430, y=160)
    remv = Button(regis, text='Remove Image', width=15, height=1, bg='#5a5a5a', fg='white', font=('Trebuchet Ms', 14, "bold"), bd=5,command=remove_img)
    remv.place(x=430, y=220)

    name = Label(regis, text="First Name", bg="#28e0da", font=("Trebuchet ms", 18, "bold"))
    name.place(x=30, y=320)
    iname = StringVar()
    tname = Entry(regis, width=18, font=("Trebuchet ms", 18, "italic bold"), textvariable=iname)
    tname.place(x=170, y=320)

    lname = Label(regis, text="Last Name", bg="#28e0da", font=("Trebuchet ms", 18, "bold"))
    lname.place(x=450, y=320)
    ilname = StringVar()
    tlname = Entry(regis, width=18, font=("Trebuchet ms", 18, "italic bold"), textvariable=ilname)
    tlname.place(x=590, y=320)

    email = Label(regis, text="Email Id", bg="#28e0da", font=("Trebuchet ms", 18, "bold"))
    email.place(x=30, y=390)
    iemail = StringVar()
    temail = Entry(regis, width=18, font=("Trebuchet ms", 18, "italic bold"), textvariable=iemail)
    temail.place(x=170, y=390)

    uname = Label(regis, text="Username", bg="#28e0da", font=("Trebuchet ms", 18, "bold"))
    uname.place(x=450, y=390)
    iuname = StringVar()
    tuname = Entry(regis, width=18, font=("Trebuchet ms", 18, "italic bold"), textvariable=iuname)
    tuname.place(x=590, y=390)

    pn = Label(regis, text="Phone Number", bg="#28e0da", font=("Trebuchet ms", 18, "bold"))
    pn.place(x=225, y=455)
    iphn = StringVar()
    tuphn = Entry(regis, width=18, font=("Trebuchet ms", 18, "italic bold"), textvariable=iphn)
    tuphn.place(x=420, y=455)

    pw = Label(regis, text="Enter Password", bg="#28e0da", font=("Trebuchet ms", 18, "bold"))
    pw.place(x=225, y=520)
    ipwd = StringVar()
    tpw = Entry(regis, width=18, show="*", font=("Trebuchet ms", 18, "italic bold"), textvariable=ipwd)
    tpw.place(x=420, y=520)

    check_var = IntVar()

    def show_pass():
        if check_var.get():
            tpw.config(show="")
        else:
            tpw.config(show="*")

    checkBs = Checkbutton(regis, text='Show Password', bg='#28e0da', font=('Trebuchet ms', 16, 'bold')
                         , onvalue=1, offvalue=0, variable=check_var, command=show_pass)
    checkBs.place(x=420, y=560)

    def regis_insert():
        name = iname.get()
        lname = ilname.get()
        email = iemail.get()
        uname = iuname.get()
        phone = iphn.get()
        pw = ipwd.get()
        tests = converted()
        conn = pymysql.connect(host='localhost', db='world', user='root', password='')
        a = conn.cursor()
        a.execute("insert into register(First_Name,Last_Name,Email_Id,Username,Phone_No,Password,Image)values('"+name+"','"+lname+"','"+email+"','"+uname+"','"+phone+"','"+pw+"',(%s))", tests)
        results = a.fetchall()
        count = a.rowcount
        print(results)
        print(count)

        if count > 0:
            messagebox.showinfo('Message', 'Login Successful!')

        else:
            messagebox.showinfo('Message', 'Login Unsuccessful!')
        conn.commit()

    submit = Button(regis, text="Submit", width=18, height=2, bg="#0b8a16",font=('Trebuchet ms', 14, 'bold'), bd=5, command=regis_insert)
    submit.place(x=220, y=620)

    exiting = Button(regis, text="Exit", width=10, height=1, bg="#abbaad", font=('Trebuchet ms', 14, 'bold'), bd=5,command=lambda: regis.destroy())
    exiting.place(x=710, y=20)

    def reset():
        iname.set('')
        ilname.set('')
        iemail.set('')
        iuname.set('')
        iphn.set('')
        ipwd.set('')
        win.config(image=None)
        win.photo = None

    clear = Button(regis, text="Clear", width=18, height=2, bg="#757d76",font=('Trebuchet ms', 14, 'bold'), bd=5, command=reset)
    clear.place(x=480, y=620)


lb1 = Label(master, text="Welcome", bg="#14c492", fg="#c45214", font=('Trebuchet Ms', 65, "bold"))
lb1.place(x=260, y=50)

lb2 = Label(master, text="to", bg="#14c492", fg="#c45214", font=('Trebuchet Ms', 35, "bold"))
lb2.place(x=420, y=170)

lb3 = Label(master, text="Educational Point", bg="#14c492", fg="#e70000", font=('Tw Cen MT', 60, "bold"))
lb3.place(x=160, y=250)

btn1 = Button(master, text="Register", width=18, bd=5, height=2, fg="#172f4a", bg='#b3bab8', font=("Trebuchet Ms", 14, "bold"), command=register)
btn1.place(x=200, y=400)
btn2 = Button(master, text="Login", width=18, bd=5, height=2, fg="#172f4a", bg='#b3bab8', font=("Trebuchet Ms", 14, "bold"), command=login)
btn2.place(x=500, y=400)
btn3 = Button(master, text="Exit", width=10, bd=5, height=1, fg="#172f4a", bg='#b3bab8', font=("Trebuchet Ms", 14, "bold"), command=lambda: master.destroy())
btn3.place(x=750, y=20)
master.mainloop()
