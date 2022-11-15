class Rating:
    userId: int
    movieId: int
    rating: str
    timestamp: int

    def __init__(self, uid: int, mid: int, rating: str, timestamp: int):
        self.userId = uid
        self.movieId = mid
        self.rating = rating
        self.timestamp = timestamp
