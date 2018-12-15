import json
import random
import sys
import time

import deck_stats.deck as deck

def analyze(deck_json):
	my_deck = deck.Deck(deck_json)

	# don't show dozens/hundreds of hands with less than 1% chance of occuring
	num_hands_to_print = 9000
	total_runs = 10000
	opening_hand_mana = {}

	for step in range(0, total_runs):
		if step < total_runs - 1:
			print("Running simulation... [%d] out of [%d]\r" % (step, total_runs,) , end="")
		else:
			print("Running simulation... [%d] out of [%d]" % (total_runs, total_runs,))

		# TODO do we want to clone? shuffle modifies original
		cards = my_deck.cards

		# TODO do we need true randomness? Does this match Magic Arena's algorithm for randomness?
		# use shuffle instead of sample so we can see what next turns will look like
		random.shuffle(cards)
		
		opening_hand = cards[0:6]	
		mana_counts = {}

		for card in opening_hand:
			# count mana in opening hand
			if isinstance(card, deck.LandCard):
				mana_key = card.get_mana_key()
				if mana_key not in mana_counts:
					mana_counts[mana_key] = 0
				mana_counts[mana_key] += 1

		# now make an appropriate key based on the mana
		opening_hand_mana_keys = []
		for mana_count_key, count in sorted(mana_counts.items()):
			# count = mana_counts[mana_count_key]
			opening_hand_mana_keys.append(str(count) + ' ' + mana_count_key + ' lands')

		opening_hand_mana_key = ', '.join(opening_hand_mana_keys)

		if opening_hand_mana_key not in opening_hand_mana:
			opening_hand_mana[opening_hand_mana_key] = 0
		opening_hand_mana[opening_hand_mana_key] += 1

	print("Simulation was completed!!!")
	sorted_opening_hands = sorted(opening_hand_mana.items(), key=lambda kv: kv[1])

	num_hands = 0

	for soh_tuple in reversed(sorted_opening_hands):
		key = soh_tuple[0]
		count = soh_tuple[1]
		if len(key) == 0:
			key = ' no lands'
		print(count, " hands with ", key)
		
		num_hands += count
		if num_hands >= num_hands_to_print:
			break

if __name__ == "__main__":
	full_file_path = sys.argv[1]
	deck_json_file = open(full_file_path, 'r')
	
	deck_json = deck_json_file.read()
	deck_json = json.loads(deck_json)

	analyze(deck_json)