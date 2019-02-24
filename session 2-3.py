class book:
    def __init__(self,name,publication_year,pages):
        self.name=name
        self.publication_year=publication_year
        self.pages=pages
    def __str__(self):
        return self.name
    __repr__=__str__

def Goruping(books):
    ancient_books=[]
    new_books=[]
    for book in books:
        if book.publication_year<1500:
            ancient_books.append(book)
            print(ancient_books)
        else:
            new_books.append(book)
            print(new_books)


b1=book("a",1300,900)
b2=book("b",1500,600)
b3=book("c",2000,300)
books=[b1,b2,b3]
Goruping(books)