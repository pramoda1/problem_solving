'''
The problem is when give the arrar or list the output is in reverse order
example
A=[1,2,3,4,5,6,7]
output
A=[7,6,5,4,3,2,1]
using swap methed 
@ and another methed is using temp list or array this is not sufficient becouse this take extra memory

'''
def reverArray(arr):
    right=len(arr)-1
    left=0
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left=+1
        right=-1
    return

if __name__== "__main__":
    arr=[1,2,3,4,5,6,7]
    print("the arrray")
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print("\n")
    reverArray(arr)
    print("the Reverse array")
    for i in range(len(arr)):
        print(arr[i],end=" ")


    