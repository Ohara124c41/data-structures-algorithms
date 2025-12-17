##### note: this information also in the trie nb

Blockchain implemented as a singly linked list of blocks. Each block stores timestamp, data, previous hash, and its own hash (SHA-256 of timestamp+data+prev). Append adds to tail, linking via previous_hash. Time per append: O(1). Space: O(n) for n blocks.
