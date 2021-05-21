from tkinter import *
import tkinter as tk
from tkinter import messagebox
import turtle
import random
import time

lives = 3
points = 0
helps = 1
coins = 50
lock = 1
answer = ''
d = ''
m = ''
k = 0
scr = turtle.Screen()
pen = turtle.Turtle()

pen.speed(200)
pen.pensize(5)
pen.up()
pen.goto(-300, 50)

pen.pd()

pen.lt(90)
pen.fd(100)
pen.rt(90)
pen.fd(70)
pen.bk(70)
pen.lt(90)
pen.fd(100)
pen.rt(90)
pen.fd(70)

pen.up()
pen.fd(70)
pen.pd()

pen.rt(90)
pen.fd(200)
pen.lt(90)
pen.fd(90)

pen.up()
pen.fd(70)
pen.pd()

pen.lt(70)
pen.fd(200)
pen.rt(140)
pen.fd(200)
pen.bk(100)
pen.rt(110)
pen.fd(77)

pen.up()
pen.rt(180)
pen.fd(150)
pen.lt(90)
pen.fd(50)
pen.pd()

pen.rt(180)
pen.fd(150)
pen.lt(90)
pen.fd(100)
pen.lt(90)
pen.fd(50)
pen.lt(90)
pen.fd(40)

pen.up()
pen.fd(60)
pen.pd()

pen.rt(90)
pen.fd(140)
pen.rt(90)
pen.fd(90)

pen.up()
pen.goto(-300, -100)
pen.pd()

pen.rt(90)
pen.fd(150)
pen.lt(90)
pen.fd(100)
pen.lt(90)
pen.fd(50)
pen.lt(90)
pen.fd(40)

pen.up()
pen.fd(60)
pen.pd()

pen.rt(90)
pen.fd(140)
pen.rt(90)
pen.fd(90)

pen.up()
pen.goto(-150, -250)
pen.pd()

pen.lt(70)
pen.fd(200)
pen.rt(140)
pen.fd(200)
pen.bk(100)
pen.rt(110)
pen.fd(77)

pen.up()
pen.goto(20, -250)
pen.pd()

pen.rt(90)
pen.fd(200)
pen.rt(150)
pen.fd(120)
pen.lt(120)
pen.fd(120)
pen.rt(150)
pen.fd(200)

pen.up()
pen.goto(200, -250)
pen.pd()

pen.lt(90)
pen.fd(100)
pen.bk(100)
pen.lt(90)
pen.fd(100)
pen.rt(90)
pen.fd(100)
pen.bk(100)
pen.lt(90)
pen.fd(100)
pen.rt(90)
pen.fd(100)


def change():
    global d
    global flag

    flag = random.choice(flags)
    d = random.choice(flags)
    flag = random.choice(flags)
    flag()


def change2():
    global d
    global flag2

    flag2 = random.choice(flags2)
    d = random.choice(flags2)
    flag2 = random.choice(flags2)
    flag2()


def change3():
    global d
    global flag3

    flag3 = random.choice(flags3)
    d = random.choice(flags3)
    flag3 = random.choice(flags3)
    flag3()


def change4():
    global d
    global flag4

    flag4 = random.choice(flags4)
    d = random.choice(flags4)
    flag4 = random.choice(flags4)
    flag4()


def change5():
    global d
    global flag5

    flag5 = random.choice(flags5)
    d = random.choice(flags5)
    flag5 = random.choice(flags5)
    flag5()


def change6():
    global d
    global flag6

    flag6 = random.choice(flags6)
    d = random.choice(flags6)
    flag6 = random.choice(flags6)
    flag6()


def start():
    pen.up()
    pen.reset()
    pen.pensize(5)
    pen.goto(100, 0)
    pen.pd()
    lbl5.destroy()
    rd.destroy()
    rd2.destroy()
    rd3.destroy()
    rd4.destroy()
    rd5.destroy()
    rd6.destroy()
    lbl6.destroy()
    btn5.destroy()
    btn18.destroy()

    lbl4 = Label(root, text='3', fg='white', bg='black', font=('Tahoma', 50))
    lbl4.pack()

    pen.speed(200)
    pen.bk(100)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)
    pen.bk(100)
    pen.rt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)

    time.sleep(1)
    pen.reset()
    pen.speed(200)
    pen.pensize(5)
    pen.up()
    pen.goto(100, 0)
    pen.pd()
    lbl4.configure(text='2')

    pen.lt(180)
    pen.fd(180)
    pen.rt(135)
    pen.fd(230)
    pen.lt(45)
    pen.fd(60)
    pen.lt(90)
    pen.fd(160)
    pen.lt(90)
    pen.fd(60)

    time.sleep(1)
    pen.reset()

    pen.speed(200)
    pen.pensize(5)
    pen.up()
    pen.goto(0, 0)
    pen.pd()

    lbl4.configure(text='1')
    pen.lt(90)
    pen.fd(200)
    pen.lt(135)
    pen.fd(90)

    time.sleep(1)
    lbl4.destroy()

    def help():
        global helps
        global coins
        global points
        if helps >= 1:
            points += 1
            coins += 10
            flags.remove(flag)
            helps -= 1
            read = 'Correct\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
            messagebox.showinfo('Nice', message=read)
            if len(flags) == 0 and lives > 0:
                rs = tk.messagebox.askyesno("WIN", "You won! Do you want to try again?")
                if rs == True:
                    welcome()
                else:
                    time.sleep(1)
                    quit()
            elif lives == 0:
                rs = tk.messagebox.askyesno("LOSE", "You lost! Do you want to try again?")
                if rs == True:
                    welcome()
                else:
                    time.sleep(1)
                    quit()
            else:
                change()

        else:
            messagebox.showerror('Error', message='You have run out of helps')

    def flaggo2():
        global lock
        global answer
        global flag
        answer = entr.get()
        lock = 0
        entr.delete(0, 'end')
        flaggo(flags)

    global lbl2
    global lbl3
    global entr
    global btn2
    global btn6

    lbl2 = Label(root, text='Flag', fg='white', bg='black', font=('Tahoma', 30), width=33)
    lbl2.grid(column=0, row=0, columnspan=2)
    lbl3 = Label(root, text='Type the country:', fg='white', bg='black', font=('Tahoma', 30))
    lbl3.grid(row=1, column=0)
    entr = Entry(root, font=('Tahoma', 20))
    entr.grid(row=1, column=1)
    flag()
    btn2 = Button(root, text='Click me', command=flaggo2, fg='white', bg='black', font=('Tahoma', 30))
    btn2.grid(row=2, column=0)
    btn6 = Button(root, text='HELP', command=help, fg='white', bg='black', font=('Tahoma', 30))
    btn6.grid(row=2, column=1)


