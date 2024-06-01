from clsBook import Book
from clsReader import Reader
from clsLibrary import Library
import json

def loadLibraryFromJson(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        books = [
            Book(
                name=book['name'],
                author=book['author'],
                year=book['year'],
                genre=book['genre'],
                pageCount=book['pageCount'],
                isbn=book['isbn'],
                copies=book['copies']
            ) for book in data['booksList']
        ]
        readers = [
            Reader(
                name=reader['name'],
                surname=reader['surname'],
                libraryCardNumber=reader['card_number'],
                booksList=[
                    Book(
                        name=book['name'],
                        author=book['author'],
                        year=book['year'],
                        genre=book['genre'],
                        pageCount=book['pageCount'],
                        isbn=book['isbn'],
                        copies=book['copies']
                    ) for book in reader['booksList']
                ]
            ) for reader in data['readersList']
        ]
        return Library(readers,books)
    
def saveLibraryToJson():
    with open("library.json", "w") as json_file:
        json.dump(library.to_dict(), json_file, indent=4)

library = loadLibraryFromJson('library.json')