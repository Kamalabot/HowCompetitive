#Distinct numerals in years ccc13s1

import sys

from typing import List

def get_year() ->str:

    year = sys.stdin.readline().strip('\n')

    return list(year)

def chk_digit(year: List[str]) ->bool:

    temp = year
    
    for i, d in enumerate(year):
        
        chker = temp.pop(i)
        
        if chker in temp:

            return False

        temp.insert(i,chker)
    
    return True
            

def find_nextYear(year: List[str])->int:

    int_year = int(''.join(year))

    while True:
        int_year = int_year + 1

        list_year = list(str(int_year))
        
        if chk_digit(list_year):            

            return int_year

            break

def main():

    input_year = get_year()

    print(find_nextYear(input_year))

if __name__ == "__main__":main()