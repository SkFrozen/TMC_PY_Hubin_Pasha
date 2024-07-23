def comp(array1, array2):
    try:
        return sorted([i**2 for i in array1]) == sorted(array2)
    except:
        return False


set1 = {1, 2, 3, 4, 4}
print(set1)

a = 5
b = 5
print(a is b)
print(0b1010)
