class FileCreator:
    def __init__(self, filename):
        self.filename = filename

    def create_file(self, content=""):
        try:
            with open(self.filename, "w") as file:
                file.write(content)
            print(f"File '{self.filename}' created successfully.")
        except Exception as e:
            print(f"Error creating file: {e}")

# Example usage:
if __name__ == "__main__":
    file_creator = FileCreator("example.txt")
    file_creator.create_file("Hello, world!")
