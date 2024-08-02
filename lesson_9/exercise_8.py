import csv
import json
import os


def convert_json_csv(file_name: str) -> str:
    """Function reads json_data and conversion to csv"""
    csv_file = file_name.replace(".json", ".csv")
    try:
        json_data = open_json_files(file_name, "r")
    except FileNotFoundError as er:
        return f"File not found: {er}"
    with open(csv_file, "w", encoding="utf-8") as w_file:
        writer = csv.DictWriter(w_file, fieldnames=json_data[0].keys())
        writer.writeheader()
        writer.writerows(json_data)
        return "Conversion complete"


def open_json_files(file_name: str, mode: str, data=None) -> list:
    """Gets the file name, if mode="r" reads file and returns a list of dictionaries
    if mode="w" opens file and writes new data
    """
    if mode == "r":
        with open(os.path.join("json_files", file_name), mode) as json_file:
            json_data = json.load(json_file)
            return json_data
    elif mode == "w":
        with open(os.path.join("json_files", file_name), mode) as json_file:
            json.dump(data, json_file, indent=4)


def add_employee(file_name: str):
    data = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": True if car == "yes" else False,
        "languages": languages,
    }
    json_data = open_json_files(file_name, "r")
    json_data.append(data)
    open_json_files(file_name, "w", json_data)


try:
    name = input("Enter employee name: ")
    birthday = input("Enter employee birthday: ")
    height = int(input("Enter employee height: "))
    weight = int(input("Enter employee weight: "))
    car = input("Enter 'yes' or 'no'. The employee has a car?: ")
    languages = input("List programming languages. For example: Python,C,C++: ").split(
        ","
    )
    add_employee("employees.json")
    print(convert_json_csv("employees.json"))
except (TypeError, ValueError) as err:
    print("Incorrect data: ", err)
