class Solution():
    def find_subset(self,index,current_subset,array,power_set):
        if index==len(array):
            power_set.append(current_subset[:])
            return
        # Include 
        current_subset.append(array[index])
        self.find_subset(index+1,current_subset,array,power_set)
        # Backtrack
        current_subset.pop()
        # Exclude
        self.find_subset(index+1,current_subset,array,power_set)
    def subsetsWithDup(self, nums):
        current_subset = []
        power_set = []
        self.find_subset(0,current_subset,nums,power_set)
        result = set(power_set)
        return result