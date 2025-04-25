from collections import deque

# Using HashMap to create a graph
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print(graph)

# BFS is implement using a deque(FIFO)
def BFS(target, root="you"):
    search_queue = deque()
    search_queue += graph[root]
    # To avoid double lined relationship causing infinite loop
    searched = []
    # When the queue is not empty
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person is target:
                print("Target found")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


BFS(target="thom", root="you")
