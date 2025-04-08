# Left Rotation of array with no. of positions
def rotation(arr, d, n):
    for i in range(0,d):
        last = arr[0]
        for i in range(n-1):
            arr[i] = arr[i + 1]
        arr[n-1] = last


def printArray(arr,n):
    for j in range(n):
        print(arr[j],end=" ")


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
d = 3
rotation(arr, d, n)
printArray(arr,n)