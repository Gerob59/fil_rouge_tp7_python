from fastapi import FastAPI
from .routes import get_routes

app = FastAPI()
app.include_router(get_routes())


# from config.sqlalchemy import bind_engine
# bind_engine()