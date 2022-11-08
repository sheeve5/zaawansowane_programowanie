from classes.Library import Library

class Book:
    title: str
    library: Library
    publication_date: str
    author_name: str
    author_surname: str
    number_of_pages: int

    def __str__(self):
        return "{}, Autor: {} {}, " \
               "\nBiblioteka przy ulicy {} w {}, " \
               "\ndata publikacji {}, {} stron".format(
                    self.title,
                    self.author_name,
                    self.author_surname,
                    self.library.street,
                    self.library.city,
                    self.publication_date,
                    self.number_of_pages)

    def __init__(self, _title: str, _library: Library, _publication_date: str,
                 _author_name: str, _author_surname: str,
                 _number_of_pages: int):
        self.title = _title
        self.author_name = _author_name
        self.author_surname = _author_surname
        self.library = _library
        self.publication_date = _publication_date
        self.number_of_pages = _number_of_pages
