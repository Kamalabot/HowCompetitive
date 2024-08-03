# ecoo12r1p2 DNA Sequencing

import sys

from typing import List

def get_dna()->str:

    strands = []

    for i in range(3):

        strands.append(sys.stdin.readline())

    return strands

promoter = "TATAAT"

def reversing(entry_strand):

    """The strands are reversed with their complementary bases"""
    #print(entry_strand)

    opponents = {'A':'T', 'C':'G', 'T': 'A', 'G': 'C'}

    temp = list(entry_strand)

    #print(temp)

    temp = temp[::-1]

    for ind, char in enumerate(temp):

        if char == 'A':

            temp[ind] = opponents['A']

        if char == 'C':

            temp[ind] = opponents['C']

        if char == 'G':

            temp[ind] = opponents['G']
        
        if char == 'T':

            temp[ind] = opponents['T']
    
    return ''.join(temp)

def revers_rna(entry_strand):

    """The strands are reversed with their complementary bases
    this time Thymine is replaced by Uracil"""
    #print(entry_strand)

    opponents = {'A':'T', 'C':'G', 'T': 'U', 'G': 'C'}

    temp = list(entry_strand)

    #print(temp)

    for ind, char in enumerate(temp):

        if char == 'A':

            temp[ind] = opponents['A']

        if char == 'C':

            temp[ind] = opponents['C']

        if char == 'G':

            temp[ind] = opponents['G']
        
        if char == 'T':

            temp[ind] = opponents['T']
    
    return ''.join(temp)

def rna_todna(entry_strand):
    print(entry_strand)
    """The strands are reversed with their complementary bases
    this time Thymine is replaced by Uracil"""
    #print(entry_strand)

    opponents = {'A':'T', 'G':'C', 'U': 'A', 'C': 'G'}

    temp = list(entry_strand)

    #print(temp)

    for ind, char in enumerate(temp):

        if char == 'U':

            temp[ind] = opponents['U']

        if char == 'C':

            temp[ind] = opponents['C']

        if char == 'G':

            temp[ind] = opponents['G']
        
        if char == 'T':

            temp[ind] = opponents['T']

        if char == 'A':

            temp[ind] = opponents['A']
    
    return ''.join(temp)


def search_revers(sub_string: str)-> str:

    """The substring that matches the reverse base on reversing function"""
    return 'good'

def find_RnA():

    pass

def main():

    reversing('TATTCC')

if __name__ == "__main__": main()
