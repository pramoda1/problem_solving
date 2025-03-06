class search:
    def solution(self,nums,target):
        left ,right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[target] == mid:
                return mid
            
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[right] < target <= nums[mid]:
                    right = mid +1
                else:
                    left = mid - 1
        
        return -1
    
se = search()

print(se.solution([4,5,6,7,0,1,2], 0))