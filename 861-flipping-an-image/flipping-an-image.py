class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for item in image:
            
            i = len(item)-1
            j = 0
            while i >= j:  
                item[i], item[j] = int(not item[j]), int(not item[i])
                i , j = i - 1, j + 1
        return image
        