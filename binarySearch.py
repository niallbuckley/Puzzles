def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2 
        l = 0
        r = len(nums)-1
        while l <= r:
            if target==nums[mid]:
                return mid
            if target < nums[mid]:
                r=mid
                mid = (r-1)+l//2
            elif target > nums[mid]:
                l=mid+1
                mid = (r-1)+l//2
        return -1

def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        
        while l <= r:
             mid = l + (r - l) // 2
  
             # Check if x is present at mid
             if nums[mid] == target:
                 return mid
  
             # If x is greater, ignore left half
             elif nums[mid] < target:
                 l = mid + 1
  
             # If x is smaller, ignore right half
             else:
                 r = mid - 1
        return -1