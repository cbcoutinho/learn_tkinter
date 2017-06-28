import tkinter as tk

root = tk.Tk()

topFrame = tk.Frame(root)
topFrame.pack()
bottomFrame = tk.Frame(root)
bottomFrame.pack(side=tk.BOTTOM)

button1 = tk.Button(topFrame, text='Button1', fg='red')
button2 = tk.Button(topFrame, text='Button2', fg='blue')
button3 = tk.Button(topFrame, text='Button3', fg='green')
button4 = tk.Button(bottomFrame, text='Button4', fg='yellow')

button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)
button4.pack()

root.mainloop()
