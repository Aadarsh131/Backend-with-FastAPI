from fastapi import APIRouter,Path,Query
from typing import Annotated

router = APIRouter()

# Path Params validation
@router.get('/user/{name}/{age}')
async def getUser(name: Annotated[str, Path(title="Path String",description="Query string for the items to search in the database that have a good match", min_length=5, max_length=50)], age: Annotated[int, Path(ge=1, le=100)]):
  return {"name": name, "age": age}

# Query Params validation
@router.get('/items')
async def read_items(q: Annotated[str|None, Query(max_length=50)] = None): #Having a default value of any type, including None, makes the parameter optional (not required). 
# when you need to declare a value as required while using Query, you can simply not declare a default value or use "=..." (Ellipsis, a part of python)
  results = {"items":[{'a':'A'},{'b':'B'}]}
  if q:
    results.update({"q":q})
  return results

# http://localhost:8000/items/?q=foo&q=bar 
@router.get('/items/multiple_values/')
# or simply Annotated[list | None] if we dont want to restrict the datatypes inside the list
async def read_multple_items(q: Annotated[list[str]|None,Query(max_length=50)]): # some example of deafult values- `= ["foo", "bar"]`
  return {"q": q} # output: {"q": ["foo","bar"]}