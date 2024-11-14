from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from .controllers.support_request_controller import router as support_request_router

origins = [
    "http://127.0.0.1:8000",
    "http://localhost:5173",
    'https://notifier.fly.dev'
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

api.mount("/", StaticFiles(directory="public", html=True), name="public")

# Serving static files
@api.get("/{full_path:path}")
async def serve_react_app():
    return FileResponse('public/index.html')