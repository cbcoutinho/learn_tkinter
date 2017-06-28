import tkinter as tk

root = tk.Tk()

photo = tk.PhotoImage(file='intro/smile.png')
label = tk.Label(root, image=photo)
label.pack()


root.mainloop()
