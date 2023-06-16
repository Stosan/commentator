from bardapi import Bard

key="WggnOxa5VgqEAWlvXLDDaod0Eq4MUPnEqUCwhqhIze6AR5GbxndNTmL_QUJvJPCnlWbadA."

def RunBard(langtype: str, query: str):
    try:
        PROMPT_KEY=f"PROMPT:Add inline comprehensive commenting to this {langtype} code, add a detailed explanation of how the function works as comment at the top of the function and do nothing else: "
        code = f'''{query}'''
        PROMPT=f"{PROMPT_KEY}{code}"
        token = key
        bard = Bard(token=token, timeout=10)
        res = bard.get_answer(PROMPT)['content']
        return res,None
    except Exception as e:
        return None,e
