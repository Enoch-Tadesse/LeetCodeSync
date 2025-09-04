class Trie:
    def __init__(self):
        self.chs = [None for _ in range(26)]
        self.is_end = False

    def back(self, board, r, c , cont, temp, root, visited):
        if root.is_end:
            cont.append("".join(temp))
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if (nr, nc) in visited:
                continue
            if (nr < 0 or nc < 0) or (nr >= len(board) or nc >= len(board[0])):
                continue
            idx = ord(board[nr][nc]) - ord('a')
            if not root.chs[idx]:
                continue
            temp.append(chr(idx + ord('a')))
            visited.add((nr, nc))
            self.back(board, nr, nc, cont, temp, root.chs[idx], visited)
            visited.discard((nr, nc))
            temp.pop()

    def get_valids(self, r, c, board):
        cont = []
        idx = ord(board[r][c]) - ord('a')
        if not self.chs[idx]:
            return cont
        self.back(board, r, c, cont, [str(board[r][c])], self.chs[idx], set([(r, c)]))
        return cont

    def insert(self, word):
        root = self
        for w in word:
            idx = ord(w) - ord('a')
            if not root.chs[idx]:
                root.chs[idx] = Trie()
            root = root.chs[idx]
        root.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.insert(w)
        ans = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                ans.extend(trie.get_valids(r, c, board))
        return list(set(ans))