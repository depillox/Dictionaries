#demo01.py
def demo01(someDictionary):
#    If someDictionary is zero length OR null None
#    Print a message but do NOT print the contents
#    Otherwise print the contents
#    Check before you do anything else: is someDictionary 
#    REALLY a dictionary
    if isinstance(someDictionary,dict):
        print("This is a dictionary")
    if someDictionary == None or len(someDictionary) == 0:
        print("The dictionary is empty or null")
    else:
        print(someDictionary)
    