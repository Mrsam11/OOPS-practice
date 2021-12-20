def merge_random(lst1,lst2):
    lst = lst1 + lst2
    lst = sorted(lst)
    return lst
    import random
    for i in range(len(lst)-1, 0, -1):
     
    # Pick a random index from 0 to i
        j = random.randint(0, i + 1)
   
    # Swap arr[i] with the element at random index
        lst[i], lst[j] = lst[j], lst[i]
        return lst

a = [1,2,3,4,5,6,7,8,9]
b = [11,12,13,14,15,6,9]
c = merge_random(a,b)
print(c)
# import random
# print(random.choices(c,k=10))
# 
# za = [1,2,3,4,5,6,7,8,9]
# z = random.sample(za, len(za))
# print(z)