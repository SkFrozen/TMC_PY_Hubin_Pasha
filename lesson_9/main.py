# import os
# import re
# import csv
# import json
# from my_lib import files_sort as fs, prohibited_words as pw


# dir_content = os.listdir()
# print(fs.files_sort_json(dir_content))
# print(fs.files_sort_txt(dir_content))

# text = """Подсудимая Эверт-Колокольцева Елизавета Александровна в судебном заседании """


# def replace_name(text: str) -> str:
#     return text.split()[0] + " N " + " ".join(text.split()[4:])


# print(replace_name(text))


# print(pw.filter_prohibited_words("censore_text.txt"))


# def find_bad_students(file_name: str) -> str:
#     """Function gets file name and creates 3 list:
#     names, surnames, grades. Prints students
#     whose grade is less than 3
#     """
#     with open(os.path.join("txt_files", file_name), "r") as text_file:
#         names = text_file.readline().split()
#         surnames = text_file.readline().split()
#         grades = text_file.readline().split()
#     bad_grades = []
#     for item in grades[1:]:
#         if item < "3":
#             bad_grades.append(grades.index(item))
#     for student in range(len(bad_grades)):
#         print(
#             surnames[bad_grades[student]].strip(","),
#             names[bad_grades[student]].strip(","),
#             ": ",
#             grades[bad_grades[student]],
#         )


# find_bad_students("students_data.txt")


# def find_sum_numbers(file_name: str) -> int:
#     content = pw.reads_content(file_name, "txt_files")
#     regx = r"\d+"
#     return sum(map(int, re.findall(regx, content)))


# print(find_sum_numbers("numbers.txt"))


# def caesar_cipher(file_name: str) -> str:
#     content = pw.reads_content(file_name, "txt_files")
#     amount_line = 1
#     encrypt_text = ""
#     for letter in content:
#         if letter == "\n":
#             amount_line += 1
#         if letter.isalpha():
#             if letter.isupper():
#                 encrypt_text += chr(((ord(letter) - 65) + amount_line) % 26 + 65)
#             else:
#                 encrypt_text += chr(((ord(letter) - 97) + amount_line) % 26 + 97)
#         else:
#             encrypt_text += letter
#     print(encrypt_text)


# caesar_cipher("requirements.txt")
