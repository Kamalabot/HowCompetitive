#Cow Gymnastics 2019 Bronze

import sys

def get_scores():
    """Used for getting the input from the stdin. Not used in the code below. 
    Used the file read and write method"""
    
    data = sys.stdin.readline().strip('\n').split(' ')

    events = int(data[0])

    rankings = int(data[1])

    rank_data = []

    for i in range(events):

        t = sys.stdin.readline().strip('\n').split(' ')

        temp = []

        for x in t:

            temp.append(int(x))

        rank_data.append(temp)

    return rank_data


def consistency(ranks):
    """Searches the ranks of the participants in each events by reviwing their index in the events. 
    In all the events the if one participant is performing better than any other participant, then the participants pairs 
    are selected."""
    
    cows = range(1, len(ranks[0]) + 1)

    consit = []

    for cow in cows:

        temp = []
        
        for events in ranks:

            temp.append(events.index(cow) + 1)

        consit.append(temp)
    #Consit matrix contains position of each cow in multiple events.    
    #print(consit)

    participant = []

    #Starting the exhaustive search on the consit matrix to find any cow has consistently outperformed another cow
    for loci, i in enumerate(consit):

        for locj, j in enumerate(consit):
            
            flag = 'pair' # Flag is used to check for consistent outperformance. We assume all cows are consistent outperformers
            
            if locj != loci:

                #print(locj, loci)

                for position in range(len(consit[0])):
                    
                    #print(position)

                    if i[position] > j[position]:

                        flag = 'unpair' #Here we find that not all cows are consistent outperformers and correct ourself.

                        #print(flag)
                
                if flag == 'pair':

                    participant.append((loci, locj)) #Pair only those cows that are consistent and with respect which participant

    #print(participant)

    return len(participant)

def main():

    with open('gymnastics.in') as gim:

        reader = gim.readlines()

    rank_data = []

    events = int(reader[0].strip('\n').split(' ')[0])

    for i in reader[1:]:

        t = i.strip('\n').split(' ')

        temp = []

        for x in t:

            temp.append(int(x))

        rank_data.append(temp)

    #print(rank_data)

    pairs = consistency(rank_data)

    with open('gymnastics.out', 'w') as go:

        go.write(str(pairs))

if __name__ == "__main__": main()


    