def start2():
    pen.up()
    pen.reset()
    pen.pensize(5)
    pen.goto(100, 0)
    pen.pd()
    lbl5.destroy()
    rd.destroy()
    rd2.destroy()
    rd3.destroy()
    rd4.destroy()
    rd5.destroy()
    rd6.destroy()
    lbl6.destroy()
    btn5.destroy()
    btn18.destroy()

    lbl4 = Label(root, text='3', fg='white', bg='black', font=('Tahoma', 50))
    lbl4.pack()

    pen.speed(200)
    pen.bk(100)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)
    pen.bk(100)
    pen.rt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)

    time.sleep(1)
    pen.reset()
    pen.speed(200)
    pen.pensize(5)
    pen.up()
    pen.goto(100, 0)
    pen.pd()
    lbl4.configure(text='2')

    pen.lt(180)
    pen.fd(180)
    pen.rt(135)
    pen.fd(230)
    pen.lt(45)
    pen.fd(60)
    pen.lt(90)
    pen.fd(160)
    pen.lt(90)
    pen.fd(60)

    time.sleep(1)
    pen.reset()

    pen.speed(200)
    pen.pensize(5)
    pen.up()
    pen.goto(0, 0)
    pen.pd()

    lbl4.configure(text='1')
    pen.lt(90)
    pen.fd(200)
    pen.lt(135)
    pen.fd(90)

    time.sleep(1)
    lbl4.destroy()

    def help2():
        global helps
        global coins
        global points
        if helps >= 1:
            points += 1
            coins += 10
            flags2.remove(flag2)
            helps -= 1
            read = 'Correct\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
            messagebox.showinfo('Nice', message=read)
            if len(flags2) == 0 and lives > 0:
                rs = tk.messagebox.askyesno("WIN", "You won! Do you want to try again?")
                if rs == True:
                    welcome()
                else:
                    time.sleep(1)
                    quit()
            elif lives == 0:
                rs = tk.messagebox.askyesno("LOSE", "You lost! Do you want to try again?")
                if rs == True:
                    welcome()
                else:
                    time.sleep(1)
                    quit()
            else:
                change2()

        else:
            messagebox.showerror('Error', message='You have run out of helps')

    def flaggo4():
        global lock
        global answer
        global flag2
        answer = entr.get()
        lock = 0
        entr.delete(0, 'end')
        flaggo3(flags2)

    global lbl2
    global lbl3
    global entr
    global btn2
    global btn6

    lbl2 = Label(root, text='Flag', fg='white', bg='black', font=('Tahoma', 30), width=33)
    lbl2.grid(column=0, row=0, columnspan=2)
    lbl3 = Label(root, text='Type the country:', fg='white', bg='black', font=('Tahoma', 30))
    lbl3.grid(row=1, column=0)
    entr = Entry(root, font=('Tahoma', 20))
    entr.grid(row=1, column=1)
    flag2()
    btn2 = Button(root, text='Click me', command=flaggo4, fg='white', bg='black', font=('Tahoma', 30))
    btn2.grid(row=2, column=0)
    btn6 = Button(root, text='HELP', command=help2, fg='white', bg='black', font=('Tahoma', 30))
    btn6.grid(row=2, column=1)


def start3():
    pen.up()
    pen.reset()
    pen.pensize(5)
    pen.goto(100, 0)
    pen.pd()
    lbl5.destroy()
    rd.destroy()
    rd2.destroy()
    rd3.destroy()
    rd4.destroy()
    rd5.destroy()
    rd6.destroy()
    lbl6.destroy()
    btn5.destroy()
    btn18.destroy()

    lbl4 = Label(root, text='3', fg='white', bg='black', font=('Tahoma', 50))
    lbl4.pack()

    pen.speed(200)
    pen.bk(100)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)
    pen.bk(100)
    pen.rt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)

    time.sleep(1)
    pen.reset()
    pen.speed(200)
    pen.pensize(5)
    pen.up()
    pen.goto(100, 0)
    pen.pd()
    lbl4.configure(text='2')

    pen.lt(180)
    pen.fd(180)
    pen.rt(135)
    pen.fd(230)
    pen.lt(45)
    pen.fd(60)
    pen.lt(90)
    pen.fd(160)
    pen.lt(90)
    pen.fd(60)

    time.sleep(1)
    pen.reset()

    pen.speed(200)
    pen.pensize(5)
    pen.up()
    pen.goto(0, 0)
    pen.pd()

    lbl4.configure(text='1')
    pen.lt(90)
    pen.fd(200)
    pen.lt(135)
    pen.fd(90)

    time.sleep(1)
    lbl4.destroy()

    def help3():
        global helps
        global coins
        global points
        if helps >= 1:
            points += 1
            coins += 10
            flags3.remove(flag3)
            helps -= 1
            read = 'Correct\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
            messagebox.showinfo('Nice', message=read)
            if len(flags3) == 0 and lives > 0:
                rs = tk.messagebox.askyesno("WIN", "You won! Do you want to try again?")
                if rs == True:
                    welcome()
                else:
                    time.sleep(1)
                    quit()
            elif lives == 0:
                rs = tk.messagebox.askyesno("LOSE", "You lost! Do you want to try again?")
                if rs == True:
                    welcome()
                else:
                    time.sleep(1)
                    quit()
            else:
                change3()

        else:
            messagebox.showerror('Error', message='You have run out of helps')

    def flaggo6():
        global lock
        global answer
        global flag3
        answer = entr.get()
        lock = 0
        entr.delete(0, 'end')
        flaggo5(flags3)

    global lbl2
    global lbl3
    global entr
    global btn2
    global btn6

    lbl2 = Label(root, text='Flag', fg='white', bg='black', font=('Tahoma', 30), width=33)
    lbl2.grid(column=0, row=0, columnspan=2)
    lbl3 = Label(root, text='Type the country:', fg='white', bg='black', font=('Tahoma', 30))
    lbl3.grid(row=1, column=0)
    entr = Entry(root, font=('Tahoma', 20))
    entr.grid(row=1, column=1)
    flag3()
    btn2 = Button(root, text='Click me', command=flaggo6, fg='white', bg='black', font=('Tahoma', 30))
    btn2.grid(row=2, column=0)
    btn6 = Button(root, text='HELP', command=help3, fg='white', bg='black', font=('Tahoma', 30))
    btn6.grid(row=2, column=1)


