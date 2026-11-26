class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        dict = {}
        for word in s:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1

        
        for i in range(len(t)):
            if t[i] in dict and dict[t[i]] != 0:
                dict[t[i]] -=1
            elif t[i] not in dict or dict[t[i]] < 1:
                return False
        
        return True