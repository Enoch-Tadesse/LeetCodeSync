class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # i = 0
        # j = len(s) - 1
        # while i < j:
        #     s[i] , s[j] = s[j] , s[i]
        #     i+=1
        #     j-=1
        output = []
        def helper(s,left,right):
            if left >= right:
                return
            s[left] , s[right] = s[right], s[left]
            helper(s,left+1,right-1)
        helper(s,0,len(s)-1)