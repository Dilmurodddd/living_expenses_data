import json

def get_data(file_path: str) -> dict:
    """
    get data from json file as dictionary
    
    Args:
        file_path (str): path to json file

    Returns:
        dict: dictionary of data
    """
    json_json=open("data.json","r").read()
    b=json.loads(json_json)
    return b


# test
file_path = "data.json"
data = get_data(file_path)
print(data)
