
# import the fresh_tomatoes module that helps to generate a website that displays a list of movies,

import fresh_tomatoes

# import the media module which has the class definition for the Movie class

import media

# Create multiple instances of the Movie class to represent a list of favorite movies

#create an instance of the movie Zootopia
zootopia = media.Movie("Zootopia",
                       "In a city of anthropomorphic animals, a rookie bunny cop and a cynical con artist fox must work together to uncover a conspiracy.",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "https://youtu.be/5nP9hU8eUfE",
                       "03/04/2016",
                       "Byron Howard, Rich Moore, Jared Bush")

#create an instance of the movie Hotel Transylvania 2
hotel_transylvania_2 = media.Movie("Hotel Transylvania 2",
                                 "Dracula and his friends try to bring out the monster in his half human, half vampire grandson in order to keep Mavis from leaving the hotel.",
                                 "https://upload.wikimedia.org/wikipedia/en/5/5d/Hotel_Transylvania_2_poster.jpg",
                                 "https://youtu.be/Zb04diozp1Q",
                                 "09/25/2015",
                                 "Genndy Tartakovsky")

#create an instance of the movie The Secret Life of Pets
life_of_pets = media.Movie("The Secret Life of Pets",
                           "That's when the pets of every stripe, fur and feather begin their own nine-to-five routine.",
                           "https://upload.wikimedia.org/wikipedia/en/6/64/The_Secret_Life_of_Pets_poster.jpg",
                           "https://youtu.be/i-80SGWfEjM",
                           "07/08/2016",
                           "Chris Renaud, Yarrow Cheney")

#create an instance of the movie Finding Dory
finding_dory = media.Movie("Finding Dory",
                           "'Finding Dory' reunites the friendly-but-forgetful blue tang fish with her loved ones.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Finding_Dory.jpg/220px-Finding_Dory.jpg",
                           "https://youtu.be/JhvrQeY3doI",
                           "06/17/2016",
                           " Andrew Stanton, Angus MacLane")

#create an instance of the Angry Birds Movie
angry_bird = media.Movie("The Angry Birds Movie",
                         "The Angry Birds Movie, we'll finally find out why the birds are so angry.",
                         "https://upload.wikimedia.org/wikipedia/en/f/f9/The_Angry_Birds_Movie_poster.png",
                         "https://youtu.be/1U2DKKqxHgE",
                         "05/20/2016",
                         "Fergal Reilly, Clay Kaytis")

#create an instance of the movie Minions
minions = media.Movie("Minions",
                      "Minions live to serve, but find themselves working for a continual series of unsuccessful masters.",
                      "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",
                      "https://youtu.be/P9-FCC6I7u0",
                      "07/10/2015",
                      "Pierre Coffin, Kyle Balda")

#create an instance of the movie Inside Out
inside_out = media.Movie("Inside Out",
                         "The film is set in the mind of a young girl where five personified emotions try to lead her through life.",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_(2015_film)_poster.jpg",
                         "https://youtu.be/yRUAzGQ3nSY",
                         "06/19/2016",
                         "Pete Docter, Ronnie del Carmen")

#create an instance of the movie The Jungle Book
jungle_book = media.Movie("The Jungle Book",
                          "Raised by a family of wolves since birth, Mowgli must leave the only home he's ever known when the fearsome tiger Shere Khan unleashes his mighty roar.",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/a/a4/The_Jungle_Book_(2016).jpg/220px-The_Jungle_Book_(2016).jpg",
                          "https://youtu.be/owgrkAQ-Log",
                          "04/15/2016",
                          "Jon Favreau")

#create an instance of the movie Frozen
frozen = media.Movie("Frozen",
                     "When their kingdom becomes trapped in perpetual winter, fearless Anna joins forces with mountaineer Kristoff and his reindeer sidekick to find Anna's sister.",
                     "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_(2013_film)_poster.jpg",
                     "https://youtu.be/TbQm5doF_Uc",
                     "11/27/2013",
                     "Chris Buck, Jennifer Lee")

#create an instance of the Peanuts Movie 
peanuts_movie = media.Movie("The Peanuts Movie",
                            "Life always seems complicated for good ol' Charlie Brown, the boy who always tries his best against seemingly impossible odds.",
                            "https://upload.wikimedia.org/wikipedia/en/7/77/Peanuts_2015.jpg",
                            "https://youtu.be/qI34nBlJxP8",
                            "11/06/2015",
                            "Steve Martino")

# create a python list named movies for the instances of the Movie class created.
# The list object will be passed as argument to the open_movies_page function 

movies = [zootopia, hotel_transylvania_2 , life_of_pets , finding_dory , angry_bird , minions , inside_out , jungle_book , frozen , peanuts_movie]

# calling the open_movies_page function in the fresh_tomatoes module with the list of movies as argument
# The open_movies_page function creates an HTML file which visualizes the list of movies in the list.

fresh_tomatoes.open_movies_page(movies)
