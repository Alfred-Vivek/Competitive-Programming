def countRotations(allwords,low,high):
    if (high < low):
        return 0 
    if (high == low):
        return low 
    mid = low + (high - low)/2; 
    mid = int(mid) 
    if (mid < high and allwords[mid+1] < allwords[mid]):
        return (mid+1)
    if (mid > low and allwords[mid] < allwords[mid - 1]):
        return mid
    if (allwords[high] > allwords[mid]):
        return countRotations(allwords, low, mid-1);
    return countRotations(allwords, mid+1, high)
def find_rotation_point(allwords):
    return countRotations(allwords,0,len(allwords)-1)

# Test Cases

actual = find_rotation_point(['cape', 'cake'])
expected = 1
print(actual == expected)

actual = find_rotation_point(['grape', 'orange', 'plum', 'radish', 'apple'])
expected = 4
print(actual == expected)

actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist', 'asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage'])
expected = 5
print(actual == expected)