from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modèle de données
class Item(BaseModel):
    text: str 
    is_done: bool = False

# Stockage temporaire
items: list[Item] = []

# Route de base
@app.get("/")
def root():
    return {"Hello": "World"}

# Créer un item
@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

# Obtenir un item par son ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

# Lister les items (avec limite)
@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[:limit]
