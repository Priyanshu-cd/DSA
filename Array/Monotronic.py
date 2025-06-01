'''
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array is monotone increasing if all its elements from left to right are non-decreasing.
An array is monotone decreasing if all  its elements from left to right are non-increasing.
Given an integer array return true if the given array is monotonic, or false otherwise.
'''

def chkMonotone(a):
    count = len(a)
    smaller = False
    greater = False
    for i in range(count-1):
            if a[i]>a[i+1]:
                if smaller == True:
                    return False
                else:
                    greater = True
            elif a[i] < a[i+1]:
                if greater == True:
                    return False
                else:
                    smaller = True  
    # if greater:
    #     print("Monotronic Increasing...")     
    # elif smaller:
    #     print("Monotronic Decreasing...")
    # else:
    #     print("Either Empty, Same or Single element Array...")
    return True

def chkMonotone2(a):
    n = len(a)
    if n==0: return True
    first=a[0]
    last = a[n-1]

    if first>last:
        for i in range(n-1):
            if a[i] < a[i+1]:return False
    elif first == last:
        for i in range(n-1):
            if a[i] != a[i+1]:return False
    else:
        for i in range(n-1):
            if a[i] > a[i+1]:return False
    return True


a=[-4,-1,3,4,2,7]
b=[7,6,4,3,-1,-4]
c=[2,2,2,2,2]
d=[9]
e=[]
print(a,chkMonotone(a))
print(b,chkMonotone(c))
print(d,chkMonotone(d))
print(e,chkMonotone2(e))

# print(a,chkMonotone2(a))
# print(b,chkMonotone2(c))
# print(d,chkMonotone2(d))
# print(e,chkMonotone2(e))



