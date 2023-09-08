import json

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    f = open(file_path, mode='r+').read()
    data = json.loads(f)
    expensive = []
    name = []
    for i in data:
        expensive.append(data[i])
        name.append(i)
    least_most = name[expensive.index(max(expensive))]
    return least_most

# test
file_path = "data.json"
most_expensive_item = most_expensive(file_path)
print(most_expensive_item)