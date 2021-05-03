from tkinter import *
from tkinter import Tk, ttk, constants, messagebox, StringVar
from services.stock_services import stock_services, InvalidValuesError, StockExistsError, GeneralError

class UserView:
    def __init__(self, root, user):
        self._root = root
        self._user = user
        self._root.geometry('950x500')
        self._frame = None
        self.clicked = StringVar()
        self._ticker = None
        self._name = None

        self._data = stock_services.initialize_data(self._user)
        self._data = stock_services.get_stock_data(self._data)
        self._list = stock_services.read_list('search_list.csv')
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._user = None
        self._data = None
        self._frame.destroy()

    def update_data(self):
        self._data = stock_services.initialize_data(self._user)
        self._data = stock_services.get_stock_data(self._data)


    def update_treeview(self):
        tree = self.stock_tree.get_children()
        for item in tree:
            self.stock_tree.delete(item)

        for data in self._data:
            name = self._data[data][0]
            date = self._data[data][2]
            price = self._data[data][1]
            now = self._data[data][3]
            money = self._data[data][4]
            procent = self._data[data][5]
            self.stock_tree.insert(parent='', index='end', iid=data, text='', values=(name, date, price, now, money, procent))

    def _clear_values(self):
        self.price_entry.delete(0, END)
        self.date_entry.delete(0, END)
        clear = '                                         '
        self._initialize_ticker_value(clear)
        self._initialize_name_value(clear)
        self._ticker = None
        self._name = None

    def _show_stock(self):
        self._clear_values()
        self._name = self.clicked.get()
        self._ticker = self._list[self._name]
        self._initialize_ticker_value(self._ticker)
        self._initialize_name_value(self._name)

    def _submit_handler(self):
        user = self._user
        ticker = self._ticker
        name = self._name
        price = self.price_entry.get()
        date = self.date_entry.get()
        try:
            stock_services.check_values(ticker, name, price, date)
        except InvalidValuesError as error:
            ticker = None
            name = None
            price = None
            date = None
            return messagebox.showinfo(
                    'ok', f'{error}',
                    parent=self._root)

        try:
            stock_services.create_new(user, ticker, name, price, date)
            self._clear_values()
            self.update_data()
            self.update_treeview()
            return messagebox.showinfo(
                'ok', f'Osake {name} lisättiin listaan',
                 parent=self._root)
        except StockExistsError:
            return messagebox.showerror(
                'error', f'Osake {name} on jo listalla',
                 parent=self._root)

    def _remove_stock(self):
        try:
            selected = self.stock_tree.focus()
            values = self.stock_tree.item(selected, 'values')
            user = self._user
            ticker = self._list[values[0]]
            stock_services.remove_stock(user, ticker)
            self._clear_values()
            self.update_data()
            self.update_treeview()
            return messagebox.showinfo(
                'ok', 'Valittu osake poistettiin',
                 parent=self._root)
        except GeneralError:
            return messagebox.showerror(
                'error', f'Osakkeen {values[0]} poisto ei onnistunut',
                 parent=self._root)

    def _update_handler(self):
        try:
            selected = self.stock_tree.focus()
            values = self.stock_tree.item(selected, 'values')
            user = self._user
            ticker = self._list[values[0]]
            price = self.price_entry.get()
            date = self.date_entry.get()
            stock_services.update_values(user, ticker, price, date)
            self._clear_values()
            self.update_data()
            self.update_treeview()
            return messagebox.showinfo(
                'ok', f'Osakkeen {values[0]} tiedot päivitettiin',
                 parent=self._root)
        except GeneralError:
            return messagebox.showinfo(
                'ok', f'Osakkeen {values[0]} päivitys ei onnistunut',
                parent=self._root)

    def _select_stock_handler(self, event):
        self._clear_values()
        selected = self.stock_tree.focus()
        values = self.stock_tree.item(selected, 'values')
        self._ticker = self._list[values[0]]
        self._name = values[0]
        self._initialize_ticker_value(self._ticker)
        self._initialize_name_value(self._name)
        self.price_entry.insert(0, values[2])
        self.date_entry.insert(0, values[1])

    def _initialize_stock_list_field(self):
        stock_view = ttk.Treeview(master=self._frame)
        stock_view.grid(row=0, columnspan=6, padx=10, pady=10)

        view_scroll = Scrollbar(stock_view)
        view_scroll.pack(side=RIGHT, fill=Y)

        self.stock_tree = ttk.Treeview(stock_view, yscrollcommand=view_scroll.set, selectmode='extended')
        self.stock_tree.pack()

        view_scroll.config(command=self.stock_tree.yview)

        self.stock_tree['columns'] = ('#1', '#2', '#3', '#4', '#5', '#6')

        # Format columns
        self.stock_tree.column('#0', width=0, stretch=NO)
        self.stock_tree.column('#1', width=200, anchor=W)
        self.stock_tree.column('#2', width=100, anchor=W)
        self.stock_tree.column('#3', width=100, anchor=CENTER)
        self.stock_tree.column('#4', width=100, anchor=CENTER)
        self.stock_tree.column('#5', width=100, anchor=CENTER)
        self.stock_tree.column('#6', width=100, anchor=CENTER)

        # Create Headings
        self.stock_tree.heading('#0', text='', anchor=W)
        self.stock_tree.heading('#1', text='Yrityksen nimi', anchor=W)
        self.stock_tree.heading('#2', text='ostopäivä', anchor=W)
        self.stock_tree.heading('#3', text='ostohinta', anchor=CENTER)
        self.stock_tree.heading('#4', text='kurssi', anchor=CENTER)
        self.stock_tree.heading('#5', text='€ kehitys', anchor=CENTER)
        self.stock_tree.heading('#6', text='% kehitys', anchor=CENTER)

        for data in self._data:
            name = self._data[data][0]
            date = self._data[data][2]
            price = self._data[data][1]
            now = self._data[data][3]
            money = self._data[data][4]
            procent = self._data[data][5]
            self.stock_tree.insert(parent='', index='end', iid=data, text='', values=(name, date, price, now, money, procent))

        self.stock_tree.bind('<ButtonRelease-1>', self._select_stock_handler)


    def _initialize_search_field(self):
        search_label = ttk.Label(master=self._slave, text='Valitse osake')
        search_label.grid(row=3, column=0, padx=10, pady=10)

        drop = ttk.OptionMenu(self._slave, self.clicked, *self._list)
        drop.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=10, pady=5)

    def _initialize_ticker_field(self):
        ticker_label = ttk.Label(master=self._slave, text='Osakkeen tunnus')
        ticker_label.grid(row=4, column=0, padx=5, pady=5)
    
    def _initialize_ticker_value(self, ticker):
        tvalue_label = ttk.Label(master=self._slave, text=ticker)
        tvalue_label.grid(row=4, column=1, padx=5, pady=5)    
        
    def _initialize_name_field(self):
        name_label = ttk.Label(master=self._slave, text='Osakkeen nimi')
        name_label.grid(row=4, column=2, padx=5, pady=5)

    def _initialize_name_value(self, name):
        nvalue_label = ttk.Label(master=self._slave, text=name)
        nvalue_label.grid(row=4, column=3, padx=5, pady=5)


    def _initialize_price_field(self):
        price_label = ttk.Label(master=self._slave, text='Hankintahinta')
        price_label.grid(row=5, column=0, padx=5, pady=5)

        self.price_entry = ttk.Entry(master=self._slave, width=30)
        self.price_entry.grid(row=5, column=1, sticky=(constants.E, constants.W), padx=10, pady=5)

    def _initialize_date_field(self):
        date_label = ttk.Label(master=self._slave, text='Hankinta ajankohta')
        date_label.grid(row=5, column=2, padx=5, pady=5)

        self.date_entry = ttk.Entry(master=self._slave, width=30)
        self.date_entry.grid(row=5, column=3, sticky=(constants.E, constants.W), padx=10, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._slave = ttk.LabelFrame(master=self._frame, text='Omien osakkeiden hallinta')
        self._slave.grid(row=1, columnspan=6, padx=10, pady=10)

        self._initialize_stock_list_field()
        self._initialize_search_field()
        self._initialize_ticker_field()
        self._initialize_name_field()
        self._initialize_price_field()
        self._initialize_date_field()

        show_stock_button = ttk.Button(
            master=self._slave,
            text='Lisää osakkeen tiedot',
            command=self._show_stock
        )

        save_data_button = ttk.Button(
            master=self._slave,
            text='Tallenna',
            command=self._submit_handler
        )
        update_data_button = ttk.Button(
            master=self._slave,
            text='Päivitä',
            command=self._update_handler
        )
        remove_data_button = ttk.Button(
            master=self._slave,
            text='Poista valittu',
            command=self._remove_stock
        )
        clear_stock_button = ttk.Button(
            master=self._slave,
            text='Tyhjennä syötteet',
            command=self._clear_values
        )
        show_stock_button.grid(row=3, column=2, padx=10, pady=5, sticky=constants.EW)
        save_data_button.grid(row=6, column=1, padx=10, pady=5, sticky=constants.EW)
        update_data_button.grid(row=6, column=3, padx=10, pady=5, sticky=constants.EW)
        remove_data_button.grid(row=7, column=1, padx=10, pady=5, sticky=constants.EW)
        clear_stock_button.grid(row=7, column=3, padx=10, pady=5, sticky=constants.EW)
