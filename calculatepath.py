from typing import Tuple, List, Dict
from queue import Queue
n = 3
end = (True,n,n)
start = (False,0,0)

def valid(state: tuple):
    return 0 <= state[1] <= n and 0 <= state[2] <= n and (state[1] == state[2] or state[1] % n is 0)
        

def neighbours(curr : tuple):
    d = -1 if curr[0] else 1
    other = not curr[0] 
    yield from (state for state in (
        (other, curr[1]+d, curr[2]),
        (other, curr[1], curr[2]+d),
        (other, curr[1]+d, curr[2]+d),
        (other, curr[1]+(2*d), curr[2]),
        (other, curr[1], curr[2]+(2*d)),
     ) if valid(state))

adjList = dict()
def path(curr, prev):
    while curr is not start:
        yield curr
        curr = prev[curr]
    yield start

def stateToString(state):
    return f"{n-state[1]}✝{n-state[2]}☺{('~>' if state[0] else '<~')}{state[1]}✝{state[2]}☺"
    
adjList = {state:list(neighbours(state)) for i in range(0,n+1) for j in range(0,n+1) for state in ((True,i,j),(False,i,j)) if valid(state)}

nodesToProcess =  Queue()
nodesToProcess.put(start)
visited = set()
prev = dict()
while not nodesToProcess.empty():
    node = nodesToProcess.get()
    if node in visited:
        continue
    visited.add(node)
    for x in adjList[node]:
        if x not in prev:
            prev[x] = node
        if x not in visited:
            nodesToProcess.put(x)

correct_path = list(reversed([x for x in path(end,prev)]))
correct_edges = [tuple(sorted((correct_path[i],correct_path[i+1]))) for i in range(len(correct_path)-1)]

if __name__ == "__main__":
    for state in correct_path:
        print(stateToString(state))