"""Reachability"""
import json
def main():
    """Demo"""
    graph, start = json.loads(input().replace("'", '"')), input()
    storage, check = {start}, {start}
    ans = []
    while check:
        current = check.pop()
        _ = [check.add(i) for i in graph[current] if i not in ans]
        storage.update(graph[current])
        ans.append(current)
    print(sorted(list(storage)))
main()
