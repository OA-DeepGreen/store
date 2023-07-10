from pathlib import Path

class StorageTree:
    def __init__(self, storage_folder):
        self.storage_folder = storage_folder
        self.depth = 2
        self.length = 2

    def tree_path(self, given_path):
        # given path has id greater than 6 characters
        # given_path: '985882921/your/path/file.txt'
        # new_path: self.storage_folder/985/882/985882921/your/path/file.txt

        # given path starts with .
        # given_path: './985882921/your/path/file.txt'
        # new_path: self.storage_folder/985/882/985882921/your/path/file.txt

        # given path has id of 6 characters
        # given_path: '985882/your/path/file.txt'
        #  new_path: self.storage_folder/985/882/985882/your/path/file.txt

        # given path has id of 4 characters
        # given_path: '9858/your/path/file.txt'
        # new_path: self.storage_folder/985/8/9858/your/path/file.txt

        # given path has id of 3 characters
        # given_path: '985/your/path/file.txt'
        # new_path: self.storage_folder/985/985/your/path/file.txt

        # given path has id of 2 characters
        # given_path: '98/your/path/file.txt'
        # new_path: self.storage_folder/98/98/your/path/file.txt
        path_parts = Path(given_path)
        first_dir = path_parts.parts[0]
        chunks = [first_dir[i:i + self.length] for i in range(0, len(first_dir), self.length)]
        tree = chunks[0:min(self.depth, len(chunks))]
        tree_path = Path(self.storage_folder, *tree, *path_parts.parts)
        return str(tree_path)



