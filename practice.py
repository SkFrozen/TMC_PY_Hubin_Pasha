# from datetime import datetime as dt

# person = {"name": "TE", "age": 25}
# time = dt.now()
# print(dt.ctime(time))
# print(f"Birthday {person['name']:*^{10 if len(person["name"]) % 2 == 0 else 11}}: {time:%m.%d.%Y %H:%M}")
# print('abc'.split())

# def bin_rec(numbers, start, end, val):
# 	mid = (start + end) // 2
# 	if numbers[mid] > val:
# 		return bin_rec(numbers, start, mid - 1, val)
# 	elif numbers[mid] < val:
# 		return bin_rec(numbers, mid + 1, end, val)
# 	else:
# 		return mid


# print(bin_rec(range(1, 11), 0, len(range(1, 11)) - 1, 7))

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

# def prime_num(n):
# 	if n <= 1:
# 		return False
# 	for i in range(2, int(n ** 0.5) + 1):
# 		if n % i == 0:
# 			return False
# 	return True

# print(prime_num(23))

# def nod(a, b):
# 	while a != b:
# 		if a > b:
# 			a = a - b
# 		else:
# 			b = b - a
# 	return a

# print(nod(18, 12))


# def caesar_code(
#     text, step=int(input("Enter step > 0 for encrypt or step < 0 for decrypt: "))
# ):
#     if step > 0:
#         return encrypt_caesar(text, step)
#     else:
#         return decrypt_caesar(text, step)


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


def matr(m, n):
    from random import randint

    a = []
    for i in range(m):
        a.append([""] * n)
    print(a)
    for i in range(m):
        for j in range(n):
            a[i][j] = randint(0, m * n)

    return a


for row in matr(5, 4):
    for elem in row:
        print(elem, end=" ")
    print()


matrix = matr(5, 4)


def find_min_max(matrix):
    min_val = matrix[0][0]
    max_val = matrix[0][0]
    for row in matrix:
        for val in row:
            if min_val > val:
                min_val = val
            if max_val < val:
                max_val = val
    return max_val, min_val


print(find_min_max(matrix))
