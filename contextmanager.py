class SafeFileWriter:
    def __init__(self, filename, mode="w"):
        # file name to open
        self.filename = filename 
        # mode with "w" to write
        self.mode = mode
        # placeholder for the file object (at this point when initlizing, it's none)
        self.file = None
#entering the context
    def __enter__(self):

        # If you do self.filename instead of self.file
        # You replace the string file name with a file object
        # you lose the file name foreveer 
        self.file = open(self.filename, self.mode)
        print("File opened")
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            print("File closed")
        if exc_type is ValueError:
            print(f"Handled Error, {exc_value}")
            return True

        return False

with SafeFileWriter("test.txt") as f:
    f.write("It finally works!\n")