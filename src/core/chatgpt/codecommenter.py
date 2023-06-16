from utils import detect_programming_language

def make_code_comments(userData: dict):
    code_commented_map = {}

    if userData.Language == "golang":
        lang_type = detect_programming_language(userData.CodeBody)
        if lang_type == "Go":
            code_commented, err = gpt3(lang_type, userData.CodeBody)
            if err is not None:
                raise HTTPException(status_code=400, detail=err.Error())
            code_commented_map["result"] = code_commented
    elif userData.Language == "python":
        lang_type = utils.detect_programming_language(userData.CodeBody)
        if lang_type == "Python":
            code_commented, err = gpt3(lang_type, userData.CodeBody)
            if err is not None:
                raise HTTPException(status_code=400, detail=err.Error())
            code_commented_map["result"] = code_commented
    elif userData.Language == "javascript":
        lang_type = utils.detect_programming_language(userData.CodeBody)
        if lang_type == "JavaScript":
            code_commented, err = gpt3(lang_type, userData.CodeBody)
            if err is not None:
                raise HTTPException(status_code=400, detail=err.Error())
            code_commented_map["result"] = code_commented
    else:
        print("Unknown language.")

    return code_commented_map