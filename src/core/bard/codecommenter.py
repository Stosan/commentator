from fastapi import HTTPException
from src.utils.languagechecker import detect_programming_language
from src.utils.removesentence import remove_first_go_paragraph, remove_first_js_paragraph, remove_first_py_paragraph, remove_last_paragraph
from src.core.bard.bard import RunBard




def make_code_comments(userData: dict):
    code_commented_map = {}
    if userData["language"] == "go":
        lang_type = detect_programming_language(userData["code_body"])
        if lang_type == "Go":
            code_commented, err = RunBard(lang_type, userData["code_body"])
            if err is not None:
                code_commented_map["result"] = err
            fs=remove_first_go_paragraph(code_commented)
            ls=remove_last_paragraph(fs)
            code_commented_map["result"] = ls
        else:
            code_commented_map["result"]="Unknown language."
    elif userData["language"] == "python":
        lang_type = detect_programming_language(userData["code_body"])
        if lang_type == "Python":
            code_commented, err = RunBard(lang_type, userData["code_body"])
            if err is not None:
                code_commented_map["result"] = err
            fs=remove_first_py_paragraph(code_commented)
            ls=remove_last_paragraph(fs)
            code_commented_map["result"] = ls
        else:
            code_commented_map["result"]="Unknown language."
    elif userData["language"] == "javascript":
        lang_type = detect_programming_language(userData["code_body"])
        if lang_type == "JavaScript":
            code_commented, err = RunBard(lang_type, userData["code_body"])
            if err is not None:
                code_commented_map["result"] = err
            fs=remove_first_js_paragraph(code_commented)
            ls=remove_last_paragraph(fs)
            code_commented_map["result"] = ls
        else:
            code_commented_map["result"]="Unknown language."
    else:
        code_commented_map["result"]="Unknown language."

    return code_commented_map