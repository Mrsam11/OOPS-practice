l1 = input("Enter list of numbers: ")
l2 = l1.split()
l3 = []
for i in l2:
    l3.append(int(i))
print(l3)
inp = int(input('''Enter number to select comprehensions: \n ==> 1 for list
comprehensions \n ==> 2 for set comprehensions \n ==> 3 for dictionary'''))
if inp == 1:
    print(list(i for i in l3))
elif inp == 2:
    print(set(i for i in l3))
elif inp == 3:
    dict2 = {i:f"item {i}" for i in l3}
    print(dict2)
    dict1 = {value:key for key,value in dict2.items()}
    print(dict1)