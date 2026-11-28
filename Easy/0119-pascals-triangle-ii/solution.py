class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = []
        n=rowIndex+1
        for i in range(n):

            if i == 0:
                res.append([1])
            else:
                prev = res[-1]
                row = [1]

                for j in range(len(prev) - 1):
                    row.append(prev[j] + prev[j+1])

                row.append(1)
                res.append(row)

        return res[rowIndex]
