# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:48:28 2017

@author: fang2
"""
import webbrowser
class Movie():
    """This class provides a way to store the films information
    You need to provide title, an simple story abstract, a url of the film poster and
    a url of movie trailer to create the object.
    You can use the method: show_trailer to open the trailer url.
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, move_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = move_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        