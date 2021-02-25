
# start code block2021 start
def one():
    print("one function")
    
def two():
    print("two function")
    
def test():
    one()
    two()
    print("hello world!")

if __name__ == "__main__":
    test()
        
# end code block2021    

#code block is for run your code automatically when run this file with command: python index.py








# List Reversing
MyList = ['Banana', 'Grape', 'Orange']
MyList.reverse()

print(MyList)


# List values assigned varriable dynamically
NumbersList = [1, 3, 5, 7 ,9]
x, y, z, a , b = NumbersList
print(x, y ,z)
print(a,b)


# Summation and loop in a line
t = sum(item for item in range(10))
print(t)

#Print string N times
str = "Hello"
print (str *3)



#Join many iterator object list 
Year = (2001, 2003, 2004)
Month = ('Oct', 'Nov', 'Dec')
Day = (10, 11, 12)
print allInOne = (zip(Year, Month, Day))
print(allInOne)





