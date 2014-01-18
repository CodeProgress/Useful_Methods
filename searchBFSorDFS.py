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
    
    