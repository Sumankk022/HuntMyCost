from typing import Optional
import uuid
from sqlalchemy import ForeignKey, text
from sqlmodel import (
    Column,
    Field,
    SQLModel,
    String,
    DateTime,
    Integer,
    func,
)

from datetime import date
from sqlalchemy.dialects.postgresql import UUID

class Expense(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        sa_column=Column(
            "id",
            UUID(as_uuid=True),
            primary_key=True,
            server_default=text("uuid_generate_v4()"),
            nullable=False
        )
    )

    name: Optional[str] = Field(
        sa_column=Column("name", type_=String(50), nullable=False)
    )
    amount: int = Field(
        sa_column=Column("amount",type_=Integer(), nullable=False)
    )
    description: str = Field(
        sa_column=Column("description", type_=String(250), nullable=True)
    )
    created_date: date = Field(
        sa_column=Column("date", type_=DateTime(), nullable=False, server_default=func.now())
    )
    user_id:uuid.UUID = Field(
        sa_column=Column("user", ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    )

    class Config:
        json_schema_extra = {
            "example":{
                "name":"expense name",
                "description": "expense description",
                "amount": 250,
                "user_id": ""
            }
        }


