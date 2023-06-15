import json
from fastapi import APIRouter, Response
from src.core.bard.codecommenter import make_code_comments
router = APIRouter()



@router.post("/create-code-comments")
def create_code_comment(user_data: dict):
    resp=make_code_comments(user_data)
    return Response(content=resp["result"], status_code=200)


