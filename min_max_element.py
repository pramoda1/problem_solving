'''

in this problem to find the minimum and maximum element in array
using these methods 
---setmin()
---setmax()

'''

def set_min(A):
    min = float('inf')
    for i in A:
        if min > i:
            min = i
    return min

def set_max(A):
    max = float('-inf')
    for i in A:
        if max < i:
            max = i
    return max

if __name__ == "__main__":
    A=[1,2,3,4,5,6,7,8,9]
    print("the minimum element in the array",set_min(A))
    print("the maximum element in the array",set_max(A))