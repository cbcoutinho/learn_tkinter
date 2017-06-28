import tkinter as tk

root = tk.Tk()

def printName(event):
    print('Hello there!')

# button_1 = tk.Button(root, text='Print Name:', command=printName)
button_1 = tk.Button(root, text='Print Name:')
button_1.bind('<Button-1>', printName)
button_1.pack()

root.mainloop()
