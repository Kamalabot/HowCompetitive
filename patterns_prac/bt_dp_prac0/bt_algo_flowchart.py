# [ Start ]
#     ↓
# [ Is Current List Full? ] → No → [ Choose a Number ]
#      ↓                           ↓
#    Yes → [ Output Permutation ] ← [ Add Number to Current List ]
#                                     ↓
#                                  [ Recursive Call ]
#                                     ↓
#                               [ Backtrack (Remove Last Number) ]
#                                     ↓
#                                [ Repeat from 'Is Current List Full?']
#                                     ↓
#                                 [ End ]


def backtrack_permutations(nums, current_permutation, results):
    if len(current_permutation) == len(nums):
        results.append(current_permutation.copy())
        return

    for num in nums:
        if num in current_permutation:
            continue
        current_permutation.append(num)
        backtrack_permutations(nums, current_permutation, results)
        current_permutation.pop()  # Backtrack


nums = [1, 2, 3]
results = []
backtrack_permutations(nums, [], results)
print(results)
