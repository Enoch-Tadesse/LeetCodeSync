class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def after(word):
            ans = []
            ans2 = []
            for w in word:
                ans2.append(w.lower())
                if w.lower() in vowels:
                    ans.append('o')
                else:
                    ans.append(w.lower())
            return ("".join(ans2), "".join(ans))
        vowels = {'a','e', 'i','o','u'}
        output = []
        seen = defaultdict(list)
        exact = set()
        cap = defaultdict(list)
        for i, word in enumerate(wordlist):
            exact.add(word)
            capital, manip = after(word)
            cap[capital].append(word)
            seen[manip].append(word)
        for q in queries:
            if q in exact:
                output.append(q)
                continue
            capital, manip = after(q)
            if capital in cap:
                output.append(cap[capital][0])
                continue
            if manip in seen:
                output.append(seen[manip][0])
                continue
            output.append("")
        return output