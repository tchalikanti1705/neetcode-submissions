class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            temp = i
            cnt = 0
            while temp!=0:
                temp = temp & (temp - 1)
                cnt+=1
            res.append(cnt)
        return res 

        