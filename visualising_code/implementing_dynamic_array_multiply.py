# Implementing the multiplication of the dynamic array of elements 
# Refer to problem 1 in Coderbyte_visualising_dynamic_array.dio"
from typing import List


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
    

print(array_multiplier([5, 8, 6, 9]))  # [432, 270, 360, 240]
# print(array_multiplier([1, 2, 3, 4]))  # [24, 12, 8, 6]
print(array_multiplier([1, 2, 3, 4, 6, 8, 7, 21, 32, 87, 97, 66, 57, 23, 42, 79]))  # [13129064682645897216, 6564532341322948608, 4376354894215299072, 3282266170661474304, 2188177447107649536, 1641133085330737152, 1875580668949413888, 625193556316471296, 410283271332684288, 150908789455699968, 135351182295318528, 198925222464331776, 230334468116594688, 570828899245473792, 312596778158235648, 166190692185391104]
