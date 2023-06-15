from fastapi import FastAPI, HTTPException
from src.api.router.api_route import router as api_router
app = FastAPI()

# Mount the user router under the /users path
app.include_router(api_router, prefix="/api/v1", tags=["api"])

@app.get("/")
def read_root():
    return {"Hello": "World"}