def start4():
    pen.up()
    pen.reset()
    pen.pensize(5)
    pen.goto(100, 0)
    pen.pd()
    lbl5.destroy()
    rd.destroy()
    rd2.destroy()
    rd3.destroy()
    rd4.destroy()
    rd5.destroy()
    rd6.destroy()
    lbl6.destroy()
    btn5.destroy()
    btn18.destroy()

    lbl4 = Label(root, text='3', fg='white', bg='black', font=('Tahoma', 50))
    lbl4.pack()

    pen.speed(200)
    pen.bk(100)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)
    pen.bk(100)
    pen.rt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)

    time.sleep(1)
    pen.reset()
    pen.speed(200)
    pen.pensize(5)
    pen.up()
    pen.goto(100, 0)
    pen.pd()
    lbl4.configure(text='2')

    pen.lt(180)
    pen.fd(180)
    pen.rt(135)
    pen.fd(230)
    pen.lt(45)
    pen.fd(60)
    pen.lt(90)
    pen.fd(160)
    pen.lt(90)
    pen.fd(60)

    time.sleep(1)
    pen.reset()

    pen.speed(200)
    pen.pensize(5)
    pen.up()
    pen.goto(0, 0)
    pen.pd()

    lbl4.configure(text='1')
    pen.lt(90)
    pen.fd(200)
    pen.lt(135)
    pen.fd(90)

    time.sleep(1)
    lbl4.destroy()

    def help4():
        global helps
        global coins
        global points
        if helps >= 1:
            points += 1
            coins += 10
            flags4.remove(flag4)
            helps -= 1
            read = 'Correct\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
            messagebox.showinfo('Nice', message=read)
            if len(flags4) == 0 and lives > 0:
                rs = tk.messagebox.askyesno("WIN", "You won! Do you want to try again?")
                if rs == True:
                    welcome()
                else:
                    time.sleep(1)
                    quit()
            elif lives == 0:
                rs = tk.messagebox.askyesno("LOSE", "You lost! Do you want to try again?")
                if rs == True:
                    welcome()
                else:
                    time.sleep(1)
                    quit()
            else:
                change4()

        else:
            messagebox.showerror('Error', message='You have run out of helps')

    def flaggo8():
        global lock
        global answer
        global flag4
        answer = entr.get()
        lock = 0
        entr.delete(0, 'end')
        flaggo7(flags4)

    global lbl2
    global lbl3
    global entr
    global btn2
    global btn6

    lbl2 = Label(root, text='Flag', fg='white', bg='black', font=('Tahoma', 30), width=33)
    lbl2.grid(column=0, row=0, columnspan=2)
    lbl3 = Label(root, text='Type the country:', fg='white', bg='black', font=('Tahoma', 30))
    lbl3.grid(row=1, column=0)
    entr = Entry(root, font=('Tahoma', 20))
    entr.grid(row=1, column=1)
    flag4()
    btn2 = Button(root, text='Click me', command=flaggo8, fg='white', bg='black', font=('Tahoma', 30))
    btn2.grid(row=2, column=0)
    btn6 = Button(root, text='HELP', command=help4, fg='white', bg='black', font=('Tahoma', 30))
    btn6.grid(row=2, column=1)


def start5():
    pen.up()
    pen.reset()
    pen.pensize(5)
    pen.goto(100, 0)
    pen.pd()
    lbl5.destroy()
    rd.destroy()
    rd2.destroy()
    rd3.destroy()
    rd4.destroy()
    rd5.destroy()
    rd6.destroy()
    lbl6.destroy()
    btn5.destroy()
    btn18.destroy()

    lbl4 = Label(root, text='3', fg='white', bg='black', font=('Tahoma', 50))
    lbl4.pack()

    pen.speed(200)
    pen.bk(100)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)
    pen.bk(100)
    pen.rt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)

    time.sleep(1)
    pen.reset()
    pen.speed(200)
    pen.pensize(5)
    pen.up()
    pen.goto(100, 0)
    pen.pd()
    lbl4.configure(text='2')

    pen.lt(180)
    pen.fd(180)
    pen.rt(135)
    pen.fd(230)
    pen.lt(45)
    pen.fd(60)
    pen.lt(90)
    pen.fd(160)
    pen.lt(90)
    pen.fd(60)

    time.sleep(1)
    pen.reset()

    pen.speed(200)
    pen.pensize(5)
    pen.up()
    pen.goto(0, 0)
    pen.pd()

    lbl4.configure(text='1')
    pen.lt(90)
    pen.fd(200)
    pen.lt(135)
    pen.fd(90)

    time.sleep(1)
    lbl4.destroy()

    def help5():
        global helps
        global coins
        global points
        if helps >= 1:
            points += 1
            coins += 10
            flags5.remove(flag5)
            helps -= 1
            read = 'Correct\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
            messagebox.showinfo('Nice', message=read)
            if len(flags5) == 0 and lives > 0:
                rs = tk.messagebox.askyesno("WIN", "You won! Do you want to try again?")
                if rs == True:
                    welcome()
                else:
                    time.sleep(1)
                    quit()
            elif lives == 0:
                rs = tk.messagebox.askyesno("LOSE", "You lost! Do you want to try again?")
                if rs == True:
                    welcome()
                else:
                    time.sleep(1)
                    quit()
            else:
                change5()

        else:
            messagebox.showerror('Error', message='You have run out of helps')

    def flaggo10():
        global lock
        global answer
        global flag5
        answer = entr.get()
        lock = 0
        entr.delete(0, 'end')
        flaggo9(flags5)

    global lbl2
    global lbl3
    global entr
    global btn2
    global btn6

    lbl2 = Label(root, text='Flag', fg='white', bg='black', font=('Tahoma', 30), width=33)
    lbl2.grid(column=0, row=0, columnspan=2)
    lbl3 = Label(root, text='Type the country:', fg='white', bg='black', font=('Tahoma', 30))
    lbl3.grid(row=1, column=0)
    entr = Entry(root, font=('Tahoma', 20))
    entr.grid(row=1, column=1)
    flag5()
    btn2 = Button(root, text='Click me', command=flaggo10, fg='white', bg='black', font=('Tahoma', 30))
    btn2.grid(row=2, column=0)
    btn6 = Button(root, text='HELP', command=help5, fg='white', bg='black', font=('Tahoma', 30))
    btn6.grid(row=2, column=1)


