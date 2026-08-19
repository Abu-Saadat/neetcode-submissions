class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        larr,rarr = [0]*n,[0]*n
        lmax,rmax = height[0],height[n-1] 
        total = 0
        for i in range(1,n):
            j = -i-1
            rarr[j] = rmax
            rmax = max(rmax,height[j])
            larr[i] = lmax
            lmax = max(lmax, height[i])
            
        for i in range(n):
            if (min(rarr[i], larr[i]) - height[i])>0:
                total+=(min(rarr[i], larr[i]) - height[i])
        return total