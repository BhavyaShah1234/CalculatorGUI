import tkinter as tk
import tkinter.font as font

root = tk.Tk()
root.title('Calculator')
root.geometry('555x625+800+50')

global num1
global num2
global operator

button_font = font.Font(root, family='Comic Sans MS', size=20, weight='bold')

inp = tk.Entry(root, width=30, bg='blue', fg='white', borderwidth=7, font=button_font)
inp.grid(row=0, column=0, columnspan=4, padx=30, pady=30)


def press_num(n):
    num = inp.get()
    inp.delete(0, 'end')
    inp.insert(-1, f'{num}{n}')


def press_op(op):
    global num1, operator
    operator = op
    num1 = int(inp.get())
    inp.delete(0, 'end')


def press_eq():
    n = inp.get()
    global num2
    num2 = int(n)
    inp.delete(0, 'end')
    if operator == '/' and num2 != 0:
        inp.insert(0, str(num1 / num2))
    if operator == '/' and num2 == 0:
        inp.insert(0, 'CANNOT DIVIDE BY ZERO')
    if operator == '*':
        inp.insert(0, str(num1 * num2))
    if operator == '-':
        inp.insert(0, str(num1 - num2))
    if operator == '+':
        inp.insert(0, str(num1 + num2))


def press_c():
    inp.delete(0, 'end')


x, y = 40, 30
b7 = tk.Button(root, padx=x, pady=y, text='7', font=button_font, command=lambda: press_num(7), fg='red', bg='green')
b8 = tk.Button(root, padx=x, pady=y, text='8', font=button_font, command=lambda: press_num(8), fg='red', bg='green')
b9 = tk.Button(root, padx=x, pady=y, text='9', font=button_font, command=lambda: press_num(9), fg='red', bg='green')
bd = tk.Button(root, padx=x, pady=y, text='/', font=button_font, command=lambda: press_op('/'), fg='blue', bg='pink')

b4 = tk.Button(root, padx=x, pady=y, text='4', font=button_font, command=lambda: press_num(4), fg='red', bg='green')
b5 = tk.Button(root, padx=x, pady=y, text='5', font=button_font, command=lambda: press_num(5), fg='red', bg='green')
b6 = tk.Button(root, padx=x, pady=y, text='6', font=button_font, command=lambda: press_num(6), fg='red', bg='green')
bm = tk.Button(root, padx=x, pady=y, text='*', font=button_font, command=lambda: press_op('*'), fg='blue', bg='pink')

b1 = tk.Button(root, padx=x, pady=y, text='1', font=button_font, command=lambda: press_num(1), fg='red', bg='green')
b2 = tk.Button(root, padx=x, pady=y, text='2', font=button_font, command=lambda: press_num(2), fg='red', bg='green')
b3 = tk.Button(root, padx=x, pady=y, text='3', font=button_font, command=lambda: press_num(3), fg='red', bg='green')
bs = tk.Button(root, padx=x, pady=y, text='-', font=button_font, command=lambda: press_op('-'), fg='blue', bg='pink')

be = tk.Button(root, padx=x, pady=y, text='=', font=button_font, command=press_eq, fg='black', bg='yellow')
b0 = tk.Button(root, padx=x, pady=y, text='0', font=button_font, command=lambda: press_num(0), fg='red', bg='green')
bc = tk.Button(root, padx=x, pady=y, text='C', font=button_font, command=press_c, fg='black', bg='yellow')
ba = tk.Button(root, padx=x, pady=y, text='+', font=button_font, command=lambda: press_op('+'), fg='blue', bg='pink')

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
bd.grid(row=1, column=3)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
bm.grid(row=2, column=3)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
bs.grid(row=3, column=3)

be.grid(row=4, column=0)
b0.grid(row=4, column=1)
bc.grid(row=4, column=2)
ba.grid(row=4, column=3)

root.mainloop()
