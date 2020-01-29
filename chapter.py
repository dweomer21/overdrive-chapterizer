from timestamp import Timestamp


class Chapter(object):
    def __init__(self, title: str, start: Timestamp, end: Timestamp):
        self.title = title
        self.start = start
        self.end = end
