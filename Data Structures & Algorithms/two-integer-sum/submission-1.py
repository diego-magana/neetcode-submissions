'''
For each number n, you need its partner target - n. Scanning the whole array for that partner every time would be slow (O(n**2)). First, build a dict that answers where the numner is in O(1). 
Then, create a hash map to store the value and index of each element in the array. 
Iterate through the array and compute the complement of the current element. 
Check if the complement exists in the hash map. 
If no such pair is found, return an empty array.

The insertion and lookup time of a hashmap is O(1):
Time complexity: O(n)
Space complexity: O(n)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary: number -> its index in nums
        numMap = {}
        # enumerate to store index and value
        
        # Pass 1: record where every number is.
        # enumerate(nums) gives you the index and the value on each
        # loop: nums: [2, 7, 11] -> (0, 2), (1, 7), (2, 11)
        for i, n in enumerate(nums):
            numMap[n] = i

        # Pass 2: for each number, look up its partner.
        for i, n in enumerate(nums):
            diff = target - n   # partner n needs 
            
            # Partner must exist (diff in numMap) 
            # and be a different element
            if diff in numMap and numMap[diff] != i:
                # return the answer
                return [i, numMap[diff]]

        # no pair found, return empty list
        return []