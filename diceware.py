
#
# This is a simple Python module for generating diceware Passwords
# Run the python script with: python diceware.py
# Provide it a number for how many words you want in your password
# There is no minimum or maximum, but to be secure aim for 5 or higher
# This generator uses variable deliminaters to add complexity
# 

import random

class DiceWare():
	def __init__(self):
		dictionary = {}
		self.wordlist = self.word_list(dictionary)
		self.delim = self.find_delim()
	
	def word_list(self,dictionary):
		with open('wordlist.txt') as f:
			for lines in f:
				a,b = lines.split(',')
				a = a.replace('\n','').replace('\r','')
				b = b.replace('\n','').replace('\r','')
				dictionary.update({a:b})
					
		return dictionary		
		
	def find_delim(self):
		delim_option = {
			'1':'-',
			'2':'_',
			'3':'.',
			'4':':',
			'5':'/'
			}
		a = random.randint(1,5)
		return delim_option[str(a)]
		
	def create_passphrase(self,number):
		passphrase = ''
		while number > 0:
			a,b,c,d,e = self.roll_dice()
			passphrase += self.wordlist[str(a)+str(b)+str(c)+str(d)+str(e)]
			if number > 1:
				passphrase += self.delim
			number -= 1
		return passphrase

	def roll_dice(self):
		dice = 5
		while dice > 0:
			result = random.randint(1,5)
			dice -= 1
			yield result


def main():
	number = raw_input("How many words would you like in your passphrase? " )
	number = int(number)
	generator = DiceWare()
	password = generator.create_passphrase(number)
	print password

main()
