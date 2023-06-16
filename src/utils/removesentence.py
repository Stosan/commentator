def remove_first_paragraph(sentence, language):
    paragraphs = sentence.split('\n\n')  # Split the sentence into paragraphs
    if len(paragraphs) > 1:
        updated_sentence = '\n\n'.join(paragraphs[1:])  # Remove the first paragraph

        # Find the index of the first occurrence of the language code block
        code_block_start = updated_sentence.find(f"```{language}")

        if code_block_start != -1:
            # Find the index of the next newline character after the code block start
            next_newline = updated_sentence.find("\n", code_block_start)

            # Remove the first line containing the language code block
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

