from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .controllers.support_request_controller import router as support_request_router

origins = [
    "http://localhost:5173",
]

api = FastAPI()

api.include_router(support_request_router)

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)