class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2:
            print("returned here")
            return len(chars)
        i = 0
        j = 0
        w = 0
        while i < len(chars):
            while j < len(chars) and chars[i] == chars[j]:
                j+=1
            # print(j)
            chars[w] = chars[i]
            w+=1
            count = j - i
            if count > 1:
                for c in str(count):
                    chars[w] = c
                    w+=1
            i = j
        return w
        