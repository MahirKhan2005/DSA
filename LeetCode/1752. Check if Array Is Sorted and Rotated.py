class Solution(object):
    def check(self,array):
        for i in range(0,len(array)):
            if array==sorted(array):
                return True
            temp = array.pop(0)
            array.append(temp)
        return False
    