from pydantic import BaseModel


class Item(BaseModel):
    item: str
    status: str


class ToDo(BaseModel):
    id: str
    item: Item


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }