from enum import Enum
import json

CARD_TYPE_LAND = 1
CARD_TYPE_CREATURE = 2

class Mana(Enum):
	red = 1
	green = 2
	blue = 3
	black = 4
	white = 5
	colorless = 6

class Deck:
	def __init__(self, card_jsons=[]):
		self.num_lands = 0
		self.land_stats = {}

		self.cards = []
		for card_json in card_jsons:
			card = None
			card_name = card_json['name']
			card_type = card_json['card_type']
			if card_type == 1:
				mana_values = card_json['mana']
				card = LandCard(name=card_name, mana_values=mana_values)
			else:
				card = Card(name=card_name, card_type=card_type)

			if card != None:
				self.cards.append(card)

		self.total_size = len(self.cards)
	
    # def as_dict(self):
    #     data = dict(
	# 		total_size=self.total_size,
	# 		num_lands=self.num_lands,
	# 		cards=self.cards,
    #     )
		
    #     return data

class Card: 
	def __init__(self, name, card_type):
		self.name = name
		self.card_type = card_type

	def as_dict(self):
		data = dict(
			name=self.name,
			card_type=self.card_type,
		)

		return data

class LandCard(Card):
	def __init__(
		self
		, name
		, mana_values=[]
	):
		super().__init__(name, CARD_TYPE_LAND)

		self.mana = []
		for mana_value in mana_values:
			self.mana.append(Mana(mana_value))

	def get_mana_key(self):
		"""
			This lets us group mana so we know what we may get in starting hands
		"""
		# return json.dumps(self.mana, cls=DeckEncoder)
		mana_keys = []
		for mana in self.mana:
			mana_keys.append(mana.name)

		return json.dumps(mana_keys)

	def as_dict(self):
		data = dict(
			name=self.name,
			card_type=self.card_type,
			mana=self.mana
		)

		return data

class DeckEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Card):
			return obj.as_dict()
		if isinstance(obj, Mana):
			return obj.value

		return json.JSONEncoder.default(self, obj)