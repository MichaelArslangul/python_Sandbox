import copy, random

def contract(ver, e):
        while len(ver) > 2:
                ind = random.randrange(0, len(e))
                [u, v] = e.pop(ind)
                ver.remove(v)
                newEdge= []
                for i in range(len(e)):
                        if e[i][0] == v:
                                e[i][0] = u
                        elif e[i][1] == v:
                                e[i][1] = u
                        if e[i][0] != e[i][1]:
                                newEdge.append(e[i])
                e = newEdge

        return len(e)


with open('kargerMinCut.txt', 'r') as infile:
        adjMat, edges, vertices = [], [], []
        for line in infile.readlines():
                adjMat.append(line)


for i in range(len(adjMat)):
               s = adjMat[i].split()
               vertices.append(int(s[0]))
               for j in range(1, len(s)):
                       if [int(s[0]), int(s[j])] not in edges:
                                edges.append([int(s[0]), int(s[j])])


result = []

for i in range(1000):
        v = copy.deepcopy(vertices)
        e = copy.deepcopy(edges)
        r = contract(v, e)
        result.append(r)

print(min(result))
