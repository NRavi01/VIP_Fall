class Trip_demand:
    def __init__(self, name, start, end, demand):
        self.id = name
        self.start = start
        self.end = end
        self.demand = demand
    def get_name(self):
        return self.id
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def get_demand(self):
        return self.demand