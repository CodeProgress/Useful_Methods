#BFS and DFS

import Queue

def search(start, successors, is_goal, search = "BFS"):
    """search:  "DFS" or "BFS"
    returns path if path, False if no path exists
    (modeled after exercise on Udacity)
    """
    if is_goal(start):
        return True
    visited = set()
    if search == "BFS":
        q = Queue.Queue() #BFS
    elif search == "DFS":
        q = Queue.LifoQueue() #DFS Note, DFS will not guarantee shortest path 
    else:
        return "Invalid search parameter"
        
    q.put([start])
    while q:
        current = q.get()
        
        if is_goal(current[-1]):
            return current
        
        successor = successors(current[-1])
        for i in successor:
            if i not in visited:
                visited.add(i)
                q.put(current + [successor[i]] + [i])
    print "No path exists"
    return False
    

# --------------
# Example
#
# From a state, the only possible successors are i+1 and i-1. Given
# a starting integer, find the shortest path to -5. 
# 
# (add print statement to above

def is_goal(state):
    if state == -5:
        return True
    else: 
        return False
    
def successors(state):
    if abs(state) > 10:
        return {}
    successors = {state + 1: '->',
                  state - 1: '<-'}
    return successors

print search(4, successors, is_goal)


