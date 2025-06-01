'''You are given an array of Integers 
in which each subsequent value is not less than the previous value.
 Write a function that takes this array as an input 
 and returns a new array with the squares of each number sorted in ascending order.'''

def sortedArray(a):
    arr=[]
    arr.append(a[0]**2)
    for i in range(1,len(a)):

            print(f"ARR::::{arr[i-1]} < {a[i]**2}")
            temp = arr[i-1]
            square = a[i]**2
            if temp > square:
                arr[i-1]=square
                arr.append(temp)
            else:
                arr.append(square)

    # arr.sort()
    return arr

def sortedArray2(a):
    count = len(a)
    arr=[0]*count
    i,j = 0,count - 1

    for k in range(count-1,-1,-1):
        if a[i]**2 > a[j]**2:
            arr[k] = a[i]**2
            i += 1
        else:
            arr[k] = a[j]**2
            j -= 1
    return arr
               
array = [-5,-2,3,4,9]
print(array,sortedArray(array))
print(array,sortedArray2(array))
