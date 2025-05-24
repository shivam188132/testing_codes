nums = [3, 3, 0, 99, -40]

def largestElement(nums):
        for i in range(len(nums)):
            for j in range(i, len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums[len(nums)-1]   

a  = largestElement(nums)
print(a)