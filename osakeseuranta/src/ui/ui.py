from tkinter import *
from tkinter import Tk, ttk
from repositories.reader import readStockListFromFile
from services.marketdata import MarketData
from services.singlestockdata import SingleStockData
from ui.day_view import DayView 
from ui.ytd_view import YTDView
from ui.year_view  import YearView

# Page change logic and methods are copied from the course material

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._root.geometry('800x650')
        self.info = None
        self.day = None
        self.index = None
        self.procent = None
        self.stocks = None
        self.market = None

        self.createInfo()
        self.initializeRead()
        self.initializeCreate()


    def createInfo(self):
        self.info = SingleStockData('^OMXH25')
        self.info.stockGetOneDayPrices()
        self.day = self.info.getDay()
        self.index = self.info.getPriceNow()
        self.procent = float(self.info.getCountChangeProcent(self.info.getPriceNow(), self.info.getPricePreviousDay()))
        if self.procent > 0:
            self.procent = ('+' + str(self.procent) + ' %')
        else:
            self.procent = (str(self.procent) + ' %')

    def initializeRead(self):
        self.stocks = readStockListFromFile('OMX25H.csv')
        self.stocks = self.stocks.read_file()
    
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
            self.market,
            self.day,
            self.index,
            self.procent
        )

        self._current_view.pack()

    def _show_ytd_view(self):
        self._hide_current_view()

        self._current_view = YTDView(
            self._root,
            self._handle_day,
            self._handle_year,
            self.stocks,
            self.market,
            self.day,
            self.index,
            self.procent
        )

        self._current_view.pack()
    
    def _show_year_view(self):
        self._hide_current_view()

        self._current_view = YearView(
            self._root,
            self._handle_day,
            self._handle_ytd,
            self.stocks,
            self.market,
            self.day,
            self.index,
            self.procent
        )

        self._current_view.pack()

