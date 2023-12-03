# Implementing the multiplication of the dynamic array of elements 
# Refer to problem 1 in Coderbyte_visualising_dynamic_array.dio"
from typing import List, Dict
import logging

logging.basicConfig(format='%(message)s -%(asctime)s',
                    filemode='w', filename='dynamic.log',
                    datefmt='%M-%d', level=logging.INFO)

# def array_multiplier(numlist: List[int]) -> List[int]:
#     """Brute force Solution"""
#     # Create a result array to hold the result
#     result = []
#     # loop over ind,num of numlist 
#     for ind, ele in enumerate(numlist):
#         # create temp variable to hold product
#         pdt = 1
#         # For each ind, loop over rest of elements
#         for loc, num in enumerate(numlist):
#             # only if loc != ind
#             if loc != ind:
#             # multiply them and store result in product
#                 pdt *= num
#         # append product to result
#         result.append(pdt)
#     # return result
#     return result

# The above solution is O(n^2) as its nested loops

def array_multiplier(numlist: List[int]) -> List[int]:
    """Greedy Algorithm"""
    # Create a main result array
    result = [1] * len(numlist)

    # create empty result_before array
    result_before = [1] * len(numlist)
    pdt_so_far = 1

    # loop over the given list: 
    for ind, num in enumerate(numlist):
    # 	assign the product of element multiplied so far to result_before list, at "ind" index 
        result_before[ind] = pdt_so_far  # result_before = 1, 5, 40, 240 
    #   Multiply the current element to pdt_so_far
        pdt_so_far *= num  # pdt_so_far = 5 | 40 | 240 | 360 < last 360 wont enter into result_before  

    # create empty result_after array
    result_after = [1] * len(numlist)
    pdt_after = 1

    # loop over the given list in reverse:
    for i in range(len(numlist), 0, -1):
    # 	assign the product of element multiplied so far to result_after list, at "i" index
        result_after[i - 1] = pdt_after  # result_after =  432, 54, 9, 1 
    # 	calculate product
        pdt_after *= numlist[i - 1]  # num_list = 9 | 54 | 432 | 2160

    print("before: ", result_before)
    print("after: ", result_after)

    # loop over the range of array elements
    for i in range(len(numlist)):
    # 	multiply the before, after product place the it in result[i]
        result[i] = result_before[i] * result_after[i]
    # return result
    return result
    

# print(array_multiplier([5, 8, 6, 9]))  # [432, 270, 360, 240]
# print(array_multiplier([1, 2, 3, 4]))  # [24, 12, 8, 6]
# print(array_multiplier([1, 2, 3, 4, 6, 8, 7, 21, 32, 87, 97, 66, 57, 23, 42, 79]))  # [13129064682645897216, 6564532341322948608, 4376354894215299072, 3282266170661474304, 2188177447107649536, 1641133085330737152, 1875580668949413888, 625193556316471296, 410283271332684288, 150908789455699968, 135351182295318528, 198925222464331776, 230334468116594688, 570828899245473792, 312596778158235648, 166190692185391104]

# Reverse words in a sentence, in-place without creating new lists

message1 = [
    'e', 'l', 's', 'e', ' ',
    'o', 'r', ' ',
    'm', 'o', 'n', 'e', 'y', ' ',
    'y', 'o', 'u', 'r', ' ',
    'a', 'l', 'l', ' ',
    'u', 's', ' ',
    'g', 'i', 'v', 'e'
]

message2 = [
    'o', 'u', 't', 's', 'i', 'd', 'e', ' ',
    'p', 'l', 'a', 'y', 'i', 'n', 'g', ' ',
    'l', 'o', 'v', 'e', 's', ' ',
    'd', 'o', 'g', ' ',
    't', 'h', 'e'
]


def reverseCharacters(message):
    return list(reversed(message))
    # The above solution violates the constraint of 
    # reversing the list in the same place


def reverseArray(msg_list, leftIdx, rightIdx):
    # as long as leftIdx is less than rightIdx 
    while leftIdx < rightIdx:
        # assign char on leftIdx to tempChar
        tempChar = msg_list[leftIdx]
        # swap the char on rightIdx to the leftIdx location
        msg_list[leftIdx] = msg_list[rightIdx]
        # assign the tempChar to rightIdx location
        msg_list[rightIdx] = tempChar
        # increase the leftIdx by 1
        leftIdx += 1
        # reduce the rightIndex by 1
        rightIdx -= 1
    # nothing is required to be returned, as the array is modified in memory


