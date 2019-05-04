class Atoi:
    _STRATING_CHAR = ['+', '-', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def my_atoi(self, seq):
        _temp_str = seq.strip()
        _ch = list(_temp_str)
        if _ch[0] not in self._STRATING_CHAR:
            return 0
        else:
            pass


if __name__ == "__main__":
    print("Output: {}".format(Atoi().my_atoi(" +42")))
    print("Output: {}".format(Atoi().my_atoi(" W42")))
