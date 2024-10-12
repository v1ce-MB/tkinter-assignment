from tkinter import*
window=Tk()
window.config(bg="violet")
window.geometry("400x500")

import random
number=random.randint(1,10000)



def click():
    print(number)

arithmetic=Button(window,text="open me", bg="maroon", fg="blue",command=click)
arithmetic.pack()







window.mainloop()