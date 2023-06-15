def remove_first_paragraph(sentence):
    paragraphs = sentence.split('\n\n')  # Split the sentence into paragraphs
    if len(paragraphs) > 1:
        updated_sentence = '\n\n'.join(paragraphs[1:])  # Remove the first paragraph
        return updated_sentence
    else:
        return sentence

def remove_last_paragraph(sentence):
    paragraphs = sentence.split('\n\n')  # Split the sentence into paragraphs
    if len(paragraphs) > 1:
        updated_sentence = '\n\n'.join(paragraphs[:-1])  # Remove the last paragraph
        return updated_sentence
    else:
        return sentence

