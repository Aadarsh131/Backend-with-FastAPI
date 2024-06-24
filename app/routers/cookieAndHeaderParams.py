from fastapi import APIRouter, Cookie, Header
from typing import Annotated
from uuid import UUID

router = APIRouter()

@router.get("/place")
async def get_place(id: Annotated[UUID | None, Cookie()] = None):
  return {"id": id}

@router.get('/place/name')
async def get_place_name(user_agent: Annotated[str | None, Header()]):
    return {"user-agent": user_agent}

# Most of the standard headers are separated by a "hyphen" character, also known as the "minus symbol" (-), But a variable like `user-agent` is invalid in Python, So, by default, Header will convert the parameter names characters from underscore (_) to hyphen (-) to extract and document the headers.
# if automatic underscore conversion is not needed then use `Header(convert_underscores=False)`

# Headers by functionality can also have duplicate values, for that we can use list[str] to store them
@router.get("/place/name/fake")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token} 
"""
# if we send:
X-Token: foo
X-Token: bar

#response would be like
{
    "X-Token values": [
        "bar",
        "foo"
    ]
}
"""