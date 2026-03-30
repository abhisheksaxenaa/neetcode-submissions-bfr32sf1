import json

class PrefixTree:

    def __init__(self):
        self.trie = self._createNode(None)

    def _createNode(self, s):
        node = {
            "key": s,
            "children": {},
            "end": False
        }
        return node

    def insert(self, word: str) -> None:
        head = self.trie
        for i,w in enumerate(list(word)):
            child = head.get("children").get(w, None)
            if child is None:
                child = self._createNode(w)
            if len(word) - 1 == i:
                child["end"] = True
            head.get("children")[w] = child
            head = child
        # print(json.dumps(self.trie))

    def find(self, word: str):
        head = self.trie
        for w in list(word):
            child = head.get("children").get(w, None)
            if child is None:
                return None
            head = child
        return head

    def search(self, word: str) -> bool:
        # accioabs comment
        # using common method to find final node
        # if there is a node and its end key is True
        # then it's the end of a word
        node = self.find(word)
        if node == None:
            return False
        return node.get("end")


    def startsWith(self, prefix: str) -> bool:
        # accioabs comment
        # using common method to find final node
        # if there is a node then startsWith makes sense
        node = self.find(prefix)
        return node is not None
        
        