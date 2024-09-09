class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2:
            return 
        l = r = 0
        while r < len(chars):
            curr = chars[r]
            count = 0
            while r < len(chars) and chars[r] == curr:
                count += 1
                r+=1
            chars[l] = curr
            # count = r - l
            l+=1
            if count > 1:
                for digit in str(count):
                    chars[l] = digit
                    l+=1
        return l
        