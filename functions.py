from guizero import Window, Text, Box, TextBox, Combo


def select_currency(currency):
    pass


def new_wallet(app):
    window = Window(app, title='Nowy portfel')
    window.show(wait=True)
    
    welcome_text = Text(window, text='Tworzenie portfela', align='top',
                        color='white', size=18)
    
    data_field = Box(window, layout='grid')
    
    portfolio_name_text = Text(data_field, color='white', size=14, grid=[0, 0],
                               width=14, height=2, text='Nazwa portfela')
    
    portfolio_name = TextBox(data_field, grid=[1, 0])
    
    currency_name_text = Text(data_field, color='white', size=14, grid=[0, 1],
                              width=14, height=2, text='Waluta')
    
    currency_name = Combo(data_field, options=['PLN'],
                          command=select_currency,
                          grid=[1, 1])


def open_wallet():
    pass


def save_wallet():
    pass


def add_transaction():
    pass


def edit_transaction():
    pass


def transaction_overview():
    pass


def delete_transaction():
    pass


def add_category():
    pass


def edit_category():
    pass


def delete_category():
    pass


def summary_reports():
    pass


def select_report():
    pass


def generate_pdf():
    pass
