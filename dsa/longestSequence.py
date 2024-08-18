def seq(arr):
    r = setind = sart = 0
    s1 = set()
    for i in range(len(arr)):
        while arr[i] in s1:
            s1.remove(arr[setind])
            setind += 1
        s1.add(arr[i])

        if i - setind + 1 > r:
            r = i - setind + 1
            sart = setind
    ls = ''.join(arr[sart:sart+r])
    print(ls)
    return r

data = 'abcdefagbwea'
print(seq(data))
