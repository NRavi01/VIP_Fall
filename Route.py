class Route:
    def __init__(self, name, links, start, end) -> None:
        self.id = name
        self.links = links
        self.start = start
        self.end = end
    def get_name(self):
        return self.id
    def get_links(self):
        return self.links
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end