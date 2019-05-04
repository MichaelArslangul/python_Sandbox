from collections import Counter
class FourSumTwo:

    def fourSumCount1(self, A, B, C, D):
        hashtable = {}
        for a in A:
            for b in B :
                if a + b in hashtable :
                    hashtable[a+b] += 1
                else :
                    hashtable[a+b] = 1
        count = 0
        for c in C :
            for d in D :
                if -c - d in hashtable :
                    count += hashtable[-c-d]
        return count



    def fourSumCount(self, A, B, C, D):
        result = 0
        AB = Counter(a+b for a in A for b in B)
        CD = Counter(c+d for c in C for d in D)
        for ab_key in AB.keys():
            if -ab_key in CD:
                result += AB[ab_key]*CD[-ab_key]
        return result

fstwo = FourSumTwo()
print("dungeon game return: {}".format(fstwo.fourSumCount(
    [-1,1,1,1,-1], [0,-1,-1,0,1], [-1,-1,1,-1,-1], [0,1,0,-1,-1])))
