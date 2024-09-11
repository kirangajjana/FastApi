from fastapi import Body,FastAPI
from pydantic import BaseModel

app=FastAPI()


class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int

    def __init__(self, id, title, author, description, rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating

class Bookrequest(BaseModel):
             id:int
             title:str
             author:str
             description:str
             rating:int 

BOOKS=[ Book(1,'computerscience pro','codingwithkiran','A veruy nice book',5),
       Book(2,'Statistics pro','codingwithkiran','A very nice book',5),
       Book(3,'Calculus pro','codingwithkiran','A very nice book',5),
       Book(4,'Datascience pro','codingwithkiran','A very nice book',5),
       Book(5,'HP1', 'Author 1', 'Book Description',2),
       Book(5,'HP2', 'Author 2', 'Book Description',3),
       Book(5,'HP3', 'Author 3', 'Book Description',2)]             

@app.get("/books")
def read_all_books():
       return BOOKS

@app.post("/create-book")
def create_book(book_request: Bookrequest):
       BOOKS.append(book_request)

