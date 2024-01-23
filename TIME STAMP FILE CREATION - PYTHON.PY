'''
1. Creating text file with content as current time stamp in it
'''
#improting datatime library
import datetime
#creating text file inside my documents and file name as file1 in appending mode
f=open("/Users/ruthiraj/Documents/file2.txt",'a')
#writing current time stamp as its content
f.write ("2nd time printing current time stamp:" +'\t')
#using datetime function to fetch current time
f.write(datetime.datetime.now().ctime())
print (datetime.datetime.now()," ")

'''
2. Python function to read a text file, that function will take name of the file and display its content
'''
def readfi(filename):
    r=open(filename,'r')
    print(r)

readfi(filename="/Users/ruthiraj/Documents/PYTHON WORKSPACE/file1.txt")