def reversewords(sentence):
    """Reverse all the characters of the given data
    Find word boundaries and re-reverse the chars of the words"""
    # reverse the sentence character wise
    reverseArray(sentence, 0, len(sentence) - 1)
    # find the word boundaries and re-reverse the words
    logging.info(f'reversed sentence: {sentence}')
    # assign 0 to startIdx variable
    startIdx = 0
    # enumerate the characters of the sentence
    for ind, elm in enumerate(sentence):
        # check if the elm is ' ' or ind is len(sentence) - 1
        if elm == ' ' or ind == len(sentence):
            # reverse the part of the sentence from startIdx, till the ind
            reverseArray(sentence, startIdx, ind - 1)
            # move the startIdx to next word
            startIdx = ind + 1


def reversewords01(sentence):
    """Reverse all the characters of the given data
    Find word boundaries and re-reverse the chars of the words"""
    # reverse the sentence character wise
    reverseArray(sentence, 0, len(sentence) - 1)
    # find the word boundaries and re-reverse the words
    logging.info(f'reversed sentence: {sentence}')
    # assign 0 to startIdx variable
    startIdx = 0
    # enumerate the characters of the sentence
    for ind in range(len(sentence)):
        # check if the elm is ' ' 
        if sentence[ind] == ' ':
            # reverse the part of the sentence from startIdx, till the ind
            reverseArray(sentence, startIdx, ind - 1)
            # move the startIdx to next word
            logging.info(f'partly reversed {sentence}')
            startIdx = ind + 1
        # check if ind has reached end of sentences
        if ind == len(sentence) - 1:
            # reverse the part of the sentence till end
            reverseArray(sentence, startIdx, ind)
            # bug out
            logging.info(f'After last part {sentence}')


# reversewords(message2)
# reverseArray(message1, 0, len(message1) - 1)
# reversewords(message1)
# logging.info(message1)
# reversewords01(message2)
# logging.info(message2)

def compareMeets(meet1: Dict[str, int], meet2: Dict[str, int]) -> List[Dict[str, int]]:
    """compares two meetings and returns either a merged meeting, or list of two
       meetings"""
    # if meet2 start time is greater than meet 1 end time
    if meet2['startTime'] > meet1['endTime']:
        # there is a gap between two meeting, so return both meetings
        return [meet1, meet2]
    # if meet2 start time is lower than meet1 end time
    elif meet2['startTime'] <= meet1['endTime']:
        # we can use meet1 start time, and take the highest endTime
        end_time = meet1['entTime'] if meet1['endTime'] > meet2['endTime'] else meet2['endTime']
        return [{'startTime': meet1['startTime'],
                 'endTime': end_time}]

# finding the free time for playing minecraft, where everyone is free from meetings
def merged_slot(meeting_list: List[Dict[str, int]]) -> List[Dict[str, int]]:
    """takes a list of dictionary of meeting start and end times
    return list dictionary of merged meetings"""
    # sort the meeting_list based on the start_time
    sorted_meetings = sorted(meeting_list, key=lambda x: x['startTime'])
    logging.info(f"sorted meetings : {sorted_meetings}")
    # declare empty merged_list
    merge_list = []
    # push the first meeting into the merge_list
    merge_list.append(sorted_meetings[0])
    idx = 1
    while True:
        chek = compareMeets(merge_list[-1],
                            sorted_meetings[idx])
        if len(chek) == 1:
            merge_list[-1] = chek[0]

        else:
            merge_list.append(chek[-1])

        idx += 1
        if idx > len(sorted_meetings) - 1:
            break
    return merge_list


meetings = [
    {'startTime': 0, 'endTime': 1},
    {'startTime': 3, 'endTime': 5},
    {'startTime': 4, 'endTime': 8},
    {'startTime': 9, 'endTime': 10},
    {'startTime': 10, 'endTime': 12},
    ]


# logging.info(compareMeets(meetings[0],
#                          meetings[1]))

# logging.info(compareMeets(meetings[3],
#                          meetings[4]))

mergedSlot = merged_slot(meetings)

logging.info(mergedSlot)  # [{'startTime': 0, 'endTime': 1}, {'startTime': 3, 'endTime': 8}, {'startTime': 9, 'endTime':12}]
