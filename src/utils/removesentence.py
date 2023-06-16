def remove_first_go_paragraph(sentence):
    paragraphs = sentence.split('\n\n')  # Split the sentence into paragraphs
    if len(paragraphs) > 1:
        updated_sentence = '\n\n'.join(paragraphs[1:])  # Remove the first paragraph
        # Find the index of the first occurrence of "```go"
        first_occurrence = updated_sentence.find("```go")

        # Find the index of the next newline character after the first occurrence
        next_newline = updated_sentence.find("\n", first_occurrence)

        # Remove the first line containing "```go"
        updated_sentence = updated_sentence[next_newline + 1:]
        return updated_sentence
    else:
        return sentence
    
def remove_first_py_paragraph(sentence):
    paragraphs = sentence.split('\n\n')  # Split the sentence into paragraphs
    if len(paragraphs) > 1:
        updated_sentence = '\n\n'.join(paragraphs[1:])  # Remove the first paragraph
        # Find the index of the first occurrence of "```go"
        first_occurrence = updated_sentence.find("```python")

        # Find the index of the next newline character after the first occurrence
        next_newline = updated_sentence.find("\n", first_occurrence)

        # Remove the first line containing "```go"
        updated_sentence = updated_sentence[next_newline + 1:]
        return updated_sentence
    else:
        return sentence
    
    
def remove_first_js_paragraph(sentence):
    paragraphs = sentence.split('\n\n')  # Split the sentence into paragraphs
    if len(paragraphs) > 1:
        updated_sentence = '\n\n'.join(paragraphs[1:])  # Remove the first paragraph
        # Find the index of the first occurrence of "```javascript"
        first_occurrence = updated_sentence.find("```javascript")

        # Find the index of the next newline character after the first occurrence
        next_newline = updated_sentence.find("\n", first_occurrence)

        # Remove the first line containing "```javascript"
        updated_sentence = updated_sentence[next_newline + 1:]
        return updated_sentence
    else:
        return sentence
    

def remove_last_paragraph(sentence):
    paragraphs = sentence.split('\n\n')  # Split the sentence into paragraphs
    if len(paragraphs) > 1:
        updated_sentence = '\n\n'.join(paragraphs[:-1])  # Remove the last paragraph
        # Find the last occurrence of "```"
        last_occurrence = updated_sentence.rfind("```")

        # Remove all words after the last occurrence of "```"
        code_cleanup = updated_sentence[:last_occurrence]
        return code_cleanup
    else:
        return sentence

