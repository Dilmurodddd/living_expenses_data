import json

def total_expenses(file_path: str) -> float:
    """
    get total expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: total expenses
    """
    # a=open("data.json","r").read()
    # b=json.loads()
    # nol=0
    # for v in b.values():
    #     if v>0:
    #         nol+=v
    # return nol





    nol=0
    a=open("data.json","r").read()
    import json
    a_json=json.loads(a)
    for k,q in a_json.items():
        if q>0:
            nol+=q
    return nol

# test
file_path = "data.json"
total = total_expenses(file_path)
print(total)
