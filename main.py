from fastapi import FastAPI

from item_schema import Item

app = FastAPI()


@app.get("/hello")
async def hello() -> str:
    return "hello"


@app.get("/param")
def return_param(name: str) -> dict:
    return {"name": name}


@app.get("/items")
def read_items() -> list[Item]:
    items = [
        Item(id=1, name="cheese"),
        Item(id=2, name="milk"),
    ]
    return items


@app.get("/items/{item_id}")
def read_item(item_id: int) -> Item:
    item = Item(id=item_id, name="cheese")
    return item
