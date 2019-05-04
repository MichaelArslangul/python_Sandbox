class SpiralMatrix:

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output = []
        if len(matrix[0]) == 0:
            return []
        expected_out_len=len(matrix)*len(matrix[0])
        for i in matrix[0]:
            output.append(i)
        del matrix[0]
        reversed = list(zip(*matrix))
        while reversed:
            for i in reversed[-1]:
                output.append(i)
            del reversed[-1]
            reversed = list(zip(*reversed[::-1]))
        return output


    def spiralOrder1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output = []
        if not matrix:
            return []
        expected_out_len=len(matrix)*len(matrix[0])

        while len(output)<=expected_out_len:
            for i in matrix[0]:
                output.append(i)
            del matrix[0]

            if len(output) >= expected_out_len:
                break
            for i in matrix:
                output.append(i[-1])
                del i[-1]
            if len(output) >= expected_out_len:
                break

            for i in matrix[-1][::-1]:
                output.append(i)
            del matrix[-1]
            if len(output) >= expected_out_len:
                break

            for i in matrix[::-1]:
                output.append(i[0])
                del i[0]
            if len(output) >= expected_out_len:
                break
        return output

sm = SpiralMatrix()
print("output: {}".format(sm.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])))

print("output: {}".format(sm.spiralOrder([[]])))

print("output: {}".format(sm.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
])))
