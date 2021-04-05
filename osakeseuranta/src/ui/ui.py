from tkinter import *
from tkinter import Tk, ttk
from repositories.reader import readStockListFromFile
from services.marketdata import MarketData
from ui.day_view import DayView 
from ui.ytd_view import YTDView
from ui.year_view  import YearView

# Page change logic and methods are copied from the course material

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._root.geometry('800x650')
        #self.title = ('Arial', 24, 'bold')
        #self.text = ('Arial', 12)
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
        self._show_day_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_ytd(self):
        self._show_ytd_view()

    def _handle_day(self):
        self._show_day_view()
    
    def _handle_year(self):
        self._show_year_view()

    def _show_day_view(self):
        self._hide_current_view()

        self._current_view = DayView(
            self._root,
            self._handle_ytd,
            self._handle_year,
            self.stocks,
            self.market
        )

        self._current_view.pack()

    def _show_ytd_view(self):
        self._hide_current_view()

        self._current_view = YTDView(
            self._root,
            self._handle_day,
            self._handle_year,
            self.stocks,
            self.market
        )

        self._current_view.pack()
    
    def _show_year_view(self):
        self._hide_current_view()

        self._current_view = YearView(
            self._root,
            self._handle_day,
            self._handle_ytd,
            self.stocks,
            self.market
        )

        self._current_view.pack()

