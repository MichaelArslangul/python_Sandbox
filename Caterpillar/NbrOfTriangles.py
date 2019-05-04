class NbrOfTriangles:
    """ You are given n sticks (of lengths 1 ˛ a0 ˛ a1 ˛ ... ˛ an≠1 ˛ 109).
    The goal is to count the number of triangles that can be constructed using
    these sticks. More precisely, we have to count the number of triplets at
    indices x<y<z, such that ax + ay > az.
    """


    def nbr_of_triangles(self, A):
        N = len(set(A))
        _result = 0

        if len(A) < 3:
            return 0
        for i in range(len(A)):
            _front = i + 2
            for j in range(i + 1, len(A)):
                while _front < len(A) and A[i] + A[j] > A[z]:
                    z += 1
                _result += z - y + 1
        return _result






ad = AbsDistinct()
A = [-23, -5, -3, -1, 0, 3, 6, 12, 17, 23]
# A = [1, 2]
print("How many absolute values are there in the A {}: {}".format(
    A, ad.nbr_of_triangles(A)))
