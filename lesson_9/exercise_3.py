import os


def read_text(file_name: str) -> list:
    """Function reads .txt file and creates a dictionary
    the key is word and the value is number of repeat
    returns list of dictionaries
    """
    common_list = []
    with open(os.path.join("txt_files", file_name), "r") as text_file:
        file_lines = text_file.readlines()
        for line in file_lines:
            list_line = line.strip(",.").split()
            common_words = {item: list_line.count(item) for item in list_line}
            common_list.append(common_words)
    return common_list


def find_common_word(words: list):
    """Function gets list of dictionaries, finds max value in each
    and writes the result to common_words.txt
    """
    text_for_file = ""
    for word in words:
        common_word = max(word, key=lambda k: word.get(k))
        count = word[common_word]
        text_for_file += f"{common_word}: {count}\n"
    with open(os.path.join("txt_files", "common_words.txt"), "w") as text_file:
        text_file.write(text_for_file)


find_common_word(read_text("text.txt"))
