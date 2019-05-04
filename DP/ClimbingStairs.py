class ClimbingStairs:
    """ Going up n stairs 1 by 1, 2 by 2, 3 by 3. How many different ways
    can we go up those stairs?
    """

    def nbr_of_ways(self, nbr_of_steps):
        _sum = []
        _sum.insert(0, None)
        _sum.insert(1, 1)
        _sum.insert(2, 2)
        _sum.insert(3, 3)
        for i in range(4, nbr_of_steps+1):
            _sum.insert(i,_sum[i-1] + _sum[i-2] + _sum[i-3])
        return _sum[nbr_of_steps]



cs = ClimbingStairs()
A = 45
print("number of ways for {} steps is: {}".format(
    A, cs.nbr_of_ways(A)))
