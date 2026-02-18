book_to_look_for = input()
searching_book = input()
book_count = 0
# book_is_found = False

while searching_book != "No More Books":
    if searching_book == book_to_look_for:
        print(f"You checked {book_count} books and found it.")
        # book_is_found = True (use this instead of the print to take it out from the loop)
        break
    book_count += 1
    searching_book = input()


if searching_book == "No More Books":
    print(f"The book you search is not here!")
    print(f"You checked {book_count} books.") 

# if book_is_found:
#    print(f"You checked {book_count} books and found it.")
# else:
#    print(f"The book you search is not here!")
#    print(f"You checked {book_count} books.")
  