def bubble(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


data = [14, 13, 12, 25, 11, 13]
print(bubble(data))
