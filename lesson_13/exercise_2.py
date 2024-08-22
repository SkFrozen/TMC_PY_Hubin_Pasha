from time import sleep


def endless_sequence(n):
    counter = 0
    while True:
        if counter >= n:
            counter = 0
        counter += 1
        yield counter


for el in endless_sequence(3):
    print(el)
    sleep(0.25)
