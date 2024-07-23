"""
Exercise 1
"""

# def bin_rec(numbers, start, end, val):
# 	mid = (start + end) // 2
# 	if numbers[mid] > val:
# 		return bin_rec(numbers, start, mid - 1, val)
# 	elif numbers[mid] < val:
# 		return bin_rec(numbers, mid + 1, end, val)
# 	else:
# 		return mid


# print(bin_rec(range(1, 11), 0, len(range(1, 11)) - 1, 7))


"""
Exercise 2
"""
# def conv_to_bin(n, b=''):
# 	while n > 0:
# 		b = str(n % 2) + b
# 		n //= 2
# 	return b
# if n > 0:
# 	b = str(n % 2) + b
# 	n //= 2
# 	return conv_to_bin(n, b)
# else:
# 	return b

# print(conv_to_bin(5))


"""
Exercise 3
"""
# def prime_num(n):
# 	if n <= 1:
# 		return False
# 	for i in range(2, int(n ** 0.5) + 1):
# 		if n % i == 0:
# 			return False
# 	return True

# print(prime_num(23))


"""
Exercise 4
"""
# def nod(a, b):
# 	while a != b:
# 		if a > b:
# 			a = a - b
# 		else:
# 			b = b - a
# 	return a

# print(nod(18, 12))


"""
Exercise 5
"""


# def caesar_code(
#     text, step=int(input("Enter step > 0 for encrypt or step < 0 for decrypt: "))
# ):
#     if step > 0:
#         return encrypt_caesar(text, step)
#     elif step < 0:
#         return decrypt_caesar(text, step)
#     else:
#         print("Enter correct value")


# def encrypt_caesar(text, step):
#     encrypted_message = ""
#     for char in text:
#         if char.isalpha():
#             step_amount = step % 26
#             if char.islower():
#                 steped = ord(char) + step_amount
#                 if steped > ord("z"):
#                     steped -= 26
#                 encrypted_message += chr(steped)
#             elif char.isupper():
#                 steped = ord(char) + step_amount
#                 if steped > ord("Z"):
#                     steped -= 26
#                 encrypted_message += chr(steped)
#         else:
#             encrypted_message += char
#     return encrypted_message


# def decrypt_caesar(encrypted_text, step):
#     return encrypt_caesar(encrypted_text, step)


# print(caesar_code("Uwnajy, pfp yatn ijqf"))


"""
Exercise 6
"""
# def vigenere_code(
#     message, keyword, choise=int(input("Enter 1 for encrypt or 0 for decrypt: "))
# ):
#     if choise == 1:
#         return encrypt_vigenere(message, keyword)
#     elif choise == 0:
#         return decrypt_vigenere(message, keyword)
#     else:
#         return "Enter correct value"


# def encrypt_vigenere(message, keyword):
#     encrypted_message = ""
#     keyword = (
#         keyword * (len(message) // len(keyword))
#         + keyword[: len(message) % len(keyword)]
#     )
#     for i in range(len(message)):
#         if message[i].isalpha():
#             shift = ord(keyword[i].lower()) - 97
#             if message[i].islower():
#                 encrypted_message += chr((ord(message[i]) - 97 + shift) % 26 + 97)
#             elif message[i].isupper():
#                 encrypted_message += chr((ord(message[i]) - 65 + shift) % 26 + 65)
#         else:
#             encrypted_message += message[i]
#     return encrypted_message


# def decrypt_vigenere(message, keyword):
#     decrypted_message = ""
#     keyword = (
#         keyword * (len(message) // len(keyword))
#         + keyword[: len(message) % len(keyword)]
#     )
#     for i in range(len(message)):
#         if message[i].isalpha():
#             shift = ord(keyword[i].lower()) - 97
#             if message[i].islower():
#                 decrypted_message += chr((ord(message[i]) - 97 - shift) % 26 + 97)
#             elif message[i].isupper():
#                 decrypted_message += chr((ord(message[i]) - 65 - shift) % 26 + 65)
#         else:
#             decrypted_message += message[i]
#     return decrypted_message


# decrypted_message = vigenere_code("Wszwdk, Lcfws!", "pool")
# print(decrypted_message)


# def print_matrix(matr):
"""
Function for matrix display
"""
#     for row in matr:
#         for elem in row:
#             print(elem, end=" ")
#         print()


"""
Exercise 7
"""


# def matr(m, n):
#     from random import randint

#     a = []
#     for i in range(m):
#         a.append([0] * n)
#     for i in range(m):
#         for j in range(n):
#             a[i][j] = randint(0, 10)
#     return a


"""
Exercise 8
"""
# matrix = matr(5, 4)

# def find_min_max(matrix):
#     min_val = matrix[0][0]
#     max_val = matrix[0][0]
#     for row in matrix:
#         for val in row:
#             if min_val > val:
#                 min_val = val
#             if max_val < val:
#                 max_val = val
#     return max_val, min_val


# print(find_min_max(matrix))

"""
Exercise 9
"""


# def matrix_sum(m, n):
#     matrix = matr(m, n)
#     matrix_sum = 0
#     column_sums = [0] * len(matrix[0])
#     for i in matrix:
#         for j, x in enumerate(i):
#             matrix_sum += x
#             column_sums[j] += x
#     column_percent = [
#         str(round((column_sum / matrix_sum) * 100, 2)) + "%"
#         for column_sum in column_sums
#     ]
#     return (
#         f"Sum elements = {matrix_sum}, propotions summs every column:"
#         + f"{', '.join(column_percent)}"
#     )


# print(matrix_sum(3, 5))


"""
Exercise 10
"""
# def matrix_multi_columns(m, n, k):
#     matrix = matr(m, n)
#     columns_multiply = []
#     for row in matrix:
#         new_row = [element * row[k - 1] for element in row]
#         columns_multiply.append(new_row)
#     return print_matrix(columns_multiply)


# matrix_multi_columns(4, 5, 3)

"""
Exercise 11
"""
# def matrix_sum_rows(m, n, l):
#     matrix = matr(m, n)
#     rows_sum = []
#     for row in matrix:
#         new_row = [element + row[l - 1] for element in row]
#         rows_sum.append(new_row)
#     return print_matrix(rows_sum)

"""
Exercise 12
"""
# matrix_sum_rows(2, 4, 3)
# def find_in_matrix(h, m=4, n=5):
#     matrix = matr(m, n)
#     match_columns = {}
#     print_matrix(matrix)
#     for c, row in enumerate(matrix):
#         has_match = False
#         for i in row:
#             if i == h:
#                 has_match = True
#                 break
#         if has_match:
#             match_columns[c + 1] = "True"
#         else:
#             match_columns[c + 1] = "False"
#     return match_columns


# print(find_in_matrix(1, 5, 5))

"""
Exercise 13
"""
# def matrix_diagonals(m, n):
#     matrix = matr(m, n)
#     n = len(matrix)
#     main_diagonal_sum = 0
#     side_diagonal_sums = 0
#     for i in range(n):
#         main_diagonal_sum += matrix[i][i]
#         side_diagonal_sums += matrix[i][n - i - 1]
#     return (
#         f"Main diagonal = {main_diagonal_sum} and side diagonal = {side_diagonal_sums}"
#     )


# print(matrix_diagonals(4, 4))

"""
Exercise 14
"""
# def next_column(m, n):
#     matrix = matr(m, n)
#     for row in matrix:
#         count = row.count(1)
#         if count % 2 == 0:
#             row.append(0)
#         else:
#             row.append(1)
#     return matrix


# print_matrix(next_column(4, 5))
