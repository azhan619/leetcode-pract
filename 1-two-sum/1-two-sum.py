class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complement_dict = {}
        
        result = []
        
        
        for i in range(0,len(nums)):
            
            complement = target - nums[i]
            
            if(complement in complement_dict.keys()):
                result.append(complement_dict[complement])
                result.append(i)
                return result
            else:
                complement_dict[nums[i]] = i
                
                
                
        return result