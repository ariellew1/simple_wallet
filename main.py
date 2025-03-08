from guizero import App, MenuBar, Box, Text
import functions

app = App(title='Simple wallet')

menu_bar = MenuBar(app,
                   toplevel=['Portfel','Transakcje', 'Kategorie', 'Raporty',],
                   options=[
                       [['Nowy', functions.new_wallet],
                        ['Otwórz', functions.open_wallet],
                        ['Zapisz', functions.save_wallet],],
                       [['Dodaj', functions.add_transaction],
                        ['Edytuj', functions.edit_transaction],
                        ['Przegląd', functions.transaction_overview],
                        ['Usuń', functions.delete_transaction]],
                       [['Dodaj', functions.add_category],
                        ['Edytuj', functions.edit_category],
                        ['Usuń', functions.delete_category],],
                       [['Podsumowanie', functions.summary_reports],
                        ['Wybierz', functions.select_report],
                        ['PDF', functions.generate_pdf],
                        ]
                    ])

app.display()
