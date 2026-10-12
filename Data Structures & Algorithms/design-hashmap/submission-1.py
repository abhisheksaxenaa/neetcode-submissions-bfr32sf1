class Link:
    def __init__(self, key = -1, val = -1, n = None):
        self.key = key
        self.val = val
        self.next = n

class MyHashMap:

    # def __init__(self):
    #     self.m = [-1] * 1000001

    # def put(self, key: int, value: int) -> None:
    #     self.m[key] = value

    # def get(self, key: int) -> int:
    #     return self.m[key]

    # def remove(self, key: int) -> None:
    #     self.m[key] = -1

    def __init__(self):
        # Creating map list of 1000 unique Links
        self.m = [Link() for _ in range(1000)]

    def hash(self, key: int) -> int:
        return key % len(self.m)

    def put(self, key: int, value: int) -> None:
        cur = self.m[self.hash(key)]
        # got the current pointer
        while cur.next:
            # possibly the existing key
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = Link(key, value)

    def get(self, key: int) -> int:
        cur = self.m[self.hash(key)]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.m[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)