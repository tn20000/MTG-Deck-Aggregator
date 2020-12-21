# Deck Aggregator for Magic: the Gathering
A simple python script to aggregate decks within an archetype using [Frank Karsten's aggregate deck method](https://strategy.channelfireball.com/all-strategy/mtg/channelmagic-articles/magic-math-a-new-way-to-determine-an-aggregate-deck-list-rg-dragons/).
## Goals
Having trouble determining the last few flex slots of your deck? Why not consider the crowds' wisdom by using this aggregator? Follow the new trend and see what pros are playing in the newest championship! This tool provides you with a quick and painless way to aggregate decklists in Arena format and output the aggregate in Arena format as well.
## Usage
There are 2 modes of aggregation: **weighted** & **unweighted**. The benefit of using weighted aggregation is that more emphasis is put on card choices of high winrate decklists.  
  
**Unweighted** aggregation simply requires putting all decklists in a folder with the same archetype, i.e. `Gruul Adventures`.  
Then, run `python aggregator.py "Gruul Adventures"`, and the aggregator decklist `Gruul Adventures.txt` will appear in the same folder. You can directly copy the decklist and import to Arena.  
  
**Weighted** aggregation requires putting the number of games won for that decklists as the start of the filename. For example, `Esper Weighted` contains `6Luis-Scott-Vargas-Esper-Doom-Foretold-Zendikar-Rising-Championship`, which is LSV's 6-win Esper Doom decklist at Zendikar Rising Championship.  
Then, run `python aggregator.py "Esper Weighted" -w` and the aggregator decklist `Esper Weighted.txt` will appear in the same folder.  
## Warnings
- Separate 60-card decks with 80-card decks. The tool currently has no way to aggregate deck with different number of cards. However, you can subclassify the archetype, i.e. separate `Dimir Control` with `Dimir Control` & `Dimir Control (Yorion)`.
- The aggregator won't put the companion directly in the companion slot. However, it'll appear in the sideboard. After importing the deck, drag the companion to the companion slot in Arena.
- The cutoff for the final slots of both the main deck and sideboard is currently arbitrary, and is determined alphabetically. However, if you have enough decks for an archetype, this isn't a problem.
## Existing Data
In the 6 existing folders contains decklists from the [Zendikar Rising Championship](https://magic.gg/decklists/zendikar-rising-championship-standard-decklists-a-k) from my favorite 3 archetypes of the current standards. The folders ended with "weighted" contain all decklists of that archetype that achieved 5 wins or greater. The other folders contain all decklists in ZNR championship of that archetype.