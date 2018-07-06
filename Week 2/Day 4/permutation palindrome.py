def has_palindrome_permutation(string):
    dic = {}
    for i in string:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1    
    flag = 0
    for i in dic:
        if dic[i]%2==1:
            flag+=1
    return flag==1 or flag==0

# Test Cases

result = has_palindrome_permutation('aabcbcd')
expected = True
print(result == expected)

result = has_palindrome_permutation('aabccbdd')
expected = True
print(result == expected)

result = has_palindrome_permutation('aabcd')
expected = False
print(result == expected)

result = has_palindrome_permutation('')
expected = True
print(result == expected)

result = has_palindrome_permutation('a')
expected = True
print(result == expected)