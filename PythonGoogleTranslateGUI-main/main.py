from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text = "type", src = "en", dest = "fr"):
    trans = Translator()
    trans1 = trans.translate(text, src, dest)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x800")
root.config(bg="lightblue")

lab_txt = Label(root, text="Translator", font=("Time New Roman", 38, "bold"), bg="lightblue")
lab_txt.place(x=100, y=40, height=40, width=300)

# frame = Frame(root)
# frame.pack(side=BOTTOM)
frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="Source Text", font=("Time New Roman", 20, "bold"), bg="lightblue")
lab_txt.place(x=100, y=100, height=20, width=300)

Sor_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=130, height=150, width=480)

list_text = list(LANGUAGES.values())
# #########################
# list_text = ['en', 'fr']

comb_sor = ttk.Combobox(frame, values=list_text)
comb_sor.place(x=10, y=300, height=40, width=160)
comb_sor.set("english")

comb_dest = ttk.Combobox(frame, values=list_text)
comb_dest.place(x=330, y=300, height=40, width=160)
comb_dest.set("french")

dest = Label(root, text="Final Text", font=("Time New Roman", 20, "bold"), bg="lightblue")
dest.place(x=100, y=360, height=20, width=300)

dest_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=180, y=300, height=40, width=140)

root.mainloop()