import word
import random

class WordList:

	def __init__(self):
		self.words = []

	def random_word(self):
		return random.choice(self.words)

	def find_word(self, word):
		for w in self.words:
			if w.text == word.text and w.language == word.language:
				return w
		return None

	def import(self, filename, language1, language2):

		with open(filename, "r") as inp:
			lines = inp.readlines()

			for line in lines:
				terms = line.split("\t")
				w1 = Word(terms[0], language1)
				wex = self.find_word(w1)
				if wex is not None:
					w1 = wex
				else:
					self.words.append(w1)

				w2 = Word(terms[1], language2)
				wex = self.find_word(w2)
				if wex is not None:
					w2 = wex
				else:
					self.words.append(w2)

				w1.pair(w2)
				w2.pair(w1)
