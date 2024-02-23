import logging
from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends
from models.user import User
from operations.user import create_user, get_all_users, get_user_by_id, delete_user_by_id
from sqlalchemy.orm import Session
from db.database import db_session


logger = logging.getLogger(__file__)
app = APIRouter(prefix="/users")


logger.info("This is the looginf info")

@app.get("/",include_in_schema=False)
def root():
    pass



@app.post("", tags=["User"],status_code=201)
def new_user(
    user:User,
    session: Annotated[Session, Depends(db_session)]
):
    '''
        This is the post api call for the user
    '''
    logger.info("This is the looginf info")
    return create_user(db=session,user=user)

@app.get("/users", tags=["User"])
def get_users(
    session: Annotated[Session, Depends(db_session)]
):
    '''
        This is the get all user api call for the user
    '''
    return get_all_users(db=session)

@app.get("/{user_id}", tags=["User"])
def get_an_user(
    user_id:UUID,
    session: Annotated[Session, Depends(db_session)] 
):
    '''
        This is the get an user api call for the user
    '''
    return get_user_by_id(user_id=user_id,db=session)

@app.delete("/{user_id}", tags=["User"])
def delete_user(
    user_id:UUID,
    session: Annotated[Session, Depends(db_session)] 
):
    '''
        This is the delete user api call for the user
    '''
    return delete_user_by_id(user_id=user_id, db=session)