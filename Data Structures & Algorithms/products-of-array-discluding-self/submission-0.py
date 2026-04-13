class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)

        ans = [ 0 for _ in range(size) ]

        product = 1

        cont_zero  = False
        count = 0
        
        for num in nums:
            if num!=0:
                product *= num
            elif num==0 :
                cont_zero = True
                count+=1
        if count>1:
            return [0]*size


        for i in range(size):
            if cont_zero == True and nums[i]==0:
                ans[i] = product
            elif cont_zero==True and nums[i]!=0:
                continue
            
            elif cont_zero ==False:
                ans[i] = int(product/nums[i])
            

        return ans


        
        