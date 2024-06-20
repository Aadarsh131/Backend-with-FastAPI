from fastapi import APIRouter,Body
from pydantic import BaseModel, Field
from typing import Annotated

router = APIRouter()

class Item(BaseModel):
  name: str
  description: str | None = None
  price: float = Field(title="price of the Item", le=5000) #You can use Pydantic's Field to declare extra validations and metadata for model attributes.
  tax: float | None = None

@router.post("/items/")
async def create_item(item: Item):
  item_dict = item.model_dump() #dict() is deprecated
  if item.tax:
      price_with_tax = item.price + item.tax
      item_dict.update({"price_with_tax": price_with_tax})
  return item_dict

@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, importance: Annotated[int,Body()]): #for single value use Body()
    return {"item_id": item_id, **item.dict(), "importance": importance}



