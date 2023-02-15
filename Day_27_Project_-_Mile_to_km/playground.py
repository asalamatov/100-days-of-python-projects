# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total
#
# ans = add(4,5,6,6,7,8)
# print(ans)
#
# def calcualate(n, **kwargs):
#
#     print(kwargs)
#
#     n+=kwargs["add"]
#     n*=kwargs["multiply"]
#     print(n)
#
# calcualate(2, add = 2, multiply=5)
#
# class Car:
#
#     def __init__(self, **kwargs):
#         self.make = kwargs.get('make')
#         self.model = kwargs.get('model')
#
# my_car = Car(make="Nissan")
# print(my_car.make)


import tkinter
from tkinter import *


def button_clicked():
    print("I got clicked")
    my_label.config(text='Button got clicked')


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label['text'] = 'New text'
#my_label.pack()
#my_label.pack(side='left')
#my_label.place(x=100, y=200)
my_label.grid(row=0, column=0)

# Button
button = Button(text='Click Me', command=button_clicked)
button.grid(row=1, column=1)

button1 = Button(text='Click Me', command=button_clicked)
button1.grid(row=0, column=2)
# Entry
input = Entry(width=20)
print(input.get())
input.grid(row=2, column=3)




window.mainloop()