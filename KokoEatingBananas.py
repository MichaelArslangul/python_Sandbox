import math
class Solution:
    def minEatingSpeed(self, piles, H):
        numberOfPiles = len(piles)
        greatestNumberOfBananas = max(piles)
        lowestK = sum(piles)//H
        if H < numberOfPiles:
            return -1
        elif H == numberOfPiles:
            return greatestNumberOfBananas
        else:
            eatenBananas = [math.ceil(piles[i]/lowestK) for i in range(len(piles))]
            minVelocity = 0
            while minVelocity <= H:
                lowestK += 1
                eatenBananas = [math.ceil(piles[i]/lowestK) for i in range(len(piles))]
                minVelocity = sum(eatenBananas)
            return minVelocity
        return -1

cc = Solution()
piles = [3,6,7,11]
H = 8
print("piles: {} and hours: {}, result: {}".format(piles, H, cc.minEatingSpeed(
    piles, H
)))
