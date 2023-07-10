import os
import subprocess
import re
import shutil

class MoveToTree:
    def __init__(self, storage_folder, dir_listing = "/tmp/jperstore_dir.txt", dry_run=True):
        self.depth = 2
        self.length = 2
        self.storage_folder = storage_folder.rstrip('/')
        self.dir_listing = dir_listing
        self.dry_run = dry_run
        self.dir_move_log = "/tmp/jperstore_dir.log"

    def move_directories(self):
        self.get_directories_to_move()
        if not os.path.isfile(self.dir_listing):
            return False

        pattern = re.compile(f"^{self.storage_folder}[/]")
        if self.dry_run:
            log_file = open(self.dir_move_log, 'w')
        count = 1
        with open(self.dir_listing, 'r') as dir_file:
            for dir_path in dir_file:
                this_path = dir_path.strip('\n')
                print(f"Processing {count}: {this_path}")
                dir = pattern.sub('', this_path)
                status, new_dir, dest = self.move_directory(this_path, dir)
                if status and self.dry_run:
                    log_file.writeline(f"source: {dir_path} | new dirs: {new_dir} | dest: {dest}")
                count += 1

        if self.dry_run:
            log_file.close()
        return True

    def get_directories_to_move(self):
        if os.path.isfile(self.dir_listing):
            os.remove(self.dir_listing)
        command = f"find {self.storage_folder} -maxdepth 1 >> {self.dir_listing}"
        subprocess.run(command, shell=True)

    def new_directories(self, first_dir):
        chunks = [first_dir[i:i + self.length] for i in range(0, len(first_dir), self.length)]
        tree = chunks[0:min(self.depth, len(chunks))]
        tree_path = os.path.join(self.storage_folder, *tree)
        return tree_path

    def move_directory(self, dir_path, dir):
        if dir == self.storage_folder:
            return False, None, None
        if len(dir.strip()) == 0:
            # parent dir
            print(f"Not processing {dir}")
            return False, None, None
        if dir.startswith('.'):
            # hidden dir
            print(f"Not processing {dir}")
            return False, None, None

        new_dir = self.new_directories(dir)
        dest = os.path.join(new_dir, dir)
        if not self.dry_run:
            os.makedirs(new_dir)
            shutil.move(dir_path, dest)
        return True, new_dir, dest



# from lib.move_to_tree import MoveToTree
# sf = "/home/anusha/Documents/src/deepgreen/jperstore_modified/"
# mt = MoveToTree(sf)
# mt.move_directories()

