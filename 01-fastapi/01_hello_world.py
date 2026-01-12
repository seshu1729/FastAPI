# uvicorn 01_hello_world:api --port 9999
# OR
# fastapi dev .\01_hello_world.py

from fastapi import FastAPI

api = FastAPI()

# GET, POST, PUT, DELETE

# GET    => When we need information
# POST   => Create or submit new to the server
# PUT    => when you change
# DELETE => when you delete


@api.get('/')
def index():
    return {"message": "Hello world"}






