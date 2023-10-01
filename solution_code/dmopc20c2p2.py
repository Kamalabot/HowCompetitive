#the longest scarf dmopc20c2p2

import sys

from typing import List

def get_relatives() -> List[int]:

    plats = sys.stdin.readline().strip('\n').split(' ')

    scarf = int(plats[0])

    relatives = int(plats[1])

    scrafinguration = sys.stdin.readline().strip('\n').split(' ')

    raw_scarf = []

    for x in scrafinguration:

        raw_scarf.append(int(x))

    request_len = []

    for p in range(relatives):

        tmp = []

        forme = sys.stdin.readline().strip('\n').split(' ')

        for x in forme:

            tmp.append(int(x))

        request_len.append(tmp)

    return request_len, raw_scarf

def find_index(color_list: List[int], color: int, location: int):

    if location == 1:

        ind = 0

        idx = 0

        while True:

            if color_list[ind] == color and ind > idx:

                idx = ind

            ind = ind + 1

            if ind > len(color_list) - 1:

                break

        return idx

    else:

        return color_list.index(color)


def scarf_colors(raw_scarf, start_color, end_color):

    # print(raw_scarf, requested_len)

    scarf_idex_start = find_index(raw_scarf, start_color, 0)

    #print(f"scarf_idex_start {scarf_idex_start}")

    scarf_idex_end = find_index(raw_scarf, end_color, 1)

    #print(f"scarf_idex_start {scarf_idex_end}")

    total_length = scarf_idex_end - scarf_idex_start + 1
    
    #print(f"total_length {total_length}")
    
    return total_length

def colors_dict(raw_scarf):

    temp = set(raw_scarf) # removing the duplicates to only find the colors.
    temp = list(temp)

    color_dict = {}

    for color in temp: #get left most and right most of each color

        left_most = find_index(raw_scarf, color, 1)

        right_most = find_index(raw_scarf, color, 0)

        color_dict[color] = [left_most, right_most]

    return color_dict

def scarf_with_dictionary(color_dictionary, start_col, end_col):

    start_idex = color_dictionary[start_col][0]

    end_idex = color_dictionary[end_col][1]

    return end_idex - start_idex + 1

def main():

    request_by_realtives, raw_scarf = get_relatives()

    gift_scarf_length = []

    dictionary_of_colors = colors_dict(raw_scarf)

    #print(request_by_realtives)

    for relative in request_by_realtives:
    
        gift_scarf_length.append(scarf_with_dictionary(dictionary_of_colors, relative[0], relative[1]))

    print(max(gift_scarf_length))

if __name__ == "__main__": main()