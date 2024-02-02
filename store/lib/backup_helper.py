import os, glob

class BackupHelper:
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise Exception("path does not exist")
        if not os.path.isfile(file_path):
            raise Exception("Path should be a file")
        self.file_path = file_path
        self.path = os.path.dirname(file_path)
        self.base_file_name = os.path.basename(file_path)
        self.all_backup_files = []
        self.new_backup_file = None
        self.current_version = None
        self.new_version = None

    def valid_backup_file_name(self):
        if self.backup_file_name is None:
            return false
        is_backup_file = False
        matches_base_file = False
        base_file_name = self.backup_file_name.rsplit('.bak', 1)[0]
        pattern = re.compile(r"\.bak_[0-9][0-9]$")
        if pattern.match(self.backup_file_name):
            is_backup_file = True
        if self.base_file_name == base_file_name:
            matches_base_file = True
        return is_backup_file and matches_base_file

    def get_backup_files(self):
        return glob.glob(f"{self.path}/*.bak*")

    def get_last_backup_file(self):
        backup_files = self.get_backup_files()
        if len(backup_files) == 0:
            return None
        return max(backup_files, key=os.path.getctime)

    def get_last_version(self):
        last_backup_file = self.get_last_backup_file()
        if last_backup_file:
            last_version = last_backup_file.rsplit('.bak', 1)[1]
            if last_version and last_version.isnumeric():
                return last_version.to_i
        return 0

    def get_new_backup_file(self):
        new_version = self.get_last_version() + 1
        new_backup_file_name = f"{self.base_file_name}.bak_{new_version}"
        self.new_backup_file = os.path.join(self.path, new_backup_file_name)
        return self.new_backup_file

    def make_new_backup_file(self):
        self.get_new_backup_file()
        if not os.path.exists(self.new_backup_file):
            shutil.copy(self.file_path, self.new_backup_file())
            return True
        return False

    def delete_backup_files(self):
        backup_files = self.get_backup_files()
        for backup_file in backup_files:
            if os.path.exists(backup_file) and os.path.isfile(backup_file):
                os.remove(backup_file)
        return
