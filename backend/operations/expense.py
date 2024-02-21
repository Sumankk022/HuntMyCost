from uuid import uuid4
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
        description=expense.description,
        created_date=expense.created_date,
        user_id=expense.user_id,

    )

    db.add(expense)