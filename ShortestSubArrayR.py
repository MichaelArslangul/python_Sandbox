from queue import SimpleQueue
import collections

class ShortestSubArrayR:
    """
    Return the length of the shortest, non-empty, contiguous subarray of A
    with sum at least K.

    If there is no non-empty subarray with sum at least K, return -1
    """
    def shortest_subarray(self, A, K):
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        #Want smallest y-x with Py - Px >= K
        ans = N+1 # N+1 is impossible
        monoq = collections.deque() #opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            #Want opt(y) = largest x with Px <= Py - K
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N+1 else -1

    def shortest_subarray2(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        rtype = -1
        _sum = 0
        pacing = 2
        sq = SimpleQueue()
        if max(A) >=K:
            return 1
        else:
            while pacing <= len(A):
                for start in range(len(A)):
                    if len(A[start:start+pacing]) >= pacing:
                        sq.put(A[start:start+pacing])
                _sum = self.check_sum(sq,K)
                if _sum >0:
                    return _sum
                pacing +=1
        return rtype

    def check_sum(self, sq, K):
        _result = -1
        while not sq.empty():
            _sum = 0
            _elem=sq.get()
            for i in _elem:
                _sum +=i
        # retun len(_elem) if _sum >= K: else -1
                if _sum >=K:
                    return len(_elem)
        return _result



    def shortest_subarray1(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        rtype = -1
        _sum = 0
        # _temp=[]
        if len(A) == 0:
            raise ValueError("doesn't work for an empty array")
        elif max(A) >=K:
            rtype = 1
        else:
            for start in range(len(A)):
                end = start +1
                _sum = A[start]
                while end <= len(A) -1:
                    _sum += A[end]
                    if _sum >= K:
                        if rtype == -1:
                            rtype = len(A[start:end+1])
                        else:
                            rtype = min(len(A[start:end+1]), rtype)
                    # _temp.append(A[start:end+1])
                    end += 1
        return rtype





sa = ShortestSubArray()
print(sa.shortest_subarray([2,-1,2], 3)) # result is 3
print(sa.shortest_subarray([1,2], 4)) # -1
print(sa.shortest_subarray([1,2,3], 4)) # 2
print(sa.shortest_subarray([1,2,3,4], 20)) # -1
print(sa.shortest_subarray([1], 1)) # 1
print(sa.shortest_subarray([1,-1,1,-1,1,1], 2)) #2
print(sa.shortest_subarray([1,2,3,4,5,6,7,8,9], 10)) #2
print(sa.shortest_subarray([1,98,56,-1,1,10], 150)) # 2
print(sa.shortest_subarray([439,-235,712,67,78,311,875,-148,401,262,-22,954,836,511,378,-444,973,877,570,144,-179,-223,-202,-495,-217,378,-322,-73,263,579,742,-382,514,-15,528,865,-385,601,885,223,109,223,618,258,353,-216,277,619,690,805,357,884,-181,816,872,-256,789,255,-241,-395,227,254,438,149,-253,-138,599,-436,197,471,850,180,674,576,602,-14,473,277,176,37,-212,541,393,604,-304,183,405,729,469,-122,601,31,194,787,629,-17,286,-317,-274,19,656,627,456,-495,254,474,404,146,851,580,124,857,-341,79,-81,-441,466,-393,168,768,645,885,917,359,-368,472,784,-294,-464,840,571,-10,509,716,-32,-134,921,486,585,228,387,-312,453,-111,720,917,904,469,-399,763,901,549,508,-252,16,-265,949,160,680,935,59,149,477,558,-72,90,-58,609,600,-173,38,865,931,-255,979,594,139,155,437,672,846,332,512,170,494,865,598,-123,-327,904,-297,-266,1000,150,972,-418,370,-444,-300,-320,477,47,43,398,-190,669,-339,892,600,88,-284,247,232,-431,50,914,814,-110,626,97,26,-368,290,973,906,-185,324,675,513,-103,700,967,383,-211,-164,-52,611,-493,-64,821,940,-80,933,862,770,-368,224,668,546,760,238,322,-185,-394,266,-50,-117,722,945,734,-212,933,-359,-36,945,73,-383,-216,-458,-117,717,122,-297,633,637,708,-78,-290,-13,728,132,812,603,464,705,648,286,68,-449,-163,967,549,718,733,512,80,-229,-41,-352,440,915,869,423,-284,202,440,173,-38,252,472,68,331,832,731,-264,562,357,172,543,-435,929,114,667,-91,807,399,-73,203,51,365,-290,-307,836,617,487,682,482,-428,-225,636,-304,-499,-85,973,866,210,141,-63,117,852,-49,750,331,720,-431,-70,-337,-369,888,883,-171,983,-238,138,345,-423,50,477,334,422,-30,-137,-276,867,202,32,-33,643,790,121,-298,-196,-410,-151,205,351,-100,-133,713,185,994,201,139,48,618,45,-401,39,-53,-114,534,444,-399,269,-319,-24,902,-259,865,575,-135,-464,-476,-463,756,533,987,232,847,860,769,535,131,243,-419,734,915,740,763,-37,-337,419,-378,-450,-179,776,549,-376,768,-243,504,380,-296,577,220,-442,765,377,47,245,823,102,422,-343,446,993,172,-113,-228,-175,218,789,-93,-205,145,-367,640,730,-10,820,-48,904,653,-125,205,44,955,564,-271,67,661,717,641,821,814,916,684,419,-413,884,-86,-364,229,-99,710,625,-394,8,785,906,531,658,118,-235,-208,954,-38,240,75,-405,-326,-385,701,44,52,40,178,829,-420,306,-281,-408,-485,899,573,-437,-82,933,665,173,472,808,259,75,-277,944,-34,340,266,648,234,-438,556,-273,-155,543,831,973,628,338,206,697,-429,793,-397,937,736,376,-40,605,57,201,744,674,693,-456,-81,964,836,578,992,929,47,-34,762,641,600,-487,676,431,-347,-168,-37,249,-10,889,217,-177,124,30,-165,235,805,-296,-131,556,-374,-232,370,889,-410,821,-319,34,340,36,67,80,79,285,811,355,588,420,365,-128,970,301,720,611,934,990,-17,955,-140,-156,356,939,174,-309,999,-472,893,328,-170,-422,48,467,25,372,110,693,744,349,539,347,-59,-466,-293,19,885,60,438,618,504,930,-124,985,-304,-147,748,839,467,-375,-412,-122,715,234,263,119,8,586,119,-55,-488,-107,-269,464,-309,999,882,-403,307,154,-182,8,744,935,-88,-95,139,603,404,991,119,919,825,-237,880,318,-297,344,-27,-8,997,-96,-265,318,-290,162,811,603,-453,223,300,-337,-254,183,307,75,-58,917,629,-422,778,353,986,-137,267,-78,450,-325,732,-288,393,568,910,-38,379,661,-495,915,-299,71,574,321,-98,539,835,701,433,-206,945,920,160,-109,393,918,132,334,623,661,83,13,-210,-130,402,801,-189,22,876,732,746,274,-230,-349,-420,761,-284,893,993,-98,358,76,45,702,228,-119,-422,901,679,971,732,142,137,840,788,-195,14,313,162,-222,304,481,366,-141,546,-304,178,-106,660,-484,873,961,995,607,-175,266,939,424,615,292,-435,-399,-434,-416,486,474,-93,-391,-183,446,-349,-298,-63,396,325,-499,166,866,-67,-453,242,898,-176,-415,405,508,214,691,923,-446,284,365,-494,272,436,361,394,-136,-68,496,353,715,-235,714,563,419,-471,-199,-32,449,230,-284,637,660,858,69,-17,-495,-494,952,356,83,914,574,87,665,299,-289,129,-299,913,999,-282,451,-300,291,744,894,-238,156,-231,144,27,808,250,252,799,295,310,541,-113,368,858,351,585,772,365,182,765,799,9,159,-373,336,522,-336,809,-262,-368,863,-77,890,686,29,-212,309,-108,711,-243,-68,-339,649,-489,352,753,732,5,965,329,-317,948,571,-364,-165,525,-294,10,663,603,-374,-207,-37,927,305,931,196,428,229,783,-335,-330,387,410,327,428,-97,400,430,741,441,-6,419,595,240,824,986,91,486,735,297,-486,263,-173,190,723,-77,64,-335],81712))
