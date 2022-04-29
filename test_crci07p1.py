#Testing script for the Platforme

from crci07p1 import get_platforms



def case1():
    plats = 3

    data =  [[1, 5, 10], [3, 1, 5], [5, 3, 7]]

    find_pillars(data)

def case2():
    plats = 5

    data =  [[50, 50, 90], [40, 40, 80], [30, 30, 70], [20, 20, 60], [10, 10, 50]]

    print(find_pillars(data))

def main():
    
    print(reversing('TCGGGCG'))

if __name__ == "__main__": main()


"""based on the pillar coordinates, the pillar location can be FOUND
We knw he platform location and their heights. Need to provide the conditions 
to find the heights of the pillars"""