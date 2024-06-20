from fastapi import APIRouter,Path
from typing import Annotated

router = APIRouter()

@router.get('/user/{name}/{age}')
async def getUser(name: Annotated[str, Path(min_length=5, max_length=50)], age: Annotated[int, Path(ge=1, le=100)]):
  return {"name": name, "age": age}
