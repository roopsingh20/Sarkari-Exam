from tkinter import *
from tkinter import messagebox
import hashlib
import pymysql
import pymysql.cursors
import random


class MainWindow:

    def __init__(self, master):
        self.master = master
        self.master.geometry("900x550")
        self.master.title("Educational Point")
        self.master.config(bg="#009FBF")

        # self.img = PhotoImage(file="G:/Siddhant Project/Quiz-Application-With-dB-Connectivity-on-Python-Tkinter--master/Resources/imag.png")
        # imgMan = Label(self.master, image=self.img, bg="azure")
        # imgMan.place(x=0, y=60)

        # self.mainTitle = Label(self.master, text="Welcome", fg="red", bg="azure", font=("Helvetica", 30, "bold italic")).place(
        #     x=400, y=200)
        lb1 = Label(self.master, text="Welcome", bg="#009FBF", fg="#5a5a5a", font=('Trebuchet Ms', 65, "bold"))
        lb1.place(x=260, y=50)

        lb2 = Label(self.master, text="to", bg="#009FBF", fg="#5a5a5a", font=('Trebuchet Ms', 35, "bold"))
        lb2.place(x=420, y=170)

        lb3 = Label(self.master, text="Educational Point", bg="#009FBF", fg="#e70000", font=('Tw Cen MT', 60, "bold"))
        lb3.place(x=160, y=250)

        btn1 = Button(self.master, text="Register", width=18, height=2, fg="royalblue4", bg='azure3',
                           font=("Trebuchet Ms", 16, "bold italic"), command=self.c_reg)
        btn2 = Button(self.master, text="Login", width=18, height=2, fg="royalblue4", bg='azure3',
                            font=("Trebuchet Ms", 16, "bold italic"), command=self.c_login)
        btn3 = Button(self.master, text="Exit", width=10, height=1, fg="royalblue4", bg='azure3',
                      font=("Trebuchet Ms", 16, "bold italic"), command=self.master.destroy)
        btn1.place(x=180, y=400)
        btn2.place(x=480, y=400)
        btn3.place(x=750, y=20)

    def c_reg(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.resizable(0, 0)
        self.app = Register(self.newWindow)

    def c_login(self):
        self.login = Toplevel(self.master)
        self.login.resizable(0, 0)
        self.log = Login(self.login)


class Register:

    def __init__(self, master):
        global mReg
        mReg = master
        self.master = master
        self.master.geometry("900x550")
        self.master.title("Application - Registration")
        self.master.config(bg="azure")
        # global f1
        # f1 = Frame(self.master, height=1080, width=1920, bg="azure", relief="ridge", bd=20)
        # f1.propagate(0)
        # f1.pack()

        # self.regNow = PhotoImage(file="G:/Siddhant Project/Quiz-Application-With-dB-Connectivity-on-Python-Tkinter--master/Resources/RegisterNow.png")
        # imgRegNow = Label(self.master, image=self.regNow, bg="azure")
        # imgRegNow.place(x=550, y=5)

        self.mainTitle = Label(self.master, text="Register Yourself", bg="azure",
                               font=("Trebuchet ms", 35, "bold italic underline")).place(x=280, y=15)
        self.name = Label(self.master, text="First Name : ", bg="azure", font=("Times New Roman", 18, "italic bold"))
        self.lname = Label(self.master, text="Last name : ", bg="azure", font=("Times New Roman", 18, "italic bold"))
        self.email = Label(self.master, text="Email id : ", bg="azure", font=("Times New Roman", 18, "italic bold"))
        self.uname = Label(self.master, text="Username :", bg="azure", font=("Times New Roman", 18, "italic bold"))
        self.pw = Label(self.master, text="Enter password : ", bg="azure", font=("Times New Roman", 18, "italic bold"))

        self.var = IntVar()

        self.tname = Entry(self.master, width=20, font=("Times New Roman", 18, "italic bold"))
        self.tlname = Entry(self.master, width=20, font=("Times New Roman", 18, "italic bold"))
        self.temail = Entry(self.master, width=20, font=("Times New Roman", 18, "italic bold"))
        self.tuname = Entry(self.master, width=20, font=("Times New Roman", 18, "italic bold"))
        self.tpw = Entry(self.master, width=20, show="*", font=("Times New Roman", 18, "italic bold"))

        self.submit = Button(self.master, text="Submit", width=20, height=5, fg="royalblue4", bg="lavender",
                             font=("Helvetica", 10, "bold italic"), command=self.c_submit)
        self.cancel = Button(self.master, text="Cancel", width=20, height=5, fg="royalblue4", bg="lavender",
                             font=("Helvetica", 10, "bold italic"), command=self.c_cancel)

        self.checkB = Checkbutton(self.master, text='Show Password', bg="azure", fg="royalblue4",
                                  font=("Helvetica", 10, "bold italic"), variable=self.var, onvalue=1,
                                  offvalue=0, command=self.Showpasswd)

        self.name.place(x=50, y=100)
        self.tname.place(x=200, y=100)
        self.lname.place(x=50, y=150)
        self.tlname.place(x=200, y=150)
        self.email.place(x=50, y=200)
        self.temail.place(x=200, y=200)
        self.uname.place(x=50, y=250)
        self.tuname.place(x=200, y=250)
        self.pw.place(x=50, y=300)
        self.tpw.place(x=200, y=300)
        self.submit.place(x=50, y=400)
        self.cancel.place(x=250, y=400)
        self.checkB.place(x=195, y=330)

    def Showpasswd(self):
        if (self.var.get()):
            self.tpw.config(show="")
        else:
            self.tpw.config(show="*")

    def check(self, l1):
        ht = 50
        f = 0
        s = 0
        for i in range(5):
            ht = ht + 50
            if len(l1[i]) == 0:
                self.l = Label(self.master, text="! You cannot leave this empty", fg='red', bg="azure")
                self.l.place(x=400, y=ht)
            else:
                self.l = Label(self.master, text="! You cannot leave this empty", bg="azure", fg="azure")
                self.l.place(x=400, y=ht)
                f = f + 1
        if l1[2].find("@") == -1 and l1[2].find(".") == -1 and len(l1[2]) != 0:
            self.l = Label(self.master, text="! Please enter a valid email id", bg="azure", fg="red")
            self.l.place(x=400, y=200)
            s = 1
        else:
            if (len(l1[2]) > 0):
                self.l = Label(self.master, text="! Please enter a valid email id", bg="azure", fg="azure")
                self.l.place(x=400, y=200)
        if len(l1[4]) < 8 and len(l1[4]) != 0:
            self.l = Label(self.master, text="! Password must atleast have 8 characters", bg="azure", fg="red")
            self.l.place(x=400, y=300)
        else:
            if (len(l1[4]) > 0):
                self.l = Label(self.master, text="! Password must atleast have 8 characters", bg="azure", fg="azure")
                self.l.place(x=400, y=300)
        if (f == 5 and len(l1[4]) >= 8 and s == 0):
            return 1
        else:
            return 0

    def c_submit(self):
        conn = pymysql.connect(host='localhost', database='world', user='root', password='')
        cursor = conn.cursor()
        name = self.tname.get()
        lname = self.tlname.get()
        email = self.temail.get()
        uname = self.tuname.get()
        pw = self.tpw.get()
        p = hashlib.sha1((uname[:5] + pw).encode('utf-8')).hexdigest()
        l1 = [name, lname, email, uname, pw]
        c = self.check(l1)
        if c == 1:
            str = "select * from reg where uname='%s'"
            arg = (uname)
            cursor.execute(str % arg)
            row = cursor.fetchone()
            if row is not None:
                messagebox.showwarning("Error", "Username Already Taken, Try Again!")
                mReg.destroy()
            else:
                try:
                    s = "insert into reg(name,lname,email,uname,p,score) values('%s','%s','%s','%s','%s','%d')"
                    arg = (name, lname, email, uname, p, 0)
                    cursor.execute(s % arg)
                    conn.commit()
                    print("DEBUG: 1 ROW ADDED")
                    self.tname.delete(0, 'end')
                    self.tlname.delete(0, 'end')
                    self.temail.delete(0, 'end')
                    self.tuname.delete(0, 'end')
                    self.tpw.delete(0, 'end')
                    messagebox.showinfo("Success", "Registration Successful!")
                    mReg.destroy()
                except:
                    conn.rollback()
        cursor.close()
        conn.close()

    def c_cancel(self):
        mReg.destroy()


class Login:

    def __init__(self, master):
        global mLogin
        mLogin = master
        self.master = master
        self.master.geometry("850x450")
        self.master.title("Application - Login")
        self.master.config(bg='#c8c8c8')

        head = Label(self.master, text="Login", bg='#c8c8c8', font=("Trebuchet ms", 80, "bold italic"))
        head.place(x=250, y=5)

        self.regNow = PhotoImage(file="G:/Siddhant Project/Quiz-Application-With-dB-Connectivity-on-Python-Tkinter--master/log.png")
        imgRegNow = Label(self.master, image=self.regNow, bg='#c8c8c8')
        imgRegNow.place(x=550, y=5)

        self.l1 = Label(self.master, text="Enter Username: ", bg='#c8c8c8', font=("Trebuchet ms", 18))
        self.e1 = Entry(self.master, width=20, font=('Trebuchet ms', 18,  'bold'))
        self.l2 = Label(self.master, text="Enter Password: ", bg='#c8c8c8', font=("Trebuchet ms", 18))
        self.e2 = Entry(self.master, width=20, show="*", font=('Trebuchet ms', 18,  'bold'))
        self.b1 = Button(self.master, text="Login", width=16, height=2, fg="royalblue4", bg="lavender",
                         font=('Trebuchet ms', 14,  'bold italic'), command=self.clicked)
        self.b2 = Button(self.master, text="Cancel", width=16, height=2, fg="royalblue4", bg="lavender",
                         font=('Trebuchet ms', 14,  'bold italic'), command=self.cancelLogin)

        self.var = IntVar()
        self.checkB = Checkbutton(self.master, text='Show Password', bg='#c8c8c8', fg="royalblue4",
                                  font=('Trebuchet ms', 16, 'bold'), variable=self.var, onvalue=1,
                                  offvalue=0, command=self.Showpasswd)

        self.l1.place(x=200, y=160)
        self.e1.place(x=400, y=160)
        self.l2.place(x=200, y=220)
        self.e2.place(x=400, y=220)
        self.b1.place(x=220, y=340)
        self.b2.place(x=460, y=340)
        self.checkB.place(x=400, y=270)

    def Showpasswd(self):
        if (self.var.get()):
            self.e2.config(show="")
        else:
            self.e2.config(show="*")

    def cancelLogin(self):
        mLogin.destroy()

    def clicked(self):
        conn = pymysql.connect(host='localhost', database='world', user='root', password='')
        cursor = conn.cursor()
        u = self.e1.get()
        pw = self.e2.get()
        self.e1.delete(0, 200)
        self.e2.delete(0, 200)
        p = hashlib.sha1((u[:5] + pw).encode('utf-8')).hexdigest()
        s = "select * from reg where uname='%s' and p='%s'"
        arg = (u, p)
        cursor.execute(s % arg)
        result = cursor.fetchall()
        if result:
            self.goinaccount(u)
        else:
            messagebox.showerror("Error", "Invalid Username or Password, Try Again!")
            mLogin.destroy()
        cursor.close()
        conn.close()

    def goinaccount(self, u):
        self.accWindow = Toplevel(mLogin)
        self.accWindow.resizable(0, 0)
        self.acWin = Account(self.accWindow, u)


class Account:

    def __init__(self, master, u):
        global mAcc
        self.u = u
        self.master = master
        mAcc = master
        self.master.geometry("1350x750+0+0")
        self.master.title("Welcome")
        self.master.config(bg="#009FBF")
        f3 = Frame(mAcc, height=1080, width=1920, bg="azure", relief="ridge", bd=20)
        f3.propagate(0)
        f3.pack()
        conn = pymysql.connect(host='localhost', database='world', user='root', password='')
        cursor = conn.cursor()
        q = "select score from reg where uname='%s'"
        arg = (u)
        cursor.execute(q % arg)
        self.prevScore = cursor.fetchone()
        cursor.close()
        conn.close()
        self.greet = Label(f3, text="Hey " + u + ", Welcome Back!", bg="azure",
                           font=("Helvetica", 30, "bold italic")).place(x=400, y=200)
        self.lastScore = Label(f3, text="Last Quiz Score = " + str(self.prevScore[0]), bg="azure",
                               font=("Helvetica", 30, "bold italic")).place(x=400, y=300)
        self.takeQuiz = Button(f3, text="Take Quiz", width=20, height=5, fg="royalblue4", bg="lavender",
                               font=("Helvetica", 10, "bold italic"), command=self.goinside)
        self.takeQuiz.place(x=500, y=400)
        self.logout = Button(f3, text="Logout", width=20, height=5, fg="royalblue4", bg="lavender",
                             font=("Helvetica", 10, "bold italic"), command=self.logout)
        self.logout.place(x=750, y=400)

    def goinside(self):
        self.quizWindow = Toplevel(self.master)
        self.quizWindow.resizable(0, 0)
        self.qw = Quiz(self.quizWindow, self.u)

    def logout(self):
        mAcc.destroy()


class Quiz:
    def __init__(self, master, u):
        self.user = u
        global mQuiz
        mQuiz = master
        self.master = master
        self.master.geometry("1350x750+0+0")
        self.master.title("Online Quiz - Registration")
        self.master.config(bg="azure")
        global f1
        f = Frame(self.master, height=1080, width=1920, bg="azure", relief="ridge", bd=20)
        conn = pymysql.connect(host='localhost', database='world', user='root', password='')
        cursor = conn.cursor()

        global l1, answerstemp
        global questions
        questions = []
        global options
        options = []
        global answers
        answers = []
        answerstemp = []
        s1 = set()

        while len(s1) < 10:
            strQ = ""
            strA = ""
            id = random.randint(1, 30)
            s1.add(id)

        while len(s1) > 0:
            s = "select qstn from questions where QID=%d"
            id = s1.pop()
            arg = (id)
            cursor.execute(s % arg)
            strQ = strQ.join(list(cursor.fetchone()))
            questions.append(strQ)

            s = "select opA,opB,opC,opD from questions where QID=%d"
            arg = (id)
            cursor.execute(s % arg)
            options.append(list(cursor.fetchone()))

            s = "select ans from questions where QID=%d"
            arg = (id)
            cursor.execute(s % arg)
            l = list(cursor.fetchone())
            answerstemp.append(l)

        mydict = {}
        for i in range(10):
            mydict[questions[i]] = options[i]
        for i in range(len(answerstemp)):
            answers.append(answerstemp[i][0])

        print("DEBUG: Answers= ", answers)

        cursor.close()
        conn.close()
        l1 = {}
        for i in range(10):
            l1[i] = 0

        f.propagate(0)
        f.pack()
        self.qno = 0
        self.score1 = 0
        self.ques = self.create_q(f, self.qno)
        self.opts = self.create_options(f)
        self.display_q(self.qno)
        self.Back = Button(f, text="<- Back", width=15, height=3, fg="royalblue4", bg="snow2",
                           font=("Helvetica", 10, "bold italic"), command=self.back).place(x=100, y=325)
        self.Next = Button(f, text="Next ->", width=15, height=3, fg="royalblue4", bg="snow2",
                           font=("Helvetica", 10, "bold italic"), command=self.next).place(x=250, y=325)
        self.submit = Button(f, text="Submit", width=34, height=2, fg="ghost white", bg="DeepSkyBlue2",
                             font=("Helvetica", 10, "bold italic"), command=self.Submit).place(x=100, y=400)

        imgID = random.randint(1, 4)
        filestr = "G:/Siddhant Project/Quiz-Application-With-dB-Connectivity-on-Python-Tkinter--master/Resources/" + str(imgID) + ".png"
        self.quizImg = PhotoImage(file=filestr)
        img = Label(f, image=self.quizImg, bg="azure")
        img.place(x=700, y=200)

    def create_q(self, master, qno):
        qLabel = Label(master, text=questions[qno], bg='azure', font=("Times New Roman", 20))
        qLabel.place(x=30, y=70)
        return qLabel

    def create_options(self, master):
        b_val = 0
        b = []
        ht = 85
        self.opt_selected = IntVar()
        while b_val < 4:
            btn = Radiobutton(master, text="", variable=self.opt_selected, value=b_val + 1, bg='azure',
                              font=("Times New Roman", 20))
            b.append(btn)
            ht = ht + 40
            btn.place(x=30, y=ht)
            b_val = b_val + 1
        return b

    def display_q(self, qno):
        b_val = 0
        self.ques['text'] = str(qno + 1) + ". " + questions[qno]
        for op in options[qno]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def next(self):
        self.qno += 1

        if self.qno >= len(questions):
            self.qno -= 1
            messagebox.showwarning("Warning", "You are at the end.Press Submit to proceed")
        else:
            l1[self.qno - 1] = self.opt_selected.get()
            self.opt_selected.set(l1[(self.qno)])
            self.display_q(self.qno)

    def back(self):
        l1[self.qno] = self.opt_selected.get()
        self.qno -= 1
        if self.qno < 0:
            self.qno += 1
            messagebox.showerror("Error", "You are already in the start!!!")
        else:
            self.display_q(self.qno)
            c = l1[self.qno]
            self.opt_selected.set(c)

    def Submit(self):
        l1[self.qno] = self.opt_selected.get()
        x = 0
        y = True
        for i in range(10):
            if (l1[i] == 0):
                x += 1
        if (x > 0 and x != 1):
            y = messagebox.askyesno("Warning", "You have not attempted " + str(
                x) + " questions, Are you sure you want to submit?, You won't be able to make changes again")
        elif (x == 1):
            y = messagebox.askyesno("Warning", "You have not attempted " + str(
                x) + " question, Are you sure you want to submit?, You won't be able to make changes again")
        if (y == True or x == 0):
            s = 0
            for i in range(10):
                if (l1[i] == answerstemp[i][0]):
                    s = s + 1
            print("DEBUG: Score: ", s)

        conn = pymysql.connect(host='localhost', database='world', user='root', password='')
        cursor = conn.cursor()
        q = "update reg set score='%d' where uname= '%s'"
        arg = (s, self.user)
        cursor.execute(q % arg)
        conn.commit()
        cursor.close()
        conn.close()

        messagebox.showinfo("Score", "Your Score is: " + str(s) + "/10")
        mQuiz.destroy()


root = Tk()
root.resizable(0, 0)
RegObj = MainWindow(root)
root.mainloop()
