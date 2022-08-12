# File of functions
import os


def show_title():
    print('#-------------------------------------------------#')
    print('#-------------Book Registration System------------#')
    print('#-------------------------------------------------#')


def show_menu():
    print('#-----------------------------#')
    print('#-------------MENU------------#')
    print('#-----------------------------#')
    print('\nSelect the operation you want to perform:')
    print('1 - Register a new book')  # ok
    print('2 - View all registered books')  # ok
    print('3 - Search a book')  # Dentro de search, poder deletar e alterar livro
    print('0 - Exit\n')


def get_operation():
    show_menu()
    return int(input('Enter your option: '))


def choose_operation(operation, books):
    if operation == 1:
        add_book(books)
    elif operation == 2:
        show_books(books)
    elif operation == 3:
        search_book(books)
    elif operation == 0:
        print("""
        See you soon!
        
        #--------------------------------------#
        #------------END OF PROGRAM------------#
        #--------------------------------------#    
        """)

    else:
        print('\nInvalid option! Enter some of the alternatives presented! \n')


def show_books(books):
    for book in books:
        print(book)
    print("\n")


def add_book(books):

    repeat = 'y'
    while repeat == 'y':
        name = input("\nInsert the name of the book: ")
        author = input("Insert the author's name: ")
        year = int(input("Insert the year of the published: "))

        books.append(
            {
                'name': name,
                'author': author,
                'published': year
            }
        )

        repeat = input("\nThe book was added! Would you like to add another one? (y/n)")
    print("\n\n")


def search_book(books):
    name = input("Type the name of a book: ")
    validate = False

    for book in books:
        if name == book['name']:
            validate = True

    if not validate:
        print("Book not found!")
        return

    operation = 1
    while operation != 0:
        if validate:
            print("\nWhat do you like to do:\n1 - Delete the book\n2- Change name\n0 - End Search ")
            operation = int(input("\nYour selection: "))





