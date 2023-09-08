import json

def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    f = open(file_path, mode='r+').read()
    data = json.loads(f)
    expensive = []
    name = []
    for i in data:
        expensive.append(data[i])
        name.append(i)
    least_expen = name[expensive.index(min(expensive))]
    return least_expen

# test
file_path = "data.json"
least_expensive_item = least_expensive(file_path)
print(least_expensive_item)
