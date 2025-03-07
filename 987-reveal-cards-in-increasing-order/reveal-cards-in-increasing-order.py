class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans = deque([])
        deck.sort(reverse = True)
        for i in range(len(deck)):
            ans.appendleft(deck[i])
            if i != len(deck)-1:
                ans.appendleft(ans.pop())
        return list(ans)