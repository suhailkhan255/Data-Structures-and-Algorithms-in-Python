'''
time Complexity = O(n) 
'''



def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i]==x:
            return True
    return False

print(linearSearch([1,3,5,7], 6))