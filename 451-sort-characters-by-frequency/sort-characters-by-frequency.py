class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = {}
        output = [0]*len(s)
        for item in s:
            if item not in count:
                count[item] = 1
            else: count[item] += 1
        strings = list(count.keys())
        fre = list(count.values())
        for i in range(len(fre)):
            for j in range(0,len(fre)-i-1):
                if fre[j] < fre[j+1]:
                    fre[j] , fre[j+1] = fre[j+1] , fre[j]
                    strings[j] , strings[j+1] = strings[j+1] , strings[j]
        for i in range(1 ,len(fre)):
            fre[i] = fre[i] + fre[i-1]
        for item in s:
            output[fre[strings.index(item)]-1] = item
            fre[strings.index(item)]-=1
        return ("").join(output)