def start6():
    pen.up()
    pen.reset()
    pen.pensize(5)
    pen.goto(100, 0)
    pen.pd()
    lbl5.destroy()
    rd.destroy()
    rd2.destroy()
    rd3.destroy()
    rd4.destroy()
    rd5.destroy()
    rd6.destroy()
    lbl6.destroy()
    btn5.destroy()
    btn18.destroy()

    lbl4 = Label(root, text='3', fg='white', bg='black', font=('Tahoma', 50))
    lbl4.pack()

    pen.speed(200)
    pen.bk(100)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)
    pen.bk(100)
    pen.rt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)

    time.sleep(1)
    pen.reset()
    pen.speed(200)
    pen.pensize(5)
    pen.up()
    pen.goto(100, 0)
    pen.pd()
    lbl4.configure(text='2')

    pen.lt(180)
    pen.fd(180)
    pen.rt(135)
    pen.fd(230)
    pen.lt(45)
    pen.fd(60)
    pen.lt(90)
    pen.fd(160)
    pen.lt(90)
    pen.fd(60)

    time.sleep(1)
    pen.reset()

    pen.speed(200)
    pen.pensize(5)
    pen.up()
    pen.goto(0, 0)
    pen.pd()

    lbl4.configure(text='1')
    pen.lt(90)
    pen.fd(200)
    pen.lt(135)
    pen.fd(90)

    time.sleep(1)
    lbl4.destroy()

    def help6():
        global helps
        global coins
        global points
        if helps >= 1:
            points += 1
            coins += 10
            flags6.remove(flag6)
            helps -= 1
            read = 'Correct\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
            messagebox.showinfo('Nice', message=read)
            if len(flags6) == 0 and lives > 0:
                rs = tk.messagebox.askyesno("WIN", "You won! Do you want to try again?")
                if rs == True:
                    welcome()
                else:
                    time.sleep(1)
                    quit()
            elif lives == 0:
                rs = tk.messagebox.askyesno("LOSE", "You lost! Do you want to try again?")
                if rs == True:
                    welcome()
                else:
                    time.sleep(1)
                    quit()
            else:
                change6()

        else:
            messagebox.showerror('Error', message='You have run out of helps')

    def flaggo12():
        global lock
        global answer
        global flag6
        answer = entr.get()
        lock = 0
        entr.delete(0, 'end')
        flaggo11(flags6)

    global lbl2
    global lbl3
    global entr
    global btn2
    global btn6

    lbl2 = Label(root, text='Flag', fg='white', bg='black', font=('Tahoma', 30), width=33)
    lbl2.grid(column=0, row=0, columnspan=2)
    lbl3 = Label(root, text='Type the country:', fg='white', bg='black', font=('Tahoma', 30))
    lbl3.grid(row=1, column=0)
    entr = Entry(root, font=('Tahoma', 20))
    entr.grid(row=1, column=1)
    flag6()
    btn2 = Button(root, text='Click me', command=flaggo12, fg='white', bg='black', font=('Tahoma', 30))
    btn2.grid(row=2, column=0)
    btn6 = Button(root, text='HELP', command=help6, fg='white', bg='black', font=('Tahoma', 30))
    btn6.grid(row=2, column=1)


def france():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.pd()
    pen.speed(100)
    pen.fillcolor('blue')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.fillcolor('white')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.fillcolor('red')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()


def belgium():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.pd()
    pen.speed(200)
    pen.fillcolor('black')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(200)
    pen.fillcolor('yellow')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(200)
    pen.fillcolor('red')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()


def japan():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.pd()
    pen.speed(100)
    pen.fillcolor('white')
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.up()
    pen.goto(-100, 30)
    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.pencolor('red')
    pen.dot(150)
    pen.up()
    pen.goto(600, 500)


def ireland():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.pd()
    pen.speed(100)
    pen.fillcolor('green')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.fillcolor('white')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.fillcolor('orange')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()


def romania():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.pd()
    pen.speed(100)
    pen.fillcolor('blue')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.fillcolor('yellow')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.fillcolor('red')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()


def italy():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.pd()
    pen.speed(100)
    pen.fillcolor('green')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.fillcolor('white')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.fillcolor('red')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()


def sweden():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.pd()
    pen.speed(200)
    pen.begin_fill()
    pen.fillcolor('blue')
    for i in range(2):
        pen.fd(350)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.end_fill()

    pen.up()
    pen.lt(90)
    pen.fd(100)
    pen.rt(90)
    pen.fillcolor('yellow')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(350)
        pen.lt(90)
        pen.fd(50)
        pen.lt(90)
    pen.end_fill()

    pen.up()
    pen.rt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(125)
    pen.lt(90)

    pen.fillcolor('yellow')
    pen.pencolor('yellow')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(250)
        pen.lt(90)
        pen.fd(50)
        pen.lt(90)
    pen.end_fill()
    pen.up()


def finland():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.pd()
    pen.speed(200)
    pen.begin_fill()
    pen.fillcolor('white')
    for i in range(2):
        pen.fd(350)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.end_fill()

    pen.up()
    pen.lt(90)
    pen.fd(100)
    pen.rt(90)
    pen.fillcolor('blue')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(350)
        pen.lt(90)
        pen.fd(50)
        pen.lt(90)
    pen.end_fill()

    pen.up()
    pen.rt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(125)
    pen.lt(90)

    pen.fillcolor('blue')
    pen.pencolor('blue')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(250)
        pen.lt(90)
        pen.fd(50)
        pen.lt(90)
    pen.end_fill()
    pen.up()


def england():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.pd()
    pen.speed(200)
    pen.begin_fill()
    pen.fillcolor('white')
    pen.pencolor('black')
    for i in range(2):
        pen.fd(350)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.end_fill()

    pen.up()
    pen.lt(90)
    pen.fd(100)
    pen.rt(90)
    pen.fillcolor('red')
    pen.pencolor('white')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(350)
        pen.lt(90)
        pen.fd(50)
        pen.lt(90)
    pen.end_fill()

    pen.up()
    pen.rt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(200)
    pen.lt(90)

    pen.fillcolor('red')
    pen.pencolor('red')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(250)
        pen.lt(90)
        pen.fd(50)
        pen.lt(90)
    pen.end_fill()
    pen.up()


def iceland():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.pd()
    pen.speed(200)
    pen.begin_fill()
    pen.fillcolor('blue')
    pen.pencolor('black')
    for i in range(2):
        pen.fd(350)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.end_fill()

    pen.up()
    pen.lt(90)
    pen.fd(100)
    pen.rt(90)
    pen.fillcolor('red')
    pen.pencolor('red')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(350)
        pen.lt(90)
        pen.fd(50)
        pen.lt(90)
    pen.end_fill()

    pen.up()
    pen.rt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(125)
    pen.lt(90)

    pen.fillcolor('red')
    pen.pencolor('red')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(250)
        pen.lt(90)
        pen.fd(50)
        pen.lt(90)
    pen.end_fill()
    pen.up()


def luxembourg():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.speed(100)
    pen.fillcolor('light blue')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('white')
    pen.pencolor('black')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('red')
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)


def norway():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.pd()
    pen.speed(200)
    pen.begin_fill()
    pen.fillcolor('red')
    pen.pencolor('black')
    for i in range(2):
        pen.fd(350)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.end_fill()

    pen.up()
    pen.lt(90)
    pen.fd(100)
    pen.rt(90)
    pen.fillcolor('blue')
    pen.pencolor('blue')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(350)
        pen.lt(90)
        pen.fd(50)
        pen.lt(90)
    pen.end_fill()

    pen.up()
    pen.rt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(125)
    pen.lt(90)

    pen.fillcolor('blue')
    pen.pencolor('blue')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(250)
        pen.lt(90)
        pen.fd(50)
        pen.lt(90)
    pen.end_fill()
    pen.up()


