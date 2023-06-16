from fastapi import FastAPI, HTTPException,Request
from src.api.router.api_route import router as api_router
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
app = FastAPI()

# Mount the user router under the /users path
app.include_router(api_router, prefix="/api/v1", tags=["api"])

app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("src.main:app",host="0.0.0.0",port=8000)

