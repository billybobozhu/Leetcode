class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<= 1:
            return [nums]
        ans=[]
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            for temp_list in self.permute(n):
                ans.append([num] + temp_list)
        return ans


a=Solution()
lista=[1,2,3]
print(a.permute(lista))