def netherlands():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.speed(100)
    pen.fillcolor('blue')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('white')
    pen.pencolor('black')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('red')
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)


def monaco():
    pen.reset()
    pen.up()
    pen.goto(-150, -100)

    pen.speed(200)
    pen.fillcolor('white')
    pen.pencolor('black')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(280)
        pen.lt(90)
        pen.fd(125)
        pen.lt(90)
    pen.end_fill()
    pen.up()

    pen.lt(90)
    pen.fd(125)
    pen.rt(90)

    pen.fillcolor('red')
    pen.pencolor('red')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(280)
        pen.lt(90)
        pen.fd(125)
        pen.lt(90)
    pen.end_fill()
    pen.up()


def poland():
    pen.reset()
    pen.goto(-150, -100)

    pen.speed(200)
    pen.fillcolor('red')
    pen.pencolor('red')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(280)
        pen.lt(90)
        pen.fd(125)
        pen.lt(90)
    pen.end_fill()
    pen.up()

    pen.lt(90)
    pen.fd(125)
    pen.rt(90)

    pen.fillcolor('white')
    pen.pencolor('black')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(280)
        pen.lt(90)
        pen.fd(125)
        pen.lt(90)
    pen.end_fill()
    pen.up()


def germany():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.speed(100)
    pen.fillcolor('yellow')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('red')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('black')
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)


def austria():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.speed(100)
    pen.fillcolor('red')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('white')
    pen.pencolor('black')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('red')
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)


def estonia():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.speed(100)
    pen.fillcolor('white')
    pen.pencolor('black')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('black')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('blue')
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)


def bulgaria():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.speed(100)
    pen.fillcolor('red')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('green')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('white')
    pen.pencolor('black')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)


def hungary():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.speed(100)
    pen.fillcolor('green')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('white')
    pen.pencolor('black')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('red')
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)


def lithuania():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.speed(100)
    pen.fillcolor('red')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('green')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('yellow')
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)


def mali():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.pd()
    pen.speed(100)
    pen.fillcolor('green')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.fillcolor('yellow')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.fillcolor('red')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()


def guinea():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.pd()
    pen.speed(100)
    pen.fillcolor('red')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.fillcolor('yellow')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.fillcolor('green')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()


def nigeria():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.pd()
    pen.speed(100)
    pen.fillcolor('green')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.fillcolor('white')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.fillcolor('green')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()


def ivory_coast():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.pd()
    pen.speed(100)
    pen.fillcolor('orange')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.fillcolor('white')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.fillcolor('green')
    pen.begin_fill()
    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()


def gabon():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.speed(100)
    pen.fillcolor('light blue')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('yellow')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('green')
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)


def sierra_leone():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.speed(100)
    pen.fillcolor('light blue')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('white')
    pen.pencolor('black')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('green')
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)


def yemen():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.speed(100)
    pen.fillcolor('black')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('white')
    pen.pencolor('black')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('red')
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)


def russia():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.speed(100)
    pen.fillcolor('red')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('blue')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('white')
    pen.pencolor('black')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)


def armenia():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.speed(100)
    pen.fillcolor('yellow')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('blue')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)

    pen.fillcolor('red')
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.lt(90)
        pen.fd(70)
        pen.lt(90)
    pen.up()
    pen.end_fill()

    pen.lt(90)
    pen.fd(70)
    pen.rt(90)


def indonesia():
    pen.reset()
    pen.up()
    pen.goto(-150, -100)

    pen.speed(200)
    pen.fillcolor('white')
    pen.pencolor('black')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(280)
        pen.lt(90)
        pen.fd(125)
        pen.lt(90)
    pen.end_fill()
    pen.up()

    pen.lt(90)
    pen.fd(125)
    pen.rt(90)

    pen.fillcolor('red')
    pen.pencolor('red')
    pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(280)
        pen.lt(90)
        pen.fd(125)
        pen.lt(90)
    pen.end_fill()
    pen.up()


def bangladesh():
    pen.reset()

    pen.up()
    pen.goto(-150, -100)

    pen.pd()
    pen.speed(100)
    pen.fillcolor('dark green')
    pen.begin_fill()
    for i in range(2):
        pen.fd(340)
        pen.lt(90)
        pen.fd(250)
        pen.lt(90)
    pen.pd()
    pen.end_fill()

    pen.up()
    pen.goto(-130, 30)
    pen.fd(100)
    pen.pd()
    pen.speed(100)
    pen.pencolor('red')
    pen.dot(150)
    pen.up()
    pen.goto(600, 500)


flags = [france, belgium, luxembourg, ireland, romania, italy, sweden, finland, england, iceland]
flags2 = [norway, netherlands, monaco, poland, germany, austria, estonia, bulgaria, hungary, lithuania]
flags3 = [france, belgium, japan, ireland, romania, italy, sweden, finland, england, iceland, norway,
          netherlands,
          monaco, poland, germany, austria, estonia, bulgaria, hungary, lithuania]
flags4 = [mali, nigeria, guinea, ivory_coast, gabon, sierra_leone]
flags5 = [yemen, japan, russia, armenia, indonesia, bangladesh]
flags6 = [france, belgium, luxembourg, ireland, romania, italy, sweden, finland, england, iceland,
          norway, netherlands, monaco, poland, germany, austria, estonia, bulgaria, hungary, lithuania,
          mali, nigeria, guinea, ivory_coast, gabon, sierra_leone, yemen, japan, russia, armenia,
          indonesia, bangladesh]

flag = random.choice(flags)
flag2 = random.choice(flags2)
flag3 = random.choice(flags3)
flag4 = random.choice(flags4)
flag5 = random.choice(flags5)
flag6 = random.choice(flags6)


def flaggo(flags):
    global lives
    global points
    global lock
    global answer
    global coins

    while lives > 0 and len(flags) > 0:
        if lock == 0:

            if answer == flag.__name__:
                points += 1
                coins += 10
                flags.remove(flag)
                read = 'Correct\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
                messagebox.showinfo('Nice', message=read)

            else:
                if points > 0:
                    points -= 1
                else:
                    points = 0
                lives -= 1
                coins -= 5
                read = 'False\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
                messagebox.showinfo('Bad', message=read)

            lock = 1

        else:
            break
    if len(flags) == 0 and lives > 0:
        rs = tk.messagebox.askyesno("WIN", "You won! Do you want to try again?")
        if rs == True:
            welcome()
        else:
            time.sleep(1)
            quit()
    elif lives == 0:
        rs = tk.messagebox.askyesno("LOSE", "You lost! Do you want to try again?")
        if rs == True:
            welcome()
        else:
            time.sleep(1)
            quit()
    else:
        change()


