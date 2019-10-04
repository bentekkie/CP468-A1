from typing import Tuple, List, Dict, Set
from queue import Queue
n = 3
State = Tuple[bool,int,int]
end : State = (True,n,n)
start : State = (False,0,0)

def valid(state: State) -> bool:
    return 0 <= state[1] <= n and 0 <= state[2] <= n and (state[1] == state[2] or state[1] % n is 0)
        

def neighbours(curr : State) -> List[State]:
    d = -1 if curr[0] else 1
    other = not curr[0] 
    return [state for state in 
        ((other, curr[1]+d, curr[2]),
        (other, curr[1], curr[2]+d),
        (other, curr[1]+d, curr[2]+d),
        (other, curr[1]+(2*d), curr[2]),
        (other, curr[1], curr[2]+(2*d)))
        if valid(state)]

adjList :  Dict[State,List[State]] = dict()
def path(curr : State, prev : Dict[State,State]):
    while curr is not start:
        yield curr
        curr = prev[curr]
    yield start

def stateToString(state : State):
    return f"{n-state[1]}✝{n-state[2]}☺{('~V' if state[0] else 'V~')}{state[1]}✝{state[2]}☺"

def edgeToString(edge : Tuple[State,State]):
    return f"\\{abs(edge[0][1]-edge[1][1])}✝{abs(edge[0][2]-edge[1][2])}☺/"

allStates = {(boat,m,c) for boat in [True,False] for m in range(4) for c in range(4) if valid((boat,m,c))}

nodesToProcess : "Queue[State]" =  Queue()
nodesToProcess.put(start)
visited : Set[State] = set()
prev : Dict[State,State] = dict()
while not nodesToProcess.empty():
    node = nodesToProcess.get()
    if node in visited:
        continue
    visited.add(node)
    adjList[node] = neighbours(node)
    for x in adjList[node]:
        if x not in prev:
            prev[x] = node
        if x not in visited:
            nodesToProcess.put(x)

correct_path = list(reversed([x for x in path(end,prev)]))
correct_edges = [tuple(sorted((correct_path[i],correct_path[i+1]))) for i in range(len(correct_path)-1)]
if __name__ == "__main__":
    prevState = None
    for state in correct_path:
        print(stateToString(state))