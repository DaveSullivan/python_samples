""" Implementation of a lexicon class that meets the test conditions specified in the test file located here:
http://learnpythonthehardway.org/book/ex48.html
"""

import re

class lexicon(object):
	def __init__(self):
		self.dict = {}
		
		directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
		self.addWords(directions, 'direction')

		verbs = ["go", "stop", "kill", "eat"]
		self.addWords(verbs, 'verb')
		
		stopwords = ['the', 'in', 'of', 'from', 'at', 'it']
		self.addWords(stopwords,'stop')
		
		nouns = ['door', 'bear', 'princess', 'cabinet']
		self.addWords(nouns, 'noun')
		
	
	def addWords(self, words, type):
		for word in words:
			self.dict.update({word: type})
	
	def getWordTypeTuple(self, word):
		type = self.dict.get(word, 'error')

		if type == 'error':
			matched = re.match('[0-9]*', word)
			print matched.group(0)
			if matched != None and matched.group(0) == word:
				try:
					word = int(word)
					type = 'number'
				except ValueError:
					pass
			
		return (type, word)
	
	def scan(self, phrase):
		words = phrase.split()
		tuples = []
		for word in words:
			tuples.append(self.getWordTypeTuple(word))
		return tuples
		
lex = lexicon()
print lex.scan("11m")
	