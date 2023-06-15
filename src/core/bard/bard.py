from bardapi import Bard

key="WggnOxa5VgqEAWlvXLDDaod0Eq4MUPnEqUCwhqhIze6AR5GbxndNTmL_QUJvJPCnlWbadA."

def RunBard(langtype: str, query: str):
    try:
        PROMPT_KEY=f"PROMPT:Add inline comprehensive commenting to this {langtype} code, add a detailed explanation of how the function works as comment at the top of the function and do nothing else:"
        code = '''
        func DetectProgrammingLanguage(function string) string {
            // Convert the function to lowercase for case-insensitive comparison
            function = strings.ToLower(function)

            if function[:3]=="def"{
                return "Python"
            } else if function[:4]=="func" {
                return "Go"
            } else if function[:8]=="function"{
                return "JavaScript"
            }

            return "Unknown"
        }
        '''
        PROMPT=f"{PROMPT_KEY}+{code}"
        token = key
        bard = Bard(token=token, timeout=30)
        res = bard.get_answer(PROMPT)['content']
        return res,None
    except Exception as e:
        return None,e
