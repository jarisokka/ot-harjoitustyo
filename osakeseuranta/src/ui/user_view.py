from tkinter import *
from tkinter import ttk, constants
from services.user_services import user_services

class UserView:
    def __init__(self, root):
        self._root = root
        self._root.geometry('800x650')
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        frameTitle = ttk.Label(master=self._frame)
        frameTitle.pack(padx=5, pady=5)

        label = ttk.Label(master=frameTitle, text='Omat osakkeet', font='Helvetica')
        label.grid(row=0, column=0, pady=5)
 
        frameInfo = ttk.Label(master=self._frame)
        frameInfo.pack(padx=5, pady=5) 

        name = ttk.Label(master=frameInfo, text='Lista omista osakkeista')
        name.grid(row=0, column=0, padx=50)


