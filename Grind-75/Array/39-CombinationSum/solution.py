from typing import List

candidates = [2, 3, 6, 7]
target = 7


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output_list = []  # Output has to be a list of combins
        self.cand = candidates  # get candidates
        self.cand_length = len(candidates)  # length of candidates
        self.find_all_combination(0, target, [])
        # this is a new way of init method

        return self.output_list

    def find_all_combination(self, index: int, target: int, path: List[int]):
        # recursion method
        if target < 0:  # tgt is -ve
            return  # ret None
        elif target == 0:  # tgt is 0
            self.output_list.append(path)
            # return empty list
        else:
            for i in range(index, self.cand_length):
                # enumerate range of index to list length
                self.find_all_combination(i, target-self.cand[i], path+[self.cand[i]])
                # fac(0, 7 - 2, [2])
                    # fac(1, 5 - 3, [2, 3])
                        # fac(2, 2 - 6, [2, 3, 6])  # return up
                            # fac(1, 2 - 2, [2, 2, 3])
        return
