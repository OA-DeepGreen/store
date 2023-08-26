import os
import subprocess
import re
import shutil
import time

class MoveToTree:
    def __init__(self, storage_folder, new_storage_folder, dir_listing = "/tmp/jperstore_dir.txt", create_new_listing = False, dry_run=True):
        self.depth = 2
        self.length = 2
        self.storage_folder = storage_folder.rstrip('/')
        self.new_storage_folder = new_storage_folder.rstrip('/')
        self.create_new_listing = create_new_listing
        self.dir_listing = dir_listing
        self.dry_run = dry_run
        self.dir_move_log = "/tmp/jperstore_dir.log"

    def move_directories(self):
        start_time = time.time()
        self.get_directories_to_move()
        if not os.path.isfile(self.dir_listing):
            print("File with list of directories to move is missing")
            return False

        pattern = re.compile(f"^{self.storage_folder}[/]")
        if self.dry_run:
            log_file = open(self.dir_move_log, 'w')
        count = 1
        with open(self.dir_listing, 'r') as dir_file:
            for line in dir_file:
                dir_path = line.strip('\n')
                print(f"Processing {count}: {dir_path}")
                this_dir = pattern.sub('', dir_path)
                status, new_dir, dest = self.move_directory(dir_path, this_dir)
                if status and self.dry_run:
                    log_file.write(f"source: {dir_path} | new dirs: {new_dir} | dest: {dest}\n")
                count += 1

        if self.dry_run:
            log_file.close()
        print(f"Number of directories moved: {count}")
        print("--- %s seconds ---" % (time.time() - start_time))
        return True

    def get_directories_to_move(self):
        if not self.create_new_listing:
            return
        if os.path.isfile(self.dir_listing):
            os.remove(self.dir_listing)
        command = f"find {self.storage_folder} -maxdepth 1 >> {self.dir_listing}"
        subprocess.run(command, shell=True)

    def new_directories(self, first_dir):
        chunks = [first_dir[i:i + self.length] for i in range(0, len(first_dir), self.length)]
        tree = chunks[0:min(self.depth, len(chunks))]
        tree_path = os.path.join(self.new_storage_folder, *tree)
        return tree_path

    def move_directory(self, dir_path, this_dir):
        if this_dir == self.storage_folder:
            return False, None, None
        if len(this_dir.strip()) == 0:
            # parent dir
            print(f"Not processing {this_dir}")
            return False, None, None
        if this_dir.startswith('.'):
            # hidden dir
            print(f"Not processing {this_dir}")
            return False, None, None
        if not os.path.exists(dir_path):
            print(f"Directory does not exist. Not processing {dir_path}")
            return False, None, None

        new_dir_path = self.new_directories(this_dir)
        dest = os.path.join(new_dir_path, this_dir)
        if not self.dry_run:
            if not os.path.exists(new_dir_path):
                os.makedirs(new_dir_path)
            shutil.move(dir_path, dest)
        return True, new_dir_path, dest


if __name__ == "__main__":
    sf = "/data/green/jperstore"
    new_sf = "/data/green/jperstore_v2"
    mt = MoveToTree(sf, new_sf, create_new_listing=False, dry_run=True)
    mt.move_directories()

