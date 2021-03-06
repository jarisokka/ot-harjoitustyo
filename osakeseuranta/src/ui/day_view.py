from tkinter import *
from tkinter import Tk, ttk, constants


class DayView:
    """Käyttöliittymä luokka joka vastaa pörssikurssien
         päiväkohtaisen kehityksen näyttämisestä"""
    def __init__(self, root, handle_ytd, handle_year, handle_login, stocks, market, day, index, procent):
        """Luokan konstruktori joka luo uuden näkymän jossa
            näytetään kurssien päiväkohtaiset kehitykset.

        Args:
            root: Päänäkymästä vastaava luokka.
            handle_ytd: Vuoden alusta näkymästä vastaava luokka.
            handle_year: Vuosi sitten näkymästä vastaava luokka.
            handle_login: Kirjautumisnäkymästä vastaava luokka.
            stocks: Sanakirja muodossa oleva listaus näytettävistä osakkeista,
                avaimena ticker-tunnus.
            market: MarketData olio joka sisältää pörssidatan.
            day: Merkkijono, joka kertoo päivämäärän muodossa dd:mm:yy.
            index: Float, joka kertoo pörssin tämän hetkisen indexin.
            procent: Merkkijono, joka kertoo pörssin tämän hetkisen prosenttikehityksen.
        """
        self._root = root
        self._handle_ytd = handle_ytd
        self._handle_year = handle_year
        self._handle_login = handle_login
        self._frame = None
        self.stocks = stocks
        self.market = market
        self.day = day
        self.index = index
        self.procent = procent
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        frameTitle = ttk.Label(master=self._frame)
        frameTitle.pack(padx=5, pady=5)

        label = ttk.Label(master=frameTitle, text='Osakkeiden kurssit', font='Helvetica')
        label.grid(row=0, column=0, pady=5)
        day = ttk.Label(master=frameTitle, text=self.day)
        day.grid(row=1, column=0)
 
        frameInfo = ttk.Label(master=self._frame)
        frameInfo.pack(padx=5, pady=5) 

        name = ttk.Label(master=frameInfo, text='OMX Helsinki')
        name.grid(row=0, column=0, padx=50)
        index = ttk.Label(master=frameInfo, text=self.index)
        index.grid(row=1, column=0, padx=50)
        procent = ttk.Label(master=frameInfo, text=self.procent)
        procent.grid(row=2, column=0, padx=50)

        button = ttk.Button(
            master=frameInfo,
            text=' Päivä ',
            state=DISABLED
        )
        button.grid(row=1, column=1)       

        button = ttk.Button(
            master=frameInfo,
            text=' Vuoden alusta ',
            command=self._handle_ytd
        )
        button.grid(row=1, column=2)

        button = ttk.Button(
            master=frameInfo,
            text=' Vuosi ',
            command=self._handle_year
        )
        button.grid(row=1, column=3)

        button = ttk.Button(
            master=frameInfo,
            text=' Kirjaudu ',
            command=self._handle_login
        )
        button.grid(row=1, column=4)

        frameMain = ttk.Label(master=self._frame)
        frameMain.pack(padx=10, pady=10) 

        view_scroll = Scrollbar(frameMain)
        view_scroll.pack(side=RIGHT, fill=Y)

        stock_tree = ttk.Treeview(frameMain, yscrollcommand=view_scroll.set, height=300)
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
        stock_tree.heading('#4', text='€ kehitys', anchor=CENTER)
        stock_tree.heading('#5', text='% kehitys', anchor=CENTER)

        # Add data
        for stock in self.stocks:
            symbol = str(stock)
            name = str(self.market.get_name_with_ticker(stock))
            price = str(self.market.get_now_price_with_ticker(stock))
            changem  = str(self.market.get_money_change_day_with_ticker(stock))
            changep  = str(self.market.get_procent_change_day_with_ticker(stock))
            stock_tree.insert(parent='', index='end', iid=stock, text='', values=(symbol, name, price, changem, changep))
        
        stock_tree.pack(padx=10, pady=10)
