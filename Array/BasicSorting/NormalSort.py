arr = [1,5,3,6,7,2]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j], arr[i]

print(arr)

            