class HouseRobber:
    """ There are n houses build in a line, each of which contains
    some value in it. A thief is going to steal the maximal value
    of these houses, but he can’t steal in two adjacent houses because
    owner of the stolen houses will tell his two neighbour
    left and right side.
    What is the maximum stolen value.
    """


    def max_loot(self, n, hval):
        if n == 0:
            return 0
        if n == 1:
            return hval[0]
        if n == 2:
            return max(hval[0], hval[1])

        # dp[i] represent the maximum value stolen so
        # for after reaching house i.
        dp = [0]*n
        dp[0] = hval[0]
        dp[1] = max(hval[0], hval[1])

        for i in range(3,n):
            dp[i] = max(hval[i]+dp[i-2], dp[i-1])

        return dp[-1]]



hr = HouseRobber()
nbr_houses = 7
h_val = [6, 7, 1, 3, 8, 2, 4]
print("most cost effective to cut a rod of length {} is: {}".format(
    nbr_houses, hr.max_loot(nbr_houses, h_val)))
