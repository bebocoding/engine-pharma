from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers.user import user, auth

from . import models
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)



origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router)
app.include_router(auth.router)


@app.get('/')
def home():
  return {"message": "Hello World"}







