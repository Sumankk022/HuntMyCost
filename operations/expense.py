from uuid import UUID, uuid4
from sqlalchemy.orm import Session
from models.expense import Expense
from fastapi.exceptions import HTTPException

def create_expense(
        db: Session,
        expense: Expense,
):
    existing_expense = (
        db.query(Expense)
        .where(
            Expense.name == expense.name,
            Expense.description == expense.description,
            Expense.created_date == expense.created_date,

        )
        .one_or_none()
    )

    if existing_expense:
        raise HTTPException(
            status_code = 409,
            detail=(
                "User already exist"
            ),
        )
    
    expense = Expense(
        id=uuid4(),
        name=expense.name,
        amount=expense.amount,
        description=expense.description,
        user_id=expense.user_id,

    )

    db.add(expense)
    return expense

def get_all_expense(db:Session):
    return db.query(Expense).all()

def get_expense_by_id(expense_id:UUID,db:Session):
    expense = db.query(Expense).filter(Expense.id == expense_id).one_or_none()
    if not expense:
        raise HTTPException(status_code=404, detail="User not found")
    return expense

def delete_expense_by_id(
        db:Session,
        expense_id:UUID,
):
    expense = db.query(Expense).filter(Expense.id == expense_id).one_or_none()
    if expense:
        db.delete(expense)
        return "Deleted Successfully"
    else:
        raise HTTPException(status_code=404, detail="Expense not found")