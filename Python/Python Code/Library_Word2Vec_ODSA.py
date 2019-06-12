#Python Standard Library Docs:  https://docs.python.org/3/library/
#Library Purpose: Read/In Large Datasets in multiple formats (csv, excel, database, etc), 
#Improved Datatypes (dataframe),  Time Series & Sampling Functions,  
#Cleaning/Transforming/Merge & Impute Missing Data for modeling 
import pandas #serializing (converting data structures to strings) and file I/O


def file_io(mylist = ["This", "is", 4, 13327], mystr = "This is a sample string"):
    # Open the file C:\\binary.dat for writing. The letter r before the
    # filename string is used to prevent backslash escaping.
    # write object to file
    myfile = open(r"C:\\Python\\binary.dat", "wb")  #wb - "Write Binary"
    pickle.dump(mylist, myfile)
    myfile.close()
    
     # Open the file for reading.
    myfile = open(r"C:\\Python\\binary.dat", "rb") #rb - "Read Binary"
    loadedlist = pickle.load(myfile)
    myfile.close()
    print(loadedlist)
    #Output: ['This', 'is', 4, 13327]

    #write text to file 
    myfile = open(r"C:\\Python\\text.txt", "w") #w - "Write "
    myfile.write(mystr)
    myfile.close()

    myfile = open(r"C:\\Python\\text.txt")
    print(myfile.read())
    #Output: 'This is a sample string'
    myfile.close()

file_io([1,2,3,'joe dirt'],'JB2')  