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

        # Add menu with exit button
        menu = tk.Menu(self)
        self.config(menu=menu)

        subMenu = tk.Menu(menu)
        menu.add_cascade(label='File', menu=subMenu)
        subMenu.add_command(label='Exit', command=self.quit)


        self.frames = {}

        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        '''
        Brings up the frame contained in 'cont'
        '''

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,
                         text='Start Page',
                         font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self,
                            text='Visit Page 1',
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

        status = tk.Label(self,
                          text='On Start Page...',
                          bd=1,
                          relief=tk.SUNKEN,
                          anchor=tk.W)
        status.pack(side=tk.BOTTOM, fill=tk.X)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,
                         text='Page One',
                         font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self,
                            text='Back to start',
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        status = tk.Label(self,
                          text='On Page One...',
                          bd=1,
                          relief=tk.SUNKEN,
                          anchor=tk.W)
        status.pack(side=tk.BOTTOM, fill=tk.X)

app = SeaofBTCapp()
app.mainloop()
