# step1: import tkinter

from tkinter import *
# step2: gui interaction
window = Tk()

# step2: adding input
window.title("Adarsh")
window.geometry("500x700")
window.config(bg = "lightblue")
frame1 = Frame(window, bg="red", width=200, height=200, cursor = "dot")
frame2 = Frame(window, bg="green", width=200, height=200, cursor = "dotbox")
button1 = Button(frame1, text="Button 1", bg="blue")
button2 = Button(frame2, text="Button 2", bg="green")
bhutton3 = Button(frame1, text="Button 3", bg="yellow")
frame1.pack(side = TOP)
frame2.pack(side = BOTTOM)
button1.pack()
button2.pack()
bhutton3.pack()
# step3: mainloop
mainloop()