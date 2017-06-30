import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
# from matplotlib import pyplot as plt

import urllib
import json

import tkinter as tk
from tkinter import ttk

LARGE_FONT  = ('Verdana', 12)
NORM_FONT   = ('Verdana', 10)
SMALL_FONT  = ('Verdana',  8)
style.use('ggplot')
# style.use('dark_background')

fig = Figure()
ax = fig.add_subplot(111)

exchange = 'BTC-e'
DatCounter = 9000
programName = 'btce'
ResampleSize = '15Min'
DataPace = '1d'
CandleWidth = 0.008

topIndicator = 'None'
middleIndicator = 'None'
bottomIndicator = 'None'
EMAs = []
SMAs = []

def addMiddleIndicator(what):
    global middleIndicator
    global DatCounter

    if DataPace == 'tick':
        popupmsg('Indicators in Tick data not available')

    elif what != 'none':
        if middleIndicator == 'None':
            if what == 'sma':
                midIQ = tk.Tk()
                midIQ.wm_title('Periods?')
                label = ttk.Label(midIQ, text='Choose how many periods to consider for SMA')
                label.pack(side='top', fill='x', pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append('sma')
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print('middle indicator set to:', middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text='Submit', width=10, command=callback)
                b.pack()
                tk.mainloop()

            elif what == 'ema':
                midIQ = tk.Tk()
                midIQ.wm_title('Periods?')
                label = ttk.Label(midIQ, text='Choose how many periods to consider for EMA')
                label.pack(side='top', fill='x', pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append('ema')
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print('middle indicator set to:', middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text='Submit', width=10, command=callback)
                b.pack()
                tk.mainloop()

        else:
            if what == 'sma':
                midIQ = tk.Tk()
                midIQ.wm_title('Periods?')
                label = ttk.Label(midIQ, text='Choose how many periods to consider for SMA')
                label.pack(side='top', fill='x', pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    # middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append('sma')
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print('middle indicator set to:', middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text='Submit', width=10, command=callback)
                b.pack()
                tk.mainloop()

            elif what == 'ema':
                midIQ = tk.Tk()
                midIQ.wm_title('Periods?')
                label = ttk.Label(midIQ, text='Choose how many periods to consider for EMA')
                label.pack(side='top', fill='x', pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    # middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append('ema')
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print('middle indicator set to:', middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text='Submit', width=10, command=callback)
                b.pack()
                tk.mainloop()
    else:
        middleIndicator = 'none'

def addTopIndicator(what):
    global topIndicator
    global DatCounter

    if DataPace == 'tick':
        popupmsg('Indicators in Tick data not available')

    elif what == 'none':
        topIndicator = what
        DatCounter = 9000

    elif what == 'rsi':
        rsiQ = tk.Tk()
        rsiQ.wm_title('Periods?')
        label = ttk.Label(rsiQ, text='Choose how many periods to consider for RSI')
        label.pack(side='top', fill='x', pady=10)

        e = ttk.Entry(rsiQ)
        e.insert(0,14)
        e.pack()
        e.focus_set()

        def callback():
            global topIndicator
            global DatCounter

            periods = (e.get())
            group = []
            group.append('rsi')
            group.append(periods)

            topIndicator = group
            DatCounter = 9000
            print('Set top indicator to', group)

            rsiQ.destroy()

        b = ttk.Button(rsiQ, text='Submit', width=10, command=callback)
        b.pack()
        tk.mainloop()

    elif what == 'macd':
        global topIndicator
        global DatCounter

        topIndicator = 'macd'
        DatCounter = 9000

def addBottomIndicator(what):
    global bottomIndicator
    global DatCounter

    if DataPace == 'tick':
        popupmsg('Indicators in Tick data not available')

    elif what == 'none':
        bottomIndicator = what
        DatCounter = 9000

    elif what == 'rsi':
        rsiQ = tk.Tk()
        rsiQ.wm_title('Periods?')
        label = ttk.Label(rsiQ, text='Choose how many periods to consider for RSI')
        label.pack(side='top', fill='x', pady=10)

        e = ttk.Entry(rsiQ)
        e.insert(0,14)
        e.pack()
        e.focus_set()

        def callback():
            global bottomIndicator
            global DatCounter

            periods = (e.get())
            group = []
            group.append('rsi')
            group.append(periods)

            bottomIndicator = group
            DatCounter = 9000
            print('Set bottom indicator to', group)

            rsiQ.destroy()

        b = ttk.Button(rsiQ, text='Submit', width=10, command=callback)
        b.pack()
        tk.mainloop()

    elif what == 'macd':
        global bottomIndicator
        global DatCounter

        bottomIndicator = 'macd'
        DatCounter = 9000

def changeTimeFrame(tf):
    global DataPace
    global DatCounter
    if tf == '7d' and resampleSize == '1Min':
        popup('Too much data!\nChoose smaller timeframe or higher OHLC Interval')
    else:
        DataPace = tf
        DatCounter = 9000

def changeSampleSize(size, width):
    global resampleSize
    global DatCounter
    global CandleWidth

    if DataPace == '7d' and resampleSize == '1Min':
        popupmsg('Too much data!\nChoose smaller timeframe or higher OHLC Interval')

    elif DataPace == 'tick':
        popupmsg("You're currently viewing tick data, not OHLC")

    else:
        resampleSize = size
        DatCounter = 9000
        CandleWidth = width

def changeExchange(exName, exCode):
    global exchange
    global DatCounter
    global programName

    exchange = exName
    programName = exCode
    DatCounter = 9000

    print(exchange, ' and ', programName)

def popupmsg(msg):
    popup = tk.Tk()

    popup.wm_title('!')
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side='top', fill='x', pady=10)

    b1 = ttk.Button(popup, text='Okay',
                    command=popup.destroy)
    b1.pack()
    popup.mainloop()

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
        menubar = tk.Menu(container)
        self.config(menu=menubar)

        fileMenu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label='File', menu=fileMenu)

        fileMenu.add_command(label='Save Settings', command=lambda: popupmsg('Not Yet Supported'))
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=self.quit)

        exchangeChoice = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label='Exchange', menu=exchangeChoice)

        exchangeChoice.add_command(label='BTC-e',
                                   command=lambda: changeExchange('BTC-e','btce'))
        exchangeChoice.add_command(label='Bitfinex',
                                   command=lambda: changeExchange('Bitfinex','bitfinex'))
        exchangeChoice.add_command(label='Bitstamp',
                                   command=lambda: changeExchange('Bitstamp','bitstamp'))
        exchangeChoice.add_command(label='Huobi',
                                   command=lambda: changeExchange('Huobi','huobi'))

        dataTF = tk.Menu(menubar, tearoff=True)
        menubar.add_cascade(label='Tick', menu=dataTF)

        dataTF.add_command(label='Tick',
                           command=lambda: changeTimeFrame('tick'))
        dataTF.add_command(label='1 Day',
                           command=lambda: changeTimeFrame('1d'))
        dataTF.add_command(label='3 Days',
                           command=lambda: changeTimeFrame('3d'))
        dataTF.add_command(label='1 Week',
                           command=lambda: changeTimeFrame('7d'))

        # OHLCI = Open High Low Close Interval
        OHLCI = tk.Menu(menubar, tearoff=True)
        menubar.add_cascade(label='OHLC Interval', menu=OHLCI)

        OHLCI.add_command(label='Tick',
                          command=lambda: changeTimeFrame('tick'))
        OHLCI.add_command(label='1 minute',
                          command=lambda: changeSampleSize('1Min', 0.0005))
        OHLCI.add_command(label='5 minutes',
                          command=lambda: changeSampleSize('5Min', 0.003))
        OHLCI.add_command(label='15 minutes',
                          command=lambda: changeSampleSize('15Min', 0.008))
        OHLCI.add_command(label='30 minutes',
                          command=lambda: changeSampleSize('30Min', 0.016))
        OHLCI.add_command(label='1 hour',
                          command=lambda: changeSampleSize('1H', 0.032))
        OHLCI.add_command(label='3 hours',
                          command=lambda: changeSampleSize('3H', 0.096))


        topIndicator = tk.Menu(menubar, tearoff=True)
        menubar.add_cascade(label='Top Indicator', menu=topIndicator)

        topIndicator.add_command(label=None,
                                 command=lambda: addTopIndicator('None'))
        topIndicator.add_command(label='RSI',
                                 command=lambda: addTopIndicator('rsi'))
        topIndicator.add_command(label='MACD',
                                 command=lambda: addTopIndicator('macd'))


        middleIndicator = tk.Menu(menubar, tearoff=True)
        menubar.add_cascade(label='Main/Middle Indicator', menu=middleIndicator)

        middleIndicator.add_command(label=None,
                                 command=lambda: addMiddleIndicator('None'))
        middleIndicator.add_command(label='SMA',
                                 command=lambda: addMiddleIndicator('sma'))
        middleIndicator.add_command(label='EMA',
                                 command=lambda: addMiddleIndicator('ema'))


        bottomIndicator = tk.Menu(menubar, tearoff=True)
        menubar.add_cascade(label='Bottom Indicator', menu=bottomIndicator)

        bottomIndicator.add_command(label=None,
                                 command=lambda: addBottomIndicator('None'))
        bottomIndicator.add_command(label='RSI',
                                 command=lambda: addBottomIndicator('rsi'))
        bottomIndicator.add_command(label='MACD',
                                 command=lambda: addBottomIndicator('macd'))






        self.frames = {}

        for page in (StartPage, BTCe_Page):
            frame = page(container, self)
            self.frames[page] = frame
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

        canvas = FigureCanvasTkAgg(fig, self)
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

ani = animation.FuncAnimation(fig, animate, interval=5000)

app.mainloop()
