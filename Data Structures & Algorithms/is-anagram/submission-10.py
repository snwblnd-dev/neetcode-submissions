class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = dict()
        for char in s:
            if char in letters_s:
                letters_s[char] += 1
            else:
                letters_s[char] = 1
        letters_t = dict()
        for char in t:
            if char in letters_t:
                letters_t[char] += 1
            else:
                letters_t[char] = 1
        return (letters_s == letters_t)