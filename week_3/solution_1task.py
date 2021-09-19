class FileReader:
    def __init__(self, request):
        self.request = request
    def read(self):
        try:
            with open(self.request, "r") as f:
                return f.read()
        except FileNotFoundError:
            return ""