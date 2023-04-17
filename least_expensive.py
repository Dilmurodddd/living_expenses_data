import json

def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    nol2=0
    nol=0
    a=open("data.json","r").read()
    b=json.loads(a)
    
    # for v in b.values():
    #     aaa=v
    # for t in b.values():
    #     if t<aaa:
    #         aaa=t
        
    bbb=list(b.values())
    w=bbb[0]           
    for k in bbb:
        if k<w:
            w=k 




    return w

# test
file_path = "data.json"
least_expensive_item = least_expensive(file_path)
print(least_expensive_item)
