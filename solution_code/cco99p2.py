#cco99p2 finding the most common words

import sys

from typing import List

from collections import Counter


def gettinput():

    datasets = int(sys.stdin.readline().strip('\n'))

    words = []
    
    indexes = []
    
    for r in range(datasets):
    
        word_list = []
    
        reader = sys.stdin.readline().strip('\n')

        indexes.append(int(reader.split(' ')[1]))
        
        n = int(reader.split(' ')[0])
        
        for x in range(n):
        
            word_list.append(sys.stdin.readline().strip('\n'))
        
        words.append(word_list)

    return words, indexes
def with_suffix(num):
    """
    num is an integer >= 1.
    Return a string of num with its suffix added; e.g. '5th'.
    """
    s = str(num)
    
    if s[-1] == '1' and s[-2:] != '11':
    
        return s + 'st'
    
    elif s[-1] == '2' and s[-2:] != '12':
    
        return s + 'nd'
    
    elif s[-1] == '3' and s[-2:] != '13':
    
        return s + 'rd'
    
    else:
    
        return s + 'th'

def common_words(words: List[str], ind: int) -> int:

    common = Counter(words).most_common()

    strs = [pairs[0] for pairs in common]

    freq = [pairs[1] for pairs in common]
    #print(freq)
    
    l = len(common)

    ord_key = {1: '1st', 2 : '2nd', 3: '3rd'}

    if ind > l - 1:

        word = ''

        print(f"{with_suffix(ind)} most common word(s):")

        print(word)

    else:
        ref_freq = freq[ind - 1]

        get_words = [pairs for pairs in common if pairs[1] == ref_freq]

        word = [x[0] for x in get_words]

        print(f"{with_suffix(ind)} most common word(s):")
    
        for w in word:
            print(w) 

def main():

    temp = gettinput()

    word_lists = temp[0]

    ind_locs = temp[1]

    for words, ind in zip(word_lists, ind_locs):

        common_words(words, ind)
    
        print('\n')
if __name__ == "__main__":main()

