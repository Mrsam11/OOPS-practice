# Write a program that create a buffet-style restaurant offers only
# five basic foods. Think of five simple foods, and store them in a
# tuple. Hint:Use a for loop to print each food the restaurant offers.
# Also the restaurant changes its menu, replacing two of the
# items with different foods and display the menu again.
foods = ['Biryani','Burger','Pizza','Fries','stakes']
tuple1 = tuple(foods)
print("Order from the Given Menu")
for food in tuple1:
    print (food)
print()
foods.remove('Biryani')
foods.remove('stakes')
foods.append('Chowmin')
foods.append("Chinese Rice")
tuple2 = tuple(foods)
print("Please Order From the change menu")
for menu in tuple2:
    print(menu)