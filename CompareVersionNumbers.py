from itertools import zip_longest
class CompareVersionNumbers:

    def compareVersion(self, version1: str, version2: str) -> int:
        for v1, v2 in zip_longest(map(int, version1.split('.')), map(int, version2.split('.')),
                                  fillvalue = 0):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0




cv = CompareVersionNumbers()
version1 = "2.1.7.1"
version2 = "2.1.4"
print("is version1 <{}>, greater than version2 <{}>: {}".format(version1, version2,
        cv.compareVersion(version1, version2)))
