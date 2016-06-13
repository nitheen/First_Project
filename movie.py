import webbrowser

class Movie():

    def __init__(self, movie_name, trailer_link):
        self.name = movie_name
        self.link = trailer_link

    def play_trailer(self):
        webbrowser.open(self.link)
