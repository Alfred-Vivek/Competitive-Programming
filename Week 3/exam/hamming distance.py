def hammingdist(x,y):
    count = 0
    z = x^y
    while z:
        count = count + 1
        z &= z-1
    return count

print(hammingdist(25,30))
print(hammingdist(1,4))
print(hammingdist(25,30))
print(hammingdist(100,250))
print(hammingdist(1,30))
print(hammingdist(0,255))