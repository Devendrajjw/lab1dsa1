def binarySearch(arr, target):
    arr.sort()
    left, right = 0, len(arr) + 1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

arr = [3, 2, 1, 12, 5, 9]
target = 2

print(binarySearch(arr, target))
