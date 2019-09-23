import random
import unittest

# SI 507 Fall 2018
# Homework 2 - Code

##COMMENT YOUR CODE WITH:
# Section Day/Time: Section001/101, 8:30 - 11:30 AM Tuesday. Discussion: 004/104
# People you worked with: Wenhao Liu

######### DO NOT CHANGE PROVIDED CODE #########
### Scroll down for assignment instructions.
#########

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)
	def deal(self, number_of_hands,hands_capacity):
		#if number_of_hands*hands_capacity>=len(self.cards):
			#total=len(self.cards)
		if hands_capacity==-1:
			total=len(self.cards)
		else:
			total=number_of_hands*hands_capacity
		a=1
		A=[[] for i in range(number_of_hands)]
		while a<=total:
			for i in range(number_of_hands):
				A[i].append(self.cards.pop(0))
				a=a+1
				if a> total:
					return A
		return A

	# deal cards in a deck to all hands
	# param: number of hands and the capacity of each hand
	# returns: lists of hands
class Hand:
	# create the Hand with an initial set of cards
	# param: a list of cards
	def __init__(self, init_cards):
		self.init_cards=init_cards

	def __str__(self):
		total = []
		for card in self.init_cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	# add a card to the hand
	# silently fails if the card is already in the hand
	# param: the card to add
	# returns: nothing
	def add_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.init_cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.init_cards.append(card) # append it to the list

	# remove a card from the hand
	# param: the card to remove
	# returns: the card, or None if the card was not in the Hand
	def remove_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.init_cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() in card_strs: # if the string representing this card is not in the list already
			self.init_cards.remove(card) # append it to the list
			#return print(card)

	# draw a card from a deck and add it to the hand
	# side effect: the deck will be depleted by one card
	# param: the deck from which to draw
	# returns: nothing
	def draw(self, deck):
		card=deck.pop_card(i=0)
		self.init_cards.append(card)
		return card
	# draw a card from a deck and add it to the hand
	# side effect: the deck will be depleted by one card
	# param: the deck from which to draw
	# returns: nothing
	def remove_book(self, rank):
		if rank==1:
			rank ="Ace"
		elif rank==11:
			rank="Jack"
		elif rank==12:
			rank="Queen"
		elif rank==13:
			rank="King"
		count=[]
		for c in self.init_cards:
			if c.rank==rank:
				count.append(c)
		if len(count)==4:
			self.init_cards.remove(count[0])
			self.init_cards.remove(count[1])
			self.init_cards.remove(count[2])
			self.init_cards.remove(count[3])
			return True
		return False

def go_fish_begin():
	deck=Deck()
	deck.shuffle()
	handlist=deck.deal(number_of_hands=2,hands_capacity=7)
	A=Hand(handlist[0])
	B=Hand(handlist[1])
	turn="A"
	con=True
	Acount=0
	Bcount=0
	while con is True:
		#A's Turn
		if turn == "A":
			A,B,deck,Acount,Bcount=play(A,B,turn,deck,Acount,Bcount)
			turn ="B"
		if turn == "B":
			A,B,deck,Acount,Bcount=play(A,B,turn,deck,Acount,Bcount)
			turn ="A"
		if len(deck.cards)==0:
			con = False
	if Acount>Bcount:
		print("A win!")
	else:
		print("B win!")

def check_trick(HAND):
	for c in HAND.init_cards:
		b=HAND.remove_book(c.rank)
		if b is True:
			return True
		else:
			return False

def play(A,B,turn,deck,Acount,Bcount):
	while True:
		if turn =="A":
			HAND=A
			OTHER=B
			print("A's turn")
		elif turn=="B":
			HAND=B
			OTHER=A
			print("B's turn")
		print("cards in your hands")
		print(HAND)
		fish=False
		x=input("The rank you request(Using 2-10,Ace,Jack,Queen and King)")
		for c in OTHER.init_cards:
			if str(x)==str(c.rank):
				OTHER.remove_card(c)
				HAND.add_card(c)
				fish=True
		if fish is False:
			b=HAND.draw(deck)
			if str(b.rank)==str(x):
				print("Fishing successful:"+str(b))
				fish=True
		t=check_trick(HAND)
		if t is True and turn=="A":
			Acount=Acount+1
		if t is True and turn=="B":
			Bcount=Bcount+1
		if fish is False:
			break
	return A,B,deck,Acount,Bcount


if __name__ == "__main__":
	go_fish_begin()
