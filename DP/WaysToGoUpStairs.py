class WaysToGoUpStairs:
    """ We can go up one or two stairs at a time. How many ways are there
    to go up N stairs
    """

    def nbr_of_ways(self, nbr_stairs):
        _nways = [0]*(nbr_stairs +1)
        _nways[0] = 0
        _nways[1] = 1
        _nways[2] = 2

        for i in range(3, nbr_stairs+1):
            _nways[i] = _nways[i-1] + _nways[i-2]
        return _nways[nbr_stairs]


wu = WaysToGoUpStairs()
nbr = 4
print("number of ways to go up {} stairs is: {}".format(
    nbr, wu.nbr_of_ways(nbr)))
