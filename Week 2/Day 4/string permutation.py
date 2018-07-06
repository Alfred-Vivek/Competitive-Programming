def get_permutations(string):
    lst = []
    rec(string,"",lst)
    return set(lst)
def rec(t, f, lst):
    if len(t)==0:
        lst.append(f)
        return
    for k in range(len(t)):
        rec(t[0:k]+t[k+1:],f+t[k],lst)

# Test Cases

actual = get_permutations('')
expected = set([''])
print(actual == expected)

actual = get_permutations('a')
expected = set(['a'])
print(actual == expected)

actual = get_permutations('ab')
expected = set(['ab', 'ba'])
print(actual == expected)

actual = get_permutations('abc')
expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
print(actual == expected)