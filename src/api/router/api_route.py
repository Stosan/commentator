import json
from fastapi import APIRouter, Response
from src.core.bard.codecommenter import make_code_comments
router = APIRouter()



@router.post("/generate-comments")
def create_code_comment(user_data: dict):
    resp=make_code_comments(user_data)
    if resp["result"] == "Unknown language.":
        return Response(content=resp["result"], status_code=400)
    return Response(content=resp["result"], status_code=200)


