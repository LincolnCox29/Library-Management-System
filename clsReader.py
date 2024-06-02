class Reader():

    def __init__(
            self,
            name: str,
            surname: str,
            libraryCardNumber: int,
            booksList
            ):
        self._name = name
        self._surname = surname
        self._libraryCardNumber = libraryCardNumber
        self._booksList = booksList

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def libraryCardNumber(self):
        return self._libraryCardNumber
    
    @property
    def booksList(self):
        return self._booksList
    
    def __str__(self) -> str:
        return f'''
        Reader: {self.name} {self.surname}, 
        Library Card Number: {self.libraryCardNumber}'''
    
    def takeBook(self, library, book):
        if book not in self._booksList and book in library.booksList:
            self._booksList.append(book.toBookWithOneCopy())
            if book.copies == 1:
                library.booksList.remove(book)
            else:
                book.delCopy()

    def returnBook(self, library, book):
        if book in self._booksList:
            self._booksList.remove(book)
            if book not in library.booksList:
                library.booksList.append(book)
            else:
                for i in range(len(library.booksList)):
                    if book == library.booksList[i]:
                        library.booksList[i].appendCopy()

    def to_dict(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'card_number': self.libraryCardNumber,
            'booksList': [book.to_dict() for book in self.booksList]
        }
    
    def checkingBookForAvailability(self, inpBook):
        for book in self.booksList:
            if book == inpBook:
                return True
        return False