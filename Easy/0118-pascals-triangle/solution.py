class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        n=numRows



        
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = []

        for i in range(numRows):

            if i == 0:
                res.append([1])
            else:
                prev = res[-1]
                row = [1]

                for j in range(len(prev) - 1):
                    row.append(prev[j] + prev[j+1])

                row.append(1)
                res.append(row)

        return res
