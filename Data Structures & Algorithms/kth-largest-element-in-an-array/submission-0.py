class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        res = 0
        while k > 0:
            largest = heapq.heappop(nums)
            res = largest
            k -=1
            
        return res*-1

