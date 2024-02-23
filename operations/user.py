from uuid import UUID, uuid4
from sqlalchemy.orm import Session
from models.user import User
from fastapi.exceptions import HTTPException

def create_user(
        db: Session,
        user: User,
):
    existing_user = (
        db.query(User)
        .where(
            User.user_name == user.user_name,
        )
        .one_or_none()
    )

    if existing_user:
        raise HTTPException(
            status_code = 409,
            detail=(
                "User already exist"
            ),
        )
    
    user = User(
        id=uuid4(),
        user_name=user.user_name,
        password=user.password,
    )

    db.add(user)
    return user

def get_all_users(db:Session):
    return db.query(User).all()

def get_user_by_id(
        db:Session,
        user_id:UUID,
):
    user = db.query(User).filter(User.id == user_id).one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def delete_user_by_id(
        db:Session,
        user_id:UUID,
):
    user = db.query(User).filter(User.id == user_id).one_or_none()
    if user:
        db.delete(user)
        return "Deleted Successfully"
    else:
        raise HTTPException(status_code=404, detail="User not found")
