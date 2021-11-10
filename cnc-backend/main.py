from fastapi import FastAPI

from src.routers import router

from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

app = FastAPI(
    title="API de CNC",
    description="Esta API es la encargada de procesar las solicitudes",
    version = "1.0",
    middleware=middleware
)

app.include_router(router)