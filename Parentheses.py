class Parentheses:
    """
    Check for a balanced number of opening/closing Parentheses
    """

    def __init__(self):
        self.OPENING = "("
        self.PAIRS = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

    def is_paren_balanced(self, expr):
        _stack = []
        for _char in expr:
            if _char == self.OPENING:
                _stack.append(self.OPENING)
            else:
                try:
                    _stack.pop()
                except IndexError:
                    return False
        return len(_stack) == 0

    def are_symbols_balanced(self, expr):
        _stack = []
        for _char in expr:
            print("char: {}".format(_char))
            if _char in self.PAIRS.keys():
                _stack.append(_char)
            else:
                try:
                    _expected_opening_symbol = _stack.pop()
                    print("symbol: {} and expected opening: {}".format(
                        _char, self.PAIRS[_expected_opening_symbol]
                    ))
                except IndexError:
                    return False
                if _char != self.PAIRS[_expected_opening_symbol]:
                    return False
        return len(_stack) == 0


p = Parentheses()
print("((())) is balanced?: {}".format(
    Parentheses().is_paren_balanced('((()))')))
print("(() is balanced?: {}".format(p.is_paren_balanced('(()')))
print("()) is balanced?: {}".format(p.is_paren_balanced('())')))
# print("[({})] is balanced?: {}".format(
#     p.are_symbols_balanced('[({})]')))
# print("{[(()]} is balanced?: {}".format(
#     p.are_symbols_balanced(
#         '{[(()]}'
#     )
# ))
# print("()) is balanced?: {}".format(
#     p.are_symbols_balanced('())')))
