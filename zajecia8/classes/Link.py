class Link:
    movieId: int
    imdbId: int
    tmdbId: int

    def __init__(self, mid: int, iid: int, tid: int):
        self.id = mid
        self.imdbId = iid
        self.tmdbId = tid
