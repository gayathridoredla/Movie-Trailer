import webbrowser
class My():
    def __init__(self,my_title,my_storyline,poster_image,trailer_youtube):
        self.title=my_title
        self.story=my_storyline
        self.poster=poster_image
        self.trailer=trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer)
        
        
