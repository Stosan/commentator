from bardapi import Bard
from src.config import appconfig


def RunBard(langtype: str, query: str):
    try:
        SQL_PROMPT_KEY = f"Add a concise and informative comment at the beginning of this {langtype} query to describe its purpose. Avoid including examples or additional notes after the commented code."
        PROMPT_KEY = f"PROMPT: Add inline comprehensive commenting to this {langtype} code. Provide a detailed explanation of how the function works as a comment at the top of the function. Avoid including examples of how to use the function, and refrain from adding any additional notes after the commented code."
        code = f'''{query}'''
        if langtype == "SQL":
            PROMPT=f"{SQL_PROMPT_KEY}{code[4:]}"
        else:
            PROMPT=f"{PROMPT_KEY}{code}"
        bard = Bard(token=appconfig.bard_key, timeout=30)
        res = bard.get_answer(PROMPT)['content']
        return res,None
    except Exception as e:
        return None,e