def flaggo3(flags2):
    global lives
    global points
    global lock
    global answer
    global coins

    while lives > 0 and len(flags2) > 0:
        if lock == 0:

            if answer == flag2.__name__:
                points += 1
                flags2.remove(flag2)
                coins += 10
                read = 'Correct\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
                messagebox.showinfo('Nice', message=read)

            else:
                if points > 0:
                    points -= 1
                else:
                    points = 0
                lives -= 1
                coins -= 5
                read = 'False\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
                messagebox.showinfo('Bad', message=read)

            lock = 1

        else:
            break
    if len(flags2) == 0 and lives > 0:
        rs = tk.messagebox.askyesno("WIN", "You won! Do you want to try again?")
        if rs == True:
            welcome()
        else:
            time.sleep(1)
            quit()
    elif lives == 0:
        rs = tk.messagebox.askyesno("LOSE", "You lost! Do you want to try again?")
        if rs == True:
            welcome()
        else:
            time.sleep(1)
            quit()
    else:
        change2()


def flaggo5(flags3):
    global lives
    global points
    global lock
    global answer
    global coins

    while lives > 0 and len(flags3) > 0:
        if lock == 0:

            if answer == flag3.__name__:
                points += 1
                flags3.remove(flag3)
                coins += 10
                read = 'Correct\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
                messagebox.showinfo('Nice', message=read)


            else:
                if points > 0:
                    points -= 1
                else:
                    points = 0
                lives -= 1
                coins -= 5
                read = 'False\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
                messagebox.showinfo('Bad', message=read)

            lock = 1

        else:
            break
    if len(flags3) == 0 and lives > 0:
        rs = tk.messagebox.askyesno("WIN", "You won! Do you want to try again?")
        if rs == True:
            welcome()
        else:
            time.sleep(1)
            quit()
    elif lives == 0:
        rs = tk.messagebox.askyesno("LOSE", "You lost! Do you want to try again?")
        if rs == True:
            welcome()
        else:
            time.sleep(1)
            quit()
    else:
        change3()


def flaggo7(flags4):
    global lives
    global points
    global lock
    global answer
    global coins

    while lives > 0 and len(flags4) > 0:
        if lock == 0:

            if answer == flag4.__name__:
                points += 1
                flags4.remove(flag4)
                coins += 10
                read = 'Correct\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
                messagebox.showinfo('Nice', message=read)

            else:
                if points > 0:
                    points -= 1
                else:
                    points = 0
                lives -= 1
                coins -= 5
                read = 'False\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
                messagebox.showinfo('Bad', message=read)

            lock = 1

        else:
            break
    if len(flags4) == 0 and lives > 0:
        rs = tk.messagebox.askyesno("WIN", "You won! Do you want to try again?")
        if rs == True:
            welcome()
        else:
            time.sleep(1)
            quit()
    elif lives == 0:
        rs = tk.messagebox.askyesno("LOSE", "You lost! Do you want to try again?")
        if rs == True:
            welcome()
        else:
            time.sleep(1)
            quit()
    else:
        change4()


def flaggo9(flags5):
    global lives
    global points
    global lock
    global answer
    global coins

    while lives > 0 and len(flags5) > 0:
        if lock == 0:

            if answer == flag5.__name__:
                points += 1
                flags5.remove(flag5)
                coins += 10
                read = 'Correct\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
                messagebox.showinfo('Nice', message=read)


            else:
                if points > 0:
                    points -= 1
                else:
                    points = 0
                lives -= 1
                coins -= 5
                read = 'False\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
                messagebox.showinfo('Bad', message=read)

            lock = 1

        else:
            break
    if len(flags5) == 0 and lives > 0:
        rs = tk.messagebox.askyesno("WIN", "You won! Do you want to try again?")
        if rs == True:
            welcome()
        else:
            time.sleep(1)
            quit()
    elif lives == 0:
        rs = tk.messagebox.askyesno("LOSE", "You lost! Do you want to try again?")
        if rs == True:
            welcome()
        else:
            time.sleep(1)
            quit()
    else:
        change5()


def flaggo11(flags6):
    global lives
    global points
    global lock
    global answer
    global coins

    while lives > 0 and len(flags6) > 0:
        if lock == 0:

            if answer == flag6.__name__:
                points += 1
                flags6.remove(flag6)
                coins += 10
                read = 'Correct\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
                messagebox.showinfo('Nice', message=read)

            else:
                if points > 0:
                    points -= 1
                else:
                    points = 0
                lives -= 1
                coins -= 5
                read = 'False\nLives:', lives, '\nPoints:', points, '\nHelps:', helps, '\nCoins:', coins
                messagebox.showinfo('Bad', message=read)

            lock = 1

        else:
            break
    if len(flags6) == 0 and lives > 0:
        rs = tk.messagebox.askyesno("WIN", "You won! Do you want to try again?")
        if rs == True:
            welcome()
        else:
            time.sleep(1)
            quit()
    elif lives == 0:
        rs = tk.messagebox.askyesno("LOSE", "You lost! Do you want to try again?")
        if rs == True:
            welcome()
        else:
            time.sleep(1)
            quit()
    else:
        change6()


def check(quiz):
    global m

    m = quiz.get()

    if m == 'Quiz 1':
        start()
    elif m == 'Quiz 2':
        start2()
    elif m == 'Quiz 3':
        start3()
    elif m == 'Quiz 4':
        start4()
    elif m == 'Quiz 5':
        start5()
    elif m == 'Quiz 6':
        start6()


def button(*args):
    check(quiz)


def buy():
    global coins
    global helps
    if coins >= 50:
        helps += 1
        coins -= 50

        lbl13.configure(text=helps)
        lbl14.configure(text=coins)
        messagebox.showinfo('Purchase', message='Successful')
    else:
        messagebox.showerror('Error', message='You do not have enough coins')


def buy2():
    global coins
    global helps
    if coins >= 100:
        helps += 2
        coins -= 100

        lbl13.configure(text=helps)
        lbl14.configure(text=coins)
        messagebox.showinfo('Purchase', message='Successful')
    else:
        messagebox.showerror('Error', message='You do not have enough coins')


def buy3():
    global coins
    global helps
    if coins >= 150:
        helps += 4
        coins -= 150

        lbl13.configure(text=helps)
        lbl14.configure(text=coins)
        messagebox.showinfo('Purchase', message='Successful')
    else:
        messagebox.showerror('Error', message='You do not have enough coins')


