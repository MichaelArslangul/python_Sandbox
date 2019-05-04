class PascalTriangle:

    def draw_triangle(self, nbr_of_rows):
        if nbr_of_rows == 0:
            return []
        elif nbr_of_rows == 1:
            return [1]
        elif nbr_of_rows > 1:
            _result = [1]
            _prev = self.draw_triangle(nbr_of_rows - 1)
            # print("Prev: {}, number of rows: {}".format(_prev, nbr_of_rows))
            for i in range(len(_prev) - 1):
                _result.append(_prev[i] + _prev[i+1])
            _result.append(1)
        return _result


if __name__ == "__main__":
    for i in range(7):
        print(PascalTriangle().draw_triangle(i))
