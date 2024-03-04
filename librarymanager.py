books_list = []
authors_set = set()
books_dict = {}

books_list.append("Python Programming")
authors_set.add("John smith")
books_dict["Python Programming"]= "John smith"

books_list.append("data structure and algorithms")
authors_set.add("jane doe")
books_dict["data structure and algorithms"]= "jane doe"

books_list.append("machine learning basics")
authors_set.add("alice johnson")
books_dict["machine learing basics"]= "alice johnson"

search_title=input("Enter the title of the book to search: ")
if search_title in books_list:
    print(f"book found! author:{books_dict [search_title]}")
else:
    print("book not found!")
print("List of books:")
for book in books_list:
    print(book)
remove_title = input("Enter the title of the book to remove: ")
if remove_title in books_list:
    remove_author = books_dict[remove_title]
    books_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dict[remove_title]
    print("book removed successfully!")
else:
    print("book not found!")
