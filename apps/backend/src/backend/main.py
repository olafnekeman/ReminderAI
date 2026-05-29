from fastapi import FastAPI
from backend.api import docs, v1

app = FastAPI()


app.include_router(docs.router)
app.include_router(v1.router)
