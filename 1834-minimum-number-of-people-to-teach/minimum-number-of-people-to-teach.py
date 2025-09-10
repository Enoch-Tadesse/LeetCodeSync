class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        cand = set()
        for i in range(len(friendships)):
            u , v = friendships[i]
            if len(set(languages[u-1]) & set(languages[v-1])) == 0:
                cand.add(u)
                cand.add(v)
        counter = defaultdict(int)
        _max = 0
        for ppl in cand:
            for lan in languages[ppl-1]:
                counter[lan] += 1
                _max = max(_max, counter[lan])
        return len(cand) - _max