'''
Time Complexity = O(n2)

bubble the larget to the end by swapping adjecent elements
repeat the process untill the array is sorted

'''

def bubble_sort(arr):
    n = len(arr)- 1
    for i in  range(n, 0, -1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1], arr[j]
    return arr
sortedList = bubble_sort([2,1,6,4,3])
print(sortedList)

