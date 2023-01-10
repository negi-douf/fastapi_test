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
