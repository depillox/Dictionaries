#demo.py
def demo(): #Define Function
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)
#    Add another key/value pair to the dictionary
    myDictionary["Indiana"] = "Hoosiers"
    print(myDictionary)
#    Remove Xavier from the dictionary
    myDictionary.pop("Xavier")
    print(myDictionary)
#    Add error handling so this(line 13) does not crash
    try: 
        print(myDictionary["Purdue"])
    except: 
        #Where the code ends up if an exception was thrown
        pass #eating the exception
#    Iterate over the dictionary 
#    Print key:value in each iteration
    for key in myDictionary.keys():
        print(key + ":" + myDictionary[key])
#    Convert the dictionary to a list called myList
#    Hmm... a dictionary has keys and values
#    What are we putting in the list?
#    List Comprehension!
    myList = [key for key in myDictionary.keys()]
    print(myList)
#    Create a new dictionary with key/value swapped
#    call it myNewDictionary
#    Still using List Comprehension
    myNewDictionary = {v:k for k,v in myDictionary.items()}
    print(myNewDictionary)
