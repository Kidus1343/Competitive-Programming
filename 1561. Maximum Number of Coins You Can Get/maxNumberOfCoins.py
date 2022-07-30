class Solution(object):
    def maxCoins(self, piles):
        piles.sort(reverse =True)
        print(piles)
        values =0
        for i in range(len(piles)//3):
            j=(i*2)+1
            values+=piles[j]
            
        return values
