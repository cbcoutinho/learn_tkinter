import numpy as np
import pandas as pd
import sys, os

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker

import urllib
import json

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

LARGE_FONT  = ('Verdana', 12)
NORM_FONT   = ('Verdana', 10)
SMALL_FONT  = ('Verdana',  8)
style.use('ggplot')
# style.use('dark_background')

fig = plt.figure()
# ax = fig.add_subplot(111)

exchange = 'BTC-e'
DatCounter = 9000
refreshRate = 0.0
programName = 'btce'
ResampleSize = '15Min'
DataPace = 'tick'
CandleWidth = 0.008
paneCount = 1

LIGHT_COLOR = '#00A3E0'
DARK_COLOR = '#183A54'

topIndicator = 'None'
middleIndicator = 'None'
bottomIndicator = 'None'
chartLoad = True
EMAs = []
SMAs = []

def tutorial():

    def leavemini(what):
        what.destroy()

    def page2():
        tut.destroy()
        tut2 = tk.Tk()

        def page3():
            tut2.destroy()
            tut3 = tk.Tk()

            tut3.wm_title('Part 3')
            label = ttk.Label(tut3, text='Part 3', font=NORM_FONT)
            label.pack(side='top', fill='x', pady=10)
            b1 = ttk.Button(tut3, text='Done', command=tut3.destroy)
            b1.pack()
            tut3.mainloop()

        tut2.wm_title('Part 2')
        label = ttk.Label(tut2, text='Part 2', font=NORM_FONT)
        label.pack(side='top', fill='x', pady=10)
        b1 = ttk.Button(tut2, text='Next', command=page3)
        b1.pack()
        tut2.mainloop()

    tut = tk.Tk()
    tut.wm_title('Tutorial')
    label = ttk.Label(tut, text='What do you need help with?', font=NORM_FONT)
    label.pack(side='top', fill='x', pady=10)

    b1 = ttk.Button(tut, text='Overview of the application', command=page2)
    b1.pack()
    b2 = ttk.Button(tut, text='How do I trade', command=lambda: popupmsg('Not yet completed'))
    b2.pack()
    b3 = ttk.Button(tut, text='Indicator Questions/Help', command=lambda: popupmsg('Not yet completed'))
    b3.pack()

    tut.mainloop()

def loadChart(startStop):
    global chartLoad

    if startStop == 'start':
        chartLoad = True
    elif startStop == 'stop':
        chartLoad = False

    # print('Chart load set to', chartLoad)

def quit():
    quit()
    # sys.exit(0)

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
        # global topIndicator
        # global DatCounter

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
        # global bottomIndicator
        # global DatCounter

        bottomIndicator = 'macd'
        DatCounter = 9000

