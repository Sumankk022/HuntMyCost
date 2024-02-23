from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import db_session
from models.expense import Expense
from operations.expense import create_expense, delete_expense_by_id, get_all_expense, get_expense_by_id

app = APIRouter(prefix="/expenses")

@app.get("/",include_in_schema=False)
def root():
    pass

@app.post("", tags=["Expense"],status_code=201)
def new_expense(
    session: Annotated[Session, Depends(db_session)],
    expense:Expense
):
    '''
        This is the post api call for the expense
    '''
    return create_expense(db=session, expense=expense)

@app.get("/expenses", tags=["Expense"])
def get_expenses(session: Annotated[Session, Depends(db_session)]):
    '''
        This is the get all expense api call for the expense
    '''
    return get_all_expense(db=session)

@app.get("/{expense_id}", tags=["Expense"])
def get_an_expense(
    expense_id:UUID,
    session: Annotated[Session, Depends(db_session)]
):
    '''
        This is the get an expense api call for the expense
    '''
    return get_expense_by_id(db=session, expense_id=expense_id)

@app.delete("/{expense_id}", tags=["Expense"])
def delete_expense(expense_id:UUID, session: Annotated[Session, Depends(db_session)]):
    '''
        This is the delete expense api call for the expense
    '''
    return delete_expense_by_id(expense_id=expense_id, db=session)