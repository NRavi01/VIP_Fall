class Link:
    def __init__(self, name, start, end) -> None:
        self.id = name
        self.start = start
        self.end = end
    def get_name(self):
        return self.id
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end