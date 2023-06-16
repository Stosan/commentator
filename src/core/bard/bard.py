from bardapi import Bard

key="WggnOxa5VgqEAWlvXLDDaod0Eq4MUPnEqUCwhqhIze6AR5GbxndNTmL_QUJvJPCnlWbadA."

def RunBard(langtype: str, query: str):
    try:
        PROMPT_KEY = "PROMPT: Add inline comprehensive commenting to this {langtype} code. Provide a detailed explanation of how the function works as a comment at the top of the function. Avoid including examples of how to use the function, and refrain from adding any additional notes after the commented code."
        code = f'''{query}'''
        PROMPT=f"{PROMPT_KEY}{code}"
        token = key
        bard = Bard(token=token, timeout=30)
        res = bard.get_answer(PROMPT)['content']
        return res,None
    except Exception as e:
        return None,e
