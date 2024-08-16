# Removes the code under the function signature, leaving
# everything above the function signature and after the
# function declaration

text_data = """
# Pattern: Prefix Sum
# Introduction: Prefix Sum involves preprocessing an array to create a new array where each element at index i
# represents the sum of the array from the start up to i. This allows for efficient sum queries on subarrays.

# Sample Problem: Given an array nums, answer multiple queries about the sum of elements within a specific range [i, j].
# Input: nums = [1, 2, 3, 4, 5, 6], i = 1, j = 3
# Output: 9

# intuition 1: creating a new "sums" array that holds incrementing sums
# intuition 2: sum of nums between indices is diff of those indices in sums array
# intuition 3: get the sum of each element by referring to earlier elem in SumArray and
# current num_array

# Example Implementation:
def prefix_sum(nums, i, j):
    P = [0] * len(nums)
    # store the sums upto that idx
    P[0] = nums[0]
    for k in range(1, len(nums)):
        P[k] = P[k - 1] + nums[k]
    print(P)
    return P[j] - P[i - 1]


nums = [1, 2, 3, 4, 5, 6]
i = 1
j = 3

print(prefix_sum(nums, i, j))

# LeetCode Problems:
# - Range Sum Query - Immutable (LeetCode #303)
# - Contiguous Array (LeetCode #525)
# - Subarray Sum Equals K (LeetCode #560)
"""

import re


def code_extracter(intext: str):
    """Remove all the lines that are having one or more tabs"""

    # reg_pattern = r"(?<=def\s+\w+\(.*\):)([\s\S]*?)(?=\ndef|$)"
    # reg_pattern = r"(def\s+\w+\(.*\):)([\s\S]*?)(?=\n(?:def\s|\Z))"
    # above regex looks for another function def to stop collecting

    reg_pattern = r"(def\s+\w+\(.*\):)(\n(    .+|\n)*)"
    # above pattern simply looks for def keyword, followed by tab indented lines

    reg_find = re.findall(pattern=reg_pattern, string=intext)
    print(reg_find)


def code_remover(intext: str):
    """Remove all the lines that are having one or more tabs"""

    reg_pattern = r"(def\s+\w+\(.*\):)(\n(    .+|\n)*)"
    # it removes the function definition also...

    after_sub = re.sub(pattern=reg_pattern, repl="", string=intext)
    return after_sub


# Modify the function bodies (here, you can choose to manipulate them as needed)
def modify_body(match):
    func_def = match.group(1)  # This is the 'def' line
    func_body = match.group(2)  # This is the body of the function
    # Example modification: add a new line at the end of the function body
    modified_body = func_body + "    print('End of function body')\n"
    return func_def + modified_body


def code_remover_withdef(intext: str):
    # Regex pattern to capture the function body but leave the 'def' line intact
    pattern = r"(def\s+\w+\(.*\):)(\n(?:\s{4}.+\n?)*)"

    # Apply the modification
    modified_code = re.sub(pattern, modify_body, intext)
    return modified_code


# code_extracter(intext=text_data)

# print(code_remover(intext=text_data))

print(code_remover_withdef(intext=text_data))
