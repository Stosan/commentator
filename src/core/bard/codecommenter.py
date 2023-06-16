from fastapi import HTTPException
from src.utils.languagechecker import detect_programming_language
from src.utils.removesentence import remove_first_paragraph, remove_last_paragraph
from src.core.bard.bard import RunBard


def make_code_comments(userData: dict):
    code_commented_map = {}
    lang_type = detect_programming_language(userData["code_body"])

    if userData["language"] == lang_type.lower():
        code_commented, err = RunBard(lang_type, userData["code_body"])
        if err is not None:
            code_commented_map["result"] = err
        else:
            fs = remove_first_paragraph(code_commented,lang_type.lower())
            ls = remove_last_paragraph(fs)
            code_commented_map["result"] = ls
    else:
        code_commented_map["result"] = "Unknown language."

    return code_commented_map
