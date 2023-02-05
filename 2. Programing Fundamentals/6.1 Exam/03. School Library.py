shelf_with_books = input().split('&')
command = input()

while command != 'Done':
    list_command_and_book = command.split(' | ')
    command_2 = list_command_and_book[0]
    book = list_command_and_book[1]
    if command_2 == 'Add Book':
        if book not in shelf_with_books:
            shelf_with_books.insert(0, book)
    elif command_2 == 'Take Book':
        if book in shelf_with_books:
            shelf_with_books.remove(book)
    elif command_2 == 'Swap Books':
        if book in shelf_with_books and list_command_and_book[2] in shelf_with_books:
            index_1 = shelf_with_books.index(book)
            index_2 = shelf_with_books.index(list_command_and_book[2])
            shelf_with_books[index_1], shelf_with_books[index_2] = shelf_with_books[index_2], shelf_with_books[index_1]
    elif command_2 == 'Insert Book':
        if book not in shelf_with_books:
            shelf_with_books.append(book)
    elif command_2 == 'Check Book':
        if int(book) < len(shelf_with_books):
            print(f"{shelf_with_books[int(book)]}")
    command = input()
        

print(', '.join(shelf_with_books))
    