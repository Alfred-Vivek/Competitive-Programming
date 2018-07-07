import random
def get_random(low,high):
    return random.randint(low,high)
def shuffle(lst):
    n = len(lst)
    for i in range(0,n-1):
        j = get_random(i,n-1)
        lst[i],lst[j] = lst[j],lst[i]
sample_list = [1, 2, 3, 4, 5]
print ('Original List:', sample_list)
shuffle(sample_list)
print ('Shuffled List:', sample_list)