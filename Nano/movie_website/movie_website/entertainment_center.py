# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:50:47 2017

@author: fang2

You can create new Movie object in this file， the movie object need title, story abstract, image url of poster and url of the trailer 
"""

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story about the boy's toy",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=nCqtQLmJTl0")
the_grandmaster = media.Movie("The Grandmaster",
                              "A story about Chinese gong fu",
                              "https://upload.wikimedia.org/wikipedia/zh/c/c9/The_Grand_Masters_poster.jpg",
                              "https://youtu.be/w5fgfUbS8cQ?list=PLvj-ZlkoqlJTcOeWePuHZoi6Ct_L2mcpt")
green_snake = media.Movie("Green Snake",
                         "A traditional Chinese myth",
                         "https://upload.wikimedia.org/wikipedia/zh/e/e2/Green_Snake.jpg",
                         "https://www.youtube.com/watch?v=rSrdmgYUrL8")
interstellar = media.Movie("Interstellar",
                           "A story about human courage",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=Rt2LHkSwdPQ")
the_martian = media.Movie("The Martian",
                          "A story show how can survive just by eating potato",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")
the_danishgirl=media.Movie("The Danish Girl",
                           "A movie about beauty and courage",
                           "https://upload.wikimedia.org/wikipedia/en/f/f2/The_Danish_Girl_%28film%29_poster.jpg",
                           "https://www.youtube.com/watch?v=d88APYIGkjk")

movies = [toy_story, the_grandmaster,green_snake, interstellar, the_martian, the_danishgirl]
fresh_tomatoes.open_movies_page(movies)    #This function is to generate html page of all movies

