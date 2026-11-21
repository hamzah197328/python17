from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("denomination calculator")
root.geometry("650x800")
root.configure(bg="lightblue")

img = Image.open("image.png")
img = img.resize((300, 300))
img = ImageTk.PhotoImage(img)

label = Label(root, image=img)
label.pack()

Label1 = Label(root, text="Welcome to the Denomination Calculator", font=("Arial", 24), bg="lightblue")
Label1.pack()

def msg():
    msgbox = messagebox.showinfo("Information", "Welcome to the Denomination Calculator")
    msgbox = messagebox.askquestion("Alert", "Want to use the denomination calculator?")
    if msgbox == "yes":
        topwin()

button1 = Button(root, text="begin", command=msg, bg ="lightgreen")
button1.place(x=275, y=700)

def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg="lightblue")
    top.geometry("650x800")

    label = Label(top, text="enter amt", font=("Arial", 24), bg="lightblue")
    entry = Entry(top)
    lbl = Label(top, text="these are the numberss for each denomination", font=("Arial", 24), bg="lightblue")

    l1 = Label(top, text ="2000", bg="lightblue")
    l2 = Label(top, text ="500", bg="lightblue")
    l3 = Label(top, text ="200", bg="lightblue")
    l4 = Label(top, text ="100", bg="lightblue")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)

    label.pack()
    entry.pack()
    lbl.pack()
    l1.pack()
    t1.pack()
    l2.pack()
    t2.pack()
    l3.pack()
    t3.pack()
    l4.pack()
    t4.pack()

    def calculator():
        try:
            global amt
            amt = int(entry.get())
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t4.delete(0, END)

            t1.insert(0, amt // 2000)
            amt %= 2000
            t2.insert(0, amt // 500)
            amt %= 500
            t3.insert(0, amt // 200)
            amt %= 200
            t4.insert(0, amt // 100)
            amt %= 100
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")


    calc_button = Button(top, text="Calculate", command=calculator, bg="lightgreen")
    calc_button.pack()


root.mainloop()