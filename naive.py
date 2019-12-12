def naive(str, substr):
    if len(str) < len(substr):
        return -1
    for i in range(len(str)):
        is_same = True
        for j in range(len(substr)):
            if str[i + j] != substr[j]:
                is_same = False
                break
        if is_same == True:
            return i
    return -1
