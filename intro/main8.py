'''
This tkinter project shows how to create a simple gui
with 'File' and 'Edit' menus with their respective submenus

'''

import tkinter as tk

def doNothing():
    print('Do nothing - alright fine')

root = tk.Tk()

# **** Main Menu ****

menu = tk.Menu(root)
root.config(menu=menu)

subMenu = tk.Menu(menu)
menu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='New Project..', command=doNothing)
subMenu.add_command(label='Save..', command=doNothing)
subMenu.add_separator()
subMenu.add_command(label='Exit', command=root.quit)

editMenu = tk.Menu(menu)
menu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Redo', command=doNothing)

# **** Toolbar ****

tb = tk.Frame(root, bg='blue')
button1 = tk.Button(tb, text='Insert Image', command=doNothing)
button1.pack(side=tk.LEFT, padx=2, pady=2)
button2 = tk.Button(tb, text='Print', command=doNothing)
button2.pack(side=tk.LEFT, padx=2, pady=2)

tb.pack(side=tk.TOP, fill=tk.X)

root.mainloop()