def changeTimeFrame(tf):
    global DataPace
    global DatCounter
    if tf == '7d' and resampleSize == '1Min':
        popupmsg('Too much data!\nChoose smaller timeframe or higher OHLC Interval')
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
    global refreshRate
    global DatCounter

    if chartLoad:
        if paneCount == 1:
            if DataPace == 'tick':
                try:
                    if exchange == 'BTC-e':

                        ax = plt.subplot2grid((6,4), (0,0),
                                              rowspan=5, colspan=4)
                        ax2 = plt.subplot2grid((6,4), (5,0),
                                               rowspan=1, colspan=4,
                                               sharex=ax)

                        dataLink = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
                        data = urllib.request.urlopen(dataLink)
                        # data = data.readall().decode('utf-8')
                        data = data.read().decode('utf-8')
                        data = json.loads(data)
                        data = data['btc_usd']
                        data = pd.DataFrame(data)

                        data['datestamp'] = np.array(data.timestamp).astype('datetime64[s]')
                        allDates = data.datestamp.tolist()

                        buys = data.loc[data.type == 'bid']
                        buyDates = buys.datestamp.tolist()

                        sells = data.loc[data.type == 'ask']
                        sellDates = sells.datestamp.tolist()

                        volume = data['amount']

                        ax.clear()
                        ax.plot_date(buyDates, buys['price'], LIGHT_COLOR, linestyle='-', marker=None, label='Buys')
                        ax.plot_date(sellDates, sells['price'], DARK_COLOR, linestyle='-', marker=None, label='Sells')

                        ax2.fill_between(allDates, 0, volume, facecolor=DARK_COLOR)
                        # ax2.fill_between(allDates, 1e-1, volume, facecolor='#FF0000')
                        # ax2.set_yscale('log')

                        ax.xaxis.set_major_locator(mticker.MaxNLocator(4))
                        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
                        plt.setp(ax.get_xticklabels(), visible=False)

                        ax.set_title('BTC-e BTCUSD Prices\nLast Price: ' + str(data.price[0]))
                        ax.set_ylabel('Price [$]')
                        ax.legend(bbox_to_anchor=(0, 1.02, 1, 0.102), loc=3, ncol=2, borderaxespad=0)

                        priceData = df['price'].astype(float).tolist()

                    elif exchange == 'Bitstamp':

                        ax = plt.subplot2grid((6,4), (0,0),
                                              rowspan=5, colspan=4)
                        ax2 = plt.subplot2grid((6,4), (5,0),
                                               rowspan=1, colspan=4,
                                               sharex=ax)


                        dataLink = 'https://www.bitstamp.net/api/transactions/'
                        data = urllib.request.urlopen(dataLink)
                        # data = data.readall().decode('utf-8')
                        data = data.read().decode('utf-8')
                        data = json.loads(data)
                        data = pd.DataFrame(data)

                        for col in ['amount', 'price']:
                            data[col] = data[col].apply(float)

                        data['datestamp'] = np.array(data.date.apply(int)).astype('datetime64[s]')
                        # data.sort_values(by='datestamp', inplace=True)
                        allDates = data.datestamp.tolist()

                        buys = data.loc[data.type == 0]
                        buyDates = buys.datestamp.tolist()

                        sells = data.loc[data.type == 1]
                        sellDates = sells.datestamp.tolist()

                        volume = data['amount'].tolist()

                        ax.clear()
                        ax.plot_date(buyDates, buys['price'], LIGHT_COLOR, linestyle='-', marker=None, label='Buys')
                        ax.plot_date(sellDates, sells['price'], DARK_COLOR, linestyle='-', marker=None, label='Sells')

                        ax2.fill_between(allDates, 0, volume, facecolor=DARK_COLOR)
                        # ax2.fill_between(allDates, 1e-1, volume, facecolor='#FF0000')
                        # ax2.set_yscale('log')

                        ax.xaxis.set_major_locator(mticker.MaxNLocator(4))
                        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
                        plt.setp(ax.get_xticklabels(), visible=False)

                        ax.set_title('Bitstamp BTCUSD Prices\nLast Price: ' + str(data.price[0]))
                        ax.set_ylabel('Price [$]')
                        ax.legend(bbox_to_anchor=(0, 1.02, 1, 0.102), loc=3, ncol=2, borderaxespad=0)

                        priceData = df['price'].astype(float).tolist()

                    elif exchange == 'Bitfinex':

                        ax = plt.subplot2grid((6,4), (0,0),
                                              rowspan=5, colspan=4)
                        ax2 = plt.subplot2grid((6,4), (5,0),
                                               rowspan=1, colspan=4,
                                               sharex=ax)

                        dataLink = 'https://api.bitfinex.com/v1/trades/btcusd?limit=2000'
                        data = urllib.request.urlopen(dataLink)
                        # data = data.readall().decode('utf-8')
                        data = data.read().decode('utf-8')
                        data = json.loads(data)
                        data = pd.DataFrame(data)

                        for col in ['amount', 'price']:
                            data[col] = data[col].apply(float)

                        data['datestamp'] = np.array(data.timestamp).astype('datetime64[s]')
                        allDates = data.datestamp.tolist()

                        buys = data.loc[data.type == 'buy']
                        buyDates = buys.datestamp.tolist()

                        sells = data.loc[data.type == 'sell']
                        sellDates = sells.datestamp.tolist()

                        volume = data['amount']

                        ax.clear()
                        ax.plot_date(buyDates, buys['price'], LIGHT_COLOR, linestyle='-', marker=None, label='Buys')
                        ax.plot_date(sellDates, sells['price'], DARK_COLOR, linestyle='-', marker=None, label='Sells')

                        ax2.fill_between(allDates, 0, volume, facecolor=DARK_COLOR)
                        # ax2.fill_between(allDates, 1e-1, volume, facecolor='#FF0000')
                        # ax2.set_yscale('log')

                        ax.xaxis.set_major_locator(mticker.MaxNLocator(4))
                        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
                        plt.setp(ax.get_xticklabels(), visible=False)

                        ax.set_title('Bitfinex BTCUSD Prices\nLast Price: ' + str(data.price[0]))
                        ax.set_ylabel('Price [$]')
                        ax.legend(bbox_to_anchor=(0, 1.02, 1, 0.102), loc=3, ncol=2, borderaxespad=0)

                        priceData = df['price'].astype(float).tolist()

                    elif exchange == 'Huobi':

                        ax = plt.subplot2grid((6,4), (0,0),
                                              rowspan=6, colspan=4)

                        dataLink = 'http://seaofbtc.com/api/basic/price?key=1&tf=1d&exchange='+programName
                        data = urllib.request.urlopen(dataLink)
                        # data = data.readall().decode('utf-8')
                        data = data.read().decode()
                        data = json.loads(data)
                        # data = pd.DataFrame(data)
                        #
                        # for col in ['amount', 'price']:
                        #     data[col] = data[col].apply(float)

                        dateStamp = np.array(data[0]).astype("datetime64[s]")
                        df = pd.DataFrame({'datestamp': dateStamp})
                        df['price'] = data[1]
                        df['volume'] = data[2]
                        df['symbol'] = 'BTCUSD'

                        df['MPLDate'] = df['datestamp'].apply(lambda date: mdates.date2num(date.to_pydatetime()))

                        df = df.set_index('datestamp')

                        lastPrice = df.price[-1]

                        ax.clear()
                        ax.plot_date(df.MPLDate, df.price, LIGHT_COLOR, label='Price [$]')

                        ax.xaxis.set_major_locator(mticker.MaxNLocator(4))
                        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

                        ax.set_title('Huobi BTCUSD Prices\nLast Price: ' + str(data.price[0]))
                        ax.set_ylabel('Price [$]')
                        ax.legend(bbox_to_anchor=(0, 1.02, 1, 0.102), loc=3, ncol=2, borderaxespad=0)

                        priceData = df['price'].astype(float).tolist()


                except Exception as e:
                    print('Failed because of:', e)

            else:
                if DatCounter > 12:
                    try:
                        if exchange == 'Huobi':
                            if topIndicator != 'none':
                                ax = plt.subplot2grid((6,4), (1,0), rowspan=5, colspan=4)
                                ax2 = plt.subplot2grid((6,4), (0,0), sharex=ax, rowspan=1, colspan=4)
                            else:
                                ax = plt.subplot2grid((6,4), (0,0), rowspan=6, colspan=4)

                        else:

                            if topIndicator != 'none' and bottomIndicator != 'none':
                                # Main Graph
                                ax = plt.subplot2grid((6,4), (1,0), rowspan=3, colspan=4)

                                # Volume Graph
                                ax2 = plt.subplot2grid((6,4), (4,0), sharex=ax, rowspan=1, colspan=4)

                                # Bottom Indicator
                                ax3 = plt.subplot2grid((6,4), (5,0), sharex=ax, rowspan=1, colspan=4)

                                # Top Indicator
                                ax0 = plt.subplot2grid((6,4), (0,0), sharex=ax, rowspan=1, colspan=4)

                            elif topIndicator != 'none':

                                # Main Graph
                                ax = plt.subplot2grid((6,4), (1,0), rowspan=4, colspan=4)

                                # Volume Graph
                                ax2 = plt.subplot2grid((6,4), (5,0), sharex=ax, rowspan=1, colspan=4)

                                # Top Indicator
                                ax0 = plt.subplot2grid((6,4), (0,0), sharex=ax, rowspan=1, colspan=4)

                            elif bottomIndicator != 'none':

                                # Main Graph
                                ax = plt.subplot2grid((6,4), (0,0), rowspan=4, colspan=4)

                                # Volume Graph
                                ax2 = plt.subplot2grid((6,4), (4,0), sharex=ax, rowspan=1, colspan=4)

                                # Bottom Indicator
                                ax0 = plt.subplot2grid((6,4), (5,0), sharex=ax, rowspan=1, colspan=4)

                            else:

                                # Main Graph
                                ax = plt.subplot2grid((6,4), (0,0), rowspan=4, colspan=4)

                                # Volume Graph
                                ax2 = plt.subplot2grid((6,4), (5,0), sharex=ax, rowspan=1, colspan=4)

                        dataLink = 'http://seaofbtc.com/api/basic/price?key=1&tf='+DataPace+'&exchange='+programName
                        data = urllib.request.urlopen(dataLink)
                        data = data.read().decode()
                        data = json.loads(data)

                        dateStamp = np.array(data[0].astype('datetime64[s]')).tolist()

                        df = pd.DataFrame({'datestamp':dateStamp,
                                           'price': data[1],
                                           'volume': data[2],
                                           'symbol': 'BTCUSD'})
                        df['MPLDate'] = df.datestamp.apply(lambda date:mdates.date2num(date.to_pydatetime()))
                        df = df.set_index('datestamp')

                        OHLC = df.price.resample(resampleSize, how='ohlc')
                        OHLC = OHLC.dropna()

                        volumeData = df.volume.resample(resampleSize, how={'volume':'sum'})

                        OHLC['dateCopy'] = OHLC.index
                        OHLC['MPLDates'] = OHLC['dateCopy'].apply(lambda date: mdates.date2num(date.to_pydatetime()))

                        del OHLC['dateCopy']

                        volumeData['dateCopy'] = volumeData.index
                        volumeData['MPLDates'] = volumeData['dateCopy'].apply(lambda date: mdates.date2num(date.to_pydatetime()))

                        del volumeData['dateCopy']

                        priceData = OHLC['close'].apply(float).tolist()


                        ax.clear()

                        if middleIndicator != 'none':
                            for m in middleIndicator:
                                ewma = pd.states.moments.ewma
                                if m[0] == 'sma':
                                    sma = pd.rolling_mean(OHLC.close, m[1])
                                    label = str(m[1])+' SMA'
                                    ax.plot(OHLC['MPLDates'], sma, label=label)

                                if m[0] == 'ema':
                                    ewma = pd.rolling_mean(OHLC.close, m[1])
                                    label = str(m[1])+' SMA'
                                    ax.plot(OHLC['MPLDates'], ema, label=label)




                    except Exception as e:
                        print('Failed in the non-tick animate:', str(e))



