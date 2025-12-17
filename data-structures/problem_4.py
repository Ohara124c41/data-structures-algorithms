class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    if user is None or group is None:
        return False
    if user in group.get_users():
        return True
    for sub in group.get_groups():
        if is_user_in_group(user, sub):
            return True
    return False


if __name__ == "__main__":
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group("sub_child_user", parent))  # True
    print(is_user_in_group("ghost", parent))  # False

    # Edge: None inputs
    print(is_user_in_group(None, parent))  # False

    # Edge: user directly in parent
    parent.add_user("root_user")
    print(is_user_in_group("root_user", parent))  # True
