'''
Intuition: Count how often each number appears, 
then pick the k most frequent. 
Sorting by count would cost O(nlogn).
Rather, use the fact that no number can appear more than n times. 
Make a list where the INDEX is a count, 
and place each number at the index of its own count. 
Reading that list from the highest index down 
gives the most frequent numbers first with no sorting required. 
This is bucket sort.

Two structures, pointing in opposite directions:
    count: number -> its count      {1: 3, 2: 2, 3:1}
    freq:  count -> numbers with it freq[3] = [1]

Time: O(n)  Space: O(n)
Trace below: nums = [1, 1, 1, 2, 2, 3], k = 2
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # number -> count

        # One bucket per possible count. 
        # The max count is n (all elements the same)
        # and used as an index -> n + 1 buckets (indices 0...n)
        # Index 0 stays empty: every number appears at least once. 
        # The comprehension creates n + 1 SEPARATE lists. 
        freq = [[] for i in range(len(nums) + 1)]
        # freq = [[], [], [], [], [], [], []] (indices 0-6)

        # Phase 1: count each number
        # .get(num, 0) returns current count, or 0 if num is new.
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # 1 -> {1:1}, 1 -> {1:2}, 1 -> {1:3}, 
        # 2 -> {..., 2:1}, 2 -> {..., 2:2}, 3 -> {..., 3:1}
        # count {1: 3, 2: 2, 3: 1}

        # Phase 2: invert count into buckets. Key step. 
        # .items() yields (key, value) pairs = (number, count).
        # The count becomes a list index, so each number lands 
        # in the bucket matching its frequency. 
        for num, cnt in count.items():
            freq[cnt].append(num)
        # (1, 3) -> freq[3] = [1]
        # (2, 2) -> freq[2] = [2]
        # (3, 1) -> freq[1] = [3]
        # freq = [[], [3], [2], [1], [], [], []]

        # Phase 3: read buckets from highest count down. 
        # range(start, stop, step): range (6, 0, -1)
        # Stops before 0, skipping the always empty bucket. 
        res = []
        for i in range(len(freq) - 1, 0, -1):
            # A bucket may hold several ties, 
            # so collect one at a time. 
            # Empty bucket means loop runs zero times.
            for num in freq[i]:
                res.append(num)
                # Check after each append so we stop at k.
                # return exits both loops and function at once.
                if len(res) == k:
                    return res
                # i = 6, 5, 4 -> empty, skip
        # i = 3 -> append 1, res = [1]
        # i = 2 -> append 2, res = [1, 2]
        # len == k -> return [1, 2]
        # (bucket 1 is never visited)



