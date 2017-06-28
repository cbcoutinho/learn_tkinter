'''
This tkinter project shows how to create a simple gui
with 'File' and 'Edit' menus with their respective submenus

'''

import tkinter as tk

def doNothing():
    print('Do nothing - alright fine')

root = tk.Tk()

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

root.mainloop()
