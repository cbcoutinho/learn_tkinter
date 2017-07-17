import os
from tkinter import *
from tkinter.filedialog import askopenfilename

file_path_1 = ''
file_path_2 = ''

#~~~~ FUNCTIONS~~~~

def open_rules_file():
  global file_path_1
  filename1 = askopenfilename()
  file_path_1 = os.path.abspath(filename1)
  print(file_path_1)
  entry1.delete(0, END)
  entry1.insert(0, file_path_1)

def open_src_file():
  global file_path_2
  filename2 = askopenfilename()
  file_path_2 = os.path.abspath(filename2)
  print(file_path_2)
  entry2.delete(0, END)
  entry2.insert(0, file_path_2)

#~~~~~~ GUI ~~~~~~~~

root = Tk()
root.title('MY GUI')
root.geometry("1000x300+250+100")

mf = Frame(root)
mf.pack()
f1 = Frame(mf, width=600, height=250)
f1.pack(fill=X)
f2 = Frame(mf, width=600, height=250)
f2.pack()
f3 = Frame(mf, width=600, height=250)
f3.pack()

file_path_1 = StringVar
file_path_2 = StringVar

Label(f1,text="Select Rules Sheet (xls)").grid(row=1, column=0, sticky='e')
entry1 = Entry(f1, width=70, textvariable=file_path_1)
entry1.grid(row=1,column=1,padx=2,pady=2,sticky='we',columnspan=25)
Button(f1, text="Browse1", command=open_rules_file).grid(row=1, column=27, sticky='ew', padx=8, pady=4)

Label(f2,text="Select COBOL Source   ").grid(row=2, column=0, sticky='e')
entry2 = Entry(f2, width=70, textvariable=file_path_2)
entry2.grid(row=2,column=1,padx=2,pady=2,sticky='we',columnspan=25)
Button(f2, text="Browse2", command=open_src_file).grid(row=2, column=27, sticky='ew', padx=8, pady=4)

Button(f3, text='Quit', command=f3.quit).grid(row=3, column=0, sticky=W, pady=4)
root.mainloop()
