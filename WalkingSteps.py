from functools import lru_cache


class WalkingSteps:
    """ walker can take 1,2,3 going up stairs. Question is, if
        he/she goes up n stairs, how many combinations are there
    """

    @lru_cache()
    def random_steps(self, n):
        if n <= 3:
            return n
        else:
            return self.random_steps(n - 1) + self.random_steps(n - 2) + \
                self.random_steps(n - 3)


walk = WalkingSteps()
for i in range(10):
    print("number of possible ways to go up {} stairs is: {}".format(
        i, walk.random_steps(i)))
