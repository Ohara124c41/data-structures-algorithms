# note: non-ipynb version for redundancy
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix=""):
        results = []
        for ch, child in self.children.items():
            new_suffix = suffix + ch
            if child.is_word:
                results.append(new_suffix)
            results.extend(child.suffixes(new_suffix))
        return results


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node.insert(ch)
            node = node.children[ch]
        node.is_word = True

    def find(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


if __name__ == "__main__":
    trie = Trie()
    words = ["ant", "anthology", "antagonist", "antonym",
             "fun", "function", "factory", "trie", "trigger",
             "trigonometry", "tripod"]
    for w in words:
        trie.insert(w)

    node = trie.find("tri")
    print(sorted(node.suffixes()))  # ['e', 'gger', 'gonometry', 'pod']

    # Edge: prefix not found
    print(trie.find("none"))  # None

    # Edge: empty prefix returns all suffixes from root
    all_suffixes = trie.root.suffixes()
    print(len(all_suffixes) == len(words))  # True
