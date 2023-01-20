if __name__=='__main__':

    from tkinter import *

    def btnClick(numbers):
        global operator
        operator = operator + str(numbers)
        text_Input  .set(operator)

    def btnClear():
        global operator
        operator=" "
        text_Input.set("")

    def btnEquals():
        global operator
        sum = str(eval(operator))
        text_Input.set(sum)
        operator = ""

    if __name__ == '__main__':
        app = Tk()
        app.title("calculator")
        app.resizable(False, False)
        operator = ""
        text_Input=StringVar()
        txtDisplay = Entry(app, font=("arial", 30,"bold"), textvariable=text_Input, bd=30, insertwidth=6, bg="yellow", justify="right").grid(columnspan=4)

        b7 = Button(app, padx=16,pady = 16, bd=9, fg="black", font=("arial", 30, "bold"), text="7", command = lambda:btnClick(7)).grid(row=1, column=0)
        b8 = Button(app, padx=16,pady = 16, bd=9, fg="black", font=("arial", 30, "bold"), text="8",command = lambda:btnClick(8)).grid(row=1, column=1)
        b9 = Button(app, padx=16,pady = 16, bd=9, fg="black", font=("arial", 30, "bold"), text="9",command = lambda:btnClick(9)).grid(row=1, column=2)
        add = Button(app, padx=16,pady = 16, bd=9, fg="black", font=("arial", 30, "bold"), text="+",command = lambda:btnClick("+")).grid(row=1, column=3)

        # second row
        b4 = Button(app, padx=16,pady = 16, bd=9, fg="black", font=("arial", 30, "bold"), text="4",command = lambda:btnClick(4)).grid(row=2, column=0)
        b5 = Button(app, padx=16,pady = 16, bd=9, fg="black", font=("arial", 30, "bold"), text="5",command = lambda:btnClick(5)).grid(row=2, column=1)
        b6 = Button(app, padx=16,pady = 16, bd=9, fg="black", font=("arial", 30, "bold"), text="6",command = lambda:btnClick(6)).grid(row=2, column=2)
        sub = Button(app, padx=16,pady = 16, bd=9, fg="black", font=("arial", 30, "bold"), text="-",command = lambda:btnClick("-")).grid(row=2, column=3)

        # third row

        b1 = Button(app, padx=16,pady = 16, bd=9, fg="black", font=("arial", 30, "bold"), text="1",command = lambda:btnClick(1)).grid(row=3, column=0)
        b2 = Button(app, padx=16,pady = 16, bd=9, fg="black", font=("arial", 30, "bold"), text="2",command = lambda:btnClick(2)).grid(row=3, column=1)
        b3 = Button(app, padx=16,pady = 16, bd=9, fg="black", font=("arial", 30, "bold"), text="3",command = lambda:btnClick(3)).grid(row=3, column=2)
        mul = Button(app, padx=16,pady = 16, bd=9, fg="black", font=("arial", 30, "bold"), text="*",command = lambda:btnClick("*")).grid(row=3, column=3)

        # fourth row

        b0 = Button(app, padx=16,pady = 16, bd=9, fg="black", font=("arial", 30, "bold"), text="0",command = lambda:btnClick(0)).grid(row=4, column=0)
        bc = Button(app, padx=16,pady = 16, bd=9, fg="black", font=("arial", 30, "bold"), text="C",command = btnClear).grid(row=4, column=1)
        be = Button(app, padx=16,pady = 16, bd=9, fg="black", font=("arial", 30, "bold"), text="=", command = btnEquals).grid(row=4, column=2)
        div = Button(app, padx=16,pady = 16, bd=9, fg="black", font=("arial", 30, "bold"), text="/",command = lambda:btnClick("/")).grid(row=4, column=3)
        decimal  = Button(app, padx=100,pady = 16, bd=9, fg="black", font=("arial", 30, "bold"), text=".",command = lambda:btnClick(".")).grid(row=5, column=0, columnspan=4)


        app.mainloop()




