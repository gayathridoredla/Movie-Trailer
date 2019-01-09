import Trailer
import ex1
resugurram=ex1.My("Resugurram",
                    "He decide to save his family",
                    "https://i.ytimg.com/vi/db_2mujPXjk/movieposter.jpg",
                    "https://www.youtube.com/watch?v=yCt-YUbs7H4")
#print(resugurram.story)
Nuvvunaakunacchav=ex1.My("Nuvvunaakunacchav",
                    "Helping to his uncle",
                    "http://www.cineradham.com/newsongs/songsadmin/movies/nuvvu-naaku-nachav.jpg",
                    "https://www.youtube.com/watch?v=RXetYLTdlKw")
#print(Nuvvunaakunacchav.story)
Aadi=ex1.My("Aadi",
              "Taking Revenge of his fathers death",
              "https://www.filmibeat.com/img/220x100x275/popcorn/movie_posters/aadi-4756.jpg",
              "https://www.youtube.com/watch?v=UBAIOhvRewc")
#print(Aadi.story)
Doraemon=ex1.My("Doraemon",
                  "Helping others",
                  "https://myanimelist.cdn-dena.com/images/anime/9/28116l.jpg",
                  "https://www.youtube.com/watch?v=g3iYcGaLFH0")
Gouthamnanda=ex1.My("Gouthamnanda",
                      "Help to father",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/3/3a/Goutham_Nanda.jpg/220px-Goutham_Nanda.jpg",
                      "https://www.youtube.com/watch?v=ztWcdGn5thU")
King=ex1.My("King",
              "Help to family",
              "http://www.idlebrain.com/images4/wp-63kingthumb.jpg",
              "https://www.youtube.com/watch?v=adzWSn-mEFw")
              
My=[resugurram,Nuvvunaakunacchav,Aadi,Doraemon,Gouthamnanda,King]
Trailer.open_movies_page(My)
                    

