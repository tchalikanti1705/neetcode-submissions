class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        psm, ssm = 0, 0
        n = len(mat)
        for i in range(len(mat)):
            psm += mat[i][i]
            ssm += mat[i][n-i-1]
        print(psm, ssm)
        if len(mat)%2==0:
            return (psm+ssm)
        return (psm + ssm) - mat[n//2][n//2]


    

        