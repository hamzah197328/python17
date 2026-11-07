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

root.mainloop()