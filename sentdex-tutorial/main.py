import tkinter as tk

LARGE_FONT = ('Verdana', 12)

# SeaofBTCapp extends the tk.Tk class by basically setting up some defaults (adds frames, start with StartPage, etc.)
class SeaofBTCapp(tk.Tk):

    # args are arguements
    # kwargs are essentially a dictionary of parameters
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.title("The title")
        container = tk.Frame(self)

        container.pack(side='top',
                       fill='both',
                       expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        '''
        Brings up the frame contained in 'cont'
        '''

        frame = self.frames[cont]
        frame.tkraise()

def quickfun(string):
    print(string)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,
                         text='Start Page',
                         font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self,
                            text='Visit Page 1',
                            command=lambda: quickfun('This worked'))
        button1.pack()

        status = tk.Label(self,
                          text='Status bar...',
                          bd=1,
                          relief=tk.SUNKEN,
                          anchor=tk.W)
        status.pack(side=tk.BOTTOM, fill=tk.X)

app = SeaofBTCapp()
app.mainloop()
