import os

voices = {
	"en": "en_IE",
	"cn": "zh_HK",
	"zh": "zh_CN",
	"ru": "ru_RU",
	"id": "id_ID"
}

class Word:

	def __init__(self, text, language):
		self.text = text
		self.language = language
		self.paired = []

	def pair(self, word):
		if word not in self.paired:
			self.paired.append(word)

	def say(self):
		os.system("say -v " + self.voices[self.language] + " " + self.text)
