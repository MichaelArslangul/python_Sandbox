class ReachingPoint:
    """ Leetcode 780
    """

    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx == tx and sy == ty:
            return True
        if sx == 0 and sy == ty or sy == 0 and sx == tx:
            return True

        while tx > sx and ty > sy:
            if tx >= ty:
                tx %= ty
            else:
                ty %= tx
            # if tx >= ty:
            #     tx -= ty
            # else:
            #     ty -= tx
            print(sx, sy, tx, ty)
            print(sx == tx)
            print(sy == ty)
        print(tx == sx and ty == sy)
        return (tx == sx and ty == sy)


rp = ReachingPoint()
sx = 9
sy = 5
tx = 12
ty = 8
print("Can we go from sx, sy ({}, {}) to tx, ty ({}, {}): {}".format(
    sx, sy, tx, ty, rp.reachingPoints(sx, sy, tx, ty)
))
