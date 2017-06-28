import tkinter as tk

root = tk.Tk()

def leftClick(event):
    print('Left')

def middleClick(event):
    print('Middle')

def rightClick(event):
    print('Right')

frame = tk.Frame(root, width=600, height=250)
frame.bind('<Button-1>', leftClick)
frame.bind('<Button-2>', middleClick)
frame.bind('<Button-3>', rightClick)
frame.pack()

root.mainloop()
