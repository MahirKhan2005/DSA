def findUnion(nums1,nums2):
    i=j=0
    union = []
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<=nums2[j]:
            if len(union)==0 or nums1[i]!=union[-1]:
                union.append(nums1[i])
            i+=1
        else:
            if len(union)==0 or nums2[j]!=union[-1]:
                union.append(nums2[j])
            j+=1

    while i<len(nums1):
        if nums1[i]!=union[-1]:
            union.append(nums1[i])
        i+=1
    while j<len(nums2):
        if nums2[j]!=union[-1]:
            union.append(nums2[j])
        j+=1
    return union

print(findUnion([1,2,3,3,4,4],[1,2,4,7,7]))