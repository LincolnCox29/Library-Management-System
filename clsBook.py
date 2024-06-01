class Book:

    def __init__(
            self,
            name: str,
            author: str,
            year: int,
            genre: str,
            pageCount: int,
            isbn: int,
            copies: int
            ):
        self._name = name
        self._author = author
        self._year = year
        self._genre = genre
        self._pageCount = pageCount
        self._isbn = isbn
        self._copies = copies

    @property
    def name(self):
        return self._name
    
    @property
    def author(self):
        return self._author
    
    @property
    def year(self):
        return self._year
    
    @property
    def genre(self):
        return self._genre
    
    @property
    def pageCount(self):
        return self._pageCount
    
    @property
    def isbn(self):
        return self._isbn
    
    @property
    def copies(self):
        return self._copies
    

    def __str__(self) -> str:
        return f'''
        Book: {self.name},
        Author: {self.author}, 
        Year: {self.year}, 
        Genre: {self.genre}, 
        Page Count: {self.pageCount}, 
        ISBN: {self._isbn}, 
        Copies: {self.copies}'''
    
    def delCopy(self):
        self._copies -= 1

    def appendCopy(self):
        self._copies += 1

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Book):
            return (
                self._name == value.name and
                self._author == value.author and
                self._year == value.year and
                self._genre == value.genre and
                self._isbn == value.isbn
                )
        return False
    
    def to_dict(self):
        return {
            'name': self.name,
            'author': self.author,
            'year': self.year,
            'genre': self.genre,
            'pageCount': self.pageCount,
            'isbn': self.isbn,
            'copies': self.copies
        }