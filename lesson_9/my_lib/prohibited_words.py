import os
import re


def filter_prohibited_words(file_name: str) -> str:
    """Function gets file name and passes censor_text,
    prohibited_words to censors_content
    Returns modified text"""
    censor_text = reads_content(file_name, "txt_files")
    prohibited_words = reads_content("stop_words.txt", "txt_files").split()
    return censors_content(prohibited_words, censor_text)


def reads_content(file_name: str, dir_name=".") -> str:
    """Function gets file name and return file content"""
    with open(os.path.join(dir_name, file_name), "r") as text_file:
        data = text_file.read()
    return data


def censors_content(prohibited_words: list, censor_text: str) -> str:
    """Function gets content finds prohibited words and replaces them with "*"
    Returns modified text"""
    final_sentences = []
    for word in prohibited_words:
        if censor_text.lower().find(word) != -1:
            censor_text = re.sub(word, "*" * len(word), censor_text.lower())
    for sentence in censor_text.split(". "):
        sentence = sentence.strip("\n").capitalize()
        final_sentences.append(sentence)
    return ". ".join(final_sentences)
