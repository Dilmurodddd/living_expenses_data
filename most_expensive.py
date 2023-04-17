import json

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    a=open("data.json","r").read()
    b=json.loads(a)
    for v in b.values():
        aa=v
    for i in b.values():
        if i>aa:
            aa=i
    return aa

# test
file_path = "data.json"
most_expensive_item = most_expensive(file_path)
print(most_expensive_item)