import os
from sqlalchemy import exc
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine

def create_db_engine():
    DATABASE_URL = os.environ.get("DATABASE_URL")

    return create_engine(DATABASE_URL,echo=False)

def db_session():
    engine = create_db_engine()

    SessionLocal = sessionmaker(bind=engine)

    session = SessionLocal()
    with session.begin():
        try:
            yield session
            session.commit()
        except exc.SQLAlchemyError:
            session.rollback()
            raise
        finally:
            session.close()
            SQLModel.metadata.create_all(bind=engine)