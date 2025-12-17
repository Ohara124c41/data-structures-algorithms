import hashlib
from datetime import datetime


class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.utcnow()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        content = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode("utf-8")
        sha.update(content)
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        prev_hash = self.tail.hash if self.tail else None
        new_block = Block(data, prev_hash)
        if self.head is None:
            self.head = new_block
        else:
            self.tail.next = new_block
        self.tail = new_block

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append((node.data, node.hash, node.previous_hash))
            node = node.next
        return out


if __name__ == "__main__":
    chain = Blockchain()
    chain.append("genesis")
    chain.append("block2")
    chain.append("block3")
    blocks = chain.to_list()
    print(len(blocks))  # 3
    print(blocks[1][2] == blocks[0][1])  # True

    # Edge: empty chain append once
    chain2 = Blockchain()
    chain2.append("only")
    print(chain2.head.previous_hash is None)  # True

    # Edge: data as empty string
    chain.append("")
    print(chain.tail.data == "")  # True
