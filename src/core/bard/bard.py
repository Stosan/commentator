from bardapi import Bard

key="WggnOxa5VgqEAWlvXLDDaod0Eq4MUPnEqUCwhqhIze6AR5GbxndNTmL_QUJvJPCnlWbadA."
PROMPT="Add inline comprehensive commenting to this go code and do nothing else:"
def RunBard(langtype: str, query: str):
    try:
        token = key
        bard = Bard(token=token, timeout=30)
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
        res = bard.get_answer(f"{code}")['content']
        return res,None
    except Exception as e:
        return None,e
