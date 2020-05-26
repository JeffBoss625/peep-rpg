
class Hector:
    def __init__(self):
        self.args = []

    def print(self, *args):
        self.args.extend(args)

class Out:
    def print(self, *args):
        print(*args)