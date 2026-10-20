from fastapi import FastAPI

app = FastAPI() #Turning on engines, creating the API instance.

#Post means we are adding a new item. Create.
@app.post("/items", status_code=201)
async def creat_items(item: dict): #Async allows the program to handle multiple tasks without waitng for each one to finish. (item:dict) allows json to be converted into a pythin dictionary.
    return item #The univeral way of returning the information witout having without having to write custome messages. 


@app.get ("/items", status_code=200)
async def read_items():
    return {"items": [...]}


@app.put ("/items", status_code=200)
async def update_items(item_id:int, item: dict):
    return 
