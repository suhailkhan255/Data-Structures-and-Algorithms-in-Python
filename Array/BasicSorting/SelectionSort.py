'''
1. select min index at 0
2. find the new min index by iterating entire array 
3. swap the values
4. now 1st item is sorted
5. now increment the initial min index by 1
5. repeat the same process 

'''

def selection_sort(arr):
    n = len(arr)-1

    for i in range(n):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i],arr[min_index] = arr[min_index], arr[i]

        # temp = arr[i]
        # arr[i] = arr[min_index]
        # arr[min_index] = temp
    return arr

print(selection_sort([2,1,6,4,3]))