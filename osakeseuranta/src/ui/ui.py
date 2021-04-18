# Page logic and methods are copied from the course material
from tkinter import *
from tkinter import Tk, ttk
from services.marketdata import MarketData
from services.singlestockdata import SingleStockData
from ui.day_view import DayView
from ui.ytd_view import YTDView
from ui.year_view  import YearView
from ui.create_user_login_view import CreateUserLoginView



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

        self.create_info()
        self.initialize_create()


    def create_info(self):
        self.info = SingleStockData('^OMXH25')
        self.info.stock_get_one_day_prices()
        self.day = self.info.get_day()
        self.index = self.info.get_price_now()
        self.procent = float(self.info.get_count_change_procent(self.info.get_price_now(), self.info.get_price_previous_day()))
        if self.procent > 0:
            self.procent = ('+' + str(self.procent) + ' %')
        else:
            self.procent = (str(self.procent) + ' %')

    def initialize_create(self):
        self.market = MarketData()
        self.stocks = self.market.initialize_read('OMX25H.csv')
        self.market.stock_create_stock_list()

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

    def _handle_login(self):
        self._show_login_view()

    def _show_day_view(self):
        self._hide_current_view()

        self._current_view = DayView(
            self._root,
            self._handle_ytd,
            self._handle_year,
            self._handle_login,
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
            self._handle_login,
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
            self._handle_login,
            self.stocks,
            self.market,
            self.day,
            self.index,
            self.procent
        )

        self._current_view.pack()

    def _show_login_view(self):
        create_user_login = Tk()
        create_user_login.attributes('-topmost',True)
        create_user_login.title("Kirjautuminen ja tunnuksien luonti")
        create_view = CreateUserLoginView(create_user_login)
        create_view.pack()
