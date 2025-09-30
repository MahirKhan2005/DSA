class Solution:
    def frequencySort(self, s: str) -> str:
        hash = {}
        for ch in s:
            hash[ch] = hash.get(ch,0) + 1
        sortedCh = sorted(hash.items(),key = lambda x:x[1], reverse=True)
        ans = ""
        for char,count in sortedCh:
            ans += char*count
        return ans