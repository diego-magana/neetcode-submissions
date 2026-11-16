'''
Two strings are anagrams when they have the same character counts. 
Turn each string into a signature (its count of each letter a-z) and group
the strings that share a signature. 
Dictionary for the grouping: key is the signature and the value is the list
of strings with that signature. 
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary: signature -> list of strings with that signature
        # defaultdict(list) creates an empty list automatically the first
        # time we access a missing key, so we can .append() right away.
        res = defaultdict(list)
        
        for s in strs:
            # 26 slots, one per letter: count[0] = 'a', ..., count[25] = 'z'
            count = [0] * 26

            for c in s:
                # ord gives a characters numeric code
                count[ord(c) - ord('a')] += 1

            # Lists cannot be dictionary keys (mutable) so
            # use a tuple with is immutable and can be a key.
            # All anagrams produce the same tuple, so they land in the same list.
            res[tuple(count)].append(s)

        # Only the groups are needed, not the signatures.
        return list(res.values()) 
