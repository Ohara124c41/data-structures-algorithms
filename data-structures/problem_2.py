import os


def find_files(suffix, path):
    results = []
    if not os.path.exists(path):
        return results
    if os.path.isfile(path):
        if path.endswith(suffix):
            results.append(path)
        return results
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        results.extend(find_files(suffix, full_path))
    return results


if __name__ == "__main__":
    import tempfile
    import shutil

    temp_dir = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(temp_dir, "subdir"))
        file1 = os.path.join(temp_dir, "a.c")
        file2 = os.path.join(temp_dir, "b.txt")
        file3 = os.path.join(temp_dir, "subdir", "c.c")
        open(file1, "w").close()
        open(file2, "w").close()
        open(file3, "w").close()

        print(sorted(find_files(".c", temp_dir)))  # [file1, file3]

        # Edge: non-existing path
        print(find_files(".c", "/non/exist"))  # []

        # Edge: directory with no matches
        print(find_files(".py", temp_dir))  # []
    finally:
        shutil.rmtree(temp_dir)
