# Write a pogram that make a dictionary called favorite_places.
# Think of three names to use as keys in the dictionary, and store
# three favorite places for each person through list. Loop through the
# dictionary, and print each person’s name and their favorite places.
# Output look alike: 
# abc likes the following places:
# - Bear Mountain
# - Death Valley
# - Tierra Del Fuego 
favorite_places = {
    'Sameer' : ['Paris','Rome','Italy'] ,
    'Saqib' : ['Turkey' , 'Disneyland', 'Switzerland'] ,
    'Amir' : ['Kashmir', 'Hunza' , 'Naran']
    }
for keys,values in favorite_places.items():
    print(f'The favorite Place of {keys} are')
    for value in values:
        print(value)
    print()