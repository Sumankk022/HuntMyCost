from uuid import UUID
from fastapi import APIRouter
from models.expense import Expense

app = APIRouter(prefix="/expenses")

@app.get("/",include_in_schema=False)
def root():
    pass

@app.post("", tags=["Expense"],status_code=201)
def new_expense(
    expense:Expense
):
    '''
        This is the post api call for the expense
    '''
    return expense

@app.get("/expenses", tags=["Expense"])
def get_expenses():
    '''
        This is the get all expense api call for the expense
    '''
    return "Get all expense call"

@app.get("/{expense_id}", tags=["Expense"])
def get_an_expense(expense_id:UUID):
    '''
        This is the get an expense api call for the expense
    '''
    return "Get an expense call"

@app.delete("/{expense_id}", tags=["Expense"])
def delete_expense(expense_id:UUID):
    '''
        This is the delete expense api call for the expense
    '''
    return "Delete expense call"