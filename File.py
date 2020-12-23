class File:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_data(self):
        fs = open(self.file_name, 'r')
        return fs.readlines()

    def save_data(self, content):
        with open(self.file_name, "w") as output_file:
            output_file.write(content)
