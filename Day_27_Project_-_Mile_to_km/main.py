from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=150, pady=100)

def button_clicked():
    km_final.config(text = str(round(float(entry.get())*1.60934, 1)))


#entry
entry = Entry(width=7)
entry.grid(column=1, row=0)

# label
miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_to = Label(text='is equal to')
is_equal_to.grid(column=0, row=1)

km_label= Label(text="Km")
km_label.grid(row=1, column=2)

km_final = Label(text=0)
km_final.grid(row=1, column=1)

#button
button = Button(text='Calculate', command=button_clicked)
button.grid(row=2, column=1)



window.mainloop()