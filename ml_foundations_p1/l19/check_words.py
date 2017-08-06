import urllib

def read_text():
	quotes = open("movie_quotes/movie_quotes.txt")
	contents_of_file = quotes.read()
	#print(contents_of_file)
	quotes.close()
	check_word(contents_of_file)

def check_word(text_to_check):
	connection = urllib.urlopen("http://wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	#print(output)
	connection.close()
	if "true" in output:
		print("Profanity Alert!!")
	elif "false" in output:
		print("This document has no curse words!")
	else:
		print("Could not scan the document properly.")

read_text()