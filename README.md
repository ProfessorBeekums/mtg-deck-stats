Magic The Gathering Deck Analysis
=================================

A tool to analyze deck builds. 

This was a very quick hack so you'll need some programming ability to get much use out of it.

The only feature at the moment is a run of 10,000 opening hands to give you likely land counts based on land composition.

Example output:
```
python3 main.py example_decks/black_green.json
Running simulation... [10000] out of [10000]
Simulation was completed!!!
1127  hands with  1 ["black"] lands, 1 ["green"] lands
742  hands with  1 ["black"] lands, 2 ["green"] lands
732  hands with  2 ["black"] lands, 1 ["green"] lands
620  hands with  1 ["green"] lands
598  hands with  1 ["black"] lands
561  hands with  1 ["black"] lands, 1 ["green", "black"] lands, 1 ["green"] lands
```

Dual lands are denoted by a JSON array of mana types. 

E.g. if your deck consists of Golgori Guildgate and Woodland Cemetary, they both get grouped into `["green", "black"]`

Making New Decks
----------------
To allow for more complex analysis in the future, the decks are stored in JSON files. 

There is a single array of card objects.

A card typically looks like:
```
{"card_type": 2, "name": "saproling token"}
```

A land card will have an extra field to denote mana generation types:
```
{"card_type": 1, "name": "swamp", "mana": [4]}
```

Creating 60 card decks in JSON manually is mind numbing so a generation script in provided in `generate_deck.py`

By default it will create a 60 card deck with

* 11 swamps
* 11 forests
* 4 golgari guildgates
* 34 saproling tokens (these don't matter yet)

On "Deck"
----------------
Some of the stuff I'm planning to work on next:
* unit tests
* analysis including first 5 draws
* analysis including mulligans + scry
* analysis including casting cost of all cards (e.g. 1bb mana vs 2b mana vs 1bu mana)

Authored by [@PBeekums](https://twitter.com/PBeekums)