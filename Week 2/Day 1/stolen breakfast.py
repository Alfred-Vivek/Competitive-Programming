def find_unique_delivery_id(ids):
    uniq = {}
    for i in ids:
        if i in uniq:
            uniq[i]+=1
        else:
            uniq[i]=1
    for i in uniq.keys():
        if uniq[i]==1:
            return i
    return 0

# Test Cases

actual = find_unique_delivery_id([1])
expected = 1
print(actual == expected)

actual = find_unique_delivery_id([1, 2, 2])
expected = 1
print(actual == expected)

actual = find_unique_delivery_id([3, 3, 2, 2, 1])
expected = 1
print(actual == expected)

actual = find_unique_delivery_id([3, 2, 1, 2, 3])
expected = 1
print(actual == expected)

actual = find_unique_delivery_id([2, 5, 4, 8, 6, 3, 1, 4, 2, 3, 6, 5, 1])
expected = 8
print(actual == expected)