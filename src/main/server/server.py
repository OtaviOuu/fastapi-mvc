from fastapi import FastAPI
from src.main.routers.pessoas_routes import pessoas_routes

app = FastAPI()
app.include_router(pessoas_routes)
