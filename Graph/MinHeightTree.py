from collections import defaultdict, Counter, deque
class MinHeightTree:
    """
    Leetcode number 310
    """

    def findMinHeightTrees(self, n, edges):
        # _graph = defaultdict(list)
        # for edge in edges:
        #     _graph[edge[0]].append(edge[1])
        #     _graph[edge[1]].append(edge[0])
        # _max_value = Counter(edges)
        if n ==1:
            return [0]
        _height = defaultdict(list)
        _graph = defaultdict(list)
        for x, y in edges:
            _graph[x].append(y)
            _graph[y].append(x)
        for i in range(n):
            _height[self.mht(i, _graph)].append(i)
        _key = min(_height.keys())
        return _height[_key]

    def mht(self, root, _graph):
        _queue = deque()
        _items_by_level = defaultdict(int)
        _level = 0
        _visited = []
        if root is not None:
            _queue.append(root)
            _queue.append("end")
            _items_by_level[_level] = root
        while _queue:
            _temp = _queue.popleft()
            if _temp != "end" and _temp not in _visited:
                _visited.append(_temp)
                for node in _graph[_temp]:
                    _queue.append(node)
            elif _temp == "end" and _queue:
                _temp_list = []
                for node in _queue:
                    if node not in _visited:
                        _temp_list.append(node)
                if _temp_list:
                    _level += 1
                    _items_by_level[_level] = _temp_list
                _queue.append("end")
            elif _temp == "end" and not _queue:
                break
        return _level
    

min_height = MinHeightTree()
# n = 4
# edges = [[1, 0], [1, 2], [1, 3]]
n=336
edges = [[0,1],[0,2],[2,3],[2,4],[4,5],[5,6],[0,7],[0,8],[1,9],[0,10],[1,11],[11,12],[3,13],[7,14],[7,15],[9,16],[14,17],[8,18],[13,19],[3,20],[2,21],[15,22],[14,23],[21,24],[20,25],[6,26],[24,27],[19,28],[22,29],[15,30],[1,31],[16,32],[12,33],[29,34],[6,35],[33,36],[8,37],[27,38],[6,39],[2,40],[37,41],[7,42],[26,43],[8,44],[25,45],[45,46],[10,47],[38,48],[45,49],[37,50],[36,51],[11,52],[36,53],[17,54],[25,55],[1,56],[8,57],[5,58],[32,59],[17,60],[16,61],[29,62],[3,63],[31,64],[0,65],[63,66],[36,67],[15,68],[51,69],[45,70],[28,71],[31,72],[41,73],[16,74],[2,75],[48,76],[48,77],[55,78],[41,79],[69,80],[74,81],[69,82],[79,83],[20,84],[38,85],[46,86],[7,87],[81,88],[62,89],[61,90],[80,91],[44,92],[9,93],[6,94],[70,95],[88,96],[27,97],[48,98],[91,99],[75,100],[100,101],[13,102],[61,103],[91,104],[99,105],[51,106],[91,107],[23,108],[55,109],[99,110],[90,111],[92,112],[101,113],[100,114],[26,115],[8,116],[92,117],[69,118],[78,119],[41,120],[114,121],[116,122],[61,123],[92,124],[29,125],[80,126],[29,127],[17,128],[66,129],[50,130],[37,131],[85,132],[30,133],[103,134],[91,135],[65,136],[81,137],[2,138],[42,139],[29,140],[16,141],[136,142],[110,143],[31,144],[85,145],[38,146],[88,147],[141,148],[67,149],[88,150],[80,151],[134,152],[0,153],[115,154],[131,155],[1,156],[91,157],[90,158],[11,159],[150,160],[141,161],[125,162],[22,163],[161,164],[86,165],[145,166],[88,167],[38,168],[27,169],[148,170],[105,171],[91,172],[159,173],[31,174],[114,175],[49,176],[137,177],[10,178],[87,179],[117,180],[130,181],[142,182],[10,183],[4,184],[26,185],[180,186],[165,187],[175,188],[110,189],[143,190],[154,191],[13,192],[47,193],[130,194],[79,195],[79,196],[135,197],[146,198],[146,199],[173,200],[82,201],[20,202],[88,203],[127,204],[188,205],[170,206],[24,207],[23,208],[29,209],[155,210],[206,211],[186,212],[137,213],[143,214],[0,215],[30,216],[89,217],[82,218],[107,219],[2,220],[74,221],[37,222],[71,223],[26,224],[199,225],[36,226],[64,227],[211,228],[21,229],[115,230],[196,231],[179,232],[191,233],[194,234],[70,235],[202,236],[141,237],[27,238],[194,239],[36,240],[74,241],[165,242],[31,243],[135,244],[175,245],[244,246],[137,247],[193,248],[232,249],[248,250],[54,251],[114,252],[199,253],[23,254],[231,255],[93,256],[36,257],[187,258],[118,259],[93,260],[147,261],[23,262],[77,263],[171,264],[55,265],[96,266],[102,267],[44,268],[195,269],[45,270],[1,271],[92,272],[122,273],[232,274],[20,275],[159,276],[184,277],[56,278],[242,279],[200,280],[150,281],[107,282],[218,283],[44,284],[222,285],[79,286],[218,287],[228,288],[255,289],[227,290],[105,291],[265,292],[105,293],[146,294],[167,295],[106,296],[262,297],[151,298],[0,299],[150,300],[58,301],[269,302],[250,303],[149,304],[151,305],[201,306],[239,307],[32,308],[83,309],[265,310],[304,311],[288,312],[10,313],[18,314],[177,315],[18,316],[113,317],[152,318],[172,319],[106,320],[166,321],[283,322],[249,323],[251,324],[173,325],[24,326],[264,327],[132,328],[219,329],[326,330],[49,331],[190,332],[44,333],[249,334],[58,335]]
# edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print("min height: for n: {} is {}".format(
    n, min_height.findMinHeightTrees(n, edges)))
