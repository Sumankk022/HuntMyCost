from fastapi import FastAPI

from . import user, expense

app = FastAPI(title="Hunt My Cost", version="0.0.1")

app.include_router(user.app)
app.include_router(expense.app)