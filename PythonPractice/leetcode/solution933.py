class RecentCounter:

    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        self.pings.append(t)
        for index, time in enumerate(self.pings):
            if t - 3000 <= time:
                break
        self.pings = self.pings[index:]
        return len(self.pings)