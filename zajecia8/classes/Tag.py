class Tag:
    userId: int
    movieId: int
    tag: str
    timestamp: int

    def __init__(self, uid: int, mid: int, tag: str, timestamp: int):
        self.userId = uid
        self.movieId = mid
        self.tag = tag
        self.timestamp = timestamp
