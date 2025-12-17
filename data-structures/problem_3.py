import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_encoding(data):
    if data == "":
        return "", None

    freq = {}
    for ch in data:
        freq[ch] = freq.get(ch, 0) + 1

    heap = [Node(ch, f) for ch, f in freq.items()]
    heapq.heapify(heap)

    if len(heap) == 1:
        root = heap[0]
        codes = {root.char: "0"}
    else:
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            parent = Node(None, left.freq + right.freq)
            parent.left = left
            parent.right = right
            heapq.heappush(heap, parent)
        root = heap[0]
        codes = {}
        _generate_codes(root, "", codes)

    encoded = "".join(codes[ch] for ch in data)
    return encoded, root


def _generate_codes(node, prefix, codes):
    if node.char is not None:
        codes[node.char] = prefix
        return
    _generate_codes(node.left, prefix + "0", codes)
    _generate_codes(node.right, prefix + "1", codes)


def huffman_decoding(data, tree):
    if tree is None or data == "":
        return ""
    decoded = []
    node = tree
    for bit in data:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            decoded.append(node.char)
            node = tree
    return "".join(decoded)


if __name__ == "__main__":
    sentence = "The bird is the word"
    enc, tree = huffman_encoding(sentence)
    print(len(enc) > 0)  # True
    dec = huffman_decoding(enc, tree)
    print(dec)  # The bird is the word

    # Edge: empty string
    enc2, tree2 = huffman_encoding("")
    print(enc2)  # ""
    print(huffman_decoding(enc2, tree2))  # ""

    # Edge: single repeated char
    enc3, tree3 = huffman_encoding("aaaaa")
    print(enc3)  # 00000
    print(huffman_decoding(enc3, tree3))  # aaaaa
