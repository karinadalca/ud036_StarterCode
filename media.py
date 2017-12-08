import webbrowser


class Movie():
  	#Triple quotes for ducumentation and can be access using media.Movie.__doc__
	"""This class provides a way to store movie related information"""
			
	#Movie constructor to initalize all instances with a title (string), 
	#storyline (string), poster image ((string)) and trailer URL (string)
	def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_poster
		self.trailer_youtube_url = movie_trailer
			
	#Opens browser window to show trailer
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)