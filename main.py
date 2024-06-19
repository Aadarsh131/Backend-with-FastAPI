from fastapi import FastAPI
 
app = FastAPI()

BOOKS = [
 {"title": "title one", "author": "author one", "category": "science"},
 {"title": "title two", "author": "author two", "category": "geography"},
 {"title": "title three", "author": "author three", "category": "science"},
 {"title": "title four", "author": "author four", "category": "arts"},
]
 
 # GET req
@app.get("/hello")
async def read_root():
    return {"Hello": "World"}

@app.get("/books")
async def books():
    return BOOKS

# order of the defined routes matter, 'authors' in "/books/authors" would be treated as a dynamic param if we have the route "/books/{id}" defined above this rotue,
# keep in mind it doesn't conflict with `/books/{id}`
# make sure all the dynamic path params routes are below the general routes without dynamic params
@app.get("/books/authors")
async def getId():
  authors = []
  for book in BOOKS:
    authors.append({"author": book['author']})
  return authors

# path params
@app.get("/books/{id}")
async def getId(id:str):
  return {"id": id}

@app.get('/books/title/{title}')
async def getBook(title: str):
   for book in BOOKS:
      if book.get("title").casefold() == title.casefold():
         return book

# Query params
# search for a book with certain category
@app.get('/books/')
async def getBooks(category: str):
   books = []
   for book in BOOKS:
      if book.get("category").casefold() == category.casefold():
         books.append(book)
   return books

# Query Params and Path params together
# search for a book with certain author & category
@app.get('/books/{title}/')
async def getBooks(title: str, category: str):
   for book in BOOKS:
      if (book.get("category").casefold() == category.casefold()) and \
        (book.get('title').casefold() == title.casefold()):
        return book




   