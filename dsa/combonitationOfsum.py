l1 = [2, 3, 4, 5,8, 7, 6, 10, 20, 5, -10, -5, 15]
given = 10

def seq(arr, giv):
    l2 = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == giv:
                l2.append((arr[i], arr[j]))
    return l2


print(seq(l1, given))
