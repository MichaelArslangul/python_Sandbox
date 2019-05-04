class CeasarCypher:

    def __init__(self, shift):
        self.shift = shift # how many elements we're going to move to the right
        self.forward_encode = []
        self.backward_encode = []
        for i in range(26):
            forward = ((i + shift)%26) + ord('a')
            backward = ((i - shift)%26) + ord('a')
            self.forward_encode.append(chr(forward))
            self.backward_encode.append(chr(backward))


    def convert_forward(self, phrase):
        return self.convert(phrase, self.forward_encode)

    def convert_backward(self, phrase):
        return self.convert(phrase, self.backward_encode)

    def convert(self, phrase, code):
        _ans = []
        for i in phrase:
            if i  == " ":
                _ans.append(" ")
            else:
                _char = ord(i) - ord('a')
                _ans.append(code[_char])
        return "".join(_ans)





cc = CeasarCypher(26)
_str = "je suis beau"
_encoded = cc.convert_forward(_str)
_convert_backwardd = cc.convert_backward(_encoded)
print("encoding the phrase: \'{}\', we have: {}".format(
    _str, _encoded))
print("decoding the encoded phrase: \'{}\', we have: {}".format(
    _encoded, _convert_backwardd))
print(dir(cc))
