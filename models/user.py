from typing import Optional
import uuid
from sqlalchemy import text
from sqlmodel import (
    Column,
    Field,
    SQLModel,
    String,
)

from sqlalchemy.dialects.postgresql import UUID

class User(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        sa_column=Column(
            "id",
            UUID(as_uuid=True),
            primary_key=True,
            server_default=text("uuid_generate_v4()"),
            nullable=False
        )
    )

    user_name: str = Field(
        sa_column=Column("user_name", type_=String(50), nullable=False)
    )

    password: str = Field(
        sa_column=Column("password", type_=String(50), nullable=False)
    )


    class Config:
        json_schema_extra = {
            "example": {
                "user_name": "test_user",
                "password": "password@123",
            }
        }