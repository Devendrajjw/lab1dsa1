d = {
    'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
    'V': 5, 'IV': 4, 'I': 1
}

n = 14
op = []
for k, v in d.items():
    while n > 0:
        if v <= n:
            op.append(k)
            n -= v
        else:
            break
print(''.join(op))
