from functions import *


def start():
    show_title()
    books = [
        {
            'name': 'O guia do mochileiro das galáxias',
            'author': 'Douglas Adams',
            'published': 1979
        },
        {
            'name': 'A Metamorfose',
            'author': 'Franz Kafka',
            'published': 1915
        },
        {
            'name': 'À Procura da Felicidade',
            'author': 'Chris Gardner',
            'published': 2007
        }
    ]

    # Insert the operation int
    operation = 1

    while operation != 0:
        try:
            show_menu()
            operation = get_operation()
            choose_operation(operation, books)
        except Exception:
            print("\nInsert a valid number!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
