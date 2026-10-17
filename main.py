from fastapi import FastAPI

app = FastAPI() # Initialize my API 

# This connectes a standard API GET request to a python function
@app.get("/")
async def root():
    return {"message":"Hello World"} # Returns standard JSON