def buy4():
    global coins
    global helps
    if coins >= 200:
        helps += 5
        coins -= 200

        lbl13.configure(text=helps)
        lbl14.configure(text=coins)
        messagebox.showinfo('Purchase', message='Successful')
    else:
        messagebox.showerror('Error', message='You do not have enough coins')


def info():
    global k
    k = 3

    global lbl16
    global lbl17
    global btn17
    lbl5.destroy()
    rd.destroy()
    rd2.destroy()
    rd3.destroy()
    rd4.destroy()
    rd5.destroy()
    rd6.destroy()
    lbl6.destroy()
    btn5.destroy()
    btn18.destroy()
    pen.up()
    pen.reset()
    pen.pensize(5)
    pen.goto(100, 0)
    pen.pd()

    lbl4 = Label(root, text='3', fg='white', bg='black', font=('Tahoma', 50))
    lbl4.pack()

    pen.speed(200)
    pen.bk(100)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)
    pen.bk(100)
    pen.rt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)

    time.sleep(1)
    pen.reset()
    pen.speed(200)
    pen.pensize(5)
    pen.up()
    pen.goto(100, 0)
    pen.pd()
    lbl4.configure(text='2')

    pen.lt(180)
    pen.fd(180)
    pen.rt(135)
    pen.fd(230)
    pen.lt(45)
    pen.fd(60)
    pen.lt(90)
    pen.fd(160)
    pen.lt(90)
    pen.fd(60)

    time.sleep(1)
    pen.reset()

    pen.speed(200)
    pen.pensize(5)
    pen.up()
    pen.goto(0, 0)
    pen.pd()

    lbl4.configure(text='1')
    pen.lt(90)
    pen.fd(200)
    pen.lt(135)
    pen.fd(90)

    time.sleep(1)
    lbl4.destroy()
    pen.reset()
    pen.pensize(5)
    pen.speed(200)
    pen.up()
    pen.goto(-280, -50)

    pen.pd()
    pen.lt(90)
    pen.fd(200)

    pen.up()
    pen.rt(90)
    pen.fd(70)
    pen.pd()

    pen.rt(90)
    pen.fd(200)
    pen.bk(200)
    pen.lt(35)
    pen.fd(240)
    pen.lt(145)
    pen.fd(200)

    pen.up()
    pen.rt(90)
    pen.fd(70)
    pen.pd()

    pen.fd(80)
    pen.bk(80)
    pen.rt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(80)
    pen.bk(80)
    pen.rt(90)
    pen.fd(100)

    pen.up()
    pen.lt(90)
    pen.fd(150)
    pen.pd()

    for i in range(2):
        pen.fd(120)
        pen.lt(90)
        pen.fd(200)
        pen.lt(90)

    lbl16 = Label(root, text='INFO', fg='white', bg='black', font=('Tahoma', 25))
    lbl16.pack()
    lbl17 = Label(root, text='Both Quiz 1 and Quiz 2 have 10 european countries,\nQuiz 2 is a bit harder than Quiz '
                             '1.\nQuiz 3 has 20 countries\nQuiz 4 has 6 African countries\nQuiz 5 has 6 Asian '
                             'countries\nQuiz 6 has 32 countries(LEVEL IMPOSSIBLE)', fg='white', bg='black',
                  font=('Tahoma', 25))
    lbl17.pack()
    btn17 = Button(root, text='Return', command=welcome, fg='white', bg='black', font=('Tahoma', 25))
    btn17.pack()


def store():
    global k
    k = 2

    pen.up()
    pen.reset()
    pen.pensize(5)
    pen.goto(100, 0)
    pen.pd()
    lbl5.destroy()
    rd.destroy()
    rd2.destroy()
    rd3.destroy()
    rd4.destroy()
    rd5.destroy()
    rd6.destroy()
    lbl6.destroy()
    btn5.destroy()
    btn18.destroy()
    lbl4 = Label(root, text='3', fg='white', bg='black', font=('Tahoma', 50))
    lbl4.pack()

    pen.speed(200)
    pen.bk(100)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)
    pen.bk(100)
    pen.rt(90)
    pen.fd(100)
    pen.lt(90)
    pen.fd(100)

    time.sleep(1)
    pen.reset()
    pen.speed(200)
    pen.pensize(5)
    pen.up()
    pen.goto(100, 0)
    pen.pd()
    lbl4.configure(text='2')

    pen.lt(180)
    pen.fd(180)
    pen.rt(135)
    pen.fd(230)
    pen.lt(45)
    pen.fd(60)
    pen.lt(90)
    pen.fd(160)
    pen.lt(90)
    pen.fd(60)

    time.sleep(1)
    pen.reset()

    pen.speed(200)
    pen.pensize(5)
    pen.up()
    pen.goto(0, 0)
    pen.pd()

    lbl4.configure(text='1')
    pen.lt(90)
    pen.fd(200)
    pen.lt(135)
    pen.fd(90)

    time.sleep(1)
    lbl4.destroy()
    pen.reset()
    pen.speed(200)
    pen.pensize(5)

    pen.up()
    pen.goto(-350, 0)
    pen.pd()

    pen.fd(100)
    pen.lt(90)
    pen.fd(80)
    pen.lt(90)
    pen.fd(100)
    pen.rt(90)
    pen.fd(80)
    pen.rt(90)
    pen.fd(100)

    pen.up()
    pen.fd(40)
    pen.pd()

    pen.fd(100)
    pen.bk(50)
    pen.rt(90)
    pen.fd(160)

    pen.lt(90)
    pen.up()
    pen.fd(90)
    pen.pd()

    for i in range(2):
        pen.fd(100)
        pen.lt(90)
        pen.fd(160)
        pen.lt(90)

    pen.up()
    pen.fd(140)
    pen.pd()

    pen.lt(90)
    pen.fd(160)
    for i in range(3):
        pen.rt(90)
        pen.fd(80)
    pen.lt(135)
    pen.fd(100)

    pen.up()
    pen.lt(45)
    pen.fd(40)
    pen.pd()

    pen.fd(100)
    pen.bk(100)
    pen.lt(90)
    pen.fd(75)
    pen.rt(90)
    pen.fd(100)
    pen.bk(100)
    pen.lt(90)
    pen.fd(75)
    pen.rt(90)
    pen.fd(100)
    global coins
    global helps
    lbl5.destroy()
    rd.destroy()
    rd2.destroy()
    rd3.destroy()
    rd4.destroy()
    rd5.destroy()
    rd6.destroy()
    lbl6.destroy()
    btn5.destroy()
    global lbl8
    global lbl9
    global lbl10
    global lbl11
    global lbl12
    global lbl13
    global lbl14
    global btn8
    global btn9
    global btn10
    global btn11
    global btn12

    lbl8 = Label(root, text='Store', fg='white', bg='black', font=('Tahoma', 25), width=40, justify='center')
    lbl8.grid(row=0, column=0, columnspan=3, padx=10)
    lbl9 = Label(root, text='1 Help', fg='white', bg='black', font=('Tahoma', 25))
    lbl9.grid(row=1, column=0, padx=10)
    lbl10 = Label(root, text='2 Helps', fg='white', bg='black', font=('Tahoma', 25))
    lbl10.grid(row=2, column=0, padx=10)
    lbl11 = Label(root, text='4 Helps', fg='white', bg='black', font=('Tahoma', 25))
    lbl11.grid(row=3, column=0, padx=10)
    lbl12 = Label(root, text='5 Helps', fg='white', bg='black', font=('Tahoma', 25))
    lbl12.grid(row=4, column=0, padx=10)
    btn8 = Button(root, text='50 Coins', command=buy, fg='white', bg='black', font=('Tahoma', 25))
    btn8.grid(row=1, column=1, padx=10)
    btn9 = Button(root, text='100 Coins', command=buy2, fg='white', bg='black', font=('Tahoma', 25))
    btn9.grid(row=2, column=1, padx=10)
    btn10 = Button(root, text='150 Coins', command=buy3, fg='white', bg='black', font=('Tahoma', 25))
    btn10.grid(row=3, column=1, padx=10)
    btn11 = Button(root, text='200 Coins', command=buy4, fg='white', bg='black', font=('Tahoma', 25))
    btn11.grid(row=4, column=1, padx=10)
    lbl13 = Label(root, text=helps, fg='white', bg='black', font=('Tahoma', 25), relief='sunken')
    lbl13.grid(row=5, column=0, padx=10)
    lbl14 = Label(root, text=coins, fg='white', bg='black', font=('Tahoma', 25), relief='sunken')
    lbl14.grid(row=5, column=1, padx=10)
    btn12 = Button(root, text='Return', command=welcome, fg='white', bg='black', font=('Tahoma', 25))
    btn12.grid(row=1, column=2, rowspan=4, padx=10)


