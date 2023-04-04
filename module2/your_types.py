""" module2/your_types.py

Get the type of each value and print it along with the value.

"""
print("yourTypes.py\n")

data_dict = {
    "firstName": "Chad",
    "lastname": "Fernandez",
    "age": 20,
    "address": "San Jose, Antique",
    "zipCode": 5700,
    "contactNumber": 639123456789,
    "sex": "Male",
    "course": "BSCS",
    "year": 1,
    "school": "University of Antique",
}


def print_type(data):
    """
    Gets the type of the data and returns a human readable string.
    """
    if isinstance(data, str):
        return "string"
    if isinstance(data, int):
        return "integer"
    if isinstance(data, float):
        return "float"
    if isinstance(data, bool):
        return "boolean"
    if isinstance(data, type(None)):
        return "none"
    return "unknown"


for key, value in data_dict.items():
    print(f"{key}: {value} ({print_type(value)})")
