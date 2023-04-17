import json
import math
def average_expenses(file_path: str) -> float:
    """
    get average expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: average expenses
    """
    nol=0
    a=open("data.json","r").read()
    import json
    a_json=json.loads(a)
    for k,q in a_json.items():
        if q>0:
            nol+=q
    
    t=nol//len(a_json)
        
    

    
    
    return t
print(average_expenses("salom"))

# # test
# file_path = "data.json"
# average = average_expenses(file_path)
# print(average)



# import json
# sonlar=[12, 45, 23, 67]
# sonlar_json=json.dumps(sonlar)



# bemor={
#     "ism":"Alijon Valiyev",
#     "yosh":30,
#     "oila":True,
#     "farzandlari":("Ali","Vali"),
#     "alergiya":None,
#     "dorilar":[
#     {
#     "nomi":"Analgin","miqdori":0.5
#     },
#     {
#     "nomi":"Panadol","miqdori":1.5
#     }
#     ]
# }
# # bemor_json=json.dumps(bemor, indent=4)
# # print(bemor_json)
# # with open("bemor.json","w") as f:
# #     json.dump(bemor,f)
# # print(bemor)
# # with open ("sonlar.json","w") as t:
# #     json.dump(sonlar,t)
# a=open("data.json","r").read()
# print(a)