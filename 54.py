
from collections import Counter

suits = ['S', 'C', 'D', 'H']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
figures = ['J', 'Q', 'K', 'A']


class Card():
	def __init__(self, string):
		if(len(string) == 3):
			self.suit = string[2]
			self.value = string[0] + string[1]
		else:
			self.suit = string[1]
			self.value = string[0]
		self.card = string
		self.next = None
		self.compute_next()
		
	def compute_next(self):
		if self.value in figures:
			if self.value != 'A':
				index = figures.index(self.value)
				self.next = figures[index+1]
		else:
			if self.value != '10':
				index = numbers.index(self.value)
				self.next = numbers[index+1]
			else:
				self.next = 'J'

	def print(self):
		print(self.card, end = ' ')

class Player():
	def __init__(self, hand):
		self.points = 0
		self.hand = []
		self.values = []
		self.suits = []
		self.unique_suits = []
		self.unique_values = []
		
		self.createHand(hand)
		
	def createHand(self, hand):
		for item in hand:
			card = Card(item)
			self.hand.append(card)
			self.values.append(card.value)
			self.suits.append(card.suit)
		self.unique_values = set(self.values)
		self.unique_suits = set(self.suits)

	def print(self):
		for card in self.hand:
			card.print()
		print(end='\n')


def royal(player):
	placeholder = player.values
	if '10' in player.values and len(player.unique_suits) == 1:
		placeholder.remove('10')
		if Counter(figures) == Counter(placeholder):
			player.points += 1000

def flush(player):
	if len(player.unique_suits) == 1 and player.points == 0 and  len(player.unique_values) == 5:
		nex = 0
		for card in player.hand:
			if card.next in player.values:	
				nex += 1
		if nex == 4:
			player.points += 500


#['5H', '5C', '6S', '7S', 'KD']
p = Player(['9S', '10S', 'JS', 'KS', 'QS'])
flush(p)

print(p.points)
