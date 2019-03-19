class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("User email has been updated.")
        
    def __repr__(self):
        return "User {name} \nemail: {email} \nBooks read: {num_of_books}".format(name = self.name, email = self.email, num_of_books = len(self.books))
    

    def __eq__(self, other_user):
        return self.name == other_user and self.email == other_user.get_email

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        for book in self.books:
            total += self.books[book]
        return total/len(self.books)

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("{title}'s ISBN has been updated".format(title = self.title))
        
    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        elif:
            print("Invalid Rating")

    def get_average_rating(self):
        total = 0
        for rating in self.ratings:
            total += rating
        return total/len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super(Book).__init__(title, isbn)
        self.author = author

    def get_author(self):
        pass 

    def __repr__(self):
        return {title} + "by" + {author}
        
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super(Book).__init__(title, isbn)
        self.subject = subject
        self.level = level
        get_subject = subject

    def get_level(self):
        pass

    def __repr__(self):
        return {title} + ", a " + {level} + "manual on" + {subject}
        
class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, subject, level, isbn):
        return Non_Fiction(title, author, isbn)

    def add_book_to_user(self, book, email, rating = None):
        for user in self.users:
            if email not in self.users:
                print("No user with email " + {email} + "!"
            else:
                print(read_book(book, rating))
                print(add_rating(book, rating))

    def add_user(self, name, email, user_books = None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for books in self.books:
            print books 

    def print_users(self):
        for users in self.users:
            print users

    def most_read_book(self):
        most_read = integer(
        for book in self.books():
            if book > largest.
                self.books.append(book)
        return most_read_book

    def highest_rated_book(self):
        highest_rated = []
        for book in self.books.keys():
            if book.get_average_rating() > highest_rated:
                highest_rated = book.get_average_rating()
            else:
                continue
        return highest_rated
    
    def most_positive_user(self):
        highest_average = 0
        highest_user = ""
        for user in self.users.values():
            if user.get_average_rating() > highest_average:
                highest_average = user.get_average_rating()
                highest_user = user.name
            else:
                continue
        return highest_user
                
        
