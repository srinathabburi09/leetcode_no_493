from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(nums):
            if len(nums) <= 1:
                return 0, nums
            
            mid = len(nums) // 2
            count_left, left = merge_sort(nums[:mid])
            count_right, right = merge_sort(nums[mid:])
            count_cross = 0
            
            # Count reverse pairs
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                count_cross += j

            # Merge step
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            
            return count_left + count_right + count_cross, merged
        
        count, _ = merge_sort(nums)
        return count
                    
