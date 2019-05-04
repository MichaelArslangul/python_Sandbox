class CuttingRods:
    """ Given a rod of length N and prices p[0], ..., p[N], where p[i]
    is the price of a length i of the rod. Find the max revenue we can
    get from the rod by cutting and selling it
    """


    def highest_revenue_recursive(self, rod_length, prices):
        _max_revenue = float("-inf")
        if rod_length == 0:
            return 0
        for i in range(rod_length):
            _temp_revenue = prices[i] + self.highest_revenue(
                rod_length -i -1, prices)
            _max_revenue = max(_temp_revenue, _max_revenue)
        return _max_revenue

    def highest_revenue_dp(self, rod_length, prices):
        _revenue = [0]*(rod_length +1)
        for i in range(1, rod_length+1):
            _max_revenue = float("-inf")
            for j in range(i):
                _max_revenue = max(_max_revenue, prices[j] + _revenue[i-j-1])
            _revenue[i] = _max_revenue
        return _revenue[rod_length]

cr = CuttingRods()
rod_length = 8
prices = [1, 5, 8, 9, 10, 17, 17, 20]
print("most cost effective to cut a rod of length {} using recursion is: {}".format(
    rod_length, cr.highest_revenue_recursive(rod_length, prices)))
print("most cost effective to cut a rod of length {} using DP is: {}".format(
    rod_length, cr.highest_revenue_dp(rod_length, prices)))
