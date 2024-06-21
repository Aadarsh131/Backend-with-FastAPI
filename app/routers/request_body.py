from fastapi import APIRouter,Body
from pydantic import BaseModel, Field, HttpUrl
from typing import Annotated

router = APIRouter()

class Image(BaseModel):
   url: HttpUrl #Pydantic type
   name: str

class Item(BaseModel):
  name: str
  description: str | None = None
  price: float = Field(title="price of the Item", le=5000) #You can use Pydantic's Field to declare extra validations and metadata for model attributes.
  tax: float | None = None
  tags: list[str] = [] # for unique values use set- set[str] = set()
  # image: Image | None = None #using nested Models, eg-  "image": {"url": "http://example.com/baz.jpg","name": "The Foo live"}
  images: list[Image] | None = None # "images": [{"url": "http://example.com/baz.jpg","name": "The Foo live"},{"url": "http://example.com/dave.jpg","name": "The Baz"}]


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


@router.post("/images/multiple")
async def create_multiple_images(images: list[Image]): #Body of pure list with custom type
   return images

