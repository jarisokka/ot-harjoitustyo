from tkinter import *
from tkinter import Tk, ttk, constants


class YearView:
    def __init__(self, root, handle_day, handle_ytd, stocks, market):
        self._root = root
        self._handle_day = handle_day
        self._handle_ytd = handle_ytd
        self._frame = None
        self.stocks = stocks
        self.market = market
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        frameTitle = ttk.Label(master=self._frame)
        frameTitle.pack(padx=10, pady=10)

        label = ttk.Label(master=frameTitle, text='Osakkeet')
        label.grid(row=0, column=0)

        frameInfo = ttk.Label(master=self._frame)
        frameInfo.pack() 

        button = ttk.Button(
            master=frameInfo,
            text=' Päivä ',
            command=self._handle_day
        )
        button.grid(row=0, column=1)       

        button = ttk.Button(
            master=frameInfo,
            text=' Vuoden alusta ',
            command=self._handle_ytd
        )
        button.grid(row=0, column=2)

        button = ttk.Button(
            master=frameInfo,
            text=' Vuosi ',
            state=DISABLED
        )
        button.grid(row=0, column=3)


        frameMain = ttk.Label(master=self._frame)
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
            changem  = str(self.market.getMoneyChangeYearTicker(stock))
            changep  = str(self.market.getProcentChangeYearTicker(stock))
            stock_tree.insert(parent='', index='end', iid=stock, text='', values=(symbol, name, price, changem, changep) )
        
        stock_tree.pack(padx=10, pady=10)