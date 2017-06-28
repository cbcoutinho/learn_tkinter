import tkinter as tk
import tkinter.messagebox

root = tk.Tk()

# tk.messagebox.showinfo('Window Title', 'Monkeys can live to 100 years')
answer = tk.messagebox.askquestion('Question 1', 'Do you like silly faces?')

if answer == 'yes':
    print(':)')
elif answer == 'no':
    print(':(')


root.mainloop()
