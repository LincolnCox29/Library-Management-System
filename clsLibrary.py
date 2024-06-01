class Library():

    def __init__(
            self,
            readersList: list,
            booksList: list
            ):
        self.readersList = readersList
        self.booksList = booksList

    def appendReader(self, newReader):
        self.readersList.append(newReader)

    def delReader(self, reader):
        self.readersList.remove(reader)

    def appendBook(self, newBook):
        self.booksList.append(newBook)

    def delBook(self, book):
        self.booksList.remove(book)

    def giveBook(self, library, book, reader):
        reader.takeBook(library, book)

    def takeBook(self, library, book, reader):
        reader.returnBook(library, book)

    def __searchAny(self, listName : str, attribute_name : str, value):
        if listName == "readersList":
            selfList = self.readersList
        else:
            selfList = self.booksList
        for book in selfList:
            attribute = getattr(book, attribute_name) # позволяет получить значение атрибута объекта по его имени
            if attribute == value:
                print(book)

    def searchBook(self, attribute_name : str, value):
        self.__searchAny('booksList', attribute_name, value)

    def searchReader(self, attribute_name : str, value):
        self.__searchAny('readersList', attribute_name, value)

    def to_dict(self):
        return {
            'booksList': [book.to_dict() for book in self.booksList],
            'readersList': [reader.to_dict() for reader in self.readersList]
        }
