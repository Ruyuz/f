from random import randint

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


class Card:
	values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10 }
	def __init__(self, suit, rank):
		if suit in suits:
			self.suit = suit
		if rank in ranks:
			self.rank = rank

class Hand:
	def __init__(self):
		self.hand = []
	def add_cards(self, card):
		self.hand.append(card)
	def current_value(self):
		ace = 0
		sum_card = 0
		possible_value = []
		for card in self.hand:
			if card.rank == 'Ace':
				ace +=1
			sum_card = sum_card + card.values[card.rank]
		possible_value.append(sum_card)
		while ace > 0:
			sum_card = sum_card + 10
			possible_value.append(sum_card)
			ace = ace - 1
		return  possible_value

class Player(Hand):
	def __init__(self, first_name, last_name, purse):
		Hand.__init__(self)
		self.first_name = first_name
		self.last_name = last_name
		self.purse = purse

class Deck:
	def __init__(self):
		self.cards = None
		self.shuffle()

	def shuffle(self):
		self.card = self.deck_generator()

	def deck_generator(self):
		card_norepeat = []
		for i in range(1, 53):
			c = Card(suits[randint(0, 3)], ranks[randint(0, 12)])
			if c not in card_norepeat:
				yield Card(suits[randint(0, 3)], ranks[randint(0, 12)])
				card_norepeat.append(c)
	
	def deal(self):
		try:
			return next(self.card)
		except StopIteration:
			return None























