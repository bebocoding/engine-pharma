from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import user

app = FastAPI()

app.include_router(user.router)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello World!"}







