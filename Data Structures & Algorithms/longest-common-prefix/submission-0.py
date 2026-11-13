'''
Line the strings up vertically and read them column by column. 
Check that every string has the same character at pos[0], pos[1], and so on. 
The first column where a string disagrees or runs out of characters is 
where the common prefix ends. Given the common prefix cannot be longer than 
a single string, we only need to scan as far as the first strings length.
'''
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # i is the column (character position being checked).
        # Use the first string as the reference to compare against.
        for i in range(len(strs[0])):
            # check column i in every string.
            for s in strs:
                # Stop if either:
                # i == len(s): s has run out of characters, or
                # s[i] != strs[0][i]: s disagrees with the reference. 
                # Checking the length first prevents s[i] from raising
                # an IndexError on a string that is too short. 
                if i == len(s) or s[i] != strs[0][i]:
                    # Everything before column i matched, return it. 
                    return s[:i]

        # Every column of strs[0] matched, whole first string is common prefix.
        return strs[0]
                