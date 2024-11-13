from api.controllers import support_request_controller
from backend.api.server import api

api.include_router(support_request_controller)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.server:api", host="0.0.0.0", port=8000, reload=True)