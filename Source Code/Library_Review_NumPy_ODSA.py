#Numpy Documentation:  https://docs.python.org/3/library/
#Tutorials:  https://www.tutorialspoint.com/numpy/,  https://docs.scipy.org/doc/numpy/user/quickstart.html
#Library Purpose: Numerical Python (NumPy) is the fundamental package for scientific computing with Python
#Includes: powerful N-dimensional array object,  useful linear algebra, Fourier transform, and random number capabilities
#Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. 
#Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.

import numpy as np
#random num gen classes
from numpy.random import rand
#Linear algebra classes
from numpy.linalg import solve, inv

def data_struct():
    print("Array creation - does not exist in python base libraries")
    x = np.array([1, 2, 3])
    print(x)  #prints array([1, 2, 3])
    y = np.arange(10)  # like Python's range, but returns an array
    print(y) #prints array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    print("Basic Numpy operations")
    a = np.array([1, 2, 3, 6])
    b = np.linspace(0, 2, 4)  # create an array with four equally spaced points starting with 0 and ending with 2.
    print(b)  #Prints 
    c = a - b #Array/set Difference
    print(c) # rints array([ 1.        ,  1.33333333,  1.66666667,  4.        ])
    a**2 #All elements ^2
    print(a) #prints array([1 2 3 6])

    print("Universal numpy functions")
    a = np.linspace(-np.pi, np.pi, 100)  
    b = np.sin(a) #sine function
    c = np.cos(a) #cosine function

    a = np.array([[1, 2, 3], [3, 4, 6.7], [5, 9.0, 5]])
    print("Transpose array - from linalg class")
    a.transpose()  
    '''array([[ 1. ,  3. ,  5. ],
       [ 2. ,  4. ,  9. ],
       [ 3. ,  6.7,  5. ]]) '''
    inv(a)
    ''' array([[-2.27683616,  0.96045198,  0.07909605],
       [ 1.04519774, -0.56497175,  0.1299435 ],
       [ 0.39548023,  0.05649718, -0.11299435]]) '''
    b =  np.array([3, 2, 1])
    print("solve the equation ax = b")
    solve(a, b) 
    #prints results - x = array([-4.83050847,  2.13559322,  1.18644068])
    c = rand(3, 3) * 20  # create a 3x3 random matrix of values within [0,1] scaled by 20
    print(c)
    ''' ex. array([[  3.98732789,   2.47702609,   4.71167924],
       [  9.24410671,   5.5240412 ,  10.6468792 ],
       [ 10.38136661,   8.44968437,  15.17639591]]) '''
    print("matrix multiplication")
    np.dot(a, c)  
    ''' ex. array([[  53.61964114,   38.8741616 ,   71.53462537],
       [ 118.4935668 ,   86.14012835,  158.40440712],
       [ 155.04043289,  104.3499231 ,  195.26228855]]) '''
    a @ c # Starting with Python 3.5 and NumPy 1.10
    ''' ex. array([[  53.61964114,   38.8741616 ,   71.53462537],
       [ 118.4935668 ,   86.14012835,  158.40440712],
       [ 155.04043289,  104.3499231 ,  195.26228855]]) '''

def data_types():
    print("find data type of variable")
    dt = np.dtype(np.int32) 
    print dt  #prints int32

    # ndarray object 
    dt = np.dtype([('age',np.int8)]) 
    a = np.array([(10,),(20,),(30,)], dtype = dt) 
    print a  #prints [(10,) (20,) (30,)]
    print a['age'] #prints [(10 20 30]

    #ndarray example - mixed types
    student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
    a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
    print a  #prints [('abc', 21, 50.0), ('xyz', 18, 75.0)]

data_struct()  
data_types()  