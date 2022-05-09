import random
from words import words
from string import ascii_uppercase
def get_valid_word(words):
	word = random.choice(words)
	while '-' in word or ' ' in word:
		word = random.choice(words)
	return word

def hangman():
	word = get_valid_word(words)
	word_letters = set(word)
	alpha = set(ascii_uppercase)
	used_letters = set()
	while len(word_letters)>0:
		print('You have entered: ', ' '.join(used_letters))

		user_letter = input('Guess a letter: ').upper()

		if user_letter in alpha - used_letters:
			used_letters.add(user_letter)
			if user_letter in word_letters:
				word_letters.remove(user_letter)
		elif user_letter in used_letters:
			print("You already entered tht before")
		else:
			print("Please enter a letter")

if __name__=="__main__":
	hangman()