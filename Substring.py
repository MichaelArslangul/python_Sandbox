class Substring:
    """ Write  a  program  to determine  whether a n input string is a substring of
    another  input  string .
      For  example, "bat" is  a  substring of "abate", b ut  not  of "beat". 
    """


    def is_substring(self, origin, sub_candidate):
        if origin is None or sub_candidate is None:
            return False
        for i in range(len(origin) - len(sub_candidate) + 1):
            if origin[i] == sub_candidate[0]:
                _not_all_letters_match = False
                for j in range(1, len(sub_candidate)):
                    if origin[i + j] != sub_candidate[j]:
                        _not_all_letters_match = True
                if not _not_all_letters_match:
                    return True
        return False


ss = Substring()
string="bacdibcdbodaefbv"
sub_candidate = "fbv"
print("Is {} a substring of {}: {}".format(
    sub_candidate, string, ss.is_substring(string, sub_candidate)))
