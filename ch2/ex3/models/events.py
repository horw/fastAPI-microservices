from beanie import Document
from typing import Optional, List
from pydantic import BaseModel


class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example":
                {
                    "title": "FastAPI Book Launch",
                    "image": "https:///",
                    "description": "Something about this story",
                    "tags": ["a", "b", "c", "d"],
                    "location": "Google Meet"
                }
        }

    class Setting:
        name = "events"


class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example":
                {
                    "title": "FastAPI Book Launch",
                    "image": "https:///",
                    "description": "Something about this story",
                    "tags": ["a", "b", "c", "d"],
                    "location": "Google Meet"
                }
        }