class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words)!=len(pattern):
            return False
        mapP, mapS = {}, {}
        for ch,word in zip(pattern,words):
            if ch in mapP and mapP[ch]!=word:
                return False
            if word in mapS and mapS[word]!=ch:
                return False
            mapP[ch] = word
            mapS[word] = ch
        return True
