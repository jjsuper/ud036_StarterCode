class Movie():
    """ This class provides a way to store movie

    Attributes:
	    title (str): This is the title of the movie.
        poster_image_url (str): This is the url of the movie poster.
        trailer_youtube_url (str): This is the url of the movie trailer.
    """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
