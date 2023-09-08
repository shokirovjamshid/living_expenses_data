import json

def average_expenses(file_path: str) -> float:
    """
    get average expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: average expenses
    """
    f = open(file_path, mode='r+').read()
    data = json.loads(f)
    s = 0
    sum_expenses = 0
    for i in data:
        sum_expenses+=data[i]
        s+=1
    average_sum = sum_expenses/s
    return average_sum

# test
file_path = "data.json"
average = average_expenses(file_path)
print(average)
