from tkinter import *

# creating a new window and configuration
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.pack()

#Buttons

def button_action():
    label.config(text="This is new text")

button = Button(text="This is button", command=button_action)
button.pack()

# entries

input = Entry(width=30)
input.insert(END, string='Some text to begin with')
print(input.get())
input.pack()

# text

text = Text(height=5, width=30)
text.focus()
text.insert(END, 'Multiline text example\n')
print(text.get('1.0', END))
text.pack()

# spinbox







window.mainloop()