from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import get_routes

# from config import Base, engine
# Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(get_routes())


@app.get("/")
def root():
    return {"message": "Hello World pushing out to ubuntu"}
