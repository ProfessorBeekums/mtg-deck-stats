import json

import deck_stats.deck as deck

if __name__ == "__main__":
	"""
		Since we're trying to future proof by using individual cards in the JSON,
		we also need a way to generate json without hating ourselves.
	"""
	file = open("example_decks/black_green.json", "w")

	cards = []

	for i in range(0,11):
		cards.append(
			deck.LandCard(
				name='swamp'
				, mana_values=[deck.Mana.black.value]
			)
		)

	for i in range(0,11):
		cards.append(
			deck.LandCard(
				name='forest'
				, mana_values=[deck.Mana.green.value]
			)
		)
	for i in range(0,4):
		cards.append(
			deck.LandCard(
				name='golgari guildgate'
				, mana_values=[deck.Mana.green.value, deck.Mana.black.value]
			)
		)

	for i in range(0, 34):
		cards.append(
			deck.Card(
				name='saproling token'
				, card_type=deck.CARD_TYPE_CREATURE
			)
		)

	file.write(json.dumps(cards, cls=deck.DeckEncoder))
	file.close()