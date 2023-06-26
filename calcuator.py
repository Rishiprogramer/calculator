import keyboard
from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator=""
    text_Input.set("")

def btnEquals():
    global operator
    sum = str(eval(operator))
    text_Input.set(sum)
    operator = sum

def decide_key(key):
    name = key.name
    if key.name == 'enter':
        btnEquals()

    elif name == '+':
        btnClick('+')

    elif name == '-':
        btnClick('-')

    elif name == '*':
        btnClick('*')

    elif name == '/':
        btnClick('/')

    elif name == '1':
        btnClick('1')

    elif name == '2':
        btnClick('2')

    elif name == '3':
        btnClick('3')

    elif name == '4':
        btnClick('4')

    elif name == '5':
        btnClick('5')

    elif name == '6':
        btnClick('6')

    elif name == '7':
        btnClick('7')

    elif name == '8':
        btnClick('8')

    elif name == '9':
        btnClick('9')

    elif name == '0':
        btnClick('0')

    elif name == '.':
        btnClick('.')

    elif name == 'backspace' or name == 'c' or name == 'C':
        btnClear()

    else:
        import winsound
        winsound.PlaySound("wan.wav",0)


if __name__ == '__main__':
    app = Tk()
    app.title("calculator")
    app.resizable(False, False)

    operator = ""
    keyboard.on_press(decide_key)
    text_Input = StringVar()

    txtDisplay = Label(app, font=("arial", 30, "bold"), textvariable=text_Input, bd=30, relief="sunken", width=15,bg="yellow", anchor='e')
    txtDisplay.grid(row=0, column=0, columnspan=4)

    b7 = Button(app, padx=16, pady=16, bd=9, fg="black", font=("arial", 30, "bold"), text="7", command=lambda: btnClick(7))
    b7.grid(row=1, column=0)
    b8 = Button(app, padx=16, pady=16, bd=9, fg="black", font=("arial", 30, "bold"), text="8", command=lambda: btnClick(8))
    b8.grid(row=1, column=1)
    b9 = Button(app, padx=16, pady=16, bd=9, fg="black", font=("arial", 30, "bold"), text="9", command=lambda: btnClick(9))
    b9.grid(row=1, column=2)
    add = Button(app, padx=16, pady=16, bd=9, fg="black", font=("arial", 30, "bold"), text="+", command=lambda: btnClick("+"))
    add.grid(row=1, column=3)

    # second row
    b4 = Button(app, padx=16, pady=16, bd=9, fg="black", font=("arial", 30, "bold"), text="4", command=lambda: btnClick(4))
    b4.grid(row=2, column=0)
    b5 = Button(app, padx=16, pady=16, bd=9, fg="black", font=("arial", 30, "bold"), text="5", command=lambda: btnClick(5))
    b5.grid(row=2, column=1)
    b6 = Button(app, padx=16, pady=16, bd=9, fg="black", font=("arial", 30, "bold"), text="6", command=lambda: btnClick(6))
    b6.grid(row=2, column=2)
    sub = Button(app, padx=16, pady=16, bd=9, fg="black", font=("arial", 30, "bold"), text="-", command=lambda: btnClick("-"))
    sub.grid(row=2, column=3)

    # third row
    b1 = Button(app, padx=16, pady=16, bd=9, fg="black", font=("arial", 30, "bold"), text="1", command=lambda: btnClick(1))
    b1.grid(row=3, column=0)
    b2 = Button(app, padx=16, pady=16, bd=9, fg="black", font=("arial", 30, "bold"), text="2", command=lambda: btnClick(2))
    b2.grid(row=3, column=1)
    b3 = Button(app, padx=16, pady=16, bd=9, fg="black", font=("arial", 30, "bold"), text="3", command=lambda: btnClick(3))
    b3.grid(row=3, column=2)
    mul = Button(app, padx=16, pady=16, bd=9, fg="black", font=("arial", 30, "bold"), text="*", command=lambda: btnClick("*"))
    mul.grid(row=3, column=3)

    # fourth row
    b0 = Button(app, padx=16, pady=16, bd=9, fg="black", font=("arial", 30, "bold"), text="0", command=lambda: btnClick(0))
    b0.grid(row=4, column=0)
    bc = Button(app, padx=16, pady=16, bd=9, fg="black", font=("arial", 30, "bold"), text="C", command=btnClear)
    bc.grid(row=4, column=1)
    be = Button(app, padx=16, pady=16, bd=9, fg="black", font=("arial", 30, "bold"), text="=", command=btnEquals)
    be.grid(row=4, column=2)
    div = Button(app, padx=16, pady=16, bd=9, fg="black", font=("arial", 30, "bold"), text="/", command=lambda: btnClick("/"))
    div.grid(row=4, column=3)
    decimal = Button(app, padx=100, pady=16, bd=9, fg="black", font=("arial", 30, "bold"), text=".", command=lambda: btnClick("."))
    decimal.grid(row=5, column=0, columnspan=4)

    app.mainloop()
