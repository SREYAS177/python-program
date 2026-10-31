# Name        : Sreyas Suresh
# Roll Number : 55
# Class       : MCA

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    with open("books.txt", "a") as file:
        file.write(title + "|" + author + "\n")

    print("Book added successfully!")


def read_books():
    books = []

    try:
        with open("books.txt", "r") as file:
            for line in file:
                if line.strip():
                    title, author = line.strip().split("|", 1)
                    books.append((title, author))
    except FileNotFoundError:
        pass

    return books


def search_book():
    keyword = input("Enter title or author to search: ").lower()
    books = read_books()
    found = False

    for title, author in books:
        if keyword in title.lower() or keyword in author.lower():
            print("Title:", title, "| Author:", author)
            found = True

    if not found:
        print("No book found.")


def generate_report():
    books = read_books()
    print("Total number of books:", len(books))

    author = input("Enter author name for report: ").lower()

    count = 0
    for title, book_author in books:
        if book_author.lower() == author:
            print("Title:", title)
            count += 1

    print("Books by this author:", count)


while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Generate Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        generate_report()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice!")
