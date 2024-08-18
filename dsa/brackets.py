def brackets(data):
    d1 = {')': '(', '}': '{', ']': '['}
    stack = []
    for br in data:
        if br in ['(', '[', '{']:
            stack.append(br)
        elif br in d1:
            if not stack:
                return False
            cr = stack.pop()
            if d1[br] != cr:
                return False
    if stack:
        return False
    return True


print(brackets('()[]'))
