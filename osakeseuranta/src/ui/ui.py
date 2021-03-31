from tkinter import *
from tkinter import Tk, ttk
from repositories.reader import readStockListFromFile
from services.marketdata import MarketData


class UI:
    def __init__(self, root):
        self._root = root
        self._root.geometry('800x650')
        self.title = ('Arial', 24, 'bold')
        self.text = ('Arial', 12)
        self.stocks = None
        self.size = None
        self.market = None

        self.initializeRead()
        self.initializeCreate()

    def initializeRead(self):
        self.stocks = readStockListFromFile('OMX25H.csv')
        self.stocks = self.stocks.read_file()
        self.size = len(self.stocks)
    
    def initializeCreate(self):
        self.market = MarketData(self.stocks)
        self.market.stockCreateStockList()


    def start(self):
        frameTitle = ttk.Label(master=self._root)
        frameTitle.pack(padx=10, pady=10)

        label = ttk.Label(master=frameTitle, text='Osakkeet', font=self.title)
        label.grid(row=0, column=0)

        frameInfo = ttk.Label(master=self._root)
        frameInfo.pack() 

        label = ttk.Label(master=frameInfo, text='päivämäärä')
        label.grid(row=0, column=0, padx=10, pady=10)
        day = ttk.Button(master=frameInfo, text=' Päivä ')
        day.grid(row=0, column=1)
        year = ttk.Button(master=frameInfo, text=' YTD ')
        year.grid(row=0, column=2)  
        ytd = ttk.Button(master=frameInfo, text=' Vuosi ')
        ytd.grid(row=0, column=3)


        frameMain = ttk.Label(master=self._root)
        frameMain.pack(padx=10, pady=10) 

        stock_tree = ttk.Treeview(frameMain, height=300)
        stock_tree['columns'] = ('#1', '#2', '#3', '#4', '#5')

        # Format columns
        stock_tree.column('#0', width=0, stretch=NO)
        stock_tree.column('#1', width=90, anchor=W)
        stock_tree.column('#2', width=200, anchor=W)
        stock_tree.column('#3', width=100, anchor=CENTER)
        stock_tree.column('#4', width=100, anchor=CENTER)
        stock_tree.column('#5', width=100, anchor=CENTER)

        # Create Headings
        stock_tree.heading('#0', text='', anchor=W)
        stock_tree.heading('#1', text='Tunnus', anchor=W)
        stock_tree.heading('#2', text='Yrityksen nimi', anchor=W)
        stock_tree.heading('#3', text='Kurssi', anchor=CENTER)
        stock_tree.heading('#4', text='Kehitys', anchor=CENTER)
        stock_tree.heading('#5', text='% Kehitys', anchor=CENTER)

        # Add data
        for stock in self.stocks:
            symbol = str(stock)
            name = str(self.market.getNameWithTicker(stock))
            price = str(self.market.getNowPriceWithTicker(stock))
            changem  = str(self.market.getMoneyChangeDayWithTicker(stock))
            changep  = str(self.market.getProcentChangeDayWithTicker(stock))
            stock_tree.insert(parent='', index='end', iid=stock, text='', values=(symbol, name, price, changem, changep) )
        
        stock_tree.pack(padx=10, pady=10)






