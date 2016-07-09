#The webbrowser module provides an interface to display Web-based documents to users.

import webbrowser

#the datetime module provides methods to work with date/time variables
from datetime import datetime


class Movie():
    """ This class provides a way to store movie related information including movie
title, movie synopsis, poster URL and a YouTube link to the movie trailer """

    # The __init__() function initializes the instances of the class Movie
    # with the given values for movie title, storyline, poster image and youtube trailer
        
    def __init__(self,movie_title,movie_storyline,poster_image,youtube_trailer,release_date,directors):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
        self.release_date = datetime.strptime(release_date, '%m/%d/%Y') # storing the release_date in the format month/day/year
        self.directors = directors
        

    # The show_trailer() function:
    #takes the youtube_url as an argument and
    #opens the url in a new browser window

    def show_trailer(self):
        webbrowser.open_new(self.trailer_youtube_url)

        
