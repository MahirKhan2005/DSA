class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
        startWeight, endWeight = max(weights), sum(weights)
        while startWeight<endWeight:
            midWeight = startWeight + (endWeight-startWeight)//2
            # Calculating the number of days 
            sumDays = 1
            tempWeight = 0
            for weight in weights:
                if weight+tempWeight<=midWeight:
                    tempWeight+=weight
                else:
                    tempWeight = weight
                    sumDays+=1
            if sumDays<=days:
                endWeight = midWeight
            else:
                startWeight = midWeight + 1
        return startWeight