from fastapi import FastAPI, HTTPException
from typing import Dict

app = FastAPI()


class CodeCommentData:
    pass

class UserData:
    pass

@app.get("/")
def read_root():
    return {"Hello": "World"}


