class Movie:
    id: int
    title: str
    genres: str

    def __init__(self, mid: int, title: str, genres: str):
        self.id = mid
        self.title = title
        self.genres = genres

