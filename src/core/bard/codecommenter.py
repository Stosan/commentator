from fastapi import HTTPException
from src.utils.languagechecker import detect_programming_language
from src.utils.removelastsentence import remove_last_paragraph,remove_first_paragraph
from src.core.bard.bard import RunBard




def make_code_comments(userData: dict):
    code_commented_map = {}
    if userData["language"] == "golang":
        lang_type = detect_programming_language(userData["code_body"])
        if lang_type == "Go":
            code_commented, err = RunBard(lang_type, userData["code_body"])
            if err is not None:
                raise HTTPException(status_code=400, detail=err.Error())
            ls=remove_last_paragraph(code_commented)
            fs=remove_first_paragraph(ls)
            code_commented_map["result"] = fs
    elif userData["language"] == "python":
        lang_type = detect_programming_language(userData["code_body"])
        if lang_type == "Python":
            code_commented, err = RunBard(lang_type, userData["code_body"])
            if err is not None:
                raise HTTPException(status_code=400, detail=err.Error())
            code_commented_map["result"] = remove_last_paragraph(code_commented)
    elif userData["language"] == "javascript":
        lang_type = detect_programming_language(userData["code_body"])
        if lang_type == "JavaScript":
            code_commented, err = RunBard(lang_type, userData["code_body"])
            if err is not None:
                raise HTTPException(status_code=400, detail=err.Error())
            code_commented_map["result"] = remove_last_paragraph(code_commented)
    else:
        print("Unknown language.")

    return code_commented_map