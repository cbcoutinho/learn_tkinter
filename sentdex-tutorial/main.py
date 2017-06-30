import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt

import urllib
import json

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ('Verdana', 12)
style.use('ggplot')
# style.use('dark_background')

f = Figure()
ax = f.add_subplot(111)

def animate(i):
    dataLink = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
    data = urllib.request.urlopen(dataLink)
    data = data.readall().decode('utf-8')
    data = json.loads(data)
    data = data['btc_usd']
    data = pd.DataFrame(data)
    data['datestamp'] = np.array(data.timestamp).astype('datetime64[s]')

    buys = data[(data['type']=='bid')]
    buyDates = buys.datestamp.tolist()

    sells = data[(data['type']=='ask')]
    sellDates = sells.datestamp.tolist()

    ax.clear()
    ax.plot_date(buyDates, buys['price'], '#00A3E0', linestyle='-', marker=None, label='Buys')
    ax.plot_date(sellDates, sells['price'], '#183A54', linestyle='-', marker=None, label='Sells')

    ax.set_title('BTC-e BTCUSD Prices\nLast Price: ' + str(data.price[0]))
    ax.set_ylabel('Price [$]')
    ax.legend(bbox_to_anchor=(0, 1.02, 1, 0.102), loc=3, ncol=2, borderaxespad=0)

# SeaofBTCapp extends the tk.Tk class by basically setting up some defaults (adds frames, start with StartPage, etc.)
class SeaofBTCapp(tk.Tk):

    # args are arguements
    # kwargs are essentially a dictionary of parameters
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        img = tk.PhotoImage(file='resources/myicon.png')
        self.tk.call('wm', 'iconphoto', self._w, img)
        self.title("The amazing tutorial app")

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Add menu with exit button
        menu = tk.Menu(container)
        self.config(menu=menu)

        fileMenu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label='File', menu=fileMenu)

        fileMenu.add_command(label='Save Settings', command=lambda: popupmsg('Not Yet Supported'))
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=self.quit)


        self.frames = {}

        for F in (StartPage, BTCe_Page):
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
                         text='Agree to the terms of the app?',
                         font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self,
                            text='Agree',
                            command=lambda: controller.show_frame(BTCe_Page))
        button1.pack()

        button2 = ttk.Button(self,
                            text='Disagree',
                            command=quit)
        button2.pack()

        status = tk.Label(self,
                          text='On Start Page...',
                          bd=1,
                          relief=tk.SUNKEN,
                          anchor=tk.W)
        status.pack(side=tk.BOTTOM, fill=tk.X)

class PageOne(tk.Frame):
    ''' This page no longer used - only available for reference'''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,
                         text='Page One',
                         font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self,
                            text='Back to start',
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self,
                            text='Visit Page Two',
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self,
                            text='Visit Graph Page',
                            command=lambda: controller.show_frame(GraphPage))
        button3.pack()

        status = tk.Label(self,
                          text='On Page One...',
                          bd=1,
                          relief=tk.SUNKEN,
                          anchor=tk.W)
        status.pack(side=tk.BOTTOM, fill=tk.X)

class BTCe_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,
                         text='Graph Page',
                         font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self,
                            text='Back to start',
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        status = tk.Label(self,
                          text='On Graph Page...',
                          bd=1,
                          relief=tk.SUNKEN,
                          anchor=tk.W)
        status.pack(side=tk.BOTTOM, fill=tk.X)

app = SeaofBTCapp()
app.geometry("800x600")

ani = animation.FuncAnimation(f, animate, interval=5000)

app.mainloop()
