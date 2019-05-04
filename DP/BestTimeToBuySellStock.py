class BestTimeToBuySellStock:
    """ Given an array representing daily stock price determines the maximum profit
    if we're allow to buy and sell stock only once
    Example:
    Input: [7,1,5,3,6,4]
    Output = 5

    Input: [7,6,4,3,1]
    Output = 0
    """


    def highest_revenue_recursive(self, day, prices):
        max_value = float('-inf')
        if day == 0:
            return 0
        max_value = self.highest_revenue_recursive(day-1, stock_prices)
        for i in range(1, day):
            max_value = max(max_value, stock_prices[day-1] - stock_prices[i-1])
        return max_value

    def highest_revenue_dp(self, day, prices):
        max_value = float('-inf')
        revenue = [0]*(day+1)

        for i in range(1, day+1):
            max_value = -1
            for j in range(i):
                revenue[i] = max(revenue[i], prices[i-1] - prices[i-j-1])
        return revenue[day]

    def highest_revenue_dp_optimized(self, day, prices):
        max_value = float('-inf')
        revenue = [0]*(day+1)

        for i in range(1, day+1):
            min_value = prices[i]
            max_value = -1
            for j in range(i):
                revenue[i] = max(revenue[i], prices[i-1] - prices[i-j-1])
        return revenue[day]

    #  Does not work, needs to be debugged
    # def highest_revenue(self, day, prices):
    #     if day == 0:
    #         return 0
    #     max_profit=0
    #     low_price=prices[0]
    #     for i in range(1,day):
    #         low_price=min(prices[:day])
    #         max_profit=max(max_profit, prices[i]-low_price)
    #     return max_profit

bs= BestTimeToBuySellStock()
day_to_optimize = 5
stock_prices = [7,1,5,3,6,4]
# stock_prices = [7,6,4,3,1]
# print("highest revenue possible for day: {} using recursion is: {}".format(
#     day_to_optimize, bs.highest_revenue_recursive(day_to_optimize, stock_prices)))
# print("highest revenue possible for day: {} using DP is: {}".format(
#     day_to_optimize, bs.highest_revenue_dp(day_to_optimize, stock_prices)))
print("highest revenue possible for day: {} using DP optimized is: {}".format(
    day_to_optimize, bs.highest_revenue_dp_optimized(day_to_optimize, stock_prices)))
# print("highest revenue possible for day: {} is: {}".format(
#     day_to_optimize, bs.highest_revenue(day_to_optimize, stock_prices)))
