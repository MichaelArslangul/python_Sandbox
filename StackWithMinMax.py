class Candy:
    """ There are N children standing in a line. Each child is assigned a rating value.

    You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
    What is the minimum candies you must give?

    Example 1:

    Input: [1,0,2]
    Output: 5
    Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
    Example 2:

    Input: [1,2,2]
    Output: 4
    Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
    """

    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        _result_forward = [1]*len(ratings)
        _result_backward = [1]*len(ratings)
        _sum = 0

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                _result_forward[i] = _result_forward[i-1] + 1

        for i in range(len(ratings) -2, -1, -1):
            if ratings[i] > ratings[i+1]:
                _result_backward[i] = _result_backward[i+1] +1

        for i in range(len(ratings)):
            _sum += max(_result_forward[i], _result_backward[i])
        return _sum


can = Candy()
# _input=[1,3,2,2,1]
_input=[1,2,87,87,87,2,1]
# _input=[1,0,2]
print("Output for: {} is: {}".format(_input, can.candy(_input)))
