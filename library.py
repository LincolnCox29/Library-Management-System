from clsBook import Book
from clsReader import Reader
from clsLibrary import Library

library = Library(
        booksList = [
            Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction", 281, 9780061120084, 10),
            Book("1984", "George Orwell", 1949, "Dystopian", 328, 9780451524935, 5),
            Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction", 180, 9780743273565, 8),
            Book("The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction", 224, 9780316769488, 7),
            Book("To the Lighthouse", "Virginia Woolf", 1927, "Modernist", 209, 9780156907392, 3),
            Book("Pride and Prejudice", "Jane Austen", 1813, "Romance", 279, 9780486284736, 6),
            Book("Moby-Dick", "Herman Melville", 1851, "Adventure", 752, 9780142437247, 4),
            Book("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 9780547928227, 9),
            Book("The Lord of the Rings", "J.R.R. Tolkien", 1954, "Fantasy", 1178, 9780544003415, 12),
            Book("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Philosophical Fiction", 671, 9780679734505, 5),
            Book("The Picture of Dorian Gray", "Oscar Wilde", 1890, "Gothic", 254, 9780141439570, 5),
            Book("War and Peace", "Leo Tolstoy", 1869, "Historical fiction", 1225, 9780143035008, 10),
            Book("The Brothers Karamazov", "Fyodor Dostoevsky", 1880, "Philosophical fiction", 796, 9780374528379, 6),
            Book("Anna Karenina", "Leo Tolstoy", 1878, "Realist novel", 864, 9780143035008, 8),
            Book("Don Quixote", "Miguel de Cervantes", 1605, "Novel", 863, 9780142437230, 11),
            Book("Les Misérables", "Victor Hugo", 1862, "Historical novel", 1232, 9780140444308, 9),
            Book("Brave New World", "Aldous Huxley", 1932, "Dystopian", 288, 9780060850524, 5),
            Book("One Hundred Years of Solitude", "Gabriel García Márquez", 1967, "Magic realism", 417, 9780060883287, 12),
            Book("The Bell Jar", "Sylvia Plath", 1963, "Semi-autobiographical", 244, 9780571081783, 7),
        ],
        readersList = [
            Reader(
                "Timothy","King",1,[
                    Book("One Hundred Years of Solitude", "Gabriel García Márquez", 1967, "Magic realism", 417, 9780060883287, 1),
                    Book("The Lord of the Rings", "J.R.R. Tolkien", 1954, "Fantasy", 1178, 9780544003415, 1),
                ]
            ),
            Reader(
                "Charles", "Norton",2,[
                    Book("One Hundred Years of Solitude", "Gabriel García Márquez", 1967, "Magic realism", 417, 9780060883287, 1),
                    Book("The Picture of Dorian Gray", "Oscar Wilde", 1890, "Gothic", 254, 9780141439570, 1),
                    Book("War and Peace", "Leo Tolstoy", 1869, "Historical fiction", 1225, 9780143035008, 1),
                    Book("Moby-Dick", "Herman Melville", 1851, "Adventure", 752, 9780142437247, 1),
                    Book("The Bell Jar", "Sylvia Plath", 1963, "Semi-autobiographical", 244, 9780571081783, 1),
                ]
            ),
            Reader(
                "Wendy", "Neal",3,[
                    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction", 180, 9780743273565, 1),
                    Book("The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction", 224, 9780316769488, 1),
                ]
            )
        ]
    )