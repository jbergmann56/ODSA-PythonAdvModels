#Reference:  https://www.w3schools.com/python/python_json.asp
#python examples: https://realpython.com/
import datetime #date functionality
import re #regular expressions - search string

#SET GLOBAL variables - Can be used throughout Python Program
txt_ex = "The rain in Spain"
search_ex = re.search("^The.*Spain$", txt_ex)
print(search_ex)
search_ex = re.search("^The.*Jeremy$", txt_ex) #returns "None"
print(search_ex)
boolean_ex = True #Boolean
int_ex = 1 #Integer
float_ex = 2.8  # float
list_ex = [int_ex, ["another", "list"], ("a", "tuple")] #Value, List & Tuple
now_ex = datetime.datetime.now()
print(now_ex)

def data_structures(): #define function 
    #List is a collection which is ordered and changeable. Allows duplicate members.
    #Note:  Python Lists replace Arrays (from most programming languages)
    print('list examples')
    mylist = ["List item 1", 2, 3.14]
    mylist[0] = "List item 1 again" # We're changing the item.
    mylist[-1] = 3.21 # Here, we refer to the last item.
    print(mylist[:])    #Prints ['List item 1', 2, 3.1400000000000001]
    print(mylist[0:2])    #Prints ['List item 1', 2]
    print(mylist[-3:-1])    #Prints ['List item 1', 2]
    print(mylist[1:])    #prints [2, 3.14]
    # Adding a third parameter, "step" will have Python step in N item increments, rather than 1.
    print(mylist[::2])    #Prints ['List item 1', 3.14]

    #Tuple is a collection which is ordered and unchangeable. Allows duplicate members. 
    print('tuple examples')
    mytuple = (1, 2, 3, 1)
    print(mytuple[0],mytuple[3])

    #Set is a collection which is unordered and unindexed. No duplicate members.
    print('set examples')
    myset = {"apple", "banana", "cherry"}
    print(myset)

    #Add multiple items to a set, using the update() method:
    myset.update(["orange", "mango", "grapes"])
    print(myset)  #prints {'apple', 'banana', 'mango', 'cherry', 'grapes', 'orange'}
    #use other set operations to manipulate set - example
    myset.discard("banana")
    print(myset)
    #Dictionary is a collection which is unordered, changeable and indexed. No duplicate members. 
    print('dictionary examples')
    mydict = {"Key 1": "Value 1", 2: 3, "pi": 3.14}
    mydict["pi"] = 3.15 # This is how you change dictionary values.
    #use set functions to manipulate set

    #get length of any type
    myfunction = len
    print('len examples')
    print(myfunction(mylist))
    print(myfunction(mytuple))
    print(myfunction(myset))
    print(myfunction(mydict))

def strings():
    strString = """This is
    a multiline
    string."""
    print(strString)
    # WARNING: Watch out for the trailing s in "%(key)s".
    print("This %(verb)s a %(noun)s." % {"noun": "test", "verb": "is"})
    #Ouptup: This is a test.
    
    #Use .format to placehold string values, similar to concatenation
    name = "Jeremy"
    "Hello, {}!".format(name)
    print(f"Hello, {name}!")
    #Output: Hello, Jeremy!
 
#run example functions
#data_structures()
#strings()