from typing import List
# intu1 : base case is len <= 1
# intu2 : enumerate the list
# intu3 : leave the curr element, and call recursively on rest
# intu4 : append curr element along with permuted list


def permute(in_list: List[int]) -> List[List[int]]:
    result = []
    # base case
    if len(in_list) <= 1:
        return [in_list]

    for idx, x in enumerate(in_list):
        # leave the current element
        rest = in_list[:idx] + in_list[idx + 1 :]
        # call permute recursively on the rest
        for p in permute(rest):
            # append the current element back to result
            result.append([x] + p)
    return result


your_list = [1, 2, 3]
print(permute(your_list))
