'''
Intuition:
The product of everything except nums[i] splits into two parts:
(prod of everything LEFT of i) * (prod of everything RIGHT of i)
Recomputing those for every i is O(n**2).
Rather, build them up with running products in two passes:
1 (left -> right): res[i] = prod of everything before i (prefix)
2 (right -> left): res[i] = prod of everything after i (postfix)
After both passes, res[i] = left part * right part (the answer)/

Shortcut: total product // nums[i] (not allowed) and will fail 
when nums contains a 0 (div by 0).

Time: O(n)  Space: O(1) extra (output list does not count)
Trace below: nums = [1, 2, 3, 4] -> expected [24, 12, 8, 6]
    i:   0      1      2      3
    = (none)*2*3*4, 1*3*4, 1*2*4, 1*2*3*(none)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Output list, one slot per element. 
        # Use 1, identity for multiplication. 
        res = [1] * (len(nums))
        # res = [1, 1, 1, 1]

        # 1: store the product of everything to the LEFT of each i.
        # prefix = running prod of nums[0..i-1]. Nothing left of idx 0
        # so start at 1 (empty product).
        prefix = 1
        for i in range(len(nums)):
            # ORDER IS KEY: store first, then multiply.
            # res[i] gets prefix before nums[i] is included, 
            # so nums[i] excludes itself. 
            res[i] = prefix
            prefix *= nums[i]   # extend running prod for the next i
        # i=0: res[0] = 1,  prefix = 1*1 = 1
        # i=1: res[1] = 1,  prefix = 1*2 = 2
        # i=2: res[2] = 2,  prefix = 2*3 = 6
        # i=3: res[3] = 6,  prefix = 6*4 = 24
        # res = [1, 1, 2, 6]   (each slot = prod of everything to its left)

        # 2: multiply in the prod of everything RIGHT of each i.
        # postfix = running prod of nums[i+1..n-1]
        # start at 1 b/c nothing is right of last idx
        # range(n-1, -1, -1) -> 3, 2, 1, 0.
        # stop is -1 b/c idx 0 must be included.
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            # Same store then multiply order.
            # *= combines right part with left part already stored in res[i]/
            res[i] *= postfix
            postfix *= nums[i]
        # i=3: res[3] = 6*1  = 6,   postfix = 1*4  = 4
        # i=2: res[2] = 2*4  = 8,   postfix = 4*3  = 12
        # i=1: res[1] = 1*12 = 12,  postfix = 12*2 = 24
        # i=0: res[0] = 1*24 = 24,  postfix = 24*1 = 24
        # res = [24, 12, 8, 6]   (left part * right part for every i)  

        # No separate prefix/postfix arrays were needed: res holds the
        # prefixes, and postfix is a single variable, so extra space is O(1).
        return res
