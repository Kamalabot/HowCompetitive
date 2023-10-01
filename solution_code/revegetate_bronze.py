#USACO 2019 February Contest, Bronze Problem 2. The Great Revegetation

""" We will assign the seeds to the pastures in such a 
way that each cows showing interest in pasture will get 
different grass"""
from typing import List

#Trying the cow pasture problem
with open("revegetate.in",'r') as f:
    reader = f.readlines()

N, K = reader[0].strip('\n').split(' ')
(N, K) = (int(N), int(K))

def get_favorites(reader: str) -> List:
    #Create two list for each pastures
    favorites = []
    for pastures in reader[1:]:
        lst = []
        #print(int(pastures.strip('\n').split(' ')[0]))
        lst.append(int(pastures.strip('\n').split(' ')[0]))

        #print(int(pastures.strip('\n').split(' ')[1]))
        lst.append(int(pastures.strip('\n').split(' ')[1]))
        favorites.append(lst)
    return favorites

favorites = get_favorites(reader)

def cows_with_favorite(favorites, pasture):
    """
    favorites is a list of favorite pastures, as returned by read_cows.
    pasture is a pasture number.
    Return list of cows that care about pasture.
    """
    cows = []
    for i in range(len(favorites)):
    
        if favorites[i][0] == pasture or favorites[i][1] == pasture:
    
            cows.append(i)
    
    return cows

def types_used(favorites, cows, pasture_types):
    """
    favorites is a list of favorite pastures, as returned by read_cows.
    cows is a list of cows.
    pasture_types is a list of grass types.
    Return a list of the grass types already used by cows.
    """
    used = []
    for cow in cows:
        pasture_a = favorites[cow][0]
        pasture_b = favorites[cow][1]
        if pasture_a < len(pasture_types):
            used.append(pasture_types[pasture_a])
        if pasture_b < len(pasture_types):
            used.append(pasture_types[pasture_b])
    return used

def smallest_available(used):
    """
    used is a list of used grass types.
    Return the smallest-numbered grass type that is not in used.
    """
    grass_type = 1
    while grass_type in used:
        grass_type = grass_type + 1
    return grass_type

pasture_types = [0]

for i in range(1, N + 1):
    cows = cows_with_favorite(favorites, i)
    eliminated = types_used(favorites, cows, pasture_types)
    pasture_type = smallest_available(eliminated)
    pasture_types.append(pasture_type)

pasture_types.pop(0)
stringing_pastures = [str(x) for x in pasture_types]

pasture_types = ''.join(stringing_pastures)
print(pasture_types)
with open('revegetate.out', 'w') as f:
    f.write(pasture_types) 