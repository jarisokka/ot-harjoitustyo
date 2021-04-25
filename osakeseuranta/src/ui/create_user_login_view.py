#Basic structure is from the course material
from tkinter import *
from tkinter import Tk, ttk, constants, messagebox
from services.user_services import user_services, UsernameExistsError, InvalidCredentialsError
from ui.user_view import UserView

class CreateUserLoginView:
    def __init__(self, root):
        self._root = root
        self._root.geometry('425x225')
        self._root.resizable(0, 0)
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._user = None

        self._initialize()  

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._root.destroy()

    def _show_user_view(self):
        userview = Tk()
        userview.attributes('-topmost',True)
        userview.title("Omat osakkeet")
        userv = UserView(userview, self._user)
        userv.pack()
        userview.mainloop()

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            return messagebox.showerror('error', 
            'Käyttäjätunnus ja salasana pakollinen', parent=self._root)

        try:
            user_services.create_user(username, password)
            self._username_entry.delete(0, END)
            self._password_entry.delete(0, END)
            return messagebox.showinfo(
                'ok', f'Käyttäjätunnus {username} luotiin onnistuneesti. Voit nyt kirjautua sisään.',
                 parent=self._root)
        except UsernameExistsError:
            return messagebox.showerror(
                'error', f'Käyttäjätunnus {username} on jo olemassa',
                 parent=self._root)

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            user_services.login(username, password)
            self._user = username
            self.destroy()
            self._show_user_view()
        except InvalidCredentialsError:
            return messagebox.showerror('error', 'Väärä käyttäjätunnus tai salasana')

    def _initialize_heading_field(self):
        heading_label = ttk.Label(master=self._frame, text='Luo uusi käyttäjätunnus tai kirjaudu sisään')
        heading_label.grid(row=0, column=1, padx=10, pady=20)          

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text='Käyttäjätunnus')
        username_label.grid(row=2, column=0, padx=5, pady=5)

        self._username_entry = ttk.Entry(master=self._frame)
        self._username_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=10, pady=5)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text='Salasana')
        password_label.grid(row=3, column=0 ,padx=5, pady=5)

        self._password_entry = ttk.Entry(master=self._frame)
        self._password_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=10, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_heading_field()
        self._initialize_username_field()
        self._initialize_password_field()

        create_user_button = ttk.Button(
            master=self._frame,
            text='Luo tunnus',
            command=self._create_user_handler
        )

        login_button = ttk.Button(
            master=self._frame,
            text='Kirjaudu',
            command=self._login_handler
        )

        self._frame.grid_columnconfigure(1, minsize=120)

        create_user_button.grid(row=5, column=1, padx=10, pady=5, sticky=constants.EW)
        login_button.grid(row=6, column=1, padx=10, pady=5, sticky=constants.EW)

