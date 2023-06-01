from multiprocessing import Process, Manager, Lock

def dfs(graph, node, visited, lock):
    visited.add(node)

    for next_node in graph[node]:
        if next_node not in visited:
            dfs(graph, next_node, visited, lock)

def para_dfs(graph, node, shared_list, lock):
    print('Executing parallel dfs')
    visited = set()

    dfs(graph, node, visited, lock)

    with lock:
        shared_list.extend(visited)

if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['C']
    }

    root = 'A'

    with Manager() as manager:
        shared_list = manager.list()
        lock = Lock()
        process_list = []

        
        search_process = Process(target=para_dfs, args=(graph, root, shared_list, lock))
        search_process.start()
        process_list.append(search_process)

        for process in process_list:
            process.join()

        print(list(shared_list))
