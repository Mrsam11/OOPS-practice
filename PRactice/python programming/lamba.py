#def a_first(a):
 #   return a[0]

a = [[8,2],[0,3],[4,5]]
a.sort(key=lambda x: x[0])
print(a)

b = lambda x,y : x if x>y else y
print(b(2,3))