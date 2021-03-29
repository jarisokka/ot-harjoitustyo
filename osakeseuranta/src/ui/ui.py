from tkinter import *
from tkinter import Tk, ttk
from repositories.reader import readStockListFromFile
from services.marketdata import MarketData


class UI:
    def __init__(self, root):
        self.stocks = readStockListFromFile('OMX25H.csv')
        self.stocks = self.stocks.read_file()
        self.size = len(self.stocks)
        self._root = root
        self._root.geometry('800x500')
        self.title = ('Arial', 24, 'bold')
        self.text = ('Arial', 12)
        self.market = MarketData(self.stocks)
        self.market.stockListStartClose()
       
    def start(self):
        frameTitle = ttk.Label(master=self._root)
        frameTitle.pack(padx=10, pady=10)

        label = ttk.Label(master=frameTitle, text='Osakkeet', font=self.title)
        label.grid(row=0, column=0)

        frameMain = ttk.Label(master=self._root)
        frameMain.pack(padx=10, pady=10) 

        stock_tree = ttk.Treeview(frameMain)
        stock_tree['columns'] = ('Tunnus', 'Yrityksen nimi', 'Hinta', 'Kehitys', '%Kehitys')

        # Format columns
        stock_tree.column('#0', width=0, stretch=NO)
        stock_tree.column('Tunnus', width=90, anchor=W)
        stock_tree.column('Yrityksen nimi', width=200, anchor=W)
        stock_tree.column('Hinta', width=100, anchor=CENTER)
        stock_tree.column('Kehitys', width=100, anchor=CENTER)
        stock_tree.column('%Kehitys', width=100, anchor=CENTER)

        # Headings
        stock_tree.heading('#0', text='', anchor=W)
        stock_tree.heading('Tunnus', text='Tunnus', anchor=W)
        stock_tree.heading('Yrityksen nimi', text='Yrityksen nimi', anchor=W)
        stock_tree.heading('Hinta', text='Kurssi', anchor=CENTER)
        stock_tree.heading('Kehitys', text='Kehitys', anchor=CENTER)
        stock_tree.heading('%Kehitys', text='% Kehitys', anchor=CENTER)

        # Add data
        for stock in self.stocks:
            symbol = str(stock)
            name = str(self.market.getNameWithTicker(stock))
            price = str(self.market.getNowPriceWithTicker(stock))
            changem  = str(self.market.getMoneyChangeWithTicker(stock))
            changep  = str(self.market.getProcentChangeWithTicker(stock))
            stock_tree.insert(parent='', index='end', iid=stock, text='', values=(symbol, name, price, changem, changep) )
        
        stock_tree.pack()






