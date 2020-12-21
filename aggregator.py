import os
import argparse

def parse(deck):
    main = {}
    side = {}
    inMain = False
    inSide = False
    for line in deck:
        if line == '\n':
            continue
        if line[-1] == '\n':
            line = line[:-1]
        if line == 'Deck':
            inMain = True
            continue
        if line == 'Sideboard':
            inSide = True
            inMain = False
            continue
        if not(inMain or inSide):
            continue
        if not(line[0].isnumeric()):
            continue
        space = line.find(' ')
        cardname = line[space + 1:]
        quantity = line[:space] 
        if inMain:
            main[cardname] = int(quantity)
        else:
            if not cardname in side:
                side[cardname] = int(quantity)
    return main, side, sum(main.values())

def aggregate(lis, N):
    aggre = {}
    for deck in lis:
        for card in deck:
            for i in range(1, deck[card] + 1):
                aggre_name = card + '_' + str(i)
                if not aggre_name in aggre:
                    aggre[aggre_name] = 1
                else:
                    aggre[aggre_name] += 1
    firstN = {}
    sorted_aggregate = sorted(list(aggre.items()), key=lambda x: x[1], reverse=True)
    for card, _ in sorted_aggregate[:N]:
        underline = card.find('_')
        cardname = card[:underline]
        if not cardname in firstN:
            firstN[cardname] = 1
        else:
            firstN[cardname] += 1
    return firstN

def writer(f, main, side):
    f.write('Deck\n')
    for card in main:
        f.write(str(main[card]) + ' ' + card + '\n')
    f.write('\nSideboard\n')
    for card in side:
        f.write(str(side[card]) + ' ' + card + '\n')
    f.close()

parser = argparse.ArgumentParser(description='MTG deck aggregator')
parser.add_argument('archetype', help='The name of the archetype to be aggregated, \
must be the same with the name of folders containing the decks to be aggregated')
parser.add_argument('-w', '--weighted', action='store_true')
args = parser.parse_args()
archetype = args.archetype
decklists = os.listdir(archetype)
mains = []
sides = []
mainSize = -1
for deck in decklists:
    main, side, N = parse(open(archetype + '/' + deck))
    if mainSize == -1:
        mainSize = N
    elif mainSize != N:
        raise RuntimeError('Decklists with different sizes found in ' + archetype +
        ', consider splitting 80-card decks and 60-card decks into different archetypes')
    if args.weighted:
        try:
            weight = int(deck[0])
        except ValueError:
            print('Please specify the number of games won for each deck as the \
                start of the filename when using weighted aggregation')
    else:
        weight = 1
    for _ in range(weight):
        mains.append(main)
        sides.append(side)
main_aggregate = aggregate(mains, mainSize)
side_aggregate = aggregate(sides, 15)
final = open(archetype + '.txt', 'w')
writer(final, main_aggregate, side_aggregate)