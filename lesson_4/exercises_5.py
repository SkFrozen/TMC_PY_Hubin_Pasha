# from math import factorial

"""
Exercise 1
"""
# x = int(input("Enter x: "))
# n = int(input("Enter n: "))

# sin = ((n * (n + 1) / 2) * pow(-1, n)) * (pow(x, (2 * n + 1)) / factorial(2 * n + 1))
# print(f"Sin(x) = {sin}")

# cos = ((n * (n + 1) / 2) * pow(-1, n)) * (pow(x, 2 * n) / factorial(2 * n))
# print(f"Cos(x) = {cos}")


"""
Exercise 2
"""
# n = 20
# k = 2
# count = 0
# salary = 0
# days_untill_n = 0

# while salary < 20:
#     if count < 6:
#         count += 1
#         salary += k
#     else:
#         count = 0
#         salary -= 2
#     days_untill_n += 1

# print(days_untill_n)

"""
Exercise 3
"""
# fib1 = fib2 = 1
# n = int(input("Enter number of fib: "))

# print(fib1, fib2, end=" ")

# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=" ")

"""
Exercise 4
"""
# list_of_numbers = [1, 3, 10, 12, 3, 5, 6, 6, 50, -23, -23]
# sum_of_nums = 0
# max_num = list_of_numbers[0]
# min_num = list_of_numbers[0]


# for num in list_of_numbers:
#     sum_of_nums += num
#     if min_num > num:
#         min_num = num
#     elif max_num < num:
#         max_num = num

# print(f"\nSum_of_nums = {sum_of_nums} \nMin_num = {min_num} \nMax_num = {max_num}")


# for i in set(list_of_numbers):
#     count = list_of_numbers.count(i)
#     if count > 1:
#         print(f"Num: {i} : count: {count}")

"""
Exercise 5
"""
# n = int(input("Enter a number from 1 to 7: "))
# sorted_list = [num for num in range(1, 8)]

# low = 0
# high = len(sorted_list) - 1
# mid = len(sorted_list) // 2

# while sorted_list[mid] != n and low <= high:
#     if n > sorted_list[mid]:
#         low = mid + 1
#     else:
#         high = mid - 1
#     mid = (low + high) // 2

# print(f"Position: {mid}")

"""
Exercise 6
"""
# arr = [5, 6, 7, 1, 2, 3, 4]
# start = 0
# end = len(arr) - 1
# mid_2 = len(arr) // 2

# while arr[mid_2] != n and start <= end:
#     if arr[start] <= arr[mid_2]:
#         if arr[start] <= n < arr[mid_2]:
#             end = mid_2 - 1
#         else:
#             start = mid_2 + 1
#     else:
#         if arr[mid_2] < n <= arr[end]:
#             start = mid_2 + 1
#         else:
#             end = mid_2 - 1
#     mid_2 = (start + end) // 2

# print(f"Position_2: {mid_2}")


# figure = input("Enter: rectangle, triangle or circle: ")

# if figure == "rectangle":
#     a = int(input("Enter first side of rectangle: "))
#     b = int(input("Enter second side of rectanle: "))
#     print(f"Square of rectangle = {a * b}")
# elif figure == "triangle":
#     a = int(input("Enter first side of triangle: "))
#     b = int(input("Enter second side of triangle: "))
#     c = int(input("Enter third side of triangle: "))
#     p = (a + b + c) / 2
#     print(f"Square of triangle = {(p * (p - a) * (p - b) * (p - c)) ** 0.5}")
# elif figure == "circle":
#     pi = 3.14
#     a = int(input("Enter radius of circle: "))
#     print(f"Square of circle = {pi * a * 2}")
# else:
#     print("Incorrect data")
