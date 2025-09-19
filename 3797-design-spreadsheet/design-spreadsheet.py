class Spreadsheet:

    def __init__(self, rows: int):
        self.spread = [[0] * 26 for _ in range(rows + 1)]

    def setCell(self, cell: str, value: int) -> None:
        self.spread[int(cell[1:])][ord(cell[0]) - ord('A')] = value

    def resetCell(self, cell: str) -> None:
        self.spread[int(cell[1:])][ord(cell[0]) - ord('A')] = 0
        
    def getValue(self, formula: str) -> int:
        a , b = formula[1:].split('+')
        if a.isdigit():
            a = int(a)
        else:
            a = self.spread[int(a[1:])][ord(a[0]) - ord('A')]
        if b.isdigit():
            b = int(b)
        else:
            b = self.spread[int(b[1:])][ord(b[0]) - ord('A')]
        return a + b


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)