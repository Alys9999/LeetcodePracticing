class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = dict()
        for j in range(len(numbers)):
            d[numbers[j]] = j
        for i in range(len(numbers)):
            if (target - numbers[i]) in d.keys():
                return [i+1, d[target-numbers[i]]+1]