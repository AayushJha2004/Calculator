from tkinter import *
import math

calculator_ = Tk()
calculator_.title("Calculator")
# calculator_.geometry("")

input_expression = StringVar()

input_expression_label = Label(calculator_, font="Calibri 20", textvariable=input_expression, justify=LEFT, height=2,
                               width=7)
input_expression_label.grid(columnspan=4, ipadx=100)

final_expression = StringVar()
final_expression_label = Label(calculator_, font="Calibri 25 bold", textvariable=final_expression, justify=LEFT,
                               height=2, width=7)
final_expression_label.grid(columnspan=4, ipadx=100)


def changeinput_expression_label(entry):
    global sum
    global sumforsqroot

    sum = sum + str(entry)
    sumforsqroot = sum
    input_expression.set(sum)


def evaluateSquareroot():
    global sum
    global sumforsqroot

    try:
        sqrt = math.sqrt(eval(str(sumforsqroot)))
        clearinput_expression_label()
        final_expression.set(sqrt)

    except(ValueError, SyntaxError, TypeError, ZeroDivisionError):
        clearinput_expression_label()
        final_expression.set("Error!")


def evaluatesum():
    global sum

    try:
        eval(sum)
        evaluated_value_sum = str(eval(sum))
        clearinput_expression_label()
        final_expression.set(evaluated_value_sum)

    except(ValueError, SyntaxError, TypeError, ZeroDivisionError):
        clearinput_expression_label()
        final_expression.set("Error!")


def clear():
    global sum
    global sumforsqroot
    sum = ""
    sumforsqroot = ""
    input_expression.set("")
    final_expression.set("")


def clearinput_expression_label():
    global sum
    global sumforsqroot

    sumforsqroot = sum
    sum = ""
    input_expression.set(sum)


def create_buttons(buttons, x, y):
    Button(calculator_, font="Calibri 14 bold", padx=14, pady=14,
           text=str(buttons), height=2, width=9, command=lambda: changeinput_expression_label(buttons)).grid(row=x,
                                                                                                             column=y,
                                                                                                             sticky=E)


buttons_list = ['C', '√', '%', '/', '7', '8', '9', '*', '4',
                '5', '6', '-', '1', '2', '3', '+', '', '', '.', '']

counter = 0
for i in range(3, 8):
    for j in range(0, 4):
        create_buttons(buttons_list[counter], i, j)
        counter = counter + 1

Button(calculator_, font="Calibri 14 bold", padx=14, pady=14,
       text="√", height=2, width=9, command=lambda: evaluateSquareroot()).grid(row=3, column=1, sticky=E)

Button(calculator_, font="Calibri 14 bold", padx=14, pady=14,
       text="AC", height=2, width=9, command=lambda: clear()).grid(row=3, column=0, sticky=E)

Button(calculator_, font="Calibri 14 bold", padx=14, pady=14,
       text="0", height=2, width=9, command=lambda: changeinput_expression_label(0)).grid(row=7, column=0, columnspan=2,
                                                                                          sticky=E)

Button(calculator_, font="Calibri 14 bold", padx=14, pady=14,
       text="=", height=2, width=9, command=lambda: evaluatesum()).grid(row=7, column=3, sticky=E)

sum = ""
sumforsqroot = ""

calculator_.mainloop()
