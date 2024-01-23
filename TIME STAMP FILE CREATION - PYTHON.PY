'''
1. Creating text file with content as current time stamp in it
'''
#importing datatime library
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
#Function that takes file name
def readfi(filename):
#open it in read mode
    r=open(filename,'r')
#print its content
    return r.read()
if __name__='__main__':
filename="/Users/ruthiraj/Documents/PYTHON WORKSPACE/file1.txt"
#Calling its function
print(readfi(filename))

