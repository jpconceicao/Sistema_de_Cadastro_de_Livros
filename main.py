# MAIN
# import functions

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
        operation = get_operation()
        choose_operation(operation, books)


def choose_operation(operation, books):
    if operation == 1:
        pass
    elif operation == 2:
        show_books(books)
    elif operation == 3:
        pass
    elif operation == 4:
        pass
    elif operation == 0:
        print('\nSee you soon!')
        print('\n#--------------------------------------#')
        print('#------------END OF PROGRAM------------#')
        print('#--------------------------------------#')
    else:
        print('\nInvalid option! Enter some of the alternatives presented! \n')


def show_books(books):
    for book in books:
        print(book)


def get_operation():
    show_menu()
    return int(input('Enter your option: '))


def show_title():
    print('#-------------------------------------------------#')
    print('#-------------Book Registration System------------#')
    print('#-------------------------------------------------#')


def show_menu():
    print('\nSelect the operation you want to perform:')
    print('1 - Register a new book')
    print('2 - View all registered books')
    print('3 - Delete a book')
    print("4 - Change a book's name")
    print('0 - Exit\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()


