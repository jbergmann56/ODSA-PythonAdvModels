#Pandas Docs: http://pandas.pydata.org/pandas-docs/stable/
#Tutorials:  10-Minute Video - http://pandas.pydata.org/pandas-docs/stable/10min.html#min
#            Examples/docs - http://pandas.pydata.org/pandas-docs/stable/text.html
#Cheat Sheet:  http://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
#
#Library Purpose: high-performance, easy-to-use data structures and data analysis tools 
#includes: includes file/io conversion to python objects, data cleaning/merging/selection
#tabular/matrix/datafram data structures, time series analysis functions, text data
#
#Additional Exercises:  https://github.com/guipsamora/pandas_exercise

#Note - Using matplot & numpy libraries with pandas examples!
import matplotlib.pylab as plt  #see graph options at: https://matplotlib.org/gallery/index.html
import numpy as np
import pandas as pd

def file_read_csv(path):
    print("Pandas File I/O Example - CSV Read")
    #load csv file into Pandas dataframe object
    data=pd.read_csv(path)
    return data

def file_write_csv(data, path):
    print("Pandas File I/O Example - CSV Write")
    #write Pandas dataframe object to local csv file
    data.to_csv(path)

def file_read_excel(data,path,sheet):
    print("Pandas File I/O Example - Read")
    #load csv file into Pandas dataframe object
    xlsx = pd.ExcelFile(path)
    data = pd.read_excel(xlsx, sheet)
    return data


def data_struct():
    #Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.)
    #Here, data can be many different things: Python Dict, ndarray (numpy), scalar value
    print("Series Example")
    data = {'b' : 1, 'a' : 0, 'c' : 2} #python dict
    s = pd.Series(data)
    print(s) 

    #2-dimensional labeled data structure with columns of potentially different types
    # DataFrame accepts many different kinds of input:  ndarray, dicts, series, another dataframe
    print("DataFrame Example")
    data = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
            'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])} #python dict
    s = pd.DataFrame(data)
    print(s) 
    print("Manipulate DataFrame Example")
    s = pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])
    print(s)  


def data_text():
    s = pd.Series(['A', '3B', 'C', 'Aaba', 'Baca', 3, 'dog', 'cat'])
    print("lowercase series")
    print(s.str.lower())

    print("Length of text elements in series")
    print(s.str.len())

    print("Pattern Matching - Number then Capital Letter")
    pattern = r'[0-9][A-Z]'
    print(s.str.contains(pattern))

#example methods to experiment on :)
#data_struct()     
#data_text()

#import text commentary from CSV file
data = file_read_csv(r"C:\\Python\\Data\\Text_Mining_Sample_CSV.csv") 
#view first 5 rows of dataframe
pd.set_option('display.max_columns', 80) 
#data munging - http://wavedatalab.github.io/datawithpython/munge.html
print(data.head())
print("Number of rows in rows, columns in dataset: {}".format(data.shape))
print("Column names in dataset: {}".format(data.columns))
#use pandas/numpy/matplotlib for visualization
print('Matplotlib object')
bar_graph = data.groupby("Comment Type").size().plot(kind='barh')
plt.show()  #show histogram of comment type categories
#write new csv file
file_write_csv(data, r"C:\\Python\\Data\\Text_Mining_Sample_CSV2.csv") 

#import Dow joens historical data from excel file, then visualize stock market data
data2 = file_read_excel(data, r"C:\\Python\\Data\\indicator_stock_hist.xls",'^DJI') 
print(data2.head())
#aggregate/select data from dataset:  http://wavedatalab.github.io/datawithpython/aggregate.html
data3 = data2[['Date', 'Close']]
print(data3.head())
#return records with year >= 2007
data4 = data3[(data3['Date'] > '2007-01-01' )]
#create time series line chart that plots Dow Jones closing values
y = data4['Close']
x = pd.to_datetime(data4['Date'])   #iterate list to transfor dates for graphical use
data5 = pd.DataFrame({'Close':y, 'Date':x}).set_index(x) 
data5.plot(kind='line')
plt.show()
#Time series functions:  http://wavedatalab.github.io/datawithpython/timeseries.html