def welcome():
    global k
    pen.reset()

    if k == 0:
        lbl.destroy()
        btn.destroy()
        btn0.destroy()
        k = 1
    elif k == 2:
        lbl8.destroy()
        lbl9.destroy()
        lbl10.destroy()
        lbl11.destroy()
        lbl12.destroy()
        lbl13.destroy()
        lbl14.destroy()
        btn8.destroy()
        btn9.destroy()
        btn10.destroy()
        btn11.destroy()
        btn12.destroy()
        k = 1
    elif k == 3:
        lbl16.destroy()
        lbl17.destroy()
        btn17.destroy()
        k = 1
    else:
        lbl2.destroy()
        lbl3.destroy()
        entr.destroy()
        btn2.destroy()
        btn6.destroy()
    global quiz
    global lbl5
    global rd
    global rd2
    global rd3
    global rd4
    global rd5
    global rd6
    global lbl6
    global btn5
    global btn18
    global lives
    global points
    global helps
    pen.reset()
    pen.up()
    pen.goto(-330, 0)
    pen.pd()

    pen.speed(200)
    pen.pensize(5)

    pen.lt(90)
    pen.fd(200)
    pen.rt(150)
    pen.fd(120)
    pen.lt(120)
    pen.fd(120)
    pen.rt(150)
    pen.fd(200)

    pen.up()
    pen.lt(90)
    pen.fd(50)
    pen.pd()

    pen.fd(100)
    pen.bk(100)
    pen.lt(90)
    pen.fd(100)
    pen.rt(90)
    pen.fd(100)
    pen.bk(100)
    pen.lt(90)
    pen.fd(100)
    pen.rt(90)
    pen.fd(100)

    pen.up()
    pen.fd(50)
    pen.rt(90)
    pen.pd()

    pen.fd(200)
    pen.bk(200)
    pen.lt(35)
    pen.fd(240)
    pen.lt(145)
    pen.fd(200)

    pen.up()
    pen.rt(90)
    pen.fd(50)
    pen.rt(90)
    pen.pd()

    pen.fd(200)
    pen.lt(90)
    pen.fd(140)
    pen.lt(90)
    pen.fd(200)

    lives = 3
    points = 0
    quiz = tk.StringVar(root)
    quiz.set('')
    quiz.trace("w", button)
    lbl5 = tk.Label(root, text='Choose quiz', fg='white', bg='black', font=('Tahoma', 35), width=28)
    lbl5.grid(row=0, column=0, columnspan=3)
    rd = tk.Radiobutton(root, text='Quiz 1', value='Quiz 1', variable=quiz, fg='white', bg='black', font=('Tahoma', 35))
    rd.grid(row=1, column=0)
    rd2 = tk.Radiobutton(root, text='Quiz 2', value='Quiz 2', variable=quiz, fg='white', bg='black',
                         font=('Tahoma', 35))
    rd2.grid(row=1, column=1)
    rd3 = tk.Radiobutton(root, text='Quiz 3', value='Quiz 3', variable=quiz, fg='white', bg='black',
                         font=('Tahoma', 35))
    rd3.grid(row=1, column=2)
    rd4 = tk.Radiobutton(root, text='Quiz 4', value='Quiz 4', variable=quiz, fg='white', bg='black',
                         font=('Tahoma', 35))
    rd4.grid(row=2, column=0)
    rd5 = tk.Radiobutton(root, text='Quiz 5', value='Quiz 5', variable=quiz, fg='white', bg='black',
                         font=('Tahoma', 35))
    rd5.grid(row=2, column=1)
    rd6 = tk.Radiobutton(root, text='Quiz 6', value='Quiz 6', variable=quiz, fg='white', bg='black',
                         font=('Tahoma', 35))
    rd6.grid(row=2, column=2)
    lbl6 = tk.Label(root, text='Click the quiz', fg='white', bg='black', font=('Tahoma', 35))
    lbl6.grid(row=3, column=0, columnspan=3)
    btn5 = Button(root, text='Store', command=store, fg='white', bg='black', font=('Tahoma', 35))
    btn5.grid(row=4, column=0)
    btn18 = Button(root, text='INFO', command=info, fg='white', bg='black', font=('Tahoma', 35))
    btn18.grid(row=4, column=2)


root = Tk()

root.title('Flag Game')
root.geometry('750x400')
root.configure(background='black')

lbl = tk.Label(root, text='Flag Game', fg='white', bg='black', font=('Tahoma', 50))
lbl.pack(padx=10)

btn = tk.Button(root, text='Start', command=welcome, fg='white', bg='black', font=('Tahoma', 50))
btn.pack(padx=10)

btn0 = Button(root, text='Exit', command=quit, fg='white', bg='black', font=('Tahoma', 50))
btn0.pack(padx=10)

quiz = tk.StringVar()

scr.title('Flag Game')

turtle.done()
