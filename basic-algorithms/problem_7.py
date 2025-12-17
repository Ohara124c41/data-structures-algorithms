class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = {}
        self.handler = handler

    def insert(self, part):
        if part not in self.children:
            self.children[part] = RouteTrieNode()


class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode(root_handler)

    def insert(self, parts, handler):
        node = self.root
        for part in parts:
            node.insert(part)
            node = node.children[part]
        node.handler = handler

    def find(self, parts):
        node = self.root
        for part in parts:
            if part not in node.children:
                return None
            node = node.children[part]
        return node.handler


class Router:
    def __init__(self, root_handler, not_found_handler=None):
        self.trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        parts = self.split_path(path)
        self.trie.insert(parts, handler)

    def lookup(self, path):
        parts = self.split_path(path)
        handler = self.trie.find(parts)
        if handler is None:
            return self.not_found_handler
        return handler

    def split_path(self, path):
        if path is None or path == "":
            return []
        path = path.strip("/")
        if path == "":
            return []
        return path.split("/")


if __name__ == "__main__":
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    print(router.lookup("/"))  # root handler
    print(router.lookup("/home"))  # not found handler
    print(router.lookup("/home/about"))  # about handler
    print(router.lookup("/home/about/"))  # about handler
    print(router.lookup("/home/about/me"))  # not found handler

    # Edge: empty path
    print(router.lookup(""))  # root handler

    # Edge: None path
    print(router.lookup(None))  # not found handler
