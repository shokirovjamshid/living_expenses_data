import json

def total_expenses(file_path: str) -> float:
    """
    get total expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: total expenses
    """
    f = open(file_path, mode='r+').read()
    data = json.loads(f)
    total_ex = 0
    for i in data:
        total_ex+=data[i]
    return total_ex


# test
file_path = "data.json"
total = total_expenses(file_path)
print(total)
