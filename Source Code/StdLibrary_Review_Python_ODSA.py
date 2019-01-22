#Python Standard Library Docs:  https://docs.python.org/3/library/
#to install a new Github package using Sublime Text IDE
#1) Enable Command Palate
#2) Identify GitHub Repository URL - ex. "Requests" = https://github.com/requests/requests.git
#3) Goto Package Control --> Install Package --> "Requests" Should appear in options
#4) Restart IDE and use import statement as seen below
import pickle #serializing (converting data structures to strings) and file I/O

def file_io(mylist = ["This", "is", 4, 13327], mystr = "This is a sample string"):
    # Open the file C:\\binary.dat for writing. The letter r before the
    # filename string is used to prevent backslash escaping.
    print("write object to file")
    myfile = open(r"C:\\Python\\binary.dat", "wb")  #wb - "Write Binary"
    pickle.dump(mylist, myfile)
    myfile.close()
    
    print("Open the file for reading.")
    myfile = open(r"C:\\Python\\binary.dat", "rb") #rb - "Read Binary"
    loadedlist = pickle.load(myfile)
    myfile.close()
    print(loadedlist)
    #Output: ['This', 'is', 4, 13327]

    print("write text to file" )
    myfile = open(r"C:\\Python\\text.txt", "w") #w - "Write "
    myfile.write(mystr)
    myfile.close()

    print("read text from file" )
    myfile = open(r"C:\\Python\\text.txt", "r")
    print(myfile.read())
    #Output: 'This is a sample string'
    myfile.close()

#Call function with arg
file_io()  
#file_io([1,2,3,'joe dirt'],'JB2')  