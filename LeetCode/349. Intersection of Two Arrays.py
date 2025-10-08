class Solution:
    def intersection(self, nums1, nums2) :
        nums1_set,nums2_set = set(nums1),set(nums2)
        ans = []
        for num in nums1_set:
            if num in nums2_set:
                ans.append(num)
        return ans