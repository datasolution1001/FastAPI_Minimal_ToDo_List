from fastapi import FastAPI

app = FastAPI()

#minimal app - get request
@app.get("/",tags=['ROOT'])
async def root() -> dict: 
    return {"Ping":"Pong"}


# Get --> Read ToDo

@app.get('/todo', tags=['todos'])
async def get_todo() -> dict: 
    return{"data": todos}

# Post --> Create Todo
@app.post("/todo", tags=["todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": "A todo has been added !"
    }


# Put --> Update Todo
@app.put("/todo/{id}", tags=["todos"])
async def update_todo(id:int, body:dict) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todo['Activity'] = body['Activity']
            return {
                "data": f"Todo with id {id} has been updated"
            }
    return {
        "data": f"Todo with this id {id} number has not found"
    }

@app.delete("/todo/{id}",tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if  int((todo["id"])) == id:
            todos.remove(todo)
            return {
                "data": f"todo with id {id} has been deleted"
            }
        return {
            "data": f"this to do with id {id} wasn't fount!"
        }


todos = [
    {"id": "1",
     "Activity": "Cycling for two hours at 4PM"
     },
    {"id": "2",
     "Activity": "Make a reading plan for the next year"
     }
]