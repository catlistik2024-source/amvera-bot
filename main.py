from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Dish(BaseModel):
    id: int
    name: str
    description: str = ''
    price: float

class Order(BaseModel):
    user_id: int
    dish_ids: List[int]

class Announcement(BaseModel):
    message: str

menu = [
    Dish(id=1, name="Бургер", description="Вкусный с говядиной", price=150),
    Dish(id=2, name="Картофель фри", description="Хрустящий", price=70),
]

orders = []
announcement = Announcement(message="Добро пожаловать в Ресторан спонтанной кухни!")

@app.get("/menu", response_model=List[Dish])
async def get_menu():
    return menu

@app.post("/menu")
async def add_dish(dish: Dish):
    if any(d.id == dish.id for d in menu):
        raise HTTPException(status_code=400, detail="Блюдо с таким id уже существует")
    menu.append(dish)
    return {"message": "Блюдо добавлено"}

@app.delete("/menu/{dish_id}")
async def delete_dish(dish_id: int):
    global menu
    menu = [d for d in menu if d.id != dish_id]
    return {"message": "Блюдо удалено"}

@app.get("/announcement")
async def get_announcement():
    return announcement

@app.post("/announcement")
async def set_announcement(new_announcement: Announcement):
    global announcement
    announcement = new_announcement
    return {"message": "Объявление обновлено"}

@app.post("/order")
async def create_order(order: Order):
    orders.append(order)
    return {"message": "Заказ принят"}

@app.get("/orders", response_model=List[Order])
async def get_orders():
    return orders
