# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:08:50 2024

@author: admin
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



##############################################+=============================================================
root = tk.Tk()
root.configure(background="black")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("700x650+200+50")
root.title("page")

      

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('login_img.png')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
  
label_l1 = tk.Label(root, text="Cataract Disease Detection",font=("Algerian", 20, ''),
                    background="Sky blue", fg="white", width=80, height=3)
label_l1.place(x=0, y=0)

label_l1 = tk.Label(root, text="  In the realm of healthcare, technology isn't just a tool; it's a lifeline, empowering us to safeguard our most precious asset – our health",font=("Calibri", 15, ''),
                    background="#DBE9FA", fg="black", width=130, height=2)
label_l1.place(x=20, y=550)


def heart():
    from subprocess import call
    call(["python","Heart.py"])

def log():
    from subprocess import call
    call(["python","Detection.py"])
    
def main():
    from subprocess import call
    call(["python","GUI_main.py"])
        
 
    
def window():
  root.destroy()


# button1 = tk.Button(root, text="Cataract Detection", command=log, width=14, height=1, font=('Calibri', 10, ' '), bg="sky blue", fg="white")
# button1.place(x=1070, y=58)

# button1 = tk.Button(root, text="Heart Detection", command=heart, width=13, height=1, font=('Calibri', 10, ' '), bg="sky blue", fg="white")
# button1.place(x=1180, y=58)

# button1 = tk.Button(root, text="GUI_main", command=main, width=13, height=1, font=('Calibri', 10, ' '), bg="sky blue", fg="white")
# button1.place(x=1280, y=58)

button4 = tk.Button(root, text="Cataract Detection", command=log, width=14, height=1,font=('times 10 bold '),bd=0,bg="sky blue", fg="white")
button4.place(x=1070, y=60)

# button4 = tk.Button(root, text="Heart Detection", command=heart, width=13, height=1,font=('times 10 bold '),bd=0,bg="sky blue", fg="white")
# button4.place(x=1180, y=60)

button4 = tk.Button(root, text="GUI_main", command=main, width=13, height=1,font=('times 10 bold '),bd=0,bg="sky blue", fg="white")
button4.place(x=1180, y=60)


      
root.mainloop()