# SeaofBTCapp extends the tk.Tk class by basically setting up some defaults (adds frames, start with StartPage, etc.)
class SeaofBTCapp(tk.Tk):

    # args are arguements
    # kwargs are essentially a dictionary of parameters
    def __init__(self, *args, **kwargs):

        # tk.Tk.__init__(self, *args, **kwargs)
        super(SeaofBTCapp, self).__init__(*args, **kwargs)
        # filename = 'resources/myicon.png'
        # filename = 'resources/myicon.ico'
        if os.name == 'nt':
            #filename = 'myicon.ico'
            filename = 'myicon.png'
            filename = os.path.abspath(os.path.join('resources', filename))
        else:
            filename = 'myicon.png'
            # filename = 'myicon.xpm'
            filename = os.path.abspath(os.path.join('resources', filename))
            # filename = '@' + os.path.abspath(os.path.join('resources', filename))

        # self.iconbitmap(bitmap=filename)
        #
        # img = ImageTk.PhotoImage(Image.open(filename))
        img = tk.PhotoImage(file=filename)
        #
        # self.tk.call('wm', 'iconphoto', self._w, img)
        # self.iconphoto(True, img)
        print(img)

        self.title("The amazing BTC trading app")
        # self.wm_title('The app')

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # *** Add menu with exit button ***

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

        # *** OHLCI = Open High Low Close Interval ***
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

         # *** Create Top/Middle/Bottom Indicators ***

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

         # *** Create a trading button ***

        tradeButton = tk.Menu(menubar, tearoff=True)
        menubar.add_cascade(label='Trading', menu=tradeButton)
        tradeButton.add_command(label='Manual Trading',
                                command=lambda: popupmsg('This is not live yet'))
        tradeButton.add_command(label='Automatic Trading',
                                command=lambda: popupmsg('This is not live yet'))

        tradeButton.add_separator()
        tradeButton.add_command(label='Quick Buy',
                                command=lambda: popupmsg('This is not live yet'))
        tradeButton.add_command(label='Quick Sell',
                                command=lambda: popupmsg('This is not live yet'))

        tradeButton.add_separator()
        tradeButton.add_command(label='Set up Quick Buy/Sell',
                                command=lambda: popupmsg('This is not live yet'))

        startStop = tk.Menu(menubar, tearoff=True)
        menubar.add_cascade(label='Start/Stop Client', menu=startStop)
        startStop.add_command(label='Resume',
                              command=lambda: loadChart('start'))
        startStop.add_command(label='Pause',
                              command=lambda: loadChart('stop'))

        # *** Create Help menu ***

        helpMenu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label='Help', menu=helpMenu)
        helpMenu.add_command(label='About MyApp',
                              command=lambda: popupmsg('This is not yet live yet'))
        helpMenu.add_command(label='Tutorial',
                              command=tutorial)




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
                            command=parent.quit)
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
