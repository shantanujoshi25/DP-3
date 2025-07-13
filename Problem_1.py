# // Time Complexity : O(n)
# // Space Complexity : O(n)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        hashMap = {}
        maxVal = 0
        for i in nums:
            if(i > maxVal):
                maxVal = i
            if(i in hashMap):
                hashMap[i]+=i
            else:
                hashMap[i] = i 

        dp = [hashMap.get(i,0) for i in range(maxVal+1)]     
        
        if(len(dp)>2):
            dp[2] = dp[2]+dp[0]

        for i in range(3,maxVal+1):
            dp[i] = max(dp[i-2],dp[i-3]) + dp[i]

        return(max(dp[-2],dp[-1]))
