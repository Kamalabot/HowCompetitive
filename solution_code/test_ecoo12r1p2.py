#Testing script for the Wesley's ANGER
from ecoo12r1p2 import reversing, find_RnA, revers_rna, rna_todna



def case1():
    strand = 'AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC' 

    find_RnA(strand)

def case2():
    strand = 'AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC' 

    find_RnA(strand)

def case3():

    strand = 'AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC' 

    find_RnA(strand)

def main():
    #case1()
    #case2()
    #case3()
    #print(reversing('TTTACCCG'))
    print('ATCGCGACGAAATATCGGGCGGGATCCATACCGACCCAGCCGCCCGA')
    print('\n')
    print(rna_todna('UAGCGCUGCUUUAU'))

    print(len('UAGCGCUGCUUUAU'))
    print('\n')
    print(reversing('TCGGGCG'))
if __name__ == "__main__": main()