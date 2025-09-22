class Solution:
    def maxFrequencyElements(self, nums) -> int:
        hash = {}
        for num in nums:
            hash[num] = hash.get(num,0) + 1
        maxfreq = 0
        for i in hash:
            if hash[i] > maxfreq:
                maxfreq = hash[i]
        total = 0
        for i in hash:
            if hash[i]==maxfreq:
                total+=maxfreq
        return total
        