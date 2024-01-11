from fastapi import FastAPI
from app.routers import todos, users, login
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router=todos.router, tags=["Todos"], prefix="/todos")
app.include_router(router=users.router, tags=["Users"], prefix="/users")
app.include_router(router=login.router, tags=["Login"], prefix="/login")