
def sum(*MyData):
    sum = 0

    for data in MyData:
        sum += data    

    return sum

def average(*MyData):
    sum = 0
    i   = 0
    
    for data in MyData:
         sum += data
         i   += 1
    
    average = sum/i
    return average
 
def maks(*MyData):
    #maks = 0
    maks = -(float("inf"))

    for data in MyData:
        if (data > maks):
            maks = data

    return maks
        
def min(*MyData):
    #min = 99999999
    min = float("inf")

    for data in MyData:
        if (data < min):
            min = data

    return min