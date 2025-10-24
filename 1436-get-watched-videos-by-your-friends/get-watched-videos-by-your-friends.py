class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        visited = set()
        q = deque([id])
        visited.add(id)
        for i in range(level):
            for _ in range(len(q)):
                ele = q.popleft()
                for fr in friends[ele]:
                    if fr not in visited:
                        q.append(fr)
                        visited.add(fr)
        ans = defaultdict(int)
        for ele in q:
            for w in watchedVideos[ele]:
                ans[w] += 1
        pairs = [(v, k) for k , v in ans.items()]
        pairs.sort()
        return [b for a, b in pairs]