import logging
from uuid import UUID
from fastapi import APIRouter


logger = logging.getLogger(__file__)
app = APIRouter(prefix="/users")


logger.info("This is the looginf info")

@app.get("/",include_in_schema=False)
def root():
    pass



@app.post("", tags=["User"],status_code=201)
def new_user():
    '''
        This is the post api call for the user
    '''
    logger.info("This is the looginf info")
    return "Post user call"

@app.get("/users", tags=["User"])
def get_users():
    '''
        This is the get all user api call for the user
    '''
    return "Get all user call"

@app.get("/{user_id}", tags=["User"])
def get_an_user(user_id:UUID):
    '''
        This is the get an user api call for the user
    '''
    return "Get an user call"

@app.delete("/{user_id}", tags=["User"])
def delete_user(user_id:UUID):
    '''
        This is the delete user api call for the user
    '''
    return "Delete user call"