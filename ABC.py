from collections import defaultdict


class ABC:

    BLOCKS = [('B', 'O'), ('X', 'K'), ('D', 'Q'), ('C', 'P'), ('N', 'A'),
              ('G', 'T'), ('R', 'E'), ('T', 'G'), ('Q', 'D'), ('F', 'S'),
              ('J', 'W'), ('H', 'U'), ('V', 'I'), ('A', 'N'), ('O', 'B'),
              ('E', 'R'), ('F', 'S'), ('L', 'Y'), ('P', 'C'), ('Z', 'M')]

    def __init__(self):
        self.blocks = defaultdict(int)

    def build_blocks(self):
        for _unit in self.BLOCKS:
            self.blocks[_unit] += 1
        return self.blocks

    def can_be_written_with_blocks(self, word):
        self.build_blocks()
        _result = []
        for _letter in word:
            for key in self.blocks.keys():
                if _letter.upper() in key and self.blocks[key] > 0:
                    self.blocks[key] -= 1
                    _result.append(_letter)
                    break
        return ''.join(_result) == word


if __name__ == "__main__":
    print("Can the word: A be spelled with our blocks?. The answer: {}".format(
        ABC().can_be_written_with_blocks("A")))
    print("Can the word: BARK be spelled with our blocks?. answer: {}".format(
        ABC().can_be_written_with_blocks("BARK")))
    print("Can the word: BOOK be spelled with our blocks?. answer: {}".format(
        ABC().can_be_written_with_blocks("BOOK")))
    print("Can the word: treat be spelled with our blocks?. answer: {}".format(
        ABC().can_be_written_with_blocks("treat")))
    print("Can the word: common be spelled with our blocks?: {}".format(
        ABC().can_be_written_with_blocks("common")))
    print("Can the word: squad be spelled with our blocks?. answer: {}".format(
        ABC().can_be_written_with_blocks("squad")))
    print("Can the word: coNFused be spelled with our blocks?: {}".format(
        ABC().can_be_written_with_blocks("coNFused")))
