#Bovine Genomics

#reading the genese

spotty = []

plainy = []

with open('cownomics.in', 'r') as yb:

    reader = yb.readlines()

data_points = reader[0].strip('\n').split(' ')

speci = int(data_points[0])

gene_len = int(data_points[1])

for ind, gen in enumerate(reader[1:]):

    if ind < speci:

        spotty.append(gen.strip('\n'))

    else:

        plainy.append(gen.strip('\n')) 

#print(spotty, plainy)   

def surmise_position(spot_cows, plain_cows):

    spotter = []

    plainer = []

    gene_len = len(spot_cows[0])

    speci_len = len(spot_cows)

    for ind in range(gene_len):

        spot_temp = [spot[ind] for spot in spot_cows]

        plain_temp = [plan[ind] for plan in plain_cows]

        spotter.append(spot_temp)

        plainer.append(plain_temp)

    positions = 0

    loc = 0

    while loc <= gene_len - 1:

        flag = 0

        for char in range(speci_len):

            if spotter[loc][char] in plainer[loc]:

                flag = 1
        
        if flag == 0:
            
            positions = positions + 1

        loc = loc + 1

    return positions

def main():
    
    with open('cownomics.out', 'w') as cowrite:
        
        cowrite.write(str(surmise_position(spotty, plainy)))

if __name__ == "__main__": main()