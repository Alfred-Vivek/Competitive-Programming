def reconstructQueue(lst):       
    dic = {} 
    h = []
    res = []    
    for i in range(len(lst)):
        p = lst[i]
        if p[0] in dic:
            dic[p[0]] += (p[1], i),
        else:
            dic[p[0]] = [(p[1], i)]
            h += p[0],       
    h.sort()        
    for i in h[::-1]:
        dic[i].sort()
        for p in dic[i]:
            res.insert(p[0], lst[p[1]])
    return res

print(reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
print(reconstructQueue([[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]]))
print(reconstructQueue([ [2,4], [5,1], [3,3], [1,5], [4,2], [6,0]]))