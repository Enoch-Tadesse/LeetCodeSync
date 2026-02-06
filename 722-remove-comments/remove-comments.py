class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        output = []
        temp = []
        comment = False

        for line in source:
            if not comment:
                temp = []

            n = len(line)
            i = 0

            while i < n:
                if comment:
                    if i + 1 < n and line[i:i+2] == "*/":
                        comment = False
                        i += 2
                        continue
                else:
                    # comment starter /*
                    if i + 1 < n and line[i:i+2] == "/*":
                        comment = True
                        i += 2
                        continue

                    # double slash
                    if i + 1 < n and line[i:i+2] == "//":
                        break
                    
                    temp.append(line[i])
                i += 1
            if not comment and temp:
                output.append("".join(temp))


        return output