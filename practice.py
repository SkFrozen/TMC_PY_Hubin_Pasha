from datetime import datetime as dt

person = {"name": "TE", "age": 25}
time = dt.now()
print(dt.ctime(time))
print(f"Birthday {person['name']:*^{10 if len(person["name"]) % 2 == 0 else 11}}: {time:%m.%d.%Y %H:%M}")
print('abc'.split())
