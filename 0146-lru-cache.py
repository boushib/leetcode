class Node:

    def __init__(self, key, val=0, _prev=None, _next=None):
        self.val = val
        self.prev = _prev
        self.next = _next
        self.key = key


class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.node_map = {}  # (key, node)
        # least and most recently used nodes
        self.lru = Node(-1)
        self.mru = Node(-1)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def append(self, node):
        prev, next = self.mru.prev, self.mru
        node.prev = prev
        node.next = next
        prev.next = node
        next.prev = node

    def remove(self, node):
        next, prev = node.next, node.prev
        next.prev, prev.next = prev, next

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1

        node = self.node_map[key]
        self.remove(node)
        self.append(node)
        return node.val

    def put(self, key: int, val: int) -> None:
        # update or add the k,v pair
        # evict LRU element if needed
        if key in self.node_map:
            node = self.node_map[key]
            node.val = val
            self.remove(node)
            self.append(node)
        else:
            node = Node(key, val)
            self.append(node)
            self.node_map[key] = node

            if len(self.node_map) > self.capacity:
                lru = self.lru.next
                self.remove(lru)
                del self.node_map[lru.key]

    def __str__(self):
        res = ""

        for k, node in self.node_map.items():
            res += f"{k}:{node.val} "
        return "{ " + res + "}"
