class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def reverse(arr):
            st, end = 0, len(arr) - 1
            while st < end:
                arr[st], arr[end] = arr[end], arr[st]
                st += 1
                end -= 1

        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for row in matrix:
            reverse(row